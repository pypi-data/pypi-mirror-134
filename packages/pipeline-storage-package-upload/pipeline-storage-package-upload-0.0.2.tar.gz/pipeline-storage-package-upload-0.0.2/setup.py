"""Setup script for demo-upload-package"""

# Standard library imports
import pathlib

# Third party imports
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).resolve().parent

# The text of the README file is used as a description
README = (HERE / "README-pypi-upload.md").read_text()

# This call to setup() does all the work
setup(
    name="pipeline-storage-package-upload",
    version="0.0.2",
    description="Pipeline storage demo on how to upload to Artifactory",
#    long_description=README,
#     long_description_content_type="text/markdown",
#     url="https://github.service.anz/loughlil/artifactory-upload-examples",
#     author="Pipeline storage",
#     author_email="info@storage.com",
#     license="MIT",
#     keywords=['artifactory'],
#     classifiers=[
# 	'Development Status :: 3 - Alpha',  
#     	'Intended Audience :: Developers',      # Define that your audience are developers
#     	'Topic :: Software Development :: Build Tools',	
#         "License :: OSI Approved :: MIT License",
#         "Programming Language :: Python :: 3",  # Specify the versions of python you want to support.
#     ],
#     packages=["storagedemo"],
#     include_package_data=True,
#     install_requires=[""],
    #entry_points={"console_scripts": ["pypi-example=storage-demo.__main__:main"]},
)
