from setuptools import setup, find_packages


setup(
    name='describeai',
    version='0.5.0',
    description='Official Python SDK for Describe.ai',
    long_description='Please visit https://www.describe-ai.com/docs for API examples and documentation.',
    py_modules=['describeai'],
    install_requires=[
             'requests>=2.26'        
    ],
    license='MIT',
)