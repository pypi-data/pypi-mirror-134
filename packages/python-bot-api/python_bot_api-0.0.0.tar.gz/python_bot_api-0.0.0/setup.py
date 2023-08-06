import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='python_bot_api',
    author='Sonal Pawar',
    author_email='makhare.sonal@gmail.com',
    description='Chuck Norris BOT API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SonalPawar2509/pythonapi',
    project_urls={
        'Documentation': 'https://github.com/SonalPawar2509/pythonapi',
        'Bug Reports':
        'https://github.com/SonalPawar2509/pythonapi/issues',
        'Source Code': 'https://github.com/SonalPawar2509/pythonapi',
    },
    #package_dir={'': 'src'},
    #packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6',
    install_requires=['requests', 'flask'],
)
