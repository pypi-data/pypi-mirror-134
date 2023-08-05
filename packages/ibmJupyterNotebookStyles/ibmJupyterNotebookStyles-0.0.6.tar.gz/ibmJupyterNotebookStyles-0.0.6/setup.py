from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = "0.0.6"
DESCRIPTION = "IBM Jupyter Notebook Styles"
LONG_DESCRIPTION = "A package for styling jupyter notebooks using the IBM design guidelines. Within your jupyter notebooks run these lines of code: import ibmJupyterNotebookStyles && ibmJupyterNotebookStyles.apply_ibm_styles()"

# Setting up
setup(
    name="ibmJupyterNotebookStyles",
    version=VERSION,
    author="(IBM)",
    author_email="<ionut.chereji@ro.ibm.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=["tests*","doc*"]),
    install_requires=["matplotlib"],
    keywords=["ibm", "style"],
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    package_data={'': ['ibm.mplstyle']},
)