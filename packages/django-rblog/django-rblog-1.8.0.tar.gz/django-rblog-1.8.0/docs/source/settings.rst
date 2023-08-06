.. _settings:

Settings
========

.. currentmodule:: django.conf.settings

Django-rgallery has a number of settings that control its behavior.
They've been given sensible defaults.

Base settings
-------------

.. attribute:: RBLOG_PRIVATE

    :Default: ``False``

    Set this option to ``False`` if you want a public blog, otherwise set
    it to  ``True`` and blog will only be available once logged in.

.. attribute:: GALLERY_DESCRIPTION

    :Example: ``'This is my new gallery'``

    String that describes your gallery

.. attribute:: GALLERY_KEYWORDS

    :Example: ``'photos, moblog, photography, photoblog, shots'``

    String with comma separated keywords that describes your gallery

.. attribute:: DROPBOX_APP_KEY

    :Example: ``d232fg3f234d32``

    Just in case you want to use dropbox as backend, we need the APP_KEY that
    dropbox gives to you when you create your app there.

.. attribute:: DROPBOX_APP_SECRET

    :Example: ``fn5njgkl2n5gnb5``

    Just in case you want to use dropbox as backend, we need the APP_SECRET that
    dropbox gives to you when you create your app there.

.. attribute:: DROPBOX_ACCESS_TYPE

    :Example: ``app_folder`` or ``dropbox``

    If the access is ``dropbox`` you need to specify the path, if it's
    ``app_folder`` it is ok with ``/``

.. attribute:: DROPBOX_ACCESS_PATH

    :Example: ``/`` or ``custom_path/``

    The path where the photos are stored in Dropbox, to export from there to our
    rgallery instance.

.. attribute:: RGALLLERY_THUMBS

    :Example: ``[60, 200, 750, 1000]``

    The list of sizes you want to make thumbnail, it mainly depends on the use
    of the photo you will make in template.

.. attribute:: FFPROBE

    :Example: ``/opt/local/bin/ffprobe``

    The path to ``ffprobe`` command in your system.

.. attribute:: FFMPEG

    :Example: ``/opt/local/bin/ffmpeg``

    The path to ``ffmpeg`` command in your system.

.. attribute:: FFMPEG_VCODEC_THUMB

    :Example: ``png``

    The photo (from video) format.

.. attribute:: FFMPEG_THUMB_SIZE

    :Example: ``444x250``

    The photo (from video) thumb size.

.. attribute:: FFMPEG_THUMB_SIZE_INVERSE

    :Example: ``250x444``

    The photo (from video) thumb inversed size.

.. attribute:: HOMETAG

    :Example: ``tag1``

    This is the default tag that will be applied to all the synced photos. It's
    not required at all.

.. attribute:: MEDIASYNCDIR

    :Example: ``/path/to/photos``

    The path where the photos are stored in local dir, this dir will be read by
    default when making a ``mediasync --storage=file`` if there is no
    ``--source`` option.

.. attribute:: THUMBNAIL_DEBUG

    :Default: ``True``

    ``False`` is great for devel enviroments where you have no all the images
    in disk, instead of see errors all the time you can put this setting to
    ``False`` and start debugging.

    .. warning::

        Don't use this option in production!


Settings example
----------------

.. code-block:: python

    ########## DJANGO-RGALLERY
    GALLERY_DESCRIPTION = 'Moblog, day by day photos, shots usually from mobile'
    GALLERY_KEYWORDS = 'photo, fotoblog, daily photos, moblog, photoblog, shots'
    DROPBOX_APP_KEY = '123d32d23dwfqwf'
    DROPBOX_APP_SECRET = 'b567brb45n45n'
    DROPBOX_ACCESS_TYPE = 'app_folder'
    DROPBOX_ACCESS_PATH = '/'
    RGALLLERY_THUMBS = [60, 200, 750, 1000]
    FFPROBE = '/opt/local/bin/ffprobe'
    FFMPEG = '/opt/local/bin/ffmpeg'
    FFMPEG_VCODEC_THUMB = 'png'
    FFMPEG_THUMB_SIZE = '444x250'
    FFMPEG_THUMB_SIZE_INVERSE = '250x444'
    HOMETAG = 'tag1'
    MEDIASYNCDIR = '/path/to/your/photos'
    ########## DJANGO-RGALLERY

