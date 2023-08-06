# import the necessary packages
from __future__ import print_function
from google.protobuf import text_format
from cStringIO import StringIO
import scipy.ndimage as nd
import numpy as np
import caffe
import os

class BatCountry:
	def __init__(self, base_path, deploy_path=None, model_path=None,
		patch_model="./tmp.prototxt", mean=(104.0, 116.0, 122.0),
		channels=(2, 1, 0)):
		# if the deploy path is None, set the default
		if deploy_path is None:
			deploy_path = base_path + "/deploy.prototxt"

		# if the model path is None, set it to the default GoogleLeNet model
		if model_path is None:
			model_path = base_path + "/bvlc_googlenet.caffemodel"

		# check to see if the model should be patched to compute gradients
		if patch_model:
			model = caffe.io.caffe_pb2.NetParameter()
			text_format.Merge(open(deploy_path).read(), model)
			model.force_backward = True
			f = open(patch_model, "w")
			f.write(str(model))
			f.close()

		# load the network and store the patched model path
		self.net = caffe.Classifier(patch_model, model_path, mean=np.float32(mean),
			channel_swap=channels)
		self.patch_model = patch_model

	def dream(self, image, iter_n=10, octave_n=4, octave_scale=1.4,
		end="inception_4c/output", clip=True, step_fn=None, preprocess_fn=None,
		deprocess_fn=None, verbose=True, visualize=False, **step_params):
		# if a step function has not been supplied, initialize it as the standard
		# gradient ascent step
		if step_fn is None:
			step_fn = BatCountry.gradient_ascent_step

		# if the preprocess function has not been supplied, initialize it
		if preprocess_fn is None:
			preprocess_fn = BatCountry.preprocess

		# if the deprocess function has not been supplied, initialize it
		if deprocess_fn is None:
			deprocess_fn = BatCountry.deprocess

		# initialize the visualization list
		visualizations = []

		# prepare base images for all octaves
		octaves = [preprocess_fn(self.net, image)]

		for i in xrange(octave_n - 1):
			octaves.append(nd.zoom(octaves[-1], (1, 1.0 / octave_scale,
				1.0 / octave_scale), order=1))

		# allocate image for network-produced details
		detail = np.zeros_like(octaves[-1])
		src = self.net.blobs["data"]

		for octave, octave_base in enumerate(octaves[::-1]):
			h, w = octave_base.shape[-2:]

			if octave > 0:
				# upscale details from the previous octave
				h1, w1 = detail.shape[-2:]
				detail = nd.zoom(detail, (1, 1.0 * h/ h1, 1.0 * w / w1), order=1)

 			# resize the network's input image size
			src.reshape(1, 3, h, w)
			src.data[0] = octave_base + detail

			for i in xrange(iter_n):
				step_fn(self.net, end=end, clip=clip, **step_params)

				# visualization
				vis = deprocess_fn(self.net, src.data[0])

				# adjust image contrast if clipping is disabled
				if not clip: 
					vis = vis * (255.0 / np.percentile(vis, 99.98))

				if verbose:
					print("octave={}, iter={}, layer={}, image_dim={}".format(octave,
						i, end, vis.shape))

				# check to see if the visualization list should be
				# updated
				if visualize:
					k = "octave_{}-iter_{}-layer_{}".format(octave, i,
						end.replace("/", "_"))
					visualizations.append((k, vis))

			# extract details produced on the current octave
			detail = src.data[0] - octave_base

		# grab the resulting image
		r = deprocess_fn(self.net, src.data[0])

		# check to see if the visualizations should be included
		if visualize:
			r = (r, visualizations)

		return r

	@staticmethod
	def gradient_ascent_step(net, step_size=1.5, end="inception_4c/output",
		jitter=32, clip=True):
		# input image is stored in Net's 'data' blob
		src = net.blobs["data"]
		dst = net.blobs[end]

		# apply jitter shift
		ox, oy = np.random.randint(-jitter, jitter + 1, 2)
		src.data[0] = np.roll(np.roll(src.data[0], ox, -1), oy, -2)

		net.forward(end=end)
		# specify the optimization objective
		dst.diff[:] = dst.data
		net.backward(start=end)
		g = src.diff[0]

		# apply normalized ascent step to the input image
		src.data[:] += step_size / np.abs(g).mean() * g

 		# unshift image
		src.data[0] = np.roll(np.roll(src.data[0], -ox, -1), -oy, -2)

		# unshift image
		if clip:
			bias = net.transformer.mean["data"]
			src.data[:] = np.clip(src.data, -bias, 255 - bias)

	def cleanup(self):
		# remove the patched model from disk
		os.remove(self.patch_model)

	@staticmethod
	def preprocess(net, img):
		return np.float32(np.rollaxis(img, 2)[::-1]) - net.transformer.mean["data"]

	@staticmethod
	def deprocess(net, img):
		return np.dstack((img + net.transformer.mean["data"])[::-1])