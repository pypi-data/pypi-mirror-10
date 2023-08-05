pixhost-uploader
================

Unofficial Python 3.2+ upload client for pixhost.org image sharing
website.

Usage
-----

.. code::

    import pixhostuploader as pixhost

    uploaded = pixhost.upload('image.jpg')

    print(uploaded)

Uploader returns 3 URLs for each image: thumbnail, full size image and a
its page on pixhost.org.

.. code::

    {
        'thumb_image': '...',
        'full_size_image': '...',
        'page_url': '...',
    }

You can also upload multiple images at once.

.. code::

    images = [
        'image.jpg',
        'another_image.jpg',
    ]
    uploaded = pixhost.upload(images)

Uploader then returns a ``list`` of URLs for each uploaded image.

