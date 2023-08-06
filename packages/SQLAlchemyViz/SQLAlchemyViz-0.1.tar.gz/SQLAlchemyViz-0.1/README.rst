=============
SQLAlchemyViz
=============

SQLAlchemyViz is a command line utility to create entity-relations diagrams
from database schemas modeled with `SQLAlchemy <http://www.sqlalchemy.org/>`_
using `Graphviz <http://www.graphviz.org/>`_.

============
Requirements
============

Requires `Graphviz <http://www.graphviz.org/>`_ installed on your machine and the
`SQLAlchemy <http://www.sqlalchemy.org/>`_ and `pydot <https://pypi.python.org/pypi/pydot>`_ packages.

=======
License
=======

SQLAlchemyViz is distributed under the `MIT License <http://www.opensource.org/licenses/mit-license.php>`_.

==========
Quickstart
==========
Usage: sqlaviz [-h] [-f FILE] [-p PROG] [-o OPTION] [--sort-columns]
               [-g GRAPHVIZ_PATH] pkg.module:metadata

Create an ER diagram from a sqlalchemy schema object.

Positional arguments:
  pkg.module:metadata   Import path for the metadata identifier.

Optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Write diagram to specified file {default:
                        diagram.pdf}.
  -p PROG, --prog PROG  Name of the graphviz layout program to use {default:
                        "neato"}. Other choices are: "dot", "twopi", "circo"
                        or "fdp".
  -o OPTION, --opt OPTION
                        Where OPTION is e.g. "graph_bgcolor=red". May be
                        supplied multiple times.
  --sort-columns        Sort columns alphabetically.
  -g GRAPHVIZ_PATH, --graphviz GRAPHVIZ_PATH
                        Path to folder containing the graphviz executables.