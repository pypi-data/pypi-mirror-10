.. _borg_init:

borg init
---------
::


    usage: borg init [-h] [-v] [--no-files-cache] [-e {none,passphrase,keyfile}]
                     REPOSITORY
    
    Initialize an empty repository
    
    positional arguments:
      REPOSITORY            repository to create
    
    optional arguments:
      -h, --help            show this help message and exit
      -v, --verbose         verbose output
      --no-files-cache
      -e {none,passphrase,keyfile}, --encryption {none,passphrase,keyfile}
                            select encryption method

Description
~~~~~~~~~~~


This command initializes an empty repository. A repository is a filesystem
directory containing the deduplicated data from zero or more archives.
Encryption can be enabled at repository init time.

