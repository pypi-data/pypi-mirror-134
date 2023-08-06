import setuptools

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sfe",
    version="0.5",
    author="haoy_zhang",
    author_email="haoy.zhang@foxmail.com",
    description="Python and finite Elements",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/yonvone/sfe.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    extras_require={"sfe": ["python"]},
)
