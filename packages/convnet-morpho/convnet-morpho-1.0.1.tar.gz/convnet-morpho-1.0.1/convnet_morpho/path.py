import subprocess
from requests_html import HTMLSession
import os
import sys
import wget

def extract_path_svg(files, srcdir=".", outdir="output"):

	url = "https://bitbucket.org/qzhudfci/convnet.morpho/raw/b3abc7aad1b6c614a023e817ae04d51db0ba5f6b/web.util"
	flist = ["jquery-3.3.1.min.js", "view_svg.js", "view_svg.html"]

	if not os.path.isdir(outdir):
		os.mkdir(outdir)
	
	for aFile in flist:
		t_path = "%s/%s" % (outdir, aFile)
		if os.path.exists(t_path):
			print("File %s already exists, skipped." % t_path)
		else:
			print("Pre-requisite file missing.")
			print("Downloading %s..." % t_path)
			wget.download("%s/%s" % (url, aFile), out=t_path)

	if srcdir!=outdir:
		for aFile in files:
			if not os.path.exists("%s/%s" % (outdir, aFile)):
				os.symlink("%s/%s" % (srcdir, aFile), "%s/%s" % (outdir, aFile))

	print(os.getcwd())

	os.chdir(outdir)
	proc = subprocess.Popen([sys.executable, "-m", "http.server"])

	print("Sleeping for 5 seconds...")
	ls_output = subprocess.Popen(["sleep", "5"])
	ls_output.communicate()  # Will block for 5 seconds

	#files = ["Pos1niss.svg", "Pos2dap.svg", "Pos3dap.svg", "Pos3niss.svg", "Pos4dap.svg"]

	for aFile in files:
		print("Doing", aFile, "...")
		o2 = open("view_svg_good.html", "w")
		c2 = subprocess.Popen(["sed", "s/Pos4dap.svg/%s/g" % aFile, "view_svg.html"], stdout=o2)
		o2.close()

		session = HTMLSession()
		r = session.get("http://localhost:8000/view_svg_good.html")
		r.html.render(sleep=5)
		obj = r.html.find("#obj", first=True)
	
		fw = open("output_%s.txt" % aFile.split(".svg")[0], "w")
		fw.write(obj.text + "\n")
		fw.close()

	proc.terminate()
	print("Webserver terminated.")
