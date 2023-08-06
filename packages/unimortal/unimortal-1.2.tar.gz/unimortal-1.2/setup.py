import setuptools


with open("requirements.txt") as f:
    requirements = []
    for library in f.read().splitlines():
        requirements.append(library)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(

    name="unimortal",
    version="1.2",
    author="Gouri Birije, Katarzyna Jagoda, Hanieh Fasihy",
    author_email="blahblah@gmail.com",    
    description="Tools to get inference from the Global Mortality Rate in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={"unimortal": ["package_data/*.*"]},    
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",        
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6.9',
    install_requires=requirements,
    
)