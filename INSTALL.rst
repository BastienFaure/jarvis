=========================
Installation instructions
=========================

Jarvis can be installed using pip::

    $ python -m pip install jarvis

This command will fetch the archive and its dependencies from the internet and install them. 

If you've downloaded the tarball, unpack it, and execute::

    $ python setup.py install --user

When Jarvis is installed in user-land, console scripts are usually installed in ``~/.local/bin/``, and you should make sure that this directory is at the top of your ``$PATH``.

System-wide installation
========================

You might prefer to install it system-wide. In this case, run the following commands::

	# mkdir /opt/jarvis
	# pip install --install-option="--install-scripts=/opt/jarvis/" dist/jarvis-0.0.0.tar.gz

In order to avoid conflicts with distros packages or manually compiled/installed binaries, console scrits are placed under ``/opt/jarvis``.

Then set the console scripts location at the top of your path::

	# echo 'export PATH="/opt/jarvis:$PATH"' > /etc/profile.d/jarvis.sh'

Troubleshoot
------------

Windows users may find that these command will only works if typed from Python's installation directory.

Some Linux distributions (e.g. Ubuntu) install Python without installing pip. Please install it before. If you don't have root privileges, download the get-pip.py script at https://bootstrap.pypa.io/get-pip.py and execute it as ``python get-pip.py --user``.
