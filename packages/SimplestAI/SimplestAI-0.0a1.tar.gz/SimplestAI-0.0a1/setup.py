import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SimplestAI",
    version="0.0.a1",
    author="Hamstory Game Studio (Cubic)",
    author_email="hamstory.game.studio@gmail.com",
    description="The simplest AI package. Q-method included!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexbronikitin/SimplestAI",
    project_urls={
        "Bug Tracker": "https://github.com/alexbronikitin/SimplestAI/issues",
        "Our Minecraft Server!":"https://2v2c.tilda.ws"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)