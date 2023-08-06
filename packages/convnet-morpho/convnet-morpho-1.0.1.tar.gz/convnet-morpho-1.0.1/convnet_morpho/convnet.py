import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import wget
import tensorflow as tf
import sys

#from alexnet import AlexNet
#from caffe_classes import class_names

def download_alexnet(outdir="alexnet"):
	url = "https://zenodo.org/record/5842250/files"
	flist = ["alexnet.pb", "alexnet.py", "alexnet_frozen.pb", "bvlc_alexnet.npy", "caffe_classes.py"]
	if not os.path.isdir(outdir):
		os.mkdir(outdir)
	for aFile in flist:
		t_path = "%s/%s" % (outdir, aFile)
		if os.path.exists(t_path):
			print("File %s already exists, skipped." % t_path)
		else:
			print("Downloading %s..." % t_path)
			wget.download("%s/%s?download=1" % (url, aFile), out=t_path)
	print("Done")

	sys.path.append(outdir)
	from alexnet import AlexNet
	from caffe_classes import class_names
	
	

def alexnet_extract_features(folder, is_visium=False, is_path=True, auto_resize=False, alexnet_path="alexnet"):

	flist = ["alexnet.pb", "alexnet.py", "alexnet_frozen.pb", "bvlc_alexnet.npy", "caffe_classes.py"]
	for aFile in flist:
		t_path = "%s/%s" % (alexnet_path, aFile)
		if not os.path.exists(t_path):
			print("Error some pre-requisite files not found: %s. Call convnet.download_alexnet() first." % t_path)
			sys.exit(1)

	print("Loading alexnet model...")
	sys.path.append(alexnet_path)
	from alexnet import AlexNet
	from caffe_classes import class_names
	
	resize_length = 227
	img_file = folder
	save_dir = folder + '/resize/'

	for path in os.listdir(img_file):
		b_path = False
		if is_visium==True and path.endswith("-1.png"):
			b_path = True
		if is_path==True and path.startswith("path"):
			b_path = True

		if b_path:
		#if path.startswith("path"):
			img_name = path
			img_full_path = img_file + '/' + path
			#print(img_name, img_full_path)
			print(img_full_path)
			img = cv2.imread(img_full_path)  # img with 3 same channels
			img_resize = np.zeros([resize_length, resize_length, 3], dtype=np.uint8)
			x_shift = int(np.round(resize_length / 2 - img.shape[0] / 2))
			y_shift = int(np.round(resize_length / 2 - img.shape[1] / 2))

			if auto_resize:
				size1, size2 = x_shift + img.shape[0], y_shift + img.shape[1]
				i1, i2 = img.shape[0], img.shape[1]
				if x_shift<0:
					x_shift = max(0, x_shift)
					size1 = resize_length - 1
					i1 = size1
				if y_shift<0:
					y_shift = max(0, y_shift)
					size2 = resize_length - 1
					i2 = size2
				img_resize[x_shift:size1, y_shift:size2, 0] = img[0:i1, 0:i2]
				img_resize[x_shift:size1, y_shift:size2, 1] = img[0:i1, 0:i2]
				img_resize[x_shift:size1, y_shift:size2, 2] = img[0:i1, 0:i2]

			else:
				img_resize[x_shift:x_shift + img.shape[0], y_shift:y_shift + img.shape[1], :] = img
			
			image_save_path = save_dir
			if not os.path.exists(image_save_path):
				os.makedirs(image_save_path)
			cv2.imwrite(image_save_path + '/' + img_name, img_resize)

	print('Finish resizing images')
	img_file = save_dir
	save_dir = folder + "/feature/"

	imagenet_mean = np.array([104., 117., 124.], dtype=np.float32)
	x = tf.placeholder(tf.float32, [None, 227, 227, 3])
	keep_prob = tf.constant(1.0)

	model = AlexNet(x, keep_prob, 1000, [], weights_path="%s/bvlc_alexnet.npy" % alexnet_path)
	feature = model.feature_out

	with tf.Session() as sess:
		load_op = model.load_initial_weights(sess)
		sess.run(load_op)
		allimgs = np.zeros(shape=(1, 227, 227, 3), dtype=np.float)
		for path in os.listdir(img_file):
			print('read image path: '+img_file + path)

			b_path = False
			if is_visium==True and path.endswith("-1.png"):
				b_path = True
			if is_path==True and path.startswith("path"):
				b_path = True

			if b_path:
			#if path.startswith("path"):
				img_name = path
				img_full_path = img_file + "/" + path
				img = cv2.imread(img_full_path)  # img with 3 same channels
				allimgs[0] = img
				feature_realval = sess.run(feature, feed_dict={x: allimgs})
				image_save_path = save_dir
				if not os.path.exists(image_save_path):
					os.makedirs(image_save_path)
				np.save(image_save_path + '/' + img_name+'.npy', feature_realval)



