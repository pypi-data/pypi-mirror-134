from setuptools import setup, find_packages


long_description = "\n" + open('README.md').read()

VERSION = '0.0.35'
DESCRIPTION = 'Simple PDF editing made fast'

# Setting up
setup(
    name="PDFpy",
    version=VERSION,
    author="JonasHri",
    author_email="jonasharriehausen@gmail.com",
    license="MIT",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['PyPDF2'],
    keywords=['python', 'PDF', 'PDFpy'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)