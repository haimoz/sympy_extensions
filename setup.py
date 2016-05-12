#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    import warnings
    warnings.warn("`setuptools` not found, using `distutils` instead.")
    from distutils.core import setup  # this is just as a fallback

setup(
        name='sympy_extensions',
        version='1.0',
        description='Extensions to the official SymPy 1.0',
        long_description="""
Currently, the extensions include symbolic expressions for `gcd`, `lcm`,
and `prime` functions in SymPy, which supports delayed substitution
and evaluation.

The versioning of this extension package matches the SymPy version it extends.
""",
        license='MIT',
        author='Haimo Zhang',
        author_email='zh.hammer.dev@gmail.com',
        url='',
        requires=['sympy(==1.0)',],
        install_requires=['sympy==1.0',],
        packages=['sympy_extensions'],
        classifiers=[
                'Development Status :: 3 - Alpha',
                'Intended Audience :: Developers',
                'Intended Audience :: Science/Research',
                'License :: OSI Approved :: MIT License',
                'Programming Language :: Python :: 2',
                'Programming Language :: Python :: 3',
                'Topic :: Utilities',
                ],
        )
