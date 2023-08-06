#!/usr/bin/python
import sys
import os
import numpy as np
import wget
from operator import itemgetter
sys.setrecursionlimit(10000)
from zipfile import ZipFile

def read_cell_type(n, n2): #n2 is annot file
	f = open(n2)
	id_to_name, name_to_id = {}, {}
	for l in f:
		l = l.rstrip("\n")
		ll = l.split("\t")
		id_to_name[ll[0]] = ll[1]
		name_to_id[ll[1]] = ll[0]
	f.close()
	f = open(n)
	mm = []
	cell_annot = []
	map_cell = {}
	ix = 0
	for l in f:
		l = l.rstrip("\n")
		ll = l.split(" ")
		mm_id = ll[0]
		mm.append(id_to_name[mm_id])
		cell_annot.append(str(ix+1))
		map_cell[str(ix+1)] = ix
		ix += 1
	f.close()
	ct_uniq = np.unique(mm)
	map_id = {}
	for ind,val in enumerate(ct_uniq):
		map_id[val] = ind+1
	mm_annot = []
	for c in mm:
		mm_annot.append(map_id[c])
	print(map_id)
	return mm_annot, map_cell

def read_domain(n):
	f = open(n)
	mm = []
	for l in f:
		l = l.rstrip("\n")
		ll = l.split(" ")
		#mm.append(int(ll[1]))
		mm.append(int(ll[0]))
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
		st = list(zip(true_label, dec[:,c]))
		#st.sort(lambda x,y: cmp(x[1], y[1]), reverse=True)
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
	r_label = list(range(num_class))
	for t in t_map:
		r_label[list(t_map[t])[0]] = t
	return r_label

def read_coord(n):
	f = open(n)
	h = f.readline().rstrip().split(",")
	ncell = 0
	for l in f:
		l = l.rstrip("\n")
		ncell+=1
	f.close()
	#Xcen = np.empty((ncell+1, 2), dtype="float32")
	Xcen = np.empty((ncell, 2), dtype="float32")
	ind = 0
	f = open(n)
	f.readline()
	#Xcen[0,:] = [-1,-1]
	for l in f:
		l = l.rstrip("\n")
		ll = l.split(",")
		dd = dict(zip(h, ll))
		#Xcen[ind+1,:] = [float(dd["Stitched_X"]), -1.0*float(dd["Stitched_Y"])]
		Xcen[ind,:] = [float(dd["Stitched_X"]), -1.0*float(dd["Stitched_Y"])]
		ind+=1
	f.close()
	return Xcen

def load_density(filter_feature=False, filter_cutoff=50, log=False, use_density=False, use_dir=None):
	domain = read_domain("seqfishplus/test.hmrf.oct14.spatial.0.99.top200.b30.0.k9.cluster.txt")
	ct, map_cell = read_cell_type("seqfishplus/test.cell.type.unsupervised.id.txt", "seqfishplus/test.cell.type.unsupervised.id.annot")
	Xcen = read_coord("seqfishplus/cell.centroid.stitched.pos.all.cells.good.txt")

	ct_reorder = np.array(ct)
	domain_reorder = np.array(domain)
	Xcen_reorder = Xcen

	num_cell = Xcen_reorder.shape[0]

	#input_dir = "features/RNA.distr/feature"
	input_dir = "seqfishplus/RNA.distr.feature"
	if use_density:
		#input_dir = "features/RNA.distr.density.6/feature"
		input_dir = "seqfishplus/RNA.distr.density.6.feature"
	if use_dir is not None:
		input_dir = use_dir

	mat = np.empty((num_cell, 4096), dtype="float64")
	for i in range(1, num_cell+1):
		file1 = "%s/%s.png.npy" % (input_dir, i)
		mat[i-1,:] = np.load(file1)

	return mat, ct_reorder, domain_reorder, Xcen_reorder, num_cell


def load_one(filter_feature=False, filter_cutoff=50, log=False, load="nissl", use_equalize=False): #load can also be dapi
	dapi_cell_order, dapi_f_name = read_map("seqfishplus/all.distances.dapi.txt")
	nissl_cell_order, nissl_f_name = read_map("seqfishplus/all.distances.nissl.txt")
	domain = read_domain("seqfishplus/test.hmrf.oct14.spatial.0.99.top200.b30.0.k9.cluster.txt")
	ct, map_cell = read_cell_type("seqfishplus/test.cell.type.unsupervised.id.txt", "seqfishplus/test.cell.type.unsupervised.id.annot")
	Xcen = read_coord("seqfishplus/cell.centroid.stitched.pos.all.cells.good.txt")

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
	domain_reorder = []
	Xcen_reorder = []
	for u in union_cell_id:
		ct_reorder.append(ct[u])
		domain_reorder.append(domain[u])
		Xcen_reorder.append(Xcen[u])

	ct_reorder = np.array(ct_reorder)
	domain_reorder = np.array(domain_reorder)
	Xcen_reorder = np.array(Xcen_reorder)
	num_cell = len(union_cell_id)	

	mat = np.zeros((num_cell, 4096), dtype="float64")
	#input===================================
	#dapi_input_dir = "features/dapi/feature"
	#nissl_input_dir = "features/nissl/feature"
	#impute_dapi_dir = "features/imputed_dapi"
	#impute_nissl_dir = "features/imputed_nissl"
	dapi_input_dir = "seqfishplus/features/feature_dapi"
	nissl_input_dir = "seqfishplus/features/feature_nissl"
	impute_dapi_dir = "seqfishplus/features/imputed_dapi"
	impute_nissl_dir = "seqfishplus/features/imputed_nissl"
	#========================================
	if use_equalize:
		#dapi_input_dir = "features_oct6/dapi_oct6/feature"
		#nissl_input_dir = "features_oct6/nissl_oct6/feature"
		#impute_dapi_dir = "features_oct6/imputed_dapi_oct6"
		#impute_nissl_dir = "features_oct6/imputed_nissl_oct6"
		dapi_input_dir = "seqfishplus/features_equalize/feature_dapi"
		nissl_input_dir = "seqfishplus/features_equalize/feature_nissl"
		impute_dapi_dir = "seqfishplus/features_equalize/imputed_dapi"
		impute_nissl_dir = "seqfishplus/features_equalize/imputed_nissl"

	empty_npy = np.load("image_zero_input.npy")

	for iu,u in enumerate(union_cell_id):
		status_dapi = u in cell_id_to_dapi
		status_nissl = u in cell_id_to_nissl

		if status_dapi==True and status_nissl==True:
			if load=="dapi":
				t_id = cell_id_to_dapi[u]
				file1 = "%s/%d/%s.png.npy" % (dapi_input_dir, dapi_f_name[t_id][0], dapi_f_name[t_id][1])
				if not os.path.isfile(file1):
					print(file1, "Does not exist D=T N=T")
					mat[iu,:] = empty_npy
				else:
					mat[iu,:] = np.load(file1)
			elif load=="nissl":
				t_id = cell_id_to_nissl[u]
				file2 = "%s/%d/%s.png.npy" % (nissl_input_dir, nissl_f_name[t_id][0], nissl_f_name[t_id][1])
				if not os.path.isfile(file2):
					print(file2, "Does not exist D=T, N=T")
					mat[iu,:] = empty_npy
				else:
					mat[iu,:] = np.load(file2)

		elif status_dapi==True and status_nissl==False:

			if load=="dapi":
				t_id = cell_id_to_dapi[u]
				file1 = "%s/%d/%s.png.npy" % (dapi_input_dir, dapi_f_name[t_id][0], dapi_f_name[t_id][1])
				if not os.path.isfile(file1):
					print(file1, "Does not exist D=T, N=F")
					mat[iu,:] = empty_npy
				else:
					mat[iu,:] = np.load(file1)
			elif load=="nissl":
				f_path = "%s/%d.png.npy" % (impute_nissl_dir, (u+1))
				if not os.path.isfile(f_path):
					print(f_path, "Does not exist D=T, N=F")
					mat[iu,:] = empty_npy
				else:
					mat[iu,:] = np.load(f_path)
		elif status_dapi==False and status_nissl==True:

			if load=="dapi":
				f_path = "%s/%d.png.npy" % (impute_dapi_dir, (u+1))
				if not os.path.isfile(f_path):
					print(f_path, "does not exist D=F, N=F")
					mat[iu,:] = empty_npy
				else:
					mat[iu,:] = np.load(f_path)
			elif load=="nissl":
				t_id = cell_id_to_nissl[u]
				file1 = "%s/%d/%s.png.npy" % (nissl_input_dir, nissl_f_name[t_id][0], nissl_f_name[t_id][1])
				if not os.path.isfile(file1):
					print(file1, "does not exist D=F, N=F")
					mat[iu,:] = empty_npy
				else:
					mat[iu,:] = np.load(file1)
		else:
			print("Should not get here")
			mat[iu,:] = np.load("image_zero_input.npy")

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

	#tx_avg = np.mean(mat2, axis=0)

	if filter_feature:
		good_id = np.where(num_valid>=filter_cutoff)[0] #filter_cutoff is 50
		mat2 = mat2[:, good_id]

	print(mat2.shape)

	#return mat2, ct_reorder, ct2_reorder, domain_reorder, Xcen_reorder, num_cell
	return mat2, ct_reorder, domain_reorder, Xcen_reorder, num_cell

def download(outdir="seqfishplus.segmented"):
	url = "https://bitbucket.org/qzhudfci/convnet.morpho/raw/b3abc7aad1b6c614a023e817ae04d51db0ba5f6b/seqfishplus"
	flist = ["all.distances.dapi.txt", "all.distances.nissl.txt", "test.hmrf.oct14.spatial.0.99.top200.b30.0.k9.cluster.txt", \
	"test.cell.type.unsupervised.id.txt", "test.cell.type.unsupervised.id.annot", "cell.centroid.stitched.pos.all.cells.good.txt"]

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

	url = "https://zenodo.org/record/4539873/files/seqfishplus.image.data.zip?download=1"
	dlist = ["features", "features_equalize", "features_shape", "features_texture", "RNA.distr.density.6.feature", "RNA.distr.feature"]
	is_exist = True
	for aDir in dlist:
		t_path = "%s/%s" % (outdir, aDir)
		if os.path.isdir(t_path):
			print("Directory %s already exists. skipped" % t_path)
		else:
			is_exist = False
	if not is_exist:
		if os.path.exists("%s/seqfishplus.image.data.zip" % outdir):
			print("File %s alrady exists, skipped." % "seqfishplus.image.data.zip")
		else:
			print("Downloading seqfishplus.image.data.zip...") 
			wget.download(url, out="%s/seqfishplus.image.data.zip" % outdir)
		with ZipFile("%s/seqfishplus.image.data.zip" % outdir, "r") as zipObj:
			zipObj.extractall("%s" % outdir)	
	print("Done")

def load(filter_feature=False, filter_cutoff=50, log=False, is_shape=False, use_equalize=False, is_texture=False, prereq_dir="seqfishplus.segmented"):
	flist = ["all.distances.dapi.txt", "all.distances.nissl.txt", "test.hmrf.oct14.spatial.0.99.top200.b30.0.k9.cluster.txt", \
	"test.cell.type.unsupervised.id.txt", "test.cell.type.unsupervised.id.annot", "cell.centroid.stitched.pos.all.cells.good.txt"]
	dlist = ["features", "features_equalize", "features_shape", "features_texture"]
	for aFile in flist:
		t_path = "%s/%s" % (prereq_dir, aFile)
		if not os.path.exists(t_path):
			print("Error some pre-requisite files not found: %s. Call load_seqfishplus_new.download() to download first." % t_path)
			sys.exit(1)
	for aDir in dlist:
		t_path = "%s/%s" % (prereq_dir, aDir)
		if not os.path.isdir(t_path):
			print("Error directory not found: %s. Call load_seqfishplus_new.download() to download first." % t_path)
			sys.exit(1)

	dapi_cell_order, dapi_f_name = read_map("%s/all.distances.dapi.txt" % prereq_dir)
	nissl_cell_order, nissl_f_name = read_map("%s/all.distances.nissl.txt" % prereq_dir)
	domain = read_domain("%s/test.hmrf.oct14.spatial.0.99.top200.b30.0.k9.cluster.txt" % prereq_dir)
	ct, map_cell = read_cell_type("%s/test.cell.type.unsupervised.id.txt" % prereq_dir, "%s/test.cell.type.unsupervised.id.annot" % prereq_dir)
	Xcen = read_coord("%s/cell.centroid.stitched.pos.all.cells.good.txt" % prereq_dir)

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
	domain_reorder = []
	Xcen_reorder = []
	for u in union_cell_id:
		ct_reorder.append(ct[u])
		domain_reorder.append(domain[u])
		Xcen_reorder.append(Xcen[u])

	ct_reorder = np.array(ct_reorder)
	domain_reorder = np.array(domain_reorder)
	Xcen_reorder = np.array(Xcen_reorder)
	num_cell = len(union_cell_id)	

	mat = np.zeros((num_cell, 4096*2), dtype="float64")
	keyword = "features"
	basedir="%s" % prereq_dir

	if use_equalize:
		keyword = "features_equalize"
	elif is_texture:
		keyword = "features_texture"
	elif is_shape:
		keyword = "features_shape"
		 
	#input===================================
	dapi_input_dir = "%s/%s/feature_dapi" % (basedir, keyword)
	nissl_input_dir = "%s/%s/feature_nissl" % (basedir, keyword)
	impute_dapi_dir = "%s/%s/imputed_dapi" % (basedir, keyword)
	impute_nissl_dir = "%s/%s/imputed_nissl" % (basedir, keyword)
	#========================================

	empty_npy = np.load("%s/image_zero_input.npy" % basedir)

	for iu,u in enumerate(union_cell_id):
		status_dapi = u in cell_id_to_dapi
		status_nissl = u in cell_id_to_nissl

		if status_dapi==True and status_nissl==True:
			t_id = cell_id_to_dapi[u]
			file1 = "%s/%d/%s.png.npy" % (dapi_input_dir, dapi_f_name[t_id][0], dapi_f_name[t_id][1])
			if not os.path.isfile(file1):
				print(file1, "Does not exist D=T N=T")
				mat[iu,0:4096] = empty_npy
			else:
				mat[iu,0:4096] = np.load(file1)
			t_id = cell_id_to_nissl[u]
			file2 = "%s/%d/%s.png.npy" % (nissl_input_dir, nissl_f_name[t_id][0], nissl_f_name[t_id][1])
			if not os.path.isfile(file2):
				print(file2, "Does not exist D=T, N=T")
				mat[iu,4096:4096*2] = empty_npy
			else:
				mat[iu,4096:4096*2] = np.load(file2)
		elif status_dapi==True and status_nissl==False:
			t_id = cell_id_to_dapi[u]
			file1 = "%s/%d/%s.png.npy" % (dapi_input_dir, dapi_f_name[t_id][0], dapi_f_name[t_id][1])
			if not os.path.isfile(file1):
				print(file1, "Does not exist D=T, N=F")
				mat[iu,0:4096] = empty_npy
			else:
				mat[iu,0:4096] = np.load(file1)
			f_path = "%s/%d.png.npy" % (impute_nissl_dir, (u+1))
			if not os.path.isfile(f_path):
				print(f_path, "Does not exist D=T, N=F")
				mat[iu,4096:4096*2] = empty_npy
			else:
				mat[iu,4096:4096*2] = np.load(f_path)
		elif status_dapi==False and status_nissl==True:
			f_path = "%s/%d.png.npy" % (impute_dapi_dir, (u+1))
			if not os.path.isfile(f_path):
				print(f_path, "does not exist D=F, N=F")
				mat[iu,0:4096] = empty_npy
			else:
				mat[iu,0:4096] = np.load(f_path)
			t_id = cell_id_to_nissl[u]
			file1 = "%s/%d/%s.png.npy" % (nissl_input_dir, nissl_f_name[t_id][0], nissl_f_name[t_id][1])
			if not os.path.isfile(file1):
				print(file1, "does not exist D=F, N=F")
				mat[iu,4096:4096*2] = empty_npy
			else:
				mat[iu,4096:4096*2] = np.load(file1)
		else:
			print("Should not get here")
			mat[iu,0:4096] = np.load("%s/image_zero_input.npy" % basedir)

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

	#print "good", mat2[:,0]
	#print "good", mat2[:,1]

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

	#mat2 = scipy.stats.zscore(mat2, axis=0)
	#mat2 = scipy.stats.zscore(mat2, axis=1)
	#print tx
	#tx_avg = np.mean(mat2, axis=0)
	#for i in range(tx_avg.shape[0]):
	#	print i, tx_avg[i]
	#good_id = np.where(tx_avg>0.1)[0]

	if filter_feature:
		#prev used
		good_id = np.where(num_valid>=filter_cutoff)[0] #filter_cutoff is 50
		#good_id = np.where(num_valid>=120)[0]
		#good_id = np.where(num_valid>=150)[0]
		#print good_id.shape
		#print mat2.shape
		#prev used
		mat2 = mat2[:, good_id]

	print(mat2.shape)

	#return mat2, ct_reorder, ct2_reorder, domain_reorder, Xcen_reorder, num_cell
	return mat2, ct_reorder, domain_reorder, Xcen_reorder, num_cell
