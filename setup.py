from setuptools import find_namespace_packages, setup

setup(
    author="vmttn",
    name="data-inclusion-schema",
    url="https://github.com/betagouv/data-inclusion-schema",
    version="0.2.0",
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pydantic[email]==1.9.0",
    ],
    extras_require={
        "dev": [
            "black==22.3.0",
            "pre-commit==2.18.1",
        ],
    },
    entry_points={
        "console_scripts": ["data-inclusion-schema=data_inclusion.schema.__main__:main"]
    },
)
