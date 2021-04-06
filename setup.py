import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

def build(name, version, descritpion, packages, install_requires = []):
    setuptools.setup(
        name=name,
        version=version,
        author="Zarlo",
        author_email="5899@zarlo.dev",
        descritpion=descritpion,
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/zarlo/fastapi_session",
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"
        ],
        packages=packages,
        install_requires=install_requires,
        zip_safe=False,
        include_package_data=True
    )

build("fastapi-session", "0.2.7", "session for FastAPI", ["fastapi_session"], ["fastapi"])
build("fastapi-session-mongo", "0.1.0", "session for FastAPI MongoBackEnd", ["fastapi_session_mongodb"], ["fastapi", "fastapi_session"])
