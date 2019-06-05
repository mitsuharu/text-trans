from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# long_description(後述)に、GitHub用のREADME.mdを指定
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='texttrans',
    packages=['texttrans', 'data'],

    version='1.0.9',

    license='MIT',

    install_requires=[],

    include_package_data=True,

    author='Mitsuharu Emoto',
    author_email='mthr1982+python@gmail.com',

    url='https://github.com/mitsuharu/text-trans',

    description='To computes transition probability of text',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='texttrans, text-trans',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
