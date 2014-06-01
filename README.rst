SVN precommit hook
====================


SVNchecker is a precommit hook, now it will check json, xml files and your commit log, 
any invalid happened you will commit failed. And the checker will tell you what the 
error is.

License: MIT (see LICENSE)

Installation and Dependencies
-----------------------------

git clone https://github.com/xsank/SVNchecker.git

copy the SVNchecker to the svn hook-path, then all the thing will be ok.
you can also custom the tools by yourself, just add the new checker file to the checker 
directory.
