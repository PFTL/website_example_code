from setuptools import setup, find_packages

setup(
    name='My Other Package',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'my_other_start=packg.start:main',
        ]
    },
    install_requires=[
        'numpy<1.18',
        'django>3.0'
    ]
)