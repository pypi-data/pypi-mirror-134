#!/usr/bin/python
import sys
import os
import numpy as np
import wget
import scipy
import scipy.stats
from operator import itemgetter
from scipy.interpolate import interp1d
from zipfile import ZipFile
sys.setrecursionlimit(10000)

def read_cell_type(n):
	f = open(n)
	mm = []
	cell_annot = []
	map_cell = {}
	ix = 0
	for l in f:
		l = l.rstrip("\n")
		ll = l.split("\t")
		mm.append(ll[2])
		cell_annot.append(ll[0])
		map_cell[ll[0]] = ix
		ix += 1
	f.close()
	ct_uniq = np.unique(mm)
	map_id = {}
	for ind,val in enumerate(ct_uniq):
		map_id[val] = ind+1
	mm_annot = []
	for c in mm:
		mm_annot.append(map_id[c])
	print("load_brain2", map_id)
	return mm_annot, map_cell
	
def read_domain(n):
	f = open(n)
	mm = []
	for l in f:
		l = l.rstrip("\n")
		ll = l.split("\t")
		mm.append(int(ll[1]))
	print(np.unique(mm))
	f.close()
	return mm

def read_map(n):
	f = open(n)
	cells = []
	f_name = []
	for l in f:
		l = l.rstrip("\n")
		ll = l.split()
		cells.append(ll[3])
		f_name.append((int(ll[1]), ll[2]))
	return cells, f_name

def get_performance_eval(dec, true_label, labels):
	num_class = dec.shape[1]
	num_example = dec.shape[0]
	auc_eval = []
	pr_eval = []
	for c in range(num_class):
		st = zip(true_label, dec[:,c])
		st.sort(key=itemgetter(1), reverse=True)
		tp, fp = 0, 0
		cond_pos = 0
		cond_neg = 0
		this_auc = []
		this_pr = []
		for ex in range(num_example):
			if st[ex][0]==labels[c]: #st[ex][0] is true_label
				cond_pos+=1
			else:
				cond_neg+=1
		for ex in range(num_example):
			if st[ex][0]==labels[c]:
				tp+=1
			else:
				fp+=1
			recall = float(tp) / cond_pos
			precision = float(tp) / (ex + 1)
			tpr = recall
			fpr = float(fp) / cond_neg
			this_pr.append((precision, recall))
			this_auc.append((tpr, fpr))
		rev_ex = num_example - 2
		while rev_ex>=0:
			t_t = this_pr[rev_ex]
			t_t_plus_1 = this_pr[rev_ex + 1]
			if t_t[0]<t_t_plus_1[0]:
				t_t = (t_t_plus_1[0], t_t[1])
				this_pr[rev_ex] = t_t
			rev_ex = rev_ex - 1

		un_tpr, un_fpr = zip(*this_auc)
		un_tpr = [0] + list(un_tpr) + [1]
		un_fpr = [0] + list(un_fpr) + [1]
		base_fpr = np.linspace(0,1,101)
		new_tpr = interp1d(un_fpr, un_tpr, kind="next")(base_fpr)
		this_auc = zip(new_tpr, base_fpr)

		un_pr, un_recall = zip(*this_pr)
		un_pr = [0] + list(un_pr) + [1]
		un_recall = [0] + list(un_recall) + [1]
		base_recall = np.linspace(0,1,102)[1:]
		new_pr = interp1d(un_recall, un_pr, kind="next")(base_recall)
		this_pr = zip(new_pr, base_recall)

		auc_eval.append(this_auc)
		pr_eval.append(this_pr)
	return auc_eval, pr_eval

def get_label_order(pr, dec):
	num_class = dec.shape[1]
	num_example = dec.shape[0]
	t_map = {}
	for ex in range(num_example):
		tc = np.argmax(dec[ex,:])
		label = pr[ex]
		t_map.setdefault(label, set([]))
		t_map[label].add(tc)
	#print t_map
	r_label = range(num_class)
	for t in t_map:
		r_label[list(t_map[t])[0]] = t
	return r_label

def read_coordinates(n):
	f = open(n)
	x,y = [],[]
	for l in f:
		l = l.rstrip("\n")
		ll = l.split()
		x.append(float(ll[2]))
		y.append(float(ll[3]))
	f.close()
	Xcen = np.empty((len(x), 2), dtype="float32")
	for i in range(len(x)):
		Xcen[i,:] = [x[i], y[i]]
	return Xcen

def download(outdir="brain2.segmented"):
	url = "https://bitbucket.org/qzhudfci/convnet.morpho/raw/b3abc7aad1b6c614a023e817ae04d51db0ba5f6b/brain2.segmented"
	#dapi_cell_order, dapi_f_name = read_map("brain2.segmented/all.align.dapi.sort.txt")
	#nissl_cell_order, nissl_f_name = read_map("brain2.segmented/all.align.nissl.sort.txt")
	#domain = read_domain("brain2.segmented/hmrf.domains.txt")
	#ct, map_cell = read_cell_type("brain2.segmented/fcortex.cell.type.annot.2.txt") #combined
	#ct2, map_cell2 = read_cell_type("brain2.segmented/fcortex.cell.type.annot.txt") #individual
	#Xcen = read_coordinates("brain2.segmented/fcortex.coordinates.txt")
	flist = ["all.align.dapi.sort.txt", "all.align.nissl.sort.txt", "hmrf.domains.txt", \
	"fcortex.cell.type.annot.2.txt", "fcortex.cell.type.annot.txt", "fcortex.coordinates.txt"]

	if not os.path.isdir(outdir):
		os.mkdir(outdir)

	for aFile in flist:
		t_path = "%s/%s" % (outdir, aFile)
		if os.path.exists(t_path):
			print("File %s already exists, skipped." % t_path)
		else:
			print("Downloading %s..." % t_path)
			wget.download("%s/%s" % (url, aFile), out=t_path)
	print("Done")

	url = "https://bitbucket.org/qzhudfci/convnet.morpho/raw/b3abc7aad1b6c614a023e817ae04d51db0ba5f6b"
	flist = ["image_zero_input.npy"]
	for aFile in flist:
		t_path = "%s/%s" % (outdir, aFile)
		if os.path.exists(t_path):
			print("File %s already exists, skipped." % t_path)
		else:
			print("Downloading %s..." % t_path)
			wget.download("%s/%s" % (url, aFile), out=t_path)
	print("Done")	

	url = "https://zenodo.org/record/4539873/files/brain2.image.data.zip?download=1"
	dlist = ["option1", "option2", "option3"]
	is_exist = True
	for aDir in dlist:
		t_path = "%s/%s" % (outdir, aDir)
		if os.path.isdir(t_path):
			print("Directory %s already exists. skipped" % t_path)
		else:
			is_exist = False
	if not is_exist:
		if os.path.exists("%s/brain2.image.data.zip" % outdir):
			print("File %s alrady exists, skipped." % "brain2.image.data.zip")
		else:
			print("Downloading brain2.image.data.zip...") 
			wget.download(url, out="%s/brain2.image.data.zip" % outdir)
		with ZipFile("%s/brain2.image.data.zip" % outdir, "r") as zipObj:
			zipObj.extractall("%s" % outdir)	
	print("Done")

#def load():
def load(filter_feature=False, filter_cutoff=50, log=False, zscore1=False, option=2, prereq_dir="brain2.segmented"):
	flist = ["all.align.dapi.sort.txt", "all.align.nissl.sort.txt", "hmrf.domains.txt", \
	"fcortex.cell.type.annot.2.txt", "fcortex.cell.type.annot.txt", "fcortex.coordinates.txt"]
	dlist = ["option1", "option2", "option3"]
	for aFile in flist:
		t_path = "%s/%s" % (prereq_dir, aFile)
		if not os.path.exists(t_path):
			print("Error some pre-requisite files not found: %s. Call load_brain2_new.download() to download first." % t_path)
			sys.exit(1)
	for aDir in dlist:
		t_path = "%s/%s" % (prereq_dir, aDir)
		if not os.path.isdir(t_path):
			print("Error directory not found: %s. Call load_brain2_new.download() to download first." % t_path)
			sys.exit(1)

	dapi_cell_order, dapi_f_name = read_map("%s/all.align.dapi.sort.txt" % prereq_dir)
	nissl_cell_order, nissl_f_name = read_map("%s/all.align.nissl.sort.txt" % prereq_dir)
	domain = read_domain("%s/hmrf.domains.txt" % prereq_dir)
	ct, map_cell = read_cell_type("%s/fcortex.cell.type.annot.2.txt" % prereq_dir) #combined
	ct2, map_cell2 = read_cell_type("%s/fcortex.cell.type.annot.txt" % prereq_dir) #individual
	Xcen = read_coordinates("%s/fcortex.coordinates.txt" % prereq_dir)

	cell_id_to_nissl = {}
	for iv,c in enumerate(nissl_cell_order):
		cell_id = map_cell[c]
		cell_id_to_nissl[cell_id] = iv
	cell_id_to_dapi = {}
	for iv,c in enumerate(dapi_cell_order):
		cell_id = map_cell[c]
		cell_id_to_dapi[cell_id] = iv

	union_cell_id = sorted(set(cell_id_to_nissl.keys()) | set(cell_id_to_dapi.keys()))
	ct_reorder = []
	ct2_reorder = []
	domain_reorder = []
	Xcen_reorder = []
	for u in union_cell_id:
		ct_reorder.append(ct[u])
		ct2_reorder.append(ct2[u])
		domain_reorder.append(domain[u])
		Xcen_reorder.append(Xcen[u])

	ct_reorder = np.array(ct_reorder)
	ct2_reorder = np.array(ct2_reorder)
	domain_reorder = np.array(domain_reorder)
	Xcen_reorder = np.array(Xcen_reorder)
	num_cell = len(union_cell_id)	

	mat = np.zeros((num_cell, 4096*2), dtype="float64")
	dapi_input_dir = ""
	nissl_input_dir = ""
	impute_dapi_dir = ""
	impute_nissl_dir = ""

	basedir="%s" % prereq_dir

	#option==1: #low contrast, light background, preserves outline	
	#Option 2 #high contrast, dark background
	#option==3:	 #medium contrast, medium light background

	dapi_input_dir = "%s/option%d/feature_dapi" % (basedir, option)
	nissl_input_dir = "%s/option%d/feature_nissl" % (basedir, option)
	impute_dapi_dir = "%s/option%d/imputed_dapi" % (basedir, option)
	impute_nissl_dir = "%s/option%d/imputed_dapi" % (basedir, option)


	empty_npy = np.load("%s/image_zero_input.npy" % basedir)
	em_path = "%s/image_zero_input.npy" % basedir
	#empty_npy = np.load("image_zero_input.npy")
	#em_path = "image_zero_input.npy"
	fw = open("%s/png.file.list" % prereq_dir, "w")

	for iu,u in enumerate(union_cell_id):
		status_dapi = u in cell_id_to_dapi
		status_nissl = u in cell_id_to_nissl
		if status_dapi==True and status_nissl==True:
			t_id = cell_id_to_dapi[u]
			file1 = "%s/%d/%s.png.npy" % (dapi_input_dir, dapi_f_name[t_id][0], dapi_f_name[t_id][1])
			if not os.path.isfile(file1):
				print(file1, "Does not exist D=T N=T")
				mat[iu,0:4096] = empty_npy
				fw.write("%s" % em_path)
			else:
				mat[iu,0:4096] = np.load(file1)
				fw.write("%s" % file1)
			fw.write("\t")
			t_id = cell_id_to_nissl[u]
			file2 = "%s/%d/%s.png.npy" % (nissl_input_dir, nissl_f_name[t_id][0], nissl_f_name[t_id][1])
			if not os.path.isfile(file2):
				print(file2, "Does not exist D=T, N=T")
				mat[iu,4096:4096*2] = empty_npy
				fw.write("%s" % em_path)
			else:
				mat[iu,4096:4096*2] = np.load(file2)
				fw.write("%s" % file2)
			fw.write("\n")
		elif status_dapi==True and status_nissl==False:
			t_id = cell_id_to_dapi[u]
			file1 = "%s/%d/%s.png.npy" % (dapi_input_dir, dapi_f_name[t_id][0], dapi_f_name[t_id][1])
			if not os.path.isfile(file1):
				print(file1, "Does not exist D=T, N=F")
				mat[iu,0:4096] = empty_npy
				fw.write("%s" % em_path)
			else:
				mat[iu,0:4096] = np.load(file1)
				fw.write("%s" % file1)
			fw.write("\t")
			f_path = "%s/%d.png.npy" % (impute_nissl_dir, (u+1))
			if not os.path.isfile(f_path):
				print(f_path, "Does not exist D=T, N=F")
				mat[iu,4096:4096*2] = empty_npy
				fw.write("%s" % em_path)
			else:
				mat[iu,4096:4096*2] = np.load(f_path)
				fw.write("%s" % f_path)
			fw.write("\n")
		elif status_dapi==False and status_nissl==True:
			f_path = "%s/%d.png.npy" % (impute_dapi_dir, (u+1))
			if not os.path.isfile(f_path):
				print(f_path, "does not exist D=F, N=F")
				mat[iu,0:4096] = empty_npy
				fw.write("%s" % em_path)
			else:
				mat[iu,0:4096] = np.load(f_path)
				fw.write("%s" % f_path)
			fw.write("\t")
			t_id = cell_id_to_nissl[u]
			file1 = "%s/%d/%s.png.npy" % (nissl_input_dir, nissl_f_name[t_id][0], nissl_f_name[t_id][1])
			if not os.path.isfile(file1):
				print(file1, "does not exist D=F, N=F")
				mat[iu,4096:4096*2] = empty_npy
				fw.write("%s" % em_path)
			else:
				mat[iu,4096:4096*2] = np.load(file1)
				fw.write("%s" % file1)
			fw.write("\n")
		else:
			print("Should not get here")
			mat[iu,0:4096] = np.load("%s/image_zero_input.npy" % basedir)
	fw.close()

	#mat = np.load("cell_img_feature.npy")
	mat2 = np.empty(mat.shape, dtype="float32")
	for i in range(mat2.shape[0]):
		for j in range(mat2.shape[1]):
			mat2[i,j] = mat[i,j]

	print(mat.shape, mat.dtype)
	print(np.max(mat), np.min(mat), np.mean(mat))
	
	f_mat2 = mat2.flatten()
	fw = open("/tmp/xa.dapi", "w")
	for i in range(f_mat2.shape[0]):
		fw.write(str(f_mat2[i]) + "\n")
	fw.close()
	
	min_val = 0.0001
	if log:
		mat2 = np.log2(mat2+min_val)

	if filter_feature:
		#tx = np.percentile(mat2, [80, 82, 84, 86, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
		num_valid = np.empty((mat2.shape[1]), dtype="float32")
		for i in range(mat2.shape[1]):
			m = np.where((mat2[:,i]>=-1.0) & (np.std(mat2[:,i])>0) & (np.std(mat2[:,i])!=0))[0]
			num_valid[i] = m.shape[0]

		fw = open("/tmp/xa.2", "w")
		for i in range(mat2.shape[1]):
			fw.write(str(num_valid[i]) + "\n")
		fw.close()

	#do just one zscore old
	if zscore1:
		mat2 = scipy.stats.zscore(mat2, axis=0)

	#mat2 = scipy.stats.zscore(mat2, axis=1)

	#print tx
	#tx_avg = np.mean(mat2, axis=0)
	#for i in range(tx_avg.shape[0]):
	#	print i, tx_avg[i]
	#good_id = np.where(tx_avg>0.1)[0]
	#good_id = np.where(num_valid>=50)[0] #good
	#good_id = np.where(num_valid>=120)[0]
	#good_id = np.where(num_valid>=150)[0]
	#print good_id.shape

	#print mat2.shape
	#mat2 = mat2[:, good_id]
	print(mat2.shape)

	return mat2, ct_reorder, ct2_reorder, domain_reorder, Xcen_reorder, num_cell
