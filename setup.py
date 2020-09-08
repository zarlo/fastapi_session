import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()


setuptools.setup(
    name="fastapi-session",
    version="0.2.5",
    author="Zarlo",
    author_email="5899@zarlo.dev",
    descritpion="session for FastAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zarlo/faskapi_session",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        "fastapi"
    ],
    zip_safe=False,
    include_package_data=True
)