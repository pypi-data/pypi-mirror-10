Generating graphs
=================

You can generate a graph of your infrastructure with the ``dot`` command::

    $ touchdown dot

This will output a ``dot`` file that can be processed with graphviz or
displayed with a tool like xdot. On Ubuntu you can run this from the
commandline:

    $ touchdown dot > mygraph.dot
    $ xdot mygraph.dot
