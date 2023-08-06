Mistune-Hilite
==============

`Python-Markdown Code Hilite <https://pythonhosted.org/Markdown/extensions/code_hilite.html>`_  port for `Mistune <https://github.com/lepture/mistune>`_.

Installation
------------

.. code:: shell

    $ pip install mistune-hilite


Usage
-----

.. code:: python

    import mistune
    import mistune_hilite

    text = '''
    def hello_world():
        print('Hello World')
    '''

    renderer = mistune_hilite.HiliteRenderer()
    markdown = mistune.Markdown(renderer=renderer)

    html = markdown(text)

Options
-------

TODO

License
-------

MIT
