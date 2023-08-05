pyrdio
======

A simple Python wrapper for Rdio's API

Usage
=====

Authentication
--------------

Some endpoints require authentication.
To get an access token, start by initializing a client, for example:

.. code-block:: python

    >>> rdio = RdioClient(settings.RDIO_CONSUMER_KEY,
    >>>            settings.RDIO_CONSUMER_SECRET,
    >>>            settings.RDIO_REDIRECT_URI)

Redirect user to auth URL:

.. code-block:: python

    >>> print rdio.get_authorize_url()

In your authentication handler, verify the request by passing the request url, and request an access token:

.. code-block:: python

    >>> rdio.verify_request_token(url)
    >>> access_token = rdio.request_access_token()

API Endpoints`
-------------

We're currently supporting the following endpoints:

-  addToPlaylist
-  createPlaylist
-  currentUser
-  getTracksByISRC
-  search
-  tracks

Feel free to add more an send a pull requests!
For questions: hery at hi dot fi

