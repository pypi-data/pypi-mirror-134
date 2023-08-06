import setuptools

setuptools.setup(
    name='youpi',
    version='0.1',
    author='Gabriel-Dropout',
    author_email='winterday0210@gmail.com',
    description='Very light and incredibly simple python library for downloading youtube video. It was inspired by pytube.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/Gabriel-Dropout/youpi',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)