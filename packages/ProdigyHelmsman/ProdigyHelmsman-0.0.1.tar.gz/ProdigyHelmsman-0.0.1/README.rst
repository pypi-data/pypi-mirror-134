.. image:: https://img.shields.io/pypi/status/ProdigyHelmsman
    :alt: PyPI - Status

.. image:: https://img.shields.io/pypi/wheel/ProdigyHelmsman
    :alt: PyPI - Wheel

.. image:: https://img.shields.io/pypi/pyversions/ProdigyHelmsman
    :alt: PyPI - Python Version

.. image:: https://img.shields.io/github/v/release/hendrikdutoit/ProdigyHelmsman
    :alt: GitHub release (latest by date)

.. image:: https://img.shields.io/github/license/hendrikdutoit/ProdigyHelmsman
    :alt: License

.. image:: https://img.shields.io/github/issues-raw/hendrikdutoit/ProdigyHelmsman
    :alt: GitHub issues

.. image:: https://img.shields.io/pypi/dm/ProdigyHelmsman
    :alt: PyPI - Downloads

.. image:: https://img.shields.io/github/search/hendrikdutoit/ProdigyHelmsman/GitHub
    :alt: GitHub Searches

.. image:: https://img.shields.io/codecov/c/gh/hendrikdutoit/ProdigyHelmsman
    :alt: CodeCov
    :target: https://app.codecov.io/gh/hendrikdutoit/ProdigyHelmsman

.. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/ProdigyHelmsman/Pre-Commit
    :alt: GitHub Actions - Pre-Commit
    :target: https://github.com/hendrikdutoit/ProdigyHelmsman/actions/workflows/pre-commit.yaml

.. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/ProdigyHelmsman/CI
    :alt: GitHub Actions - CI
    :target: https://github.com/hendrikdutoit/ProdigyHelmsman/actions/workflows/ci.yaml

.. image:: https://img.shields.io/pypi/v/ProdigyHelmsman
    :alt: PyPi

Demo REST API to do enquiries of the details of a country.

    The strange name comes from the name of an entity and helmsman whois also a navigator hence looking for details of a country. TThe strange name also contribute to finding a unique name on yPI and at the same time not squatting usefull names on the public domain.


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
