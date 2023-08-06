# stacks-textblock

A Stacks app for creating blocks of text.

## Dependencies

* `django-textplusstuff` >= 0.4
* `stacks-page` >= 0.1.1

## Release Notes

### 0.2

* Adding 1-up & 2-up StacksTextBlockList renditions and 'Full Width' StacksTextBlock rendition.

### 0.1.1

* Including templates in PyPI release.

### 0.1

* Initial open source release

## Running Tests

All commands below are run from within the `stacks-textblock` outer folder of this repo.

First create a new virtual environment and install the test requirements:

    $ pip install -r test_requirements.txt

Before running tests, first ensure this app passes a `flake8` linter check:

    $ flake8 stacks_textblock

Run the test suite with this command:

    $ coverage run --source=stacks_textblock runtests.py

See test coverage with this command:

    $ coverage report -m


