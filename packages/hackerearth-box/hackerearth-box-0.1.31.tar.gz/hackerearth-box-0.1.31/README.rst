Library Name- BOX
=================

Task
----

Automate the installation/updation of modules/packages on the servers
according to a given dependency config file

Dependency Config File Format
=============================

.. figure:: http://i.imgur.com/52CY8JA.png
   :alt: Dependency Config File Format

Library Components
------------------

-  *config\_parser.py* - parses dependency config from given filepath
-  *utils.py* - set of utility functions such as
   dependency\_install\_manager, steps execution callable for fabric,
   etc.
-  *install.py* - this is the main file, which contains function to be
   called when the library is used
-  *exceptions.py* - this contains the various exceptions classes used
   in the library

Inputs to be given
------------------

-  **dependency config file** this is a dictionary of the given format
   with steps, action and package\_name this imports the endpoints
   callable.
-  **machines information** this is a set of machine callables which
   define a set of machines each machine has 3 components - user, key,
   endpoint

Flow
----

-  user creates a set of callables which return endpoints for machines
-  now a dependency config file is created in specified format, which
   takes callables for server for each package, and action is defined
   (INSTALL/UNINSTALL).
-  now, path to dependency config file is given to the library function
   ( handle\_dependencies() ) alongwith action(explained below)

   -  action - this is the required action of the user, i.e. if the user
      wants to execute all the packages to be installed, he will specify
      action=INSTALL, else UNINSTALL(for executing packages to be
      uninstalled)

-  handle\_dependencies() passes the dependency config filepath to the
   config\_parser which returns a dictionary of endpoints (as key) and
   packages( as value)
-  now, for every machine manage\_dependencies\_on\_machine() is called
   which takes machine and its packages and installs them using utility
   functions

3rd Party Library used
~~~~~~~~~~~~~~~~~~~~~~

-  `fabric <http://www.fabfile.org/>`__

Examples
--------

You can find examples of dependency config file, and sample machine
group class `here <box/examples/install_dependencies>`__ and
`here <box/examples/machines.py>`__.

If you are using django, you might like to use this library via a
management command , which you can find
`here <box/examples/management>`__.
