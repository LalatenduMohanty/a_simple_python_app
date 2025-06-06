from setuptools import setup, find_packages

setup(
    name="simple_app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple Python application demonstrating setuptools usage",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/simple_app",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "simple-app=simple_app.main:main",
        ],
    },
) 