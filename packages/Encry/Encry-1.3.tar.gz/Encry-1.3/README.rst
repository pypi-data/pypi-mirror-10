Welcome To Encry!
=================

This is a simple, and fairly insecure Encryption module for python

Meant to be perfect for things like chat messages...


To use simply type this command once installed
----------------------------------------------
 ``$ Encry.py --help``

 Note:
  this command may change (see changelog)

You can use this as a normal command
------------------------------------
	``$ Encry.py -e test -d``
	
	this means encrypt(-e) the message(test) with the default key(-d)
	you can get a randomly generated key with -r

	to decrypt your previous message do:
		
	``$ Encry.py --entry 1 -d``

	this means look for entry(1) in output.txt and decrypt it(-d)

You can also use this as a python module
----------------------------------------
simply type:

``>>>import Encry``
	
    that's it!

better documentation coming soon!

Changelog:
----------

- -1.1.1: Added a changelog

- -1.1.2: improved the documentation

- -1.1.2.1: Removed the annoying formating on the README file

- -1.1.3: Added some backdoor stuff to get ready for 1.2

- -1.2: Added Joshification

- -1.2.1: Fixed Joshification

- -1.3: Added functionality to the --settings command

Patch Notes For Current Release:

- The --settings command actually changes settings!
- For now there are 3 of the settings you can change(see below)
- Fixed a bunch of minor bugs
- You can now install user made settings files from anywhere! (``--settings -i``)
- Moved the ``-J`` command to ``--setup`` for sense-making purposes
- Using ``--settings`` by itself will now display a sample file for you to edit
- Added propper documentation

Change settings in the command line!
------------------------------------
``$ Encry.py --settings (setting) (variable)``

For now there are 3 variables:

1. enigmafy - will change the encryption process (true or false)

2. debug - turns on/off debug mode (true/false)

3. out - the output file, you can insert a path here to put the file wherever you want!


Please, If you have any bug reports, and/or ideas, Please email me:
-------------------------------------------------------------------
shadow889566@gmail.com