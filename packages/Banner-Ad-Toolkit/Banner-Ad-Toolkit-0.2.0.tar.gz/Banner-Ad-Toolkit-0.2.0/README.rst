Banner Ad Toolkit
=================

Author: Tim Santor tsantor@xstudios.agency

Overview
========

Banner ad development is, at its core, a very repetitive task. You
constantly do the same thing over and over. This toolkit aims to ease a
bit of that repetitive work and while the tasks it does are relatively
small, the speed and ease at which you can do them ends up saving you
precious time.

**Ask yourself these questions:**

1. **Need a quick way to create all the PSDs you'll need?** No problem!
   One simple command will generate all the PSDs you need at the proper
   dimensions with the proper file names.

2. **Made sweeping changes to your campaign PSDs?** No problem! One
   simple command will export all your static files while ensuring they
   are no larger than a specified size. No more manually running Save
   for Web on each of them.

3. **Need a simple way for your client to review your Flash and static
   versions?** No problem! One simple command will generate all your
   preview HTML and even upload it to your server if you want.

4. **Not a command line geek?** No problem! Create a simple config file
   and don't ever add a parameter to any of the available commands. I
   got you covered.

The workflow described below is one developed over many years of doing
banner ad design and devleopment. While it may seem additional work at
first, I promise you will find that doing each and every campaign in
this way will greatly speed up your workflow. Now on to the good
stuff...

Requirements
============

-  Python 2.7.x
-  ImageMagick
-  pngquant

**NOTE**: This has only been tested on a Mac (10.10.2) at this time.

Installation
============

You can install directly via pip:

::

    pip install Banner-Ad-Toolkit

Or from the BitBucket repository (master branch by default):

::

    git clone https://bitbucket.org/tsantor/banner-ad-toolkit
    cd banner-ad-toolkit
    sudo python setup.py install

Usage
=====

Create a Manifest
-----------------

Most of the command line tools provided are governed by a manifest file.
Create an Excel doc with the following column headers and add as many
rows as needed for each banner size you need:

+----------+---------+----------+------------+---------------------+---------------------+
| Type     | Width   | Height   | Max Size   | Prefix              | Suffix              |
+==========+=========+==========+============+=====================+=====================+
| Static   | 300     | 600      | 40KB       | PREFIX (optional)   | SUFFIX (optional)   |
+----------+---------+----------+------------+---------------------+---------------------+
| Static   | 160     | 600      | 40KB       | PREFIX (optional)   | SUFFIX (optional)   |
+----------+---------+----------+------------+---------------------+---------------------+
| Static   | 300     | 250      | 40KB       | PREFIX (optional)   | SUFFIX (optional)   |
+----------+---------+----------+------------+---------------------+---------------------+
| Static   | 728     | 90       | 40KB       | PREFIX (optional)   | SUFFIX (optional)   |
+----------+---------+----------+------------+---------------------+---------------------+

**NOTE**: Columns may be in any order. You may add any additional
columns you need, but they will be ignored.

-  **Type:** ``Static``, ``Flash`` or anything else, however Flash types
   will be ignored (currently) by the tools.
-  **Max Size:** File size should be defined using KB or MB (eg -
   ``40KB``, ``1MB``)
-  **Prefix:** A prefix to prepend to your file name
-  **Suffix:** A suffix to append to your file name

**NOTE**: File names will be generated as
``PREFIX_WIDTHxHEIGHT_SUFFIX.psd``

Export as CSV
^^^^^^^^^^^^^

Export (Save As) your Excel doc as a CSV.

File Structure (Optional)
-------------------------

While not required, using the following project structure is recommended
as the command line defaults follow this convention which ends up making
the commands require less input from the user.

::

    PROJECT
    ├── Flash
    │   ├── bin
    │   ├── lib
    │   └── src
    ├── PSD
    ├── manifest.csv
    ├── manifest.xlsx
    └── adkit.ini

Create a Config file (Optional)
-------------------------------

This step is optional, but if you take the few seconds to create a
``adkit.ini`` all commands will end up requiring little to no input from
you. At any time, you may override any of the config settings by
specifying a new parameter value on the command line. All options in the
config match their command line equivalents. A basic config looks
something like this:

::

    [default]
    manifest = manifest.csv

    [psd]
    input = PSD

    [flash]
    input = Flash/bin

    [upload]
    user = username
    ip = xxx.xxx.xxx.xxx
    remote_dir = /var/www/vhosts/domain.com/path/to/dir/
    url = http://domain.com/path/to/dir/

**NOTE**: When running any adkit command, ensure you run it from the
root of your project folder where the ``adkit.ini`` resides (see
recommended File Structure above)

Quickstart
----------

Rather than doing the above, quickly get up and running by generating a
``adkit.ini`` and ``manifest.xlsx``.

::

    adkit-quickstart

    NOTE: You will still need to edit each generated file, this just
    helps save some typing.

Generate PSDs
-------------

Once you have your manifest CSV, we can auto-generate blank PSDs at
specific sizes with desired filenames. Simply run the following command:

::

    adkit-generate -m /path/to/manifest.csv -o /path/to/output

    # With an adkit.ini config
    adkit-generate

**NOTE**: For all available commands, run ``adkit-generate -h``. You may
run this multiple times without overwriting any existing PSDs. Useful if
you add more sizes later.

Export Statics
--------------

Once all your banner PSDs are complete, ensure they are saved in their
'static' state. This will automatically save static image versions
without going over predefined max file sizes defined in the manifest.
Simply run the following command:

::

    adkit-export -m /path/to/manifest.csv -i /path/to/input/

    # With an adkit.ini config
    adkit-export

**NOTE**: For all available commands, run ``adkit-export -h``.

Generate Preview HTML
---------------------

Once all your banner SWFs are complete, simply run the following
command:

::

    adkit-preview -i /path/to/flash/bin

    # With an adkit.ini config
    adkit-preview

**NOTE**: Copy or move your static backups to the bin dir to ensure your
previews contain both the swf and static version. Typically the bin dir
is what would be delivered to the client as it contains your final SWFs
and static backups.

Upload Preview Files
^^^^^^^^^^^^^^^^^^^^

If you want to upload these files to a server at the same time use:

::

    adkit-preview -i /path/to/flash/bin -u

    # With an adkit.ini config
    adkit-preview -u

**NOTE**: For all available commands, run ``adkit-preview -h``

Issues
======

If you experience any issues, please create an
`issue <https://bitbucket.org/tsantor/banner-ad-toolkit/issues>`__ on
Bitbucket.
