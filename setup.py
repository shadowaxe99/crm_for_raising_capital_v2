from setuptools import setup, find_packages

setup(
    name='crm_for_raising_capital',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'crm_for_raising_capital=main:main',
        ],
    },
    install_requires=[
        'openai',
    ],
)