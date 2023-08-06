import setuptools
import json

# def next_version()->str:
#     config_key = "package_version"
#     with open("version.json", "r", encoding="utf-8") as fh:
#         version_config = json.loads(fh.read())
#     split_version = version_config.get(config_key).split(".")
#     # Increase minor version
#     split_version[-1] = str(int(split_version[-1]) + 1)
#     version_config[config_key] =  ".".join(split_version)
#     with open("version.json", "w", encoding="utf-8") as fh:
#         fh.write(json.dumps(version_config, indent=4))
#     return version_config.get(config_key)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="otmcm-backend",
    version="0.0.21",
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