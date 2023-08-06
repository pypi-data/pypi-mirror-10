.. -*- mode: rst -*-

=========
pygenomes
=========

-------------------------------------------------------------------------------
A simple and excellent tool for downloading genome data from UCSC ftp site.
-------------------------------------------------------------------------------

:Author:     FEI YUAN  <fyuan3@uh.edu>
:Homepage:   https://github.com/TinyNecessaryTools/Biology.git
:Version:    Version 0.1.0
:Date:       2015-07-07
:Copyright:  MIT


About
-----

`pygenomes` is a Python module and also a command-line tool for downloading genome data from UCSC ftp site. 

Using this tool you can easily check available taxa or available groups of taxa by simply typing the name of the tool or add -g flag with a group name. 

Download genome or chromosome data with this tool also very simple. You can download data by using commom name, scientific name, or even specific assembly name (e.g. ``human``, ``Homo sapiens``, ``hg38``). 

If there is available data in the ftp site, you also can download data via interactive mode, which will allow you to choose specific genome assembly.To do this, you only need to assign a True value for assembly, then according to the available list prompted to you, simply input the interested assembly.


Features
--------

- Install a Python module named ``pygenomes.py``
- Install a Python command-line script named ``pygenomes``
- Easily check available taxa and genomes in commend-line
- Simply download genomes via common, scientific, or assembly name
- Using interactive mode, simply download specific assembly genome
- Easily download genome and chromosome in specific file format
- Pure Python module and without any third-party dependence


Examples
--------

You can use `pygenomes` as a Python module e.g. like in the following
interactive Python session (the function's signature might still change 
a bit in the future)::

    >>> from pygenomes import genomes
    >>>
    # prints out available taxa in group of mammals
    >>> genomes(group="group_name")                    # i.e. 'mammals'
    # download human reference genome (hg19) in .2bit format
    >>> genomes(taxa="taxa")                           # i.e. 'human'
    # interactive mode, ask for inputting and downloading specific assembly
    >>> genomes(taxa="taxa", assembly="assembly")      # i.e. 'cow', '1'
    # try to download chromosome data, per fa.gz file per chromosome
    >>> genomes(taxa="taxa", chrs="format")            # i.e. 'cow', '1'

In addition, there is a script named ``pygenomes``, which can be used 
more easily from the system command-line like this (you can see many 
more examples when typing ``pygenomes -h`` on the command-line)::

    
    $ pygenomes -g -1                 # prints out all available taxa

    $ pygenomes -g mammal             # prints out all available taxa in group 
                                        of mammal
    $ pygenomes -t yeast              # download yeast reference genome in 
                                        .2bit format
    $ pygenomes -t yeast -a 1         # interactive mode, ask for inputing and 
                                        downloading specific assembly
    $ pygenomes -t cow -f fa.gz       # try to download cow reference genome 
                                        in fa.gz format
    $ pygenomes -t dog -a 1 -o /tmp   # interactive mode, ask for inputing, 
                                        file will be stored in /tmp
    $ pygenomes -t cat -c 1           # download cat chromosome data, per 
                                        chromosome per fa.gz file
  

Installation
------------

There are three ways to install `pygenomes`, depending on whether you have
module installation tools available on your system or not.

1. Using `pip`
++++++++++++++

With the `pip` command on your system and a working internet connection, you can install `pygenomes` with only one command in a terminal::

  $ [sudo] pip install pygenomes                    

If the `pip` command is not available to you and you want to install it before installing `pygenomes`, you might want to go to the 
`pip Install homepage <https://pip.pypa.io/en/stable/installing.html>`_ 
and follow the `instructions there <https://pip.pypa.io/en/stable/installing.html#install-pip>`_.

2. Using `easy_install`
++++++++++++++++++++++++

Like pip, with the `easy_install` command on your system and a working internet connection, you can install `pygenomes` also with only one command in a terminal::

  $ [sudo] easy_install pygenomes

If the `easy_install` command is not available to you and you want to
install it before installing `pygenomes`, you might want to go to the 
`Easy Install homepage <http://peak.telecommunity.com/DevCenter/EasyInstall>`_ 
and follow the `instructions <http://peak.telecommunity.com/DevCenter/EasyInstall#installing-easy-install>`_.

3. Manual installation
+++++++++++++++++++++++

Alternatively, if you do not have `pip` or `easy_install` and do not want to install one of them first, you can still install the `pygenomes` tarball after downloading the file ``pygenomes-0.0.1.tar.gz`` and decompressing it with the following command::

  $ tar xfz pygenomes-0.0.1.tar.gz

Then change into the newly created directory ``pygenomes`` and install
`pygenomes` by running the following command::

  $ [sudo] python setup.py install
  
All three methods will install a Python module file named ``pygenomes.py`` in the ``site-packages`` subfolder of your Python interpreter and a script 
tool named ``pygenomes`` in your ``bin`` directory, usually in 
``/usr/local/bin`` for *NIX and Mac OS; a script tool named ``pygenomes.exe`` will be created and stored in ``Pythonxx\Scripts`` on Windows.


Dependencies
------------

`Pygenomes` does not depend any third-party module, only need Python standard modules (`os`, `sys`, `subprocess`, `ftplib`, `getopt`). However, I should let you know, when it works, it will use `rsync` first (UCSC recommend download method), if it is not available, it will try to use `wget`, if this also failed, it will download genomes by using ftp (Python standard module `ftplib`, Windows does not have `rsync` and `wget`, it will always use `ftplib`). So, there is no need for you to worry about its dependencies, the only thing you need to do is install it and then enjoy it.


Bug reports
-----------

Please report bugs and patches to FEI YUAN <fyuan4@uh.edu> 
Don't forget to include information about the operating system and Python versions being used.
