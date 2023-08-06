from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()


if __name__ == "__main__":
    setup(
        name="mlcutter",
        version="0.0.1",
        description="mlcutter",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Abhishek Thakur",
        author_email="abhishek4@gmail.com",
        url="https://github.com/abhishekkrthakur/mlcutter",
        license="Apache License",
        packages=find_packages(),
        include_package_data=True,
        platforms=["linux", "unix"],
        python_requires=">3.5.2",
    )
