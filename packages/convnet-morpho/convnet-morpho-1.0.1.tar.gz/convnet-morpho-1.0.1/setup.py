import subprocess
from distutils.command.build import build as _build
import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

# This class handles the pip install mechanism.
class build(_build):  # pylint: disable=invalid-name
  sub_commands = _build.sub_commands + [("CustomCommands", None)]

CUSTOM_COMMANDS = [
	["libdir=`ls -1 build|grep \"lib\"`; cd build/$libdir/convnet_morpho/ && touch finished"]]

class CustomCommands(setuptools.Command):
  """A setuptools Command class able to run arbitrary commands."""

  def initialize_options(self):
    pass

  def finalize_options(self):
    pass

  def RunCustomCommand(self, command_list):
    print("Running command: %s" % command_list)
    p = subprocess.Popen(
        command_list,
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    # Can use communicate(input='y\n'.encode()) if the command run requires
    # some confirmation.
    stdout_data, _ = p.communicate()
    print("Command output: %s" % stdout_data)
    if p.returncode != 0:
      raise RuntimeError(
          "Command %s failed: exit code: %s" % (command_list, p.returncode))

  def run(self):
    for command in CUSTOM_COMMANDS:
      self.RunCustomCommand(command)

setuptools.setup(
	name="convnet-morpho",
	version="1.0.1",
	author="Qian Zhu",
	author_email="qian_zhu@dfci.harvard.edu",
	description="convnet-morpho is a cell morphology analysis library",
	long_description="It includes functions to read and process cell segmentations, that are made either from automatic or manual segmentations. It also includes a deep-learning based morphology analysis library - for this it uses the convolutional neural network AlexNet for image feature extraction. Finally it contains feature aggregation, dimensionality reduction and visualization, and a module for integrative and joint analysis of morphology and gene expression.",
	long_description_content_type="text/markdown",
	url="https://bitbucket.org/qzhudfci/convnet.morpho",
	packages=setuptools.find_packages(),
	entry_points = {
		"console_scripts": [
			"about_convnet_morpho = convnet_morpho.about_convnet_morpho:main"
		]
	},
	classifiers=(
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	),
	python_requires=">=3.6",
	package_data={"convnet_morpho":  ["cluster.py", "path.py", 
		"convnet.py", "crop.py", "load_brain1_new.py", "load_brain2_new.py",
		"load_seqfishplus_new.py", "reader.py"]}, 

	install_requires=[
		"scipy", "numpy", "pandas", "seaborn", "matplotlib", "jsbeautifier"],
	cmdclass={
		"build": build,
		"CustomCommands": CustomCommands,
		}	
)
	
