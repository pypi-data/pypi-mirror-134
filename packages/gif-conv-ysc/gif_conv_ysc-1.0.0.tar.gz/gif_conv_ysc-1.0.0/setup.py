from setuptools import setup, find_packages

setup(
    name             = 'gif_conv_ysc',
    version          = '1.0.0',
    description      = 'Test package for distribution',
    author           = 'Yooseong Choi',
    author_email     = 'choiys3574@naver.com',
    url              = '',
    download_url     = '',
    install_requires = ['pillow'],
	include_package_data = True,
	packages = find_packages(),
    keywords         = ['GIFCONVERTER', 'gifconverter'],
    python_requires  = '>=3.9',
    zip_safe = False,
    classifiers      = [
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
) 