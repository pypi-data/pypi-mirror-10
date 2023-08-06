.. _borg_change-passphrase:

borg change-passphrase
----------------------
::


    usage: borg change-passphrase [-h] [-v] [--no-files-cache] REPOSITORY
    
    Change repository key file passphrase
    
    positional arguments:
      REPOSITORY
    
    optional arguments:
      -h, --help        show this help message and exit
      -v, --verbose     verbose output
      --no-files-cache

Description
~~~~~~~~~~~


The key files used for repository encryption are optionally passphrase
protected. This command can be used to change this passphrase.

