import pathlib
import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

name = 'PyTaskFarmer'
version = '0.1.0'

setuptools.setup(
    name=name,
    version=version,
    description='Simple task farmer using file locks to syncrhonize among multiple nodes.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://gitlab.cern.ch/berkeleylab/pytaskfarmer',
    packages=['taskfarmer'],
    scripts=['pytaskfarmer.py'],
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'release': ('setup.py', version),
            'source_dir': ('setup.py', 'docs')}},
    )
