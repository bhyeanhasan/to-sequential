from setuptools import setup, find_packages

setup(
    name='to_sequential',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
        'numpy>=1.18.0'
    ],
    author='Md. Babul Hasan (Noyon)',
    author_email='bhyean@gmail.com',
    description='A utility to generate sequential data for sequential models from a Pandas DataFrame.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bhyeanhasan/to-sequential',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
