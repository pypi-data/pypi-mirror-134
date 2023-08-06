import math
import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
sys.setrecursionlimit(10000)
from sklearn import svm
import scanpy as sc
import load_seqfishplus_new
import argparse

def do_and_plot_leiden(mat, file_prefix="mat1", outdir="."):
	adata = sc.AnnData(X=mat)
	sc.pp.neighbors(adata, use_rep='X', metric="cosine", n_neighbors=50, random_state=None)
	print("Done pp neighbors")
	sc.tl.umap(adata, min_dist=0.1, random_state=None)
	print("Done umap")
	sc.tl.leiden(adata, resolution=1.0, key_added = "leiden_1.0")
	print("Done leiden 1.0")
	sc.tl.leiden(adata, resolution=1.4, key_added = "leiden_1.4")
	print("Done leiden 1.4")
	sc.tl.leiden(adata, resolution=2.0, key_added = "leiden_2.0")
	print("Done leiden 2.0")
	sc.tl.leiden(adata, resolution=2.5, key_added = "leiden_2.5")
	print("Done leiden 2.5")
	#sc.pl.umap(adata, color=['leiden_1.0','leiden_1.4', 'leiden_2.0', "leiden_2.5"])
	sc.pl.umap(adata, color=['leiden_2.0', "leiden_2.5"])
	adata.obs["leiden_1.0"].to_csv("test.%s.leiden.1.0.csv" % file_prefix)
	adata.obs["leiden_1.4"].to_csv("test.%s.leiden.1.4.csv" % file_prefix)
	adata.obs["leiden_2.0"].to_csv("test.%s.leiden.2.0.csv" % file_prefix)
	adata.obs["leiden_2.5"].to_csv("test.%s.leiden.2.5.csv" % file_prefix)
	adata.write("%s/%s.h5ad" % (outdir, file_prefix), compression="gzip")

	return adata

def read_adata(h5ad_file):
	binary_file = h5ad_file
	adata = sc.read_h5ad(binary_file)
	return adata

def feature_aggregation(mat, adata, key="leiden_2.0", sigmoid=True):
	mat2 = mat
	adata.obs[key].to_csv("/tmp/%s.csv" % key)

	px_int = pd.read_csv("/tmp/%s.csv" % key, index_col=0, dtype="int32").to_numpy().flatten()
	t_max = np.max(px_int)
	#aggregate to feature clusters (t_max+1)
	agg_mat = np.empty((mat2.shape[0], t_max+1), dtype="float32")
	for i in range(t_max+1):
		t_ids = np.where(px_int==i)[0]
		Y = np.zeros((px_int.shape[0]), dtype="int32")
		Y[t_ids] = 1
		X = np.transpose(mat2)
		clf = svm.LinearSVC(class_weight="balanced", dual=False, C=1e-5, verbose=0, max_iter=10000, tol=1e-4, random_state=100)
		clf.fit(X, Y)
		coef = clf.coef_
		#z = coef
		if sigmoid:
			z = 1/(1+np.exp(-coef))
		else:
			z = coef
		print(i, "Done")
		agg_mat[:,i] = z
	return agg_mat	
		
