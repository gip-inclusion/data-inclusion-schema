from setuptools import find_namespace_packages, setup

setup(
    author="vmttn",
    name="data-inclusion-schema",
    url="https://github.com/betagouv/data-inclusion-schema",
    version="0.4.0",
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pydantic[email]>=1.9.1",
    ],
    extras_require={
        "dev": [
            "black==22.10.0",
            "pre-commit==2.20.0",
        ],
    },
    entry_points={
        "console_scripts": ["data-inclusion-schema=data_inclusion.schema.__main__:main"]
    },
)
