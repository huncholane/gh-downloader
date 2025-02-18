from setuptools import setup, find_packages

setup(
    name="gh-downloader",
    version="0.1",
    packages=find_packages(),
    py_modules=["main"],
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "gh-downloader=main:main",
        ],
    },
)
