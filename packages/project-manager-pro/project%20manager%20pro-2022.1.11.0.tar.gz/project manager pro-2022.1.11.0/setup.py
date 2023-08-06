import os

from project_manager_pro._version import version
from setuptools import setup

with open('readme.md', 'r', encoding='utf-8') as file:
    readme = file.read()


setup(
    name='project manager pro',                                # название пакета
    version=version,
    author='FullDungeon',
    author_email='ddd.dungeon@gmail.com',
    description='Управление проектами',                    # краткое описание
    long_description=readme,                               # полное опсиание (файл readme.md)
    long_description_content_type='text/markdown',
    url='',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=['colorama'],
    packages=['project_manager_pro'],
    entry_points={                                         # точка входа
        'console_scripts': [
            'pmp = project_manager_pro.cli.main:main',
        ],
    },
)