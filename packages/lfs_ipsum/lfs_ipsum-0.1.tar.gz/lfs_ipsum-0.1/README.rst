Populate your lfs installation generated content.

As of now it only generates categories. 

Installation
------------

Add ``lfs_ipsum`` to your buldout's egg list:

    [buildout]
    eggs =
        django-lfs
        lfs_ipsum
    ...
    [django]
    recipe =
        djangorecipe

    eggs =
        ${buildout:eggs}

Run buildout.

    bin/buildout

Add ``lfs_ipsum`` to your list of installed apps.

    INSTALLED_APPS = (
        ...
        'lfs_ipsum',
    )


Usage
-----

bin/django generate_categories