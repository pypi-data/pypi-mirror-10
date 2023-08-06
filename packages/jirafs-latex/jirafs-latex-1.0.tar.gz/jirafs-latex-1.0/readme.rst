Jirafs-Latex
=============

Automatically convert Latex documents into PDF documents
when uploading them to JIRA.

Installation
------------

1. Install from PIP::

    pip install jirafs-latex

2. Enable for a ticket folder::

    jirafs plugins --enable=latex

Note that you can globally enable this (or any) plugin by adding the
``--global`` flag to the above command::

    jirafs plugins --global --enable=latex

Requirements
------------

* Requires ``xelatex``.

