.. _borg_delete:

borg delete
-----------
::


    usage: borg delete [-h] [-v] [--no-files-cache] [-s] TARGET
    
    Delete an existing repository or archive
    
    positional arguments:
      TARGET            archive or repository to delete
    
    optional arguments:
      -h, --help        show this help message and exit
      -v, --verbose     verbose output
      --no-files-cache
      -s, --stats       print statistics for the deleted archive

Description
~~~~~~~~~~~


This command deletes an archive from the repository or the complete repository.
Disk space is reclaimed accordingly. If you delete the complete repository, the
local cache for it (if any) is also deleted.

