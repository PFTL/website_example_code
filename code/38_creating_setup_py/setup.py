from setuptools import setup, find_packages

setup(
    name='My First Setup File',
    version='1.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'my_start=my_package.__main__:main',
        ]
    },
    install_requires=[
        'numpy>1.18',
        'django<3.0'
    ],
    extras_require={
        'opt1': ['serial'],
        'opt2': ['pyserial'],
    }
)