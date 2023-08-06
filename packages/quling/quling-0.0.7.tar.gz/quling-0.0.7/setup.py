from setuptools import setup,find_packages


setup(
    name="quling",
    version="0.0.7",
    include_package_data=True,
    author="xw",
    author_email="260726831@qq.com",
    maintainer="wx",
    license="MIT License",
    description="此库用于处理前面是0的近似与数型字符串，去掉前面的0后以数型输出。This package is used to handle near-numeric strings preceded by0,remove the 0 from it，then output it as a number.",
    long_description="此库用于处理前面是0的近似与数型字符串，去掉前面的0后以数型输出。This package is used to handle near-numeric strings preceded by0,remove the 0 from it，then output it as a number./markdown",
    url="https://github.com/",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"],
    python_requires=">=3.5",
    install_requires=[""],



)