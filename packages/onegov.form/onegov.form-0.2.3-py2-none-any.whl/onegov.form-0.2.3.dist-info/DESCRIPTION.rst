
Provides fields, widgets and shared form code, as well as the ability to
define custom forms using JSON. Those forms are stored on the database and
are meant to be customer defined forms.

Through the web creating of forms is possible with this, but onegov.form does
not offer any UI to do that.

Run the Tests
-------------

Install tox and run it::

    pip install tox
    tox

Limit the tests to a specific python version::

    tox -e py27

Conventions
-----------

Onegov Form follows PEP8 as close as possible. To test for it run::

    tox -e pep8

Onegov Form uses `Semantic Versioning <http://semver.org/>`_

Build Status
------------

.. image:: https://travis-ci.org/OneGov/onegov.form.png
  :target: https://travis-ci.org/OneGov/onegov.form
  :alt: Build Status

Coverage
--------

.. image:: https://coveralls.io/repos/OneGov/onegov.form/badge.png?branch=master
  :target: https://coveralls.io/r/OneGov/onegov.form?branch=master
  :alt: Project Coverage

Latests PyPI Release
--------------------
.. image:: https://pypip.in/v/onegov.form/badge.png
  :target: https://crate.io/packages/onegov.form
  :alt: Latest PyPI Release

License
-------
onegov.form is released under GPLv2

Changelog
---------

Unreleased
~~~~~~~~~~

0.2.3 (2015-05-29)
~~~~~~~~~~~~~~~~~~~

- Fix unicode errors in Python 2.7.
  [href]

0.2.2 (2015-05-29)
~~~~~~~~~~~~~~~~~~~

- Make sure special fields like the csrf token are included in the fieldsets.
  [href]

0.2.1 (2015-05-28)
~~~~~~~~~~~~~~~~~~~

- Makes sure multiple fields with the same labels are handled more
  intelligently.
  [href]

0.2.0 (2015-05-28)
~~~~~~~~~~~~~~~~~~~

- Rewrites most of the parsing logic. Pyparsing is no longer used for
  indentation, instead the form source is transalted into YAML first, then
  parsed further.

  This fixes all known indentation problems.

  [href]

0.1.0 (2015-05-22)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to store forms and related submissions in the database.
  [href]

- Adds a custom markdownish form syntax.

  See http://onegov.readthedocs.org/en/latest/onegov_form.html#module-onegov.form.parser.grammar
  [href]

0.0.1 (2015-04-29)
~~~~~~~~~~~~~~~~~~~

- Initial Release [href]


