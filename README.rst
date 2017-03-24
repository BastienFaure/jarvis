.. These are the Travis-CI and Coveralls badges for your repository. Replace
   your *github_repository* and uncomment these lines by removing the leading
   two dots.

.. .. image:: https://travis-ci.org/*github_repository*.svg?branch=master
    :target: https://travis-ci.org/*github_repository*

.. .. image:: https://coveralls.io/repos/github/*github_repository*/badge.svg?branch=master
    :target: https://coveralls.io/github/*github_repository*?branch=master


======
Jarvis
======

Jarvis is a very simple pentest companion that provides the following features:

* penetration tests results directory management
* unified structure for each assessment
* hooks for useful commands and automated output saving
* unified command history file

It is fully written with Python and is designed to be easily maintainable.

Command hooking
===============

As a pentester, I often faced with difficulties related to output recording. Sometimes, a very looonnnng ``nmap`` scan launched without output options may be very painful due to the lack of exploitable files. I'm not even talking about closed terminals containing juicy outputs that may lack in a security assessment report.

For these reasons, I decided to implement a command hooking feature that would automatically add output options to command lines and record outputs if such options would not exist.

Basically, each command exposed by Jarvis is a specific method called on a Python. This method retrieves the supplied command line, adds arguments and patches the command lines, and finally runs the built command in a patched environnement.

Installation
============

See `install`_

.. _install: INSTALL.rst


Usage
=====

Once installed, you can continue to use your favorites pentest tools without problems. 

For using Jarvis, you will have to provide a ``/etc/jarvis.conf`` file::

	[jarvis]
	pentests_history = /home/user/.pentests_history
	user_directory = user
	output_directory = records
	pentest_tree = [
		"%(user_directory)s",
		"%(user_directory)s/img",
		"%(user_directory)s/scripts",
		"%(user_directory)s/records"
		]
	notesfiles = notes.txt
	interface = eth0
	editor = vim

Here is a quick description of available options (all of them are mandatory):

* ``pentests_directory`` : path to the file that will contain all the paths to performed pentests
* ``user_directory`` : since a pentest is supposed to be performed by several persons, this is the name of your directory within the pentest's one
* ``output_directory`` : the directory within your user's directory that will contain all records produced by available hooks
* ``pentest_tree`` : this is a very important one, it describes the structure of your pentest directory that will be created after a ``pentest init``. For the moment, I'm too lazy for creating directories accordingly to previously described options, but this should come soon. Note that some commands will obviously fail if you do not create ``user_directory`` or ``output_directory``
* ``notesfiles`` : the file that will be used for taking notes
* ``interface`` : the network interface through which test are going made
* ``editor`` : your preferred editor (``vim``, ``emacs``, whatever)

If you want to start a new pentest, run the following commands::

	$ pentest start /path/to/pentest
	$ pentest init

The first command will append an entry inside the pentests history file. The second will create your pentest directory structure.
