******
AppCLI
******

..
  AppCLI is a Python library for making command-line applications.  More 
  broadly, it's a framework for defining object properties that read their 
  default values from arbitrary sources, e.g. the command-line, configuration 
  files, environment variables, REST APIs, etc.

  defining objects with properties that are initialized from blah blah blah
  sources such as the command line, 

  It works by (allowing|providing a framework for) objects to define parameters 
  that are initialized|read from external sources, e.g. the command-line, 
  configuration files, environment variables.  

  It works by giving classes a simple way to define parameters that will be 
  initialized from external sources, e.g. the command-line, configuration 
  files, environment variables, etc.

  It works by providing a simple way for classes to define parameters that will 
  be initialized from external sources, e.g. the command-line, configuration 
  files, environment variables, etc.


  Library for making command-line applications in python.

  More broadly, it's a framework for creating objects with parameters that can 
  read default values from multiple sources, e.g. the command-line, config 
  files, environmnt variables, etc.

  for defining object parameters that can query multiple sources---e.g. the 
  command-line, configuration files, environment variables, etc.---
  default parameters of an object 
  
  Philosophy
  - 


  - Params from any source; 
  - 

  Benefits
  - Params from any source
  - objects usable from python

  Example

  - Can't have so many comments; makes it hard to grok.
  - Just want to give a sense of what it looks like.
  - Advanced users will want to see the syntax to get a sense of how it works.

  - Features to include:
    - cast?
      - int/float: do some math thing?

    - default?

    - at least two configs
      - docopt
      - appcli?
      - env var?
    - 


.. image:: https://img.shields.io/pypi/v/appcli.svg
   :target: https://pypi.python.org/pypi/appcli

.. image:: https://img.shields.io/pypi/pyversions/appcli.svg
   :target: https://pypi.python.org/pypi/appcli

.. image:: https://img.shields.io/readthedocs/appcli.svg
   :target: https://appcli.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/github/workflow/status/kalekundert/appcli/Test%20and%20release/master
   :target: https://github.com/kalekundert/appcli/actions

.. image:: https://img.shields.io/coveralls/kalekundert/appcli.svg
   :target: https://coveralls.io/github/kalekundert/appcli?branch=master

AppCLI is a Library for making command line apps.  You can also think of it as 
a library for initializing objects with values from disparate sources, e.g.  
config files, environment variables, command-line options, etc.  It's 
philosophy is that (i) it should be easy to incorporate options from the 
command line and config files, and (ii) the object should remain usable as a 
normal object in python.

Usage
=====
The following snippets introduce the basic concepts behind ``appcli``::

    import appcli
    from appcli import DocoptConfig, AppDirsConfig, Key


    # Inheriting from App will give us the ability to instantiate MyApp objects 
    # without calling the constructor, i.e. exclusively using information from 
    # the command-line and the config files.  We'll take advantage of this in 
    # the '__main__' block at the end of the script:

    class MyApp(appcli.App):
        """
    Do a thing.

    Usage:
        myapp <x> [-y]
    """
        
        # The `__config__` class variable defines locations to search for 
        # parameter values.  In this case, we specify that `docopt` should be 
        # used to parse command line arguments, and that `appdirs` should be 
        # used to find configuration files.  Note however that appcli is not 
        # tied to any particular command-line argument parser or file format.  
        # A wide variety of `Config` classes come with `appcli`, and it's also 
        # easy to write your own.

        __config__ = [
                DocoptConfig(),
                AppDirsConfig(),
        ]
        
        # The `appcli.param()` calls define attributes that will take their 
        # value from the configuration source specified above.  For example, 
        # the `x` parameter will look for an argument named `<x>` specified on 
        # the command line.  The `y` parameter is similar, but will also (i) 
        # look for a value in the configuration files if none if specified on 
        # the command line, (ii) convert the value to an integer, and (iii) use 
        # a default of 0 if no other value is found.

        x = appcli.param(
                Key(DocoptConfig, '<x>'),
        )
        y = appcli.param(
                Key(DocoptConfig, '-y'),
                Key(AppDirsConfig, 'y'),
                cast=int,
                default=0,
        )

        # Define a constructor because we want this object to be fully usable 
        # from python.  Because <x> is a required argument on the command line, 
        # it makes sense for it to be a required argument to the constructor as 
        # well.

        def __init__(self, x):
            self.x = x

        # Define one or more methods that actually do whatever this application 
        # is supposed to do.  These methods can be named anything; think of 
        # MyApp as a totally normal class by this point.  Note that `x` and `y` 
        # can be used exactly like regular attributes.

        def main(self):
            return self.x * self.y

    # Invoke the application from the command line.  Note that we can't call 
    # the constructor because it requires an `x` argument, and we don't have 
    # that information yet (because it will come from the command line).  
    # Instead we use the `from_params()` method provided by `appcli.App`.  This 
    # constructs an instance of MyApp without calling the construtor, instead 
    # depending fully on the command-line and the configuration files to 
    # provide values for every parameter.  The call to `appcli.load()` triggers 
    # the command line to be parsed, such that the `app` instance is fully 
    # initialized when the `main()` method is called.

    if __name__ == '__main__':
        app = Main.from_params()
        appcli.load(app)
        app.main()

Note that we could seamlessly use this object in another python script::

    from myapp import MyApp

    # Because we don't call `appcli.load()` in this script, the command line 
    # would not be parsed.  The configuration files would still be read, 
    # however.  In the snippet below, for example, the value of `app.y` could 
    # come from the configuration file.  See `Config.autoload` for more 
    # information on controlling which configs are used in which contexts.

    app = MyApp('abc')
    app.main()

Examples
========
For some examples of ``appcli`` being used in real scripts, check out the 
`Stepwise — Molecular Biology`__ repository.  Almost every script in this 
repository uses ``appcli``.  Below are some particular scripts that might be 
useful:

Simple scripts:

- `aliquot.py <https://github.com/kalekundert/stepwise_mol_bio/blob/master/stepwise_mol_bio/aliquot.py>`_
- `anneal.py <https://github.com/kalekundert/stepwise_mol_bio/blob/master/stepwise_mol_bio/anneal.py>`_
- `kld.py <https://github.com/kalekundert/stepwise_mol_bio/blob/master/stepwise_mol_bio/kld.py>`_

Long but straight-forward scripts:

- `pcr.py <https://github.com/kalekundert/stepwise_mol_bio/blob/master/stepwise_mol_bio/pcr.py>`_
- `spin_cleanup.py <https://github.com/kalekundert/stepwise_mol_bio/blob/master/stepwise_mol_bio/spin_cleanup.py>`_
- `gels/gel.py <https://github.com/kalekundert/stepwise_mol_bio/blob/master/stepwise_mol_bio/gels/gel.py>`_
- `gels/stain.py <https://github.com/kalekundert/stepwise_mol_bio/blob/master/stepwise_mol_bio/gels/stain.py>`_

Complex scripts:

- `serial_dilution.py <https://github.com/kalekundert/stepwise_mol_bio/blob/master/stepwise_mol_bio/serial_dilution.py>`_

  This script features parameters that depend on other parameters.  
  Specifically, the user must provide values for any three of ``volume``, 
  ``conc_high``, ``conc_low``, and ``factor``.  Whichever one isn't specified 
  is inferred from the ones that are.  This is implemented by making the 
  ``appcli`` parameters (which in this case read only from the command-line and 
  not from any config files) private, then adding public properties that are 
  calculated from the private ones.

- `digest.py <https://github.com/kalekundert/stepwise_mol_bio/blob/master/stepwise_mol_bio/digest.py>`_

  This script is actually pretty simple, but it makes used of 
  ``__bareinit__()`` to download some data from the internet.  As alluded to 
  above, ``__init__()`` is not called when ``App`` instances are initialized 
  from the command-line, because ``__init__()`` might require arbitrary 
  arguments and is therefore considered to be part of the python API.  Instead, 
  ``App`` instances are initialized by calling ``__bareinit__()`` with no 
  arguments.

- `ivtt.py <https://github.com/kalekundert/stepwise_mol_bio/blob/master/stepwise_mol_bio/ivtt.py>`_

  This script defines a custom ``Config`` class to read from a sequence 
  database. (This example might go out of date, though; I have plans to move 
  that custom ``Config`` into a different package.)

__ https://github.com/kalekundert/stepwise_mol_bio 
