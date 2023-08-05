normalize_cz_unicode
====================

.. image:: https://badge.fury.io/py/normalize_cz_unicode.png
    :target: http://badge.fury.io/py/normalize_cz_unicode

.. image:: https://pypip.in/d/normalize_cz_unicode/badge.png
        :target: https://pypi.python.org/pypi/normalize_cz_unicode


Sanitize unicode inputs from unwanted characters.

Principle of the module is simple; Use translation table. If the character is
not in translation table, convert it to ``latin2``. If it can't be converted,
try to normalize it using unicode `NKFD` normalization. If it can't be
normalized, replace it with ``?``.

Usage
-----

.. code-block:: python

    >>> from normalize_cz_unicode import normalize

.. code-block:: python

    >>> print normalize("Tohle je smajlík: 😭 , který tu ale nechci.")
    Tohle je smajlík: ? , který tu ale nechci.

Various whitespace and special dash characters are normalized to basic ascii:

.. code-block:: python

    >>> a = u"Spojovníky ― a další havěť jako nedělitelné mezery taky nechci."
    u'Spojovn\xedky \u2015 a dal\u0161\xed hav\u011b\u0165 jako ned\u011bliteln\xe9\u202fmezery\u2007taky nechci.'
    >>> normalize(a)
    u'Spojovn\xedky - a dal\u0161\xed hav\u011b\u0165 jako ned\u011bliteln\xe9 mezery taky nechci.'


Installation
------------

Module is hosted at `PYPI <https://pypi.python.org/pypi/normalize_cz_unicode>`_, and
can be installed using `PIP`_::

    sudo pip install normalize_cz_unicode

.. _PIP: http://en.wikipedia.org/wiki/Pip_%28package_manager%29
