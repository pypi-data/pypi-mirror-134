import setuptools, os

with open("PYPI_README.md", "r") as fh:
    long_description = fh.read()

apiVersion = ""
try:
    apiVersion = os.environ["DOM_API_APIVERSION"]
except: pass

setuptools.setup(
    name="DomApi",
    version=apiVersion,
    author="James Truxon",
    author_email="contact@jamestruxon.com",
    description="Python tool for completion time analysis of batch pizza orders",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jtruxon/DomApi",
    #download_url="https://github.com/jtruxon/DomApi/dist/DomApi-0.0.1.tar.gz",
    include_package_data=True,
    package_data={"": ["resources/*"],}, #https://setuptools.pypa.io/en/latest/userguide/datafiles.html
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=[],
    test_suite='tests',
    install_requires=['werkzeug==0.16.1', 'flask==1.1.4', 'flask-restplus', 'jsonschema', 'gunicorn', 'pytest'],
)

