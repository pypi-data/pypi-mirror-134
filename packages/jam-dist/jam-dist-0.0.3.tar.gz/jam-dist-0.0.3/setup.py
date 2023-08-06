from setuptools import setup, find_packages

setup(
    name="jam-dist",
    packages=find_packages(exclude=["notebooks", "tests"]),
    version="0.0.3",
    license="MIT",
    description="Distribution Research Toolbox",
    author="Qsh.zh",
    author_email="Qsh.zh27@gmail.com",
    url="https://github.com/qsh-zh/jam-dist",
    keywords=[
        "artificial intelligence",
        "deep learning",
        "sampling",
    ],
    install_requires=["einops>=0.3", "torch>=1.6", "gdown>=4.2.0"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
    ],
)
