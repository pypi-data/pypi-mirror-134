import numpy as np
import sys
import os
import re
from skimage import io
import cv2

def pad(mat, pad=5, option="white"):
	new_mat = np.empty((mat.shape[0]+pad*2, mat.shape[1]+pad*2), dtype=mat.dtype)
	for p in range(new_mat.shape[0]):
		for q in range(new_mat.shape[1]):
			if option=="white":
				new_mat[p,q] = 65535
			else:
				new_mat[p,q] = 0
	for p in range(pad, pad+mat.shape[0]):
		for q in range(pad, pad+mat.shape[1]):
			new_mat[p,q] = mat[p-pad, q-pad]
	return new_mat

def read_output(n):
	f = open(n)
	f.readline()
	image = {}
	l = f.readline().rstrip("\n").split()
	image["x"] = float(l[1])
	image["y"] = float(l[3])
	image["width"] = float(l[5]) - float(l[1])
	image["height"] = float(l[7]) - float(l[3])
	f.readline()
	bounding = []
	while True:
		l = f.readline()
		if l=="": break
		l = l.rstrip("\n")
		if l.startswith("path"):
			bounding.append(l)
		if l=="": break
	paths = {}
	while True:
		l = f.readline()
		if l=="": break
		l = l.rstrip("\n")
		if l=="": break
		ll = l.split()
		paths.setdefault(ll[1], [])
		paths[ll[1]].append((float(ll[-2]), float(ll[-1])))
	
	return image, bounding, paths

def transform_coord(x, y, offset_x, offset_y, width, height):
	new_x = (x - offset_x) / width * 2048.0
	new_y = (y - offset_y) / height * 2048.0
	return new_x, new_y

def crop_images(svg_image, svg_bounding, svg_paths, img_filename, outdir, img_maxsize=227, resize_scale_factor=1.0, padding=5, MAX=65535):
	new_coord = []
	new_paths = {}
	for p in svg_paths:
		new_paths.setdefault(p, [])
		for i,j in svg_paths[p]:
			new_i, new_j = transform_coord(i, j, svg_image["x"], svg_image["y"], svg_image["width"], svg_image["height"])
			new_i = int(new_i)
			new_j = int(new_j)
			new_coord.append((new_i, new_j))
			new_paths[p].append((new_i, new_j))

	mat = io.imread(img_filename)

	outdir = outdir

	for p in new_paths:
		pts = np.array(new_paths[p])
		rect = cv2.boundingRect(pts)
		x,y,w,h = rect
		cropped = mat[y:y+h, x:x+w].copy()
		pts = pts - pts.min(axis=0)

		#MAX = 65535
		mask = np.zeros(cropped.shape, np.uint16)
		cv2.drawContours(mask, [pts], -1, (MAX, MAX, MAX), -1, cv2.LINE_AA)

		#resized_mask = cv2.resize(pad(mask, pad=5, option="black"), None, fx=1.45, fy=1.45, interpolation=cv2.INTER_CUBIC)
		#resized = cv2.resize(pad(cropped, pad=5, option="black"), None, fx=1.45, fy=1.45, interpolation=cv2.INTER_CUBIC)

		dst = cropped.copy()
		for i in range(dst.shape[0]):
			for j in range(dst.shape[1]):
				if mask[i,j]==MAX:
					dst[i,j]=cropped[i,j]
				else:
					dst[i,j]=0

		resized = cv2.resize(pad(dst, pad=padding, option="black"), None, fx=resize_scale_factor, fy=resize_scale_factor, interpolation=cv2.INTER_CUBIC)
		#cv2.imwrite("mask.png", mask)
		#resized = cv2.resize(pad(mask, pad=5, option="black"), None, fx=1.45, fy=1.45, \
		#resized = cv2.resize(pad(dst, pad=5, option="black"), None, fx=1.45, fy=1.45, \
		#interpolation=cv2.INTER_CUBIC)

		#print resized.shape[0], resized.shape[1]
		if resized.shape[0]>img_maxsize or resized.shape[1]>img_maxsize:
			print("dimension exceed 227", resized.shape)
			t_factor = img_maxsize / max(resized.shape[0], resized.shape[1])
			resized = cv2.resize(pad(dst, pad=5, option="black"), None, fx=t_factor, fy=t_factor, interpolation=cv2.INTER_CUBIC)
			print("New dimension", resized.shape)
			
		#cv2.imwrite("%s/%s.png" % (outdir, p), cv2.resize(pad(mask, pad=10, option="black"), None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)) # (mask on black bg)
		cv2.imwrite("%s/%s.png" % (outdir, p), resized) #(mask on black bg)


if __name__=="__main__":
	image, bounding, paths = read_output(sys.argv[1])
	#print image
	#print bounding
	#print paths
	new_coord = []
	new_paths = {}
	for p in paths:
		#print "Path", p #comment sept 4
		new_paths.setdefault(p, [])
		for i,j in paths[p]:
			new_i, new_j = transform_coord(i, j, image["x"], image["y"], image["width"], image["height"])
			new_i = int(new_i)
			new_j = int(new_j)
			new_coord.append((new_i, new_j))
			new_paths[p].append((new_i, new_j))

	#mat = io.imread("../Pos.16.Page.1.Composite.png")
	mat = io.imread(sys.argv[2])
	#print mat.shape
	#print mat
	#for i, j in new_coord:
	#	mat[int(j), int(i)] = 65535
	#io.imsave("../Pos.16.modified.png", mat)

	outdir = sys.argv[3]

	for p in new_paths:
		pts = np.array(new_paths[p])
		#print pts
		rect = cv2.boundingRect(pts)
		x,y,w,h = rect
		cropped = mat[y:y+h, x:x+w].copy()
		#print "Cropped dimension", cropped.shape
		pts = pts - pts.min(axis=0)

		MAX = 65535
		mask = np.zeros(cropped.shape, np.uint16)
		cv2.drawContours(mask, [pts], -1, (MAX, MAX, MAX), -1, cv2.LINE_AA)

		#resized_mask = cv2.resize(pad(mask, pad=5, option="black"), None, fx=1.45, fy=1.45, interpolation=cv2.INTER_CUBIC)
		#resized = cv2.resize(pad(cropped, pad=5, option="black"), None, fx=1.45, fy=1.45, interpolation=cv2.INTER_CUBIC)

		dst = cropped.copy()
		for i in range(dst.shape[0]):
			for j in range(dst.shape[1]):
				if mask[i,j]==MAX:
					dst[i,j]=cropped[i,j]
				else:
					dst[i,j]=0

		resized = cv2.resize(pad(dst, pad=5, option="black"), None, fx=1.0, fy=1.0, interpolation=cv2.INTER_CUBIC)
		#cv2.imwrite("mask.png", mask)
		#resized = cv2.resize(pad(mask, pad=5, option="black"), None, fx=1.45, fy=1.45, \
		#resized = cv2.resize(pad(dst, pad=5, option="black"), None, fx=1.45, fy=1.45, \
		#interpolation=cv2.INTER_CUBIC)

		#print resized.shape[0], resized.shape[1]
		if resized.shape[0]>227 or resized.shape[1]>227:
			print("dimension exceed 227", resized.shape)
			t_factor = 227.0 / max(resized.shape[0], resized.shape[1])
			resized = cv2.resize(pad(dst, pad=5, option="black"), None, fx=t_factor, fy=t_factor, interpolation=cv2.INTER_CUBIC)
			print("New dimension", resized.shape)
			
			

		#cv2.imwrite("%s/%s.png" % (outdir, p), cv2.resize(pad(mask, pad=10, option="black"), None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)) # (mask on black bg)
		cv2.imwrite("%s/%s.png" % (outdir, p), resized) #(mask on black bg)



		#cv2.imwrite("dst.png", dst)
		#cv2.imwrite("%s/%s.png" % (outdir, p), dst) #original (cropped on black bg)
		#cv2.imwrite("cropped.png", cropped)

		'''
		w_dst = cropped.copy()
		for i in range(dst.shape[0]):
			for j in range(dst.shape[1]):
				if mask[i,j]==MAX:
					w_dst[i,j]=cropped[i,j]
				else:
					w_dst[i,j]=MAX
		'''
		#cv2.imwrite("wdst.png", w_dst)


	'''
	## (3) do bit-op
	dst = cv2.bitwise_and(new_cropped, new_cropped, mask=mask)

	## (4) add the white background
	bg = np.ones_like(new_cropped, np.uint16)*MAX
	cv2.bitwise_not(bg,bg, mask=mask)
	dst2 = bg+ dst
	cv2.imwrite("dst2.png", dst2)	
	'''
