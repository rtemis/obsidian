# Setup for code
from setuptools import setup, find_packages

setup(
    name='example',
    version='0.1.0',
    description='Setup for Obsidian Code',
    author='Leah Hadeed',
    author_email='leahmh97@gmail.com',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
      'Pillow',
      'Flask',
      'pymongo',
      'opencv-python',
      'pyzbar'
      'python-barcode'
      'Flask-QRcode',
      'barcode',
      'tkinter'
    ],
#     extras_require={'plotting': ['matplotlib>=2.2.0', 'jupyter']},
#     setup_requires=['pytest-runner', 'flake8'],
#     tests_require=['pytest'],
    # Interface for plugins
#     entry_points={
#         'console_scripts': ['my-command=exampleproject.example:main']
#     },
    # This is for data that needs to be included for code not python
#     package_data={'exampleproject': ['data/schema.json']}
)
