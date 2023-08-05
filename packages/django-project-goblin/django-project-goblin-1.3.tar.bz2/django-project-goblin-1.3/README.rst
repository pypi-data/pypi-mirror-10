=====================
Django Project Goblin
=====================

Overview
========

Project Goblin was created to list and manage projects. Note that the projects
are not stored, but only listed. This is useful if you want to showcase
projects on your blog, come out with new announcements, etc.

Installation
============

The easiest way is to use PIP:

::

    pip install django-project-goblin

Add ``'goblin'`` to the list of installed apps.

::

    INSTALLED_APPS = (
        # ...
        'goblin',
        #...
    )


Models
======

Once installed, you'll have access to Project Goblin's models:

Project
-------

A project is a software project and can contain many releases. The main
attributes for a software project are (self-explainator):

* name
* description
* README (a longer description)
* homepage (URL link to a project).
* Status

Project Status
---------------

Adds a little control over how you were involved in the project. Solely used 
for controlling what's shown and what isn't shown.

For example, I may add a status called "contribution," to show that I was a 
contributor to the project. Then in my views to list all my contributions I 
can just filter by ``project.status.status == 'contribtuion'``.

Release
-------

The release has a foreign key relation to `Project`_ and to `Change`_. This is
used to make readers aware of the release that has taken place for the project.

The attributes for a release are

* project (FK to `Project`_)
* version (The `Version`_ number)
* download (URL to download the release)

Change
------

A change is a difference of one release over another. A change is something
that is

1. Added,
2. Removed,
3. Fixed, or
4. something else (Other).

In addition, a change is given a description (the ``what`` field) where the
developer can write a description of the change that occurred.

Fields & Input
==============

Version
-------

A version is--essentially--a list with an added attribute "stage" that can be
one of the following values:

* DEV
* ALPHA
* BETA
* TEST
* RELEASE

When comparing versions, the stage is always incorporated in the comparison.
For example, the versions ``0.1`` and ``0.1`` are equal, but the versions
``0.1-test`` and ``0.1-dev`` are not.

VersionField
------------

Model field for a version. For now, this is a CharField. However, a restriction
does exist for the version format. It must pass the following regexp test:::

    (\d+\.)+\d+((\-(dev|test|release))|[ab])

Here are examples of acceptable input::

    0.1a
    1.5.8
    13.4-dev

Here are examples of not-so-acceptable (e.g. invalid!) input::

    0-alpha14
    0.1.-34.0

You get the idea.

Errors Thrown
=============

NotLatestVersionException
-------------------------

This is thrown when a release is being added to a project and the release's
version is not greater than the last added version. For example, if a project's
latest version is 1.0 and you're trying to add a version 0.8, the exception
will be thrown.
