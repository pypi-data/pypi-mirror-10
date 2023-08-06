**************************
djangocms-lab-publications
**************************

``djangocms-lab-publications`` is a Django app for adding sets of scientific publications with PubMed metadata to a Django site with django CMS-specific features. It uses ``pubmed-lookup`` to query PubMed using PubMed IDs or PubMed URLs.

Source code is available on GitHub at `mfcovington/djangocms-lab-publications <https://github.com/mfcovington/djangocms-lab-publications>`_. Information about and source code for ``pubmed-lookup`` is available on GitHub at `mfcovington/pubmed-lookup <https://github.com/mfcovington/pubmed-lookup>`_.

.. contents:: :local:


Installation
============

**PyPI**

.. code-block:: sh

    pip install djangocms-lab-publications

**GitHub**

.. code-block:: sh

    pip install https://github.com/mfcovington/djangocms-lab-publications/releases/download/0.1.4/djangocms-lab-publications-0.1.4.tar.gz


Configuration
=============

Do the following in ``settings.py``:

- Add ``cms_lab_publications`` and its dependencies to ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'taggit',
        'taggit_helpers',
        'cms_lab_publications',
        'easy_thumbnails',
        'filer',
        'mptt',
    )


- Specify your media settings, if necessary:

.. code-block:: python

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



- Add ``filer`` and ``easy_thumbnail`` settings: 

.. code-block:: python

    # For filer's Django 1.7 compatibility
    MIGRATION_MODULES = {
        ...
        'filer': 'filer.migrations_django',
    }

    # For easy_thumbnails to support retina displays (recent MacBooks, iOS)
    THUMBNAIL_HIGH_RESOLUTION = True
    THUMBNAIL_QUALITY = 95
    THUMBNAIL_PROCESSORS = (
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters',
    )
    THUMBNAIL_PRESERVE_EXTENSIONS = ('png', 'gif')
    THUMBNAIL_SUBDIR = 'versions'


If ``cms_lab_publications`` is used in a project served by Apache, a config directory must be created within the Apache user's home directory. This config directory is used by code within biopython's ``Bio.Entrez.Parser.DataHandler`` which is used by ``pubmed_lookup``, a dependency of ``cms_lab_publications``.

.. code-block:: sh

    # In this snippet, the Apache user is 'www-data' and
    # the Apache user's home directory is '/var/www/'
    sudo su - root
    cd /var/www/
    chown :www-data
    chmod g+s 
    mkdir -p /var/www/.config/biopython/Bio/Entrez/DTDs


Migrations
==========

Create and perform ``cms_lab_publications`` migrations:

.. code-block:: sh

    python manage.py makemigrations cms_lab_publications
    python manage.py migrate


Usage
=====

- Start the development server:

.. code-block:: sh

    python manage.py runserver

- Visit: ``http://127.0.0.1:8000/``
- Create a CMS page.
- Insert the ``Publication Set Plugin`` into a placeholder field.

*Version 0.1.4*


Revision History
================

0.1.4 2015-06-24

- Allow manual entry of Publications that don't have a PubMed ID
- Use django-taggit-helpers in admin
- Rename deprecated queryset method
- Configure bumpversion & wheel for easier distribution
- Convert README and changelog to reStructuredText for distribution via PyPI
- Minor changes to admin interface

  - Change pagination description to 'pubs per page'
  - Add/update help text for 'tags' and 'pagination'


0.1.3 2015-06-03

- Allow bulk PubMed queries for a Publication Set
- Allow a Publication Set to be created without publications
- Default to no pagination (hides page '1' button for short publication sets)
- Set default Publication Set label to 'Publications'
- Admin improvements

  - Publication Admin

    - Reorder Publication Admin's inlines
    - Add year and PubMed ID to Publication Admin search field
    - Display (and sort by) # of Publication Sets in Publication Admin

  - Publication Set Admin

    - In Publication Set Admin, move publications from a tabular inline to a vertical filter
    - Reorder Publication Set Admin's list display items
    - Filter Publication Set records by whether its Bulk PubMed Query failed
    - Display whether a Publication Set's Bulk PubMed Query status is OK

  - Other

    - Update and improve layout of help text
    - Add short descriptions for custom list display items
    - Add docstring for MissingAttachmentListFilter


0.1.2 2015-05-27

- Expand documentation for installation and configuration
- Add mini_citation field to Publication

  - Helps identify publication when in edit mode (without expanding PubMed Metadata fieldset)
  - Helps naming associated files (PDF, Supplemental, and Image) by providing a base name
  - Bumps ``pubmed-lookup`` dependency to version 0.1.1

- Many improvements to Publication and Publication Set Admins

  - Rearrange Publication Admin fieldsets
  - Add PublicationSetInline to PublicationAdmin
  - Add save button across tops of Publication and Publication Set Admins
  - Now Powered by Blackina
  - Display whether a record has PDF/Supp/Image attachments in Publication Admin
  - Filter PublicationAdmin by missing/existing attachments
  - Filter Publication and Publication Set Admins by tags for the current model only
  - Show (and sort by) 'number of publications' for records in Publication Set Admin


0.1.1 2015-05-23

- Allow multiple Publication Set plugins per page
- Use Publication Set's name, not label, for ``__str__`` and ordering


0.1.0 2015-05-22

- A Django app for adding sets of scientific publications with PubMed metadata to a Django site with django CMS-specific features


