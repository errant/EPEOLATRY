from setuptools import setup, find_packages

VERSION = '0.0.1'

with open('requirements.txt') as f:
    requirements = f.readlines()

with open('README.md') as f:
    readme = f.read()

setup(
    name='epeolatry',
    author='Tom Morton',
    url='https://github.com/errant/epeloatry',
    version=VERSION,
    packages=find_packages(),
    license='MIT',
    description='Document to TXT parsing',
    long_description=readme,
    install_requires=requirements,
    entry_points = """
    [epeolatry.parsers]
    pdf   = epeolatry.parsers.pdf
    image = epeolatry.parsers.image
    """,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ])