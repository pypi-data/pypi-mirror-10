# Frojd-Fabric-Cli
This is a Cli tool for Frojd-Fabric that will generate files and supply base settings.

## Requirements
To install Frojd-Fabric you need Python 2.7, virtualenv and pip.

## Installation

### Stable
- `pip install frojd_fabric_cli`

### Unstable
- `pip install git+git://github.com/Frojd/Frojd-Fabric-CLI.git@develop`

### For development
- `git clone git@github.com:Frojd/Frojd-Fabric.git`
- `virtualenv venv`
- `source venv/bin/activate`
- `pip install --editable .`

## Getting started

### Walkthrough

1. First go to your project folder.

	`cd myproject`
	
2. Setup a virtual environment
	
	`virtualenv venv`
	
3. Activate it

	`source venv/bin/activate`
	
4. Now time to install

	`pip install frojd_fabric_cli`
	
5. **(Optional)** Now is a good time to setup git, the cli will auto detect this if present

	`git init ...`
	
6. Time to run the script. lets create a deploy environment that concist of two servers using a wordpress recipe.

	`frojd_fabric --stages=stage,prod --recipe=wordpress`
	
	This command will create the following files.
	
	```
	/fabfile.py
	/stages/
		__init__.py
		stage.py
		prod.py
	```
	
	This script will create the necessary files and add git repro setting (if present) and recipe import. Once generated, you'll need to add SSH settings and recipe unique settings by editing the files.


	
### Command

```
frojd_fabric
    --stages=local,stage,prod (Your deploy stages)
    --path=/tmp/ (Path to the project, optional)
    --recipe=wordpress (The recipe you will be use, optional)
```


## Roadmap

### Implemented
- Generate stage folder
- __init__ in stage folder
- Individual stage files
- Cli interface
- Repro url

### Not yet implemented
- Additional stage file config data
- A way of auto generating fabricrc / stage config depending on recipe
- Merged back into Frojd-Fabric


## Developing
- Coverage
	- `coverage run runtests.py`
	- `coverage report -m`
	- `coverage html`
	- `open htmlcov/index.html`
	- `coverage erase`
- Test
	- `python runtests.py`

## Code guide
- Pep8
- TDD

## Contributing
Want to contribute? Awesome. Just send a pull request.

## Licence
Frojd-Fabric-Cli is released under the [MIT License](http://www.opensource.org/licenses/MIT).
