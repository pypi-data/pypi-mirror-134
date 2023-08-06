from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Simple database creator and manager.'
LONG_DESCRIPTION = 'Simple database creator and manager that also allows for column, tables, etc. to be created as well as performing operations on the database like insert, update, select, delete'

# setting up
setup(
    # name must match the folder of the package
    name="dbtoolspy",
    version=VERSION,
    author="Gregory Bockus",
    author_email="gregory.bockus@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        # additional package dependencies that must be installed for your package to work
        'mysql-connector',
        'python-dotenv',
        'flask'
    ],
    keywords=['python', 'mysql', 'database', 'manager'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
