import setuptools
 
f = open("README.md", "r", encoding="utf-8")
long_description = f.read()
f.close()

#for formal
setuptools.setup(
    name="xyj_database",
    version="0.1",
    author="Yijie Xia",  
    author_email="yijiexia@pku.edu.cn", 
    description="A package for show data",
    long_description=long_description, 
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    package_data = {"":['*.html', "*.csv"]},
    install_requires = ["flask"],
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6', 
)
