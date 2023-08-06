from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()


if __name__ == "__main__":
    setup(
        name="kolab",
        description="kolab",
        long_description=long_description,
        long_description_content_type="text/markdown",
        entry_points={"console_scripts": ["kolab=kolab.cli.kolab:main"]},
        author="Abhishek Thakur",
        url="https://github.com/abhishekkrthakur/kolab",
        license="Apache License",
        packages=find_packages(),
        include_package_data=True,
        platforms=["linux", "unix"],
        python_requires=">3.5.2",
    )
