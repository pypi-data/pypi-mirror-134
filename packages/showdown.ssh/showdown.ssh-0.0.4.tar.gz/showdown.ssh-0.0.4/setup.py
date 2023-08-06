import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="showdown.ssh",
    version="0.0.4",
    author="Boshimoto",
    license="MIT License",
    author_email="author@example.com",
    description="A tool to automate local network health checks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/boshimoto/showdown",
    project_urls={
        "Bug Tracker": "https://github.com/boshimoto/showdown/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "showdown"},
    install_requires=[
        'netmiko',
    ],
    packages=setuptools.find_packages(where="showdown"),
    python_requires=">=3.6",
)