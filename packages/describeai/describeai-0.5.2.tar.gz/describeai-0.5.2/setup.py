import setuptools
from setuptools import setup, find_packages


setup(
    name='describeai',
    version='0.5.2',
    description='Official Python SDK for Describe.ai',
    long_description='Please visit https://beta.clevr-ai.com/docs for API examples and documentation.',
    install_requires=[
             'requests>=2.26'        
    ],
    license='MIT',
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"}
)


