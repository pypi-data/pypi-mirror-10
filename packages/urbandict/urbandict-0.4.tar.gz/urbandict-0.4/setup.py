# Causes `python setup.py test` to not crash.
# See https://groups.google.com/forum/#!msg/nose-users/fnJ-kAUbYHQ/_UsLN786ygcJ
import multiprocessing
from setuptools import setup

setup(name='urbandict',
        version='0.4',
        py_modules=['urbandict'],
        scripts=['urbandicli'],
        author='Roman Bogorodskiy',
        author_email='bogorodskiy@gmail.com',
        url='https://github.com/novel/py-urbandict',
        classifiers=[
                "Environment :: Console",
                "Intended Audience :: End Users/Desktop",
                "Intended Audience :: Developers",
                "Programming Language :: Python :: 2",
                "Programming Language :: Python :: 3",
            ],
        )
