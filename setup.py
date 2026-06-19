from setuptools import setup, find_packages
import os

version = {}
with open("version.py", encoding="utf-8") as f:
    exec(f.read(), version)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirement_path = os.path.join(os.path.dirname(__file__), "requirements.txt")

install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn",
        "imbalanced-learn",
        "xgboost",
        "lightgbm"
    ],

if os.path.isfile(requirement_path):
    with open(requirement_path, encoding="utf-8") as f:
        install_requires = [line.strip() for line in f if line.strip() and not line.startswith("#")]


setup(
    name="multiclasspredict",
    version=version["__version__"],
    description="Multi Class Prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/usegalaxy-eu/MultiClassPredict",
    packages=find_packages(include=["multiclasspredict", "multiclasspredict.*"]),
    license="MIT",
    install_requires=install_requires,
    
    entry_points={
        "console_scripts": [
            "multiclasspredict=multiclasspredict.cli:cli"
        ]
    },

    include_package_data=True,
    python_requires=">=3.8",
)
