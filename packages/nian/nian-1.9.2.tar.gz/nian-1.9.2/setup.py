import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nian",
    version="1.9.2",
    author="初慕苏流年",
    author_email="1274210585@qq.com",
    description="测试版本，音乐爬取",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://None/",
    classifiers=["Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    #package_dir={"": "nian"},
    packages=setuptools.find_packages(),
    python_requires=">=3.0",
)
