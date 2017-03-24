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

It is fully written with Python and is designed to be easily maintainable.

Command hooking
===============

As a pentester, I often faced with difficulties related to output recording. Sometimes, a very looonnnng ``nmap`` scan launched without output options may be very painful due to the lack of exploitable files. I'm not even talking about closed terminals containing juicy outputs that may lack in a security assessment report.

For these reasons, I decided to implement a command hooking feature that would automatically add output options to command lines and record outputs if such options would not exist.

Basically, each command exposed by Jarvis is a specific method called on a Python. This method retrieves the supplied command line, adds arguments and patches the command lines, and finally runs the built command in a patched environnement.
