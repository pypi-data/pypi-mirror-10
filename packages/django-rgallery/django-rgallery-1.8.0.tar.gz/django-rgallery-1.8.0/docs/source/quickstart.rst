Quickstart
==========

.. _installation:

Installation
------------

* Install Django-rgallery with your favorite Python package manager, ``pip``
  will install the dependencies too (compressor, sorl.thumbnail, taggit,
  etc...)::

    pip install django-rgallery

* Add ``'compressor'``, ``'sorl.thumbnail'``, ``'taggit'`` and ``'rgallery'`` to
  your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        # rgallery-dependencies
        'compressor',
        'sorl.thumbnail',
        'taggit',
        'rgallery',
    )

* Add a proper url for the application in your project urls.py::

    url(r'^gallery/', include('rgallery.urls',
                              namespace='rgallery',
                              app_name='rgallery')),

  You probably wants to add this urls too just in case you're using
  ``debug_toolbar`` and serving media elements in a development enviroment::

    if settings.DEBUG:
        import debug_toolbar
        urlpatterns += patterns(
            '',
            url(r'^__debug__/', include(debug_toolbar.urls)),
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT, }),
        )


* Execute a ``syncdb`` command in your django project::

    ./manage.py syncdb

* See the list of :ref:`settings` to modify Django Compressor's
  default behaviour and make adjustments for your website.

.. _dependencies:

Dependencies
------------

Other required packages
^^^^^^^^^^^^^^^^^^^^^^^

In case you're installing Django-rgallery differently (e.g. directly from
the repo), make sure to attach it in develop mode::

    python setup.py develop

This ensures that you install all the required dependencies.

Template dependencies
^^^^^^^^^^^^^^^^^^^^^

Django-rgallery templates have some functionality that depends on software like
jquery_ or dropzonejs_. You have to install and link them from your django
project ``site_base.html`` template. The static files dependencies are the
following:

- jquery_
- bootstrap_
- fontawesome_
- mediaelementjs_
- colorbox_
- dropzonejs_
- select2_
- jquery-cookie_

At this point, a good recommendation to work with static files as packages for
install, update new versions... is bower_. You can just install ``bower`` in
your system, create a ``bower.json`` a ``.bowerrc`` files like the following
ones and type a::

    bower install

.. _bowerjson:

bower.json
""""""""""

.. code-block:: json

    {
      "name": "my-project",
      "version": "1.0.0",
      "dependencies": {
        "jquery": "~1.9.1",
        "bootstrap": "~3.0.3",
        "font-awesome": "~4.0.3",
        "mediaelement": "~2.13.1",
        "jquery-colorbox": "~1.4.26",
        "dropzone": "3.10.2",
        "select2": "3.5.2",
        "jquery-cookie": "~1.4.1"
      }
    }

.bowerrc
""""""""

In the ``.bowerrc`` file we can configure where to store the bower installation,
in this case ``project/static/vendors`` will do the job:

.. code-block:: json

    {
        "directory" : "project/static/vendors"
    }

site_base.html
""""""""""""""

We have to put all the css/js referencies and links in our project
``site_base.html``, let me show you a sample:

.. code-block:: html

    {% load staticfiles %}
    <link rel="stylesheet" href="{% static 'vendors/font-awesome/css/font-awesome.min.css' %}">
    <link rel="stylesheet" href="{% static 'vendors/mediaelement/build/mediaelementplayer.min.css' %}">
    <link rel="stylesheet" href="{% static 'vendors/jquery-colorbox/example3/colorbox.css' %}">
    <link rel="stylesheet" href="{% static 'vendors/dropzone/downloads/css/dropzone.css' %}">
    <link rel="stylesheet" href="{% static 'vendors/select2/select2.css' %}">
    <link rel="stylesheet" href="{% static 'vendors/select2/select2-bootstrap.css' %}">
    ....
    <script type="text/javascript" src="{% static 'vendors/jquery/jquery.js' %}"></script>
    <script type="text/javascript" src="{% static 'vendors/bootstrap/js/transition.js' %}"></script>
    <script type="text/javascript" src="{% static 'vendors/bootstrap/js/alert.js' %}"></script>
    <script type="text/javascript" src="{% static 'vendors/bootstrap/js/modal.js' %}"></script>
    <script type="text/javascript" src="{% static 'vendors/bootstrap/js/dropdown.js' %}"></script>
    <script type="text/javascript" src="{% static 'vendors/bootstrap/js/scrollspy.js' %}"></script>
    <script type="text/javascript" src="{% static 'vendors/bootstrap/js/tab.js' %}"></script>
    <script type="text/javascript" src="{% static 'vendors/bootstrap/js/tooltip.js' %}"></script>
    <script type="text/javascript" src="{% static 'vendors/bootstrap/js/popover.js' %}"></script>
    <script type="text/javascript" src="{% static 'vendors/bootstrap/js/button.js' %}"></script>
    <script type="text/javascript" src="{% static 'vendors/bootstrap/js/collapse.js' %}"></script>
    <script type="text/javascript" src="{% static 'vendors/bootstrap/js/carousel.js' %}"></script>
    <script type="text/javascript" src="{% static 'vendors/bootstrap/js/affix.js' %}"></script>
    <script type="text/javascript" src="{% static 'vendors/jquery-colorbox/jquery.colorbox.js' %}"></script>
    <script type="text/javascript" src="{% static 'vendors/mediaelement/build/mediaelement-and-player.min.js' %}"></script>
    <script type="text/javascript" src="{% static 'vendors/dropzone/downloads/dropzone.min.js' %}"></script>
    <script type="text/javascript" src="{% static 'vendors/select2/select2.min.js' %}"></script>
    <script type="text/javascript" src="{% static 'vendors/jquery-cookie/jquery.cookie.js' %}"></script>

Optionally you can add your own custom css/less/js files:

.. code-block:: html

    <link rel="stylesheet" href="{% static 'less/custom.less' %}" type="text/less">
    ...
    <script type="text/javascript" src="{% static 'js/custom.js' %}"></script>


.. _fromscratch:

From Scratch
------------
To install Django-rgallery in a Django project from scratch we have to be used
to tools like ``pip``, ``virtualenv``, ``bower``... We are going to start
creating the Django base project where we'll install Django-gallery.

Django base project
^^^^^^^^^^^^^^^^^^^

We are going to start creating the virtualenv where we will install Django and
our base project `MyCustomProject`::

    $ mkdir MyCustomProject
    $ cd MyCustomProject
    $ virtualenv env
    $ . env/bin/activate

Now it's time to install Django and create our Django project::

    (env)$ pip install "Django < 1.9"
    (env)$ django-admin.py startproject --template=https://bitbucket.org/r0sk/tsd-template/get/1.8.zip my_custom_prj

We're using a two-scoops-django template and Django 1.8 for now, next step is
to install requirements and check that bower has all the Django-rgallery
dependencies::

    (env)$ cd my_custom_prj
    (env)$ pip install -r requirements/devel.txt
    (env)$ cd my_custom_prj
    (env)$ chmod +x manage.py

We must ensure that :ref:`bowerjson` has all mentioned dependencies and lastly::

    (env)$ bower install

After that it's time to sync database, check your project settings, ensure that
the database is created and you have access with the proper user/pass and::

    (env)$ ./manage.py syncbd

Adding Django-rgallery
^^^^^^^^^^^^^^^^^^^^^^

Now that you have a base project ready for Django-rgallery, let's install and
configure it, something so similar as we did in :ref:`installation` before,
``pip install django-rgallery``, add the ``INSTALLED_APPS``, edit the
``urls.py`` file, perform a new ``syncdb`` and add the custom :ref:`settings`.

If all is going in a good way and you have the proper ``site_base.html``
template (in the ``rgallery/templates/rgallery`` directory there is a sample
about how the ``site_base.html`` should be) you will see something similar to:

.. image:: django-rgallery002.png

.. _jquery: http://jquery.com
.. _dropzonejs: http://www.dropzonejs.com/
.. _bootstrap: http://getbootstrap.com
.. _fontawesome: http://fontawesome.io/
.. _mediaelementjs: http://mediaelementjs.com/
.. _colorbox: http://www.jacklmoore.com/colorbox/
.. _select2: https://select2.github.io/
.. _jquery-cookie: https://github.com/carhartl/jquery-cookie
.. _bower: http://bower.io/