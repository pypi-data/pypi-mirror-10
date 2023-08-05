
Run the Tests
-------------

Install tox and run it::

    pip install tox
    tox

Limit the tests to a specific python version::

    tox -e py27

Conventions
-----------

Onegov Town follows PEP8 as close as possible. To test for it run::

    tox -e pep8

Onegov Town uses `Semantic Versioning <http://semver.org/>`_

Build Status
------------

.. image:: https://travis-ci.org/OneGov/onegov.town.png
  :target: https://travis-ci.org/OneGov/onegov.town
  :alt: Build Status

Coverage
--------

.. image:: https://coveralls.io/repos/OneGov/onegov.town/badge.png?branch=master
  :target: https://coveralls.io/r/OneGov/onegov.town?branch=master
  :alt: Project Coverage

Latests PyPI Release
--------------------
.. image:: https://pypip.in/v/onegov.town/badge.png
  :target: https://crate.io/packages/onegov.town
  :alt: Latest PyPI Release

License
-------
onegov.town is released under GPLv2

Note that Imperavi Redactor (assets/js/redactor.min.js) itself is a proprietary
commercial software, owned by Imperavi. We (Seantis GmbH) bought an OEM license
to distribute Redactor alongside onegov.town, so you may use it for free, but
you are not allowed to use it independently of onegov.town.

Changelog
---------

Unreleased
~~~~~~~~~~

0.0.2 (2015-05-05)
~~~~~~~~~~~~~~~~~~~

- Images are now always shown in order of their creation.
  [href]

- Adds image thumbnails and the ability to select previously uploaded images
  in the html editor.
  [href]

- Adds support for image uploads through the html editor.
  [href]

- Replaces the markdown editor with a WYSIWYG html editor.
  [href]

- Upgrade to Zurb Foundation 5.5.2.
  [href]

- Show a wildcard next to required form fields.
  [href]

- Adds hints to form fields, rendered as placemarks.
  [href]

- The page markdown editor no longer steals the focus when opening the page.
  [href]

0.0.1 (2015-04-29)
~~~~~~~~~~~~~~~~~~~

- Initial release.
  [href]


