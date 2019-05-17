import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='cl1p',
    version='0.4',
    author="Maulik Patel",
    author_email="maulikp163@gmail.com",
    description="Copy and paste using the internet",
    long_description=long_description,
    include_package_data=True,
    long_description_content_type="text/markdown",
    url="https://github.com/maulik9898/cl1p",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

    ],
    install_requires=[
        "pyperclip", "beautifulsoup4", "colorama", "requests"
    ],
    entry_points={
        'console_scripts': [
            'cl1p=cl1p.cl1p:run'
        ],
    },
)
