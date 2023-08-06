.. _borg_check:

borg check
----------
::


    usage: borg check [-h] [-v] [--no-files-cache] [--repository-only]
                      [--archives-only] [--repair] [--last N]
                      REPOSITORY
    
    Check repository consistency
    
    positional arguments:
      REPOSITORY         repository to check consistency of
    
    optional arguments:
      -h, --help         show this help message and exit
      -v, --verbose      verbose output
      --no-files-cache
      --repository-only  only perform repository checks
      --archives-only    only perform archives checks
      --repair           attempt to repair any inconsistencies found
      --last N           only check last N archives (Default: all)

Description
~~~~~~~~~~~


The check command verifies the consistency of a repository and the corresponding
archives. The underlying repository data files are first checked to detect bit rot
and other types of damage. After that the consistency and correctness of the archive
metadata is verified.

The archive metadata checks can be time consuming and requires access to the key
file and/or passphrase if encryption is enabled. These checks can be skipped using
the --repository-only option.

