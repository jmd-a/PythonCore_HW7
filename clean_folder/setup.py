from setuptools import setup, find_packages

setup(
    name='clean-folder',
    version='1.0.0',
    description='A tool to clean up and sort files in a folder',
    author='jmd.a',
    author_email='tovkun.andrii@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:main',
        ],
    },
)