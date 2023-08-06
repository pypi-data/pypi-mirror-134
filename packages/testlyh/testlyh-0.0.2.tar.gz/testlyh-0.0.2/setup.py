import setuptools

REQUIRED=[#'requests', 'maya', 'records',

]
PACKAGES = ['lxxgg']

setuptools.setup(
    name="testlyh",
    version="0.0.2",
    author="lyh",
    author_email="1271521082@qq.com",
    description="this is a test",
    long_description_content_type="text/markdown",
    url="https://github.com/",
    packages=PACKAGES,include_package_data=True,zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)