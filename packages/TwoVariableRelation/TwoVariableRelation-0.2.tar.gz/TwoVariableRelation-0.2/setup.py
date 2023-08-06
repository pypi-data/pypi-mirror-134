import setuptools
with open("README.md","r") as fh:
	long_description=fh.read()
setuptools.setup(
    name="TwoVariableRelation",                     
    version="0.2",                       
    author="Aanal Shah,Shalini",                     
    description="TwoVariableRelation Package is intended to establish the relationship between two features of the dataset.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    py_modules=["TwoVariableRelation"],             
    package_dir={'':'src'},     
                        
)



