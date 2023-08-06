**PyAV** Documentation
======================

**PyAV** aims to be a Pythonic binding for FFmpeg_ or Libav_. We aim to provide all of the power and control of the underlying library, but manage the gritty details for you as much as possible.

Currently we provide the basics of:

- :class:`containers <.Container>`
- devices (by specifying a format)
- audio/video/subtitle :class:`streams <.Stream>`
- :class:`packets <.Packet>`
- audio/video :class:`frames <.Frame>`
- :class:`data planes <.Plane>`
- :class:`subtitles <.Subtitle>`
- and a few more utilities.

.. _FFmpeg: http://ffmpeg.org
.. _Libav: http://libav.org


Basic Demo
----------

::

    import av

    container = av.open('/path/to/video.mp4')
    video = next(s for s in container.streams if s.type == b'video')

    for packet in container.demux(video):
        for frame in packet.decode():
            frame.to_image().save('/path/to/frame-%04d.jpg' % frame.index)


Contents
--------

.. toctree::
    :maxdepth: 2

    about
    installation
    api
    includes


Indices and Tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

