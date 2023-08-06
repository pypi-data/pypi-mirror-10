.. _commands:

Commands
--------

Django-rgallery has some custom commands to ease tasks as sync the backends or
make proper thumbs.

mediasync
^^^^^^^^^

The ``mediasync`` custom command allows you to synchronize from a backend or
storage option to Django-rgallery. It's the main key of this project, tries to
download and parse photos from a source bucket, saving it on the database and
converting the photos to fit the web. This command has some interesting
arguments:

``--storage``
  Either ``dropbox`` or ``file``. The ``dropbox`` one tries to connect with
  the dropbox api credentials and retrieve the photos from the app_folder,
  please check :ref:`settings` for more information:

  .. code-block:: bash

    ./manage.py mediasync --storage=dropbox
    ./manage.py mediasync --storage=file --source=/path/to/photos

``--source``
  ``/path/to/photos``, only valid when ``--storage=file``. This argument say
  to Django-rgallery where to retrieve the photos locally, it should be a
  local folder:

  .. code-block:: bash

    ./manage.py mediasync --storage=file --source=/path/to/photos

``--tags``
  ``comma,separated,tags``. If you want to add some photos with a custom tag
  you can specify it with this argument:

  .. code-block:: bash

    ./manage.py mediasync --storage=file --source=/photos --tags=tag1,tag2

``--thumbs``
  Either ``yes`` or ``no`` (default). If you want to create thumbs of the new
  photos you can specify it with this argument:

  .. code-block:: bash

    ./manage.py mediasync --storage=file --source=/photos --thumbs=yes


mkthumb
^^^^^^^

The ``mkthumb`` command allows you to create missing thumbs. Probably sometimes
you get some photo with no thumb caused to a bad upload, connection issues or
whatever. You can rebuild thumbs with this command::

    ./manage.py mkthumb
