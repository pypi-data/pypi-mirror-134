from setuptools import setup, find_packages
import pathlib
here = pathlib.Path(__file__).parent.resolve()

# Date based release version number
VERSION = '2022.01.14' 
DESCRIPTION = 'Setup a snowflake connection and execute queries. Connection is setup via service account secrets or SSO web authintication login'
LONG_DESCRIPTION = (here / 'README.md').read_text(encoding='utf-8')

# Setting up
setup(
        # package name. 
        # pip install snowcatcher
        # https://pypi.org/project/snowcatcher/
        name="snowcatcher", 
        version=VERSION,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        author='Todd.Jordan',
        packages=find_packages(),
        install_requires=[],
)