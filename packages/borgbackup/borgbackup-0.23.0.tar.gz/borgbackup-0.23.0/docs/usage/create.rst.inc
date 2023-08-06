.. _borg_create:

borg create
-----------
::


    usage: borg create [-h] [-v] [--no-files-cache] [-s] [-p] [-e PATTERN]
                       [--exclude-from EXCLUDEFILE] [--exclude-caches]
                       [-c SECONDS] [--do-not-cross-mountpoints] [--numeric-owner]
                       [--timestamp yyyy-mm-ddThh:mm:ss]
                       ARCHIVE PATH [PATH ...]
    
    Create new archive
    
    positional arguments:
      ARCHIVE               archive to create
      PATH                  paths to archive
    
    optional arguments:
      -h, --help            show this help message and exit
      -v, --verbose         verbose output
      --no-files-cache
      -s, --stats           print statistics for the created archive
      -p, --progress        print progress while creating the archive
      -e PATTERN, --exclude PATTERN
                            exclude paths matching PATTERN
      --exclude-from EXCLUDEFILE
                            read exclude patterns from EXCLUDEFILE, one per line
      --exclude-caches      exclude directories that contain a CACHEDIR.TAG file
                            (http://www.brynosaurus.com/cachedir/spec.html)
      -c SECONDS, --checkpoint-interval SECONDS
                            write checkpoint every SECONDS seconds (Default: 300)
      --do-not-cross-mountpoints
                            do not cross mount points
      --numeric-owner       only store numeric user and group identifiers
      --timestamp yyyy-mm-ddThh:mm:ss
                            manually specify the archive creation date/time (UTC).
                            alternatively, give a reference file/directory.

Description
~~~~~~~~~~~


This command creates a backup archive containing all files found while recursively
traversing all paths specified. The archive will consume almost no disk space for
files or parts of files that have already been stored in other archives.

See "borg help patterns" for more help on exclude patterns.

