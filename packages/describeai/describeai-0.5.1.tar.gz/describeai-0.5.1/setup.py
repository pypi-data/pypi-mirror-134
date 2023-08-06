from setuptools import setup, find_packages


setup(
    name='describeai',
    version='0.5.1',
    description='Official Python SDK for Describe.ai',
    long_description='Please visit https://www.describe-ai.com/docs for API examples and documentation.',
    py_modules=['describeai'],
    install_requires=[
             'requests>=2.26'        
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    license='MIT',
)