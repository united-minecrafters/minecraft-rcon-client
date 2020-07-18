import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="minecraft-crazygmr101",
    version="0.1.0",
    author="Daniel Nash",
    author_email="dannash987@gmail.com",
    description="A package letting you interact with a Java Minecraft server through RCON",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/united-minecrafters/minecraft-rcon-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
