import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRED = [
    'Flask','MyQR==2.3.1'
]


setuptools.setup(
    name="polarishub_flask",
    version="0.1.5",
    author="Guochao Xie",
    author_email="guochaoxie@link.cuhk.edu.cn",
    description="PolarisHub Flask version",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/XieGuochao/polarishub_flask",
    packages=setuptools.find_packages(),
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['phub=polarishub_flask.app:main']
    },
    package_data = {'':['files/*', 'files/*/*', 'server/*/*', 'temp/*', "server/*", "server/*/*/*"]}
)