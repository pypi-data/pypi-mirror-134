import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="csuayyy",                     # This is the name of the package
    version="0.0.5",                        # The release version
    author="Armaan Goel",                     # Full name of the author
    author_email="armaangoel78@gmail.com",
    description="CLI for easily interfacing with Berkeley CSUA",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),    # List of all python modules to be installed     
    entry_points={
        'console_scripts': [
    		'csuayyy=csuayyy.src.main:main',
    		'csua=csuayyy.src.main:main'
    	]
    },                               
    python_requires='>=3.6',                # Minimum version requirement of the package
    install_requires=['pexpect', 'termcolor']                     # Install other dependencies if any
)