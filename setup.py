from doctest import testsource
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="userwatch-python",
    version="0.0.3",
    author="Userwatch",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(
        "src", exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    py_modules=["userwatch", "userwatch_public_pb2",
                "userwatch_shepherd_pb2", "userwatch_shepherd_pb2_grpc"],
    package_dir={'': 'src/'},
    install_requires=["grpcio>=1.30", "protobuf>=3.0"],
    setup_requires=['pytest-runner'],
    test_suites=['tests']
)
