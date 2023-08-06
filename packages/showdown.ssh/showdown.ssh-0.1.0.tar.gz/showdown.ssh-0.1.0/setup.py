import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="showdown.ssh",
    version="0.1.0",
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
    packages=setuptools.find_packages(include=['showdown']),
    python_requires=">=3.8",
    install_requires=[
        "netmiko>=3.4.0",
        "setuptools>=60.5.0",
        "paramiko>=2.7.2",
        "scp>=0.13.6",
        "tenacity",
        "textfsm>=1.1.2",
        "ntc-templates>=2.1.0",
        "pyserial",
        "importlib_resources ; python_version<'3.8'",
    ],
)