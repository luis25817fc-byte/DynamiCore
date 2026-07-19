from setuptools import setup, find_packages

setup(
    name="dynamicore",
    version="1.0.0",
    author="Luis Daniel Flores Segura",
    description="High-performance deterministic structural dynamics engine",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "fastapi",
        "pydantic",
        "uvicorn"
    ],
    python_requires=">=3.10",
    license="MIT",
)
