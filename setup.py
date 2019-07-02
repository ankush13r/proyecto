import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="robotankush",
    version="1.0.2",
    author="Ankush Rana",
    author_email="ankush.ran13@gmail.com",
    description="This is just a test for uploading proyect",
    long_description=long_description,
    long_description_content_type="",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
