import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trifledb",
    version="0.1.1.dev0",
    author="Shankar Arunachalam",
    author_email="shankar.arunachalam@gmail.com",
    description="A stupid simple key value store with an API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shankararunachalam/trifledb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
    	'gunicorn',
	'uvicorn[standard]',
	'fastapi',
	'fastapi-versioning',
	'requests',
	'pytest'
    ],
)