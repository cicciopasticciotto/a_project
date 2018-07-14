#!/usr/bin/env python

import os

from setuptools import setup, find_packages

module_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    setup(
        name='test_travis',
        version="0.1",
        description='Description',
        long_description=open(os.path.join(module_dir, 'README.md'),encoding='utf-8').read(),
        long_description_content_type="text/markdown",
        url='https://github.com/asdrubaleblabla/test_travis',
        author='Someone',
        #author_email='matproj-develop@googlegroups.com',
        #license='modified BSD',
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            #'atomate', 'abipy>=0.4.1', 'pymatgen>=2018.4.20', 'maggma','monty',
            'six', "numpy"#'pydash', 'tqdm', 'matminer',
            #'prettyplotlib', 'pybtex', 'networkx', 'sumo',
        ],
        classifiers=["Programming Language :: Python :: 3",
                     "Programming Language :: Python :: 3.6",
                     'Development Status :: 2 - Pre-Alpha',
                     'Intended Audience :: Science/Research',
                     'Intended Audience :: System Administrators',
                     'Intended Audience :: Information Technology',
                     'Operating System :: OS Independent',
                     #'Topic :: Other/Nonlisted Topic',
                     #'Topic :: Scientific/Engineering'
                     ],
        test_suite='nose.collector',
        tests_require=['nose'],
        python_requires='>=3.6',
    )

