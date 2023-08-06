==============
Python OAR CLI
==============

OAR Command line interface

Installation
============

Requirements:
  - python >= 2.7
  - python-mysqldb/python-psycopg2 (for oar database archive)

You can install, upgrade, uninstall oar-cli with these commands::

  $ pip install [--user] oar-cli
  $ pip install [--user] --upgrade oar-cli
  $ pip uninstall oar-cli

Or from git (last development version)::

  $ pip install git+https://github.com/oar-team/python-oar-cli.git

Or if you already pulled the sources::

  $ pip install path/to/sources

Or if you don't have pip::

  $ easy_install oar-cli


OAR Database archive
====================

This script allow you to copy your OAR database to another database for
archiving purposes.

In order to do this, the tool offers two commands that can be launched
regularly to simplify both databases maintenance.

Sync
----

This command is used to copy data to archive on the archive database. It is
only useful when handling a *small amount of data*.

If your database is too big, we advise you to first create manually your
archive database with a dump. If your archive database does not exist yet, and
if it will be located on the same machine than your current OAR database, the
'sync' command will clone the OAR database to the archive (extremely efficient
for postgresql).


Usage
~~~~~

::

    Usage: oar-database-archive sync [OPTIONS]

      Send all resources and finished jobs to archive database.

    Options:
      --chunk INTEGER        Chunk size  [default: 10000]
      --ignore-jobs TEXT     Ignore job state  [default: ^Terminated, ^Error]
      --current-db-url TEXT  The url for your current OAR database.
      --archive-db-url TEXT  The url for your archive OAR database.
      -h, --help             Show this message and exit.

Jobs unfinished (i.e. current jobs) are not copied by default. The symbol '^'
means negation.

For more information about the URL format, please refer to the SQLAlchemy
documentation: http://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls


Examples
~~~~~~~~

::

    $ oar-database-archive sync --archive-db-url postgresql://oar:oar@server:5432/oar_archive

This command will dump your current OAR database (configured in oar.conf) in
the given database. The second run will only copy the missing rows.

**From postgresql to mysql**::

    $ oar-database-archive sync --current-db-url postgresql://user:password@server1:5432/oar \
                            --archive-db-url mysql://user:password@server2:3306/oar_archive

**From mysql to sqlite**::

    $ oar-database-archive sync --current-db-url mysql://user:password@server1:3306/oar \
                            --archive-db-url sqlite:////tmp/archive.db

Purge
-----

The purge command is used to delete jobs and resources (previously archived)
from the current OAR database.


Usage
~~~~~

::

    Usage: oar-database-archive purge [OPTIONS]

      Purge old resources and old jobs from your current database.

    Options:
      --ignore-jobs TEXT       Ignore job state  [default: ^Terminated, ^Error]
      --max-job-id INTEGER     Purge only jobs lower than this id
      --ignore-resources TEXT  Ignore resource state  [default: ^Dead]
      --current-db-url TEXT    The url for your current OAR database.
      -h, --help               Show this message and exit.

These options are almost similar. By default, all finished jobs are purged. You
can use ``--max-job-id`` to ignore all jobs with an ID greater than the ID used
as parameter..

All resources in 'Dead' state are also purged. If we do not want to purge
resources, the filter ``--ignore-resources all`` needs to be used.

Example
~~~~~~~

::

    $ oar-database-archive purge \
        --ignore-resources ^Dead \
        --ignore-jobs ^Terminated  --ignore-jobs ^Error \
        --max-job-id 100000 \
        --current-db-url postgresql://scott:tiger@localhost/oar_prod_database

This commande is used to delete all resourced marked as 'Dead' and all finished
jobs (and associated events) with a ID smaller than 100000.


OAR CLI changelog
=================

Version 0.3.5
-------------

Released on July 08th 2015

- Emptied admission_rules table before migration
- Used postgresql binary COPY by default
- Split big queries with BETWEEN clause to improved performance and avoided mysql crashes

Version 0.3.4
-------------

Released on July 07th 2015

- Removed OFFSET sql clause from big queries to avoided mysql crashes

Version 0.3.3
-------------

Released on June 24th 2015

- Added ``--conf`` option to used custom oar configuration file
- Used postgresql COPY with csv format by default
- Fixed modify nullable operation during schema upgrade


Version 0.3.2
-------------

Released on June 23rd 2015

- Minor bug fixes

Version 0.3.1
-------------

Released on June 23rd 2015

- Fixed project description in Pypi

Version 0.3.0
-------------

Released on June 23rd 2015

- Renamed the project to OAR CLI !
- Added ``oar-database-migrate`` script.
- Added ``--schema-only`` and ``--data-only`` features to ``oar-database-migrate`` script
- Supported postgresql bulk insert using COPY clause to improved performance.
- Handled database connection errors.
- Managed the schema upgrade with alembic
- Fixed max_job_to_sync query if we want to copy all jobs


Version 0.2.0
-------------

Released on June 05th 2015

Database Archive
~~~~~~~~~~~~~~~~

    - Made deterministic order_by to sync queries in order to avoid IntegrityError during copy (Fixed #1)
    - Handled IntegrityError during bulk INSERT (Fixed #1)
    - Used Postgresql DELETE with the USING clause to improve performance (Fixed #2)
    - Made the delete orphan queries faster with LEFT JOIN in Mysql (Fixed #2)
    - Removed count query when performing a bulk delete query (Fixed #2)
    - Configured debug logging to displayed SQL queries
    - Added option to disable pagination during sync operation
    - Displayed default values in the CLI

Version 0.1.2
-------------

Released on May 05th 2015

- [database-archive] : Added ability to ignore all resources during purge

Version 0.1.1
-------------

Released on May 04th 2015

- Fixed pypi package

Version 0.1.0
-------------

First public preview release.


