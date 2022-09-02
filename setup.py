from doctest import testsource
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="userwatch-python",
    version="0.0.5",
    author="Userwatch",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["userwatch", "google/type"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    py_modules=["userwatch", "google/type"],
    package_dir={'': 'src/'},
    install_requires=["grpcio>=1.30", "protobuf>=4.0"],
    setup_requires=['pytest-runner'],
    test_suites=['tests']
)
