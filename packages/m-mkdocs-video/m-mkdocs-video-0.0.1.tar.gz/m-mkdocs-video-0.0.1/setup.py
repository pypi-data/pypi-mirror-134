import os
import pathlib

from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

__PACKAGE_NAME__ = 'mobio'
__TEMPLATE_DIR__ = 'libs'


def package_data_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        p = pathlib.Path(path)
        path = pathlib.Path(*p.parts[1:])
        for filename in filenames:
            paths.append(os.path.join(path, filename))
    return paths


data_files = package_data_files(os.path.join(__PACKAGE_NAME__, __TEMPLATE_DIR__))
print(data_files)

setup(
    name='m-mkdocs-video',
    version='0.0.1',
    author='MOBIO',
    author_email='contact@mobio.vn',
    description='Libs check filetype',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=find_packages(),
    package_data={'': data_files},
    entry_points={
        'mkdocs.plugins': [
            'mkdocs-video = mkdocs_video.plugin:Plugin',
        ]
    }
)
