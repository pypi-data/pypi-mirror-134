import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname("__file__"))

version = {}
with open(os.path.join(here, "ghproject", "__version__.py")) as f:
    exec(f.read(), version)

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="ghproject",
    version=version["__version__"],
    description="Tool for uploading project boards to GitHub",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/mwakok/ghproject",
    author="Maurits Kok",
    author_email="mwakok@gmail.com",
    license="Apache Software License 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    test_suite="tests",
    packages=find_packages(exclude=["*tests*"]),
    python_requires=">=3.7,<3.9",
    include_package_data=True,
    install_requires=["python-frontmatter", "requests>=2.24.0"],
    extras_require={
        "dev": [
            "black",
            "bump2version",
            "isort",
            "pre_commit",
            "pytest",
            "pytest-cov",
            "sphinx",
            "sphinx-rtd-theme",
        ]
    },
)
