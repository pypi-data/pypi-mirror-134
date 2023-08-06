from setuptools import setup

long_description = None
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='durl',
    packages=['durl'],
    version='0.0.3',
    license='MIT',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nosarthur/durl',
    platforms=['linux', 'osx', 'win32'],
    keywords=['git', 'cui', 'command-line'],
    author='Dong Zhou',
    author_email='zhou.dong@gmail.com',
    entry_points={'console_scripts': ['durl = durl.__main__:main']},
    python_requires='~=3.7',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Version Control :: Git",
        "Topic :: Terminals",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    # include_package_data=True,
)
