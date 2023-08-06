import pathlib

from setuptools import setup, find_packages

from pokemontcgsdkasync.config import __version__, __pypi_package_name__, __github_username__, __github_repo_name__

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text(encoding='utf-8')

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

url = 'https://github.com/' + __github_username__ + '/' + __github_repo_name__
download_url = "{}/tarball/{}".format(url, __version__)

setup(
    name=__pypi_package_name__,
    version=__version__,
    description='Pokemon TCG SDK for pokemontcg.io using asyncio',
    long_description=README,
    long_description_content_type="text/markdown",
    url=url,
    author='Paolo D\'Alessandro',
    author_email='pole.gamedev@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    keywords='pokemon tcg sdk trading card game api rest async',
    download_url=download_url,
    packages=find_packages(),
    include_package_data=False,
    python_requires=">=3.6",
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
        'dacite>=1.6.0,<2.0.0',
        'aiohttp>=3.8.1,<4.0.0',
    ],
    extras_require={
        'tests': tests_require,
    },
    # entry_points={
    #     'console_scripts': [
    #         # add cli scripts here in this form:
    #         # 'pokemontcgsdk=pokemontcgsdk.cli:main',
    #     ],
    # },
)
