from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='cutesdk',
    version='0.1.4',
    author='idoubi',
    author_email='me@idoubi.cc',
    description='sdks for open platforms',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://cutesdk.com',
    packages=find_packages(),
    install_requires=[
        'diskcache',
        'requests',
    ],
)
