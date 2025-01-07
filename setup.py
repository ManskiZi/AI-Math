from setuptools import setup, find_packages

setup(
    name="AI_Math",  # Name of your package
    version="0.1",
    description="A library for mathematical operations used in AI",
    author="Devon",
    author_email="your-email@example.com",
    url="https://github.com/ManskiZi/AI-Math",
    packages=find_packages(),  # Automatically find Python modules
    install_requires=[
        "numpy>=1.21.0",  # List dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify Python version compatibility
)
