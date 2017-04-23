=========================
Installation instructions
=========================

User installation
=================

Jarvis can be installed using pip::

    $ python -m pip install jarvis-pentest

Sometimes, the version available on Pypi is somehow "far away" from the bleeding edge, and you may want to pull the last available version::
    
    $ python -m pip install git+https://github.com/BastienFaure/jarvis
    
Theses commands will fetch the package and its dependencies from the internet and install them. 

If you've downloaded the tarball, unpack it, and execute::

    $ python setup.py install --user

When Jarvis is installed in user-land, console scripts are usually installed in ``~/.local/bin/``, and you should make sure that this directory is at the top of your ``$PATH``.

System-wide installation
========================

You might prefer to install it system-wide. In this case, run the following commands::

	# mkdir /opt/jarvis
	# pip install --install-option="--install-scripts=/opt/jarvis/" jarvis-pentest

Sometimes, the version available on Pypi is somehow "far away" from the bleeding edge, and you may want to pull the last available version::

	# pip install --install-option="--install-scripts=/opt/jarvis/" git+https://github.com/BastienFaure/jarvis

In order to avoid conflicts with distros packages or manually compiled/installed binaries, console scrits are placed under ``/opt/jarvis``.

Then set the console scripts location at the top of your path::

	# echo 'export PATH="/opt/jarvis:$PATH"' > /etc/profile.d/jarvis.sh

External dependancies
=====================

There are two non-Python dependancies that are used for managing screenshots.

Debian::

	# apt-get install zenity pinta imagemagick python-dev

Fedora/Redhat::

	# dnf install python-devel zenity imagemagick pinta
	


Troubleshoot
------------

Windows users may find that these command will only works if typed from Python's installation directory.

Some Linux distributions (e.g. Ubuntu) install Python without installing pip. Please install it before. If you don't have root privileges, download the get-pip.py script at https://bootstrap.pypa.io/get-pip.py and execute it as ``python get-pip.py --user``.
