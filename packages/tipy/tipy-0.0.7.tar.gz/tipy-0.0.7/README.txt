REQUIREMENTS
------------

tipy is written for Python 3:

python3

In order to install tipy using the setup.py you will need:

python3-setuptools

The GUI require:

python3-pyqt5

INSTALLATION
------------

Install with pip:

# pip3 install tipy

Install from sources:

# python3 setup.py install

After the installation you will need to change the owner of ~/.config/tipy.
The directory is created during the installation, which require root permissions
and therefore set every created file owner to root.
Typing the following should works:

# sudo chown <your_user_name> -R ~/.config/tipy/
