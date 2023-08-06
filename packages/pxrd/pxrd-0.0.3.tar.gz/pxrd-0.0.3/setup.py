from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pxrd',
    version='0.0.3',
    author="Asier Murciego Alonso",
    author_email="asier.murciego@deusto.es",
    description="PC-Axis PX file reader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/murci/pxrd",
    # list folders, not files
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    # scripts=['scripts/px2csv.py'],
    entry_points={
       'console_scripts': [
           'px2csv=pxrd.px2csv:main',
       ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['pcaxis', 'px'],
    python_requires=">=3.6",
)