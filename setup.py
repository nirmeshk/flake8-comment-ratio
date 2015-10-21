# coding: utf-8

from __future__ import with_statement
from setuptools import setup

install_requires = ['flake8']

setup(
    name='flake8-comment-ratio',
    version=get_version(),
    description="A plugin to find comment to code ratio for flake8",
    long_description=get_long_description(),
    keywords='flake8 comment code ratio',
    author='Nirmesh Khandelwal',
    author_email='nirmesh.khandelwal@gmail.com',
    url='https://github.com/nirmeshk/flake8-comment-ratio',
    license='MIT',
    py_modules=['flakes_comment_ratio'],
    zip_safe=False,
    entry_points={
        'flake8.extension': [
            'flakes_comment_ratio = flakes_comment_ratio:CommentToCodeRatio',
        ],
    },
    install_requires=install_requires,
    tests_require=test_requires,
    test_suite="nose.collector",
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ]
)
