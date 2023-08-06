import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ngobot-json",
    version="1.1.2",
    author="Nseobong Gregory Obot",
    author_email="obot.greg@icloud.com",
    description="HTTP Response code Python-format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ngobot/ngobot_json",
    project_urls={
        "Bug Tracker": "https://github.com/ngobot/ngobot_json/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "ngobot-json"},
    packages=setuptools.find_packages(where="ngobot-json"),
    python_requires=">=3.6",
)