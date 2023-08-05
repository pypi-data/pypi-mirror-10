$ drifter
#########

  drifter is a simplified control for virtualboxes that doesn't require the vm to be packaged in a specific and ill documented format.  Which allows use to create your environment with Virtualbox and then drift will take care of bringing them up and shutting them down.

Why drifter?
============
If you are currently using Vagrant or straight-up virtualbox and you are happy, then there is nothing for you to see here.  However, if you are annoyed with how difficult it is to convert a virtualbox vm into a vbox usable by Vagrant, then Drifter might just be for you.

In general, I like the idea of Vagrant, but I have specific problems with the following:

- Security concerns with what is being downloaded from an untrusted source
- The limited vm's available from that source, Specifically the \*BSDs and Windows
- Vagrant's intentional inability to auto create a vbox from a virtualbox image

drifter's answer

- Drifter currently supports virtualbox vms. You build it, drifter will control it.
- Drifter currently has 5 commands: list, add, remove, up and down. Easy to remember, easy to script.
- Drifter's configuration, Drifterfile, is in YAML not some language specific module. On top of that, you don't even need to edit it directly.  Use init, add and remove to create and make changes, but it's still yaml so diff'ing is unsurprising.
- Drifter lets you document your environment and store that documentation with your source.
- Drifter fires up your vms in order and shuts them down in reverse order.


Development
-----------
In a virtual environment..

..

  $ hg clone ssh://hg@bitbucket.org/dundeemt/drifter

  $ pip install --editable .

  $ drifter --help

Then you can edit the source and run ``drifter cmd``
