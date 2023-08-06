from setuptools import setup, find_packages

setup(
    name='secret',
    version='0.4',
    description='Manage secrets',
    license='Apache2',
    url='https://github.com/futurice/secret',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=['boto3>=0.0.18', 'pycryptodome>=3.1'],
    entry_points={
        'console_scripts': [
            'secret = secret:main'
            ]
        }
)
