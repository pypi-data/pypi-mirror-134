from gzip import READ
from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='Pro Video Ferramentas tolls show',
    version=1.0,
    description='This packges has tools from camera and video recorder.',
    long_description=Path('README.md').read_text(),
    author='krc0d3r',
    author_email='kl3b7r@gmail.com',
    keywords=['camera', 'video', 'process'],
    packages=find_packages()

)
