from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'inorbit_cli',
    version = '0.1.1',
    author = 'InOrbit Inc.',
    author_email = 'support@inorbit.ai',
    license = '<the license you chose>',
    description = 'CLI tool to interact with InOrbit Cloud Platform',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    # url = '<github url where the tool code will remain>',
    py_modules = [],
    packages = find_packages(),
    install_requires = [requirements],
    extras_require={
        'dev': [
            'twine',
            'lark',
            'pytest',
            'pytest-env',
            'requests-mock',
        ]
    },
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    # see https://click.palletsprojects.com/en/8.0.x/setuptools/#setuptools-integration
    entry_points = '''
        [console_scripts]
        inorbit = inorbit.cli:cli
    '''
)
