mezzanine-slideshows
====================

mezzanine-sermons is for use with the `Mezzanine
CMS <http://mezzanine.jupo.org/>`__. It allows the management and display of sermons and sermon series.

Requirements
------------

mezzanine-sermons requires that the following python apps be
installed:

-  Python 3.4
-  Mezzanine 3.1 (and its dependencies)
-  Django 1.7 +  (this app uses the django migrations framework)

Installation
------------

1. The easiest method is to install directly from pypi using
   `pip <http://www.pip-installer.org/>`__ by running the command below:

::

    $ pip install mezzanine-sermons


2. Add mezzanine\_sermons to INSTALLED\_APPS in settings.py
   immediately after your Django apps and before your Mezzanine apps:

   .. code:: python

       INSTALLED_APPS = (
           ...
           "mezzanine_sermons",
           ...
           )


4. Run ``python manage.py migrate mezzanine_sermons`` to create the
   mezzanine-slideshows models.

5. The app comes with three templates which can hook into your project.
   Hook the url into your project

   .. code:: python

       url(r'^sermons/', include('mezzanine_sermons.urls', namespace="sermons", app_name='mezzanine_sermons')),


   Then create pages using base.html at:
   *   sermons
   *   sermons/allseries

   The block {% full_width_content %} must appear in your base as this is where the template places the data.

