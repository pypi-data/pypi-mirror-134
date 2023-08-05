import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="otmcm-backend",
    version="0.0.4",
    author="Huan Tran",
    author_email="huankimtran@gmail.com",
    description="Backend package for otmcm algotrading environment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/huankimtran/OTMCM",
    project_urls={
        "Bug Tracker": "https://github.com/huankimtran/OTMCM",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "pyzmq >= 18.1.1"
    ],
    scripts=[
        "bin/otmcm_launch.py"
    ]
)