.. _backends:

Backends
--------

In some cases it's useful to use a kind of backend as dropbox, but in other
cases something like a local dir where the photos are stored in or a form in
the web could be great sources too.

Dropbox
^^^^^^^

The dropbox backend connects to the dropbox api to download and save the photos
from a proper folder to Django-rgallery. You can activate it by enabling custom
dropbox :ref:`settings` and running the ``mediasync`` custom command
(:ref:`commands`) with the proper ``--storage=dropbox`` option::

    python manage.py mediasync --storage=dropbox

File
^^^^

The file backend connects to a local folder and download all the photos there,
saving them into Django-rgallery. You can activate it by running custom
``mediasync`` command (:ref:`commands`) with the proper ``--storage=file`` and
``--source=/path/to/photos``
options::

    python manage.py mediasync --storage=file --source=/path/to/photos


Form
^^^^

The form backend is used to save photos from the DropzoneJS input. If you're a
site administrator it will appears in your Django-gallery index page:

.. image:: django-rgallery001.png