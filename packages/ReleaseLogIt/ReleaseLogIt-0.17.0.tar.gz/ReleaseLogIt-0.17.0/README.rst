.. image:: https://img.shields.io/pypi/status/ReleaseLogIt
    :alt: PyPI - Status

.. image:: https://img.shields.io/pypi/wheel/ReleaseLogIt
    :alt: PyPI - Wheel

.. image:: https://img.shields.io/pypi/pyversions/ReleaseLogIt
    :alt: PyPI - Python Version

.. image:: https://img.shields.io/github/v/release/hendrikdutoit/ReleaseLogIt
    :alt: GitHub release (latest by date)

.. image:: https://img.shields.io/github/license/hendrikdutoit/ReleaseLogIt
    :alt: License

.. image:: https://img.shields.io/github/issues-raw/hendrikdutoit/ReleaseLogIt
    :alt: GitHub issues

.. image:: https://img.shields.io/pypi/dm/ReleaseLogIt
    :alt: PyPI - Downloads

.. image:: https://img.shields.io/github/search/hendrikdutoit/ReleaseLogIt/GitHub
    :alt: GitHub Searches

.. image:: https://img.shields.io/codecov/c/gh/hendrikdutoit/ReleaseLogIt
    :alt: CodeCov
    :target: https://app.codecov.io/gh/hendrikdutoit/ReleaseLogIt

.. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/ReleaseLogIt/Pre-Commit
    :alt: GitHub Actions - Pre-Commit
    :target: https://github.com/hendrikdutoit/ReleaseLogIt/actions/workflows/pre-commit.yaml

.. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/ReleaseLogIt/CI
    :alt: GitHub Actions - CI
    :target: https://github.com/hendrikdutoit/ReleaseLogIt/actions/workflows/ci.yaml

.. image:: https://img.shields.io/pypi/v/ReleaseLogIt
    :alt: PyPi

Manage release notes for Python projects.

    ReleaseIt keeps release notes for Python projects in a dict structure. It aims to standardise, facilitate and automate the management of release notes when publishing a project to GitHub, PyPI and ReadTheDocs. It is developed as part of the PackageIt project, but can be used independently as well. See also https://pypi.org/project/PackageIt/

=======
Testing
=======

This project uses ``pytest`` to run tests and also to test docstring examples.

Install the test dependencies.

.. code-block:: bash

    $ pip install -r requirements_test.txt

Run the tests.

.. code-block:: bash

    $ pytest tests
    === XXX passed in SSS seconds ===

==========
Developing
==========

This project uses ``black`` to format code and ``flake8`` for linting. We also support ``pre-commit`` to ensure these have been run. To configure your local environment please install these development dependencies and set up the commit hooks.

.. code-block:: bash

    $ pip install black flake8 pre-commit
    $ pre-commit install

=========
Releasing
=========

Releases are published automatically when a tag is pushed to GitHub.

.. code-block:: bash

    # Set next version number
    export RELEASE = x.x.x
    
    # Create tags
    git commit --allow -empty -m "Release $RELEASE"
    git tag -a $RELEASE -m "Version $RELEASE"
    
    # Push
    git push upstream --tags

