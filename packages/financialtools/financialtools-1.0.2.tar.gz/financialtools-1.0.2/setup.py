from setuptools import setup

setup(
    name='financialtools',
    version='1.0.2',
    py_modules=['finance','csvwriter','info','dash'],
    author="Ryan Gilmore",
    author_email = "ryan.gilmore1088@icloud.com",
    url="https://github.com/jugglingworm12/financetools",
    long_description="Python Package for financial analysis",
    install_requires=[
        "Click","pandas","matplotlib","yfinance","streamlit"
    ],
    entry_points={
        'console_scripts': [
            'fintools = finance:cli',
        ],
    },
    classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
    ],
)
