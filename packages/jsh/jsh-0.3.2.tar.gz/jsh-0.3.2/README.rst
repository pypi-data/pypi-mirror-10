=================================
jsh --- a Junos-style CLI library
=================================

If you've ever logged in to a Junos_ device, you'll know how good the CLI is.
It offers:

- tab-completion, including completion of names of items in the config
- help by pressing "?" at any point
- completion on pressing space or enter

We have tried to reproduce some of these features in a Python library based
on Readline.

The library takes a CLI "layout" which is a dictionary that is a tree
describing your CLI commands.  For example, if you wanted to have a totally
useless CLI with just an ``exit`` command, you would define it like this:

.. code-block:: python

    import jsh

    layout = {
        'exit': jsh.exit
    }

    cli = jsh.JSH(layout)

    while True:
        try:
            cli.read_and_execute()
        except jsh.JSHError as err:
            print err
        except EOFError:
            break

This would give you a CLI that looks like:

::

    > ?
    Possible completions:
      exit
    > ex?
    Possible completions:
      exit
    > exit ?
    Possible completions:
      <[Enter]>   Execute this command
    > exit

Now suppose you want to add some help text to describe the ``exit`` command.
For that, you need to turn ``'exit'`` into a dictionary as follows:

.. code-block:: python

    layout = {
        'exit': {
            '?': 'Quit this silly application',
            None: jsh.exit
        }
    }

So the action to take when enter is pressed after typing ``exit`` is under
the ``None`` key, and the help text is under ``'?'``.

This makes the help look like this:

::

    > ?
    Possible completions:
      exit   Quit this silly application

Let's now add some commands with more than one word and some custom
handlers.  We'll add ``show version`` and ``show pid``.  First, we'll need to
write the functions to handle them.  These functions will take a single
argument, the ``JSH`` instance.

.. code-block:: python

    import os

    def show_version(cli):
        print 'Useless CLI version 0.0.1'

    def show_pid(cli):
        print 'My PID is {0}'.format(os.getpid())

Now add these to the layout, along with help text.  The individual words in
the commands will correspond to levels in the layout tree:

.. code-block:: python

    layout = {
        'show': {
            '?': 'Display various information',
            'pid': {
                '?': 'Display my PID',
                None: show_pid
            },
            'version': {
                '?': 'Display my version',
                None: show_version
            }
        },
        'exit': {
            '?': 'Quit this silly application',
            None: jsh.exit
        }
    }

We now have this:

::

    > ?
    Possible completions:
      exit   Quit this silly application
      show   Display various information
    > show ?
    Possible completions:
      pid       Display my PID
      version   Display my version
    > show
    Incomplete command 'show'
    > show pid ?
    Possible completions:
      <[Enter]>   Execute this command
    > show pid
    My PID is 4633
    > show version
    Useless CLI version 0.0.1
    >

Now let's add some shopping list functionality: adding items to the list,
viewing the list, removing items from the list.  Viewing the list is easy:

.. code-block:: python

    shopping_list = []

    def show_list(cli):
        if not shopping_list:
            print 'Shopping list is empty'
        else:
            print 'Items:'
            print '\n'.join(shopping_list)

Adding items is even easier, but this function takes an argument:

.. code-block:: python

    def add_item(cli, item):
        shopping_list.append(item)

Let's add these to our CLI layout:

.. code-block:: python

    layout = {
        'add': {
            '?': 'Add stuff',
            'item': {
                '?': 'Add item to shopping list',
                str: {
                    '?': ('item', 'Item description'),
                    None: add_item
                }
            }
        },
        'show': {
            '?': 'Display various information',
            'list': {
                '?': 'Display shopping list',
                None: show_list
            },
            'pid': {
                '?': 'Display my PID',
                None: show_pid
            },
            'version': {
                '?': 'Display my version',
                None: show_version
            }
        },
        'exit': {
            '?': 'Quit this silly application',
            None: jsh.exit
        }
    }

There's some new stuff here, let's examine it:

.. code-block:: python

    [...]
    'item': {
        '?': 'Add item to shopping list',
        str: {
            '?': ('item', 'Item description'),
            None: add_item
        }
    }
    [...]

``str`` says that the parser should expect an arbitrary string at this point
in the command.  Pressing enter after the arbitrary string will run the
``add_item`` function with two arguments: the ``JSH`` instance and the arbitrary
string entered by the user.  Also notice that the help text is now a tuple
with the descriptive text as the second element.  The first element is a
metavariable, and you will see how this is used below.

Our CLI now looks like this:

::

    > show ?
    Possible completions:
      list      Display shopping list
      pid       Display my PID
      version   Display my version
    > show list
    Shopping list is empty
    > add ?
    Possible completions:
      item   Add item to shopping list
    > add item ?
    Possible completions:
      <item>   Item description
    > add item carrots ?
    Possible completions:
      <[Enter]>   Execute this command
    > add item carrots
    > add item courgettes
    > show list
    Items:
    carrots
    courgettes
    >

We now need a command to remove items from the list.  Here's the function to
do it:

.. code-block:: python

    def remove_item(cli, item):
        try:
            shopping_list.remove(item)
        except ValueError:
            print 'Item not in list'

Let's expand the CLI layout to handle this:

.. code-block:: python

    layout = {
        'add': {
            '?': 'Add stuff',
            'item': {
                '?': 'Add item to shopping list',
                str: {
                    '?': ('item', 'Item description'),
                    None: add_item
                }
            }
        },
        'remove': {
            '?': 'Get rid of stuff',
            'item': {
                '?': 'Remove item from shopping list',
                str: {
                    '?': ('item', 'Item to remove'),
                    None: remove_item
                }
            }
        },
        'show': {
            '?': 'Display various information',
            'list': {
                '?': 'Display shopping list',
                None: show_list
            },
            'pid': {
                '?': 'Display my PID',
                None: show_pid
            },
            'version': {
                '?': 'Display my version',
                None: show_version
            }
        },
        'exit': {
            '?': 'Quit this silly application',
            None: jsh.exit
        }
    }

We now have:

::

    > add item bananas
    > add item oranges
    > add item strawberries
    > show list
    Items:
    bananas
    oranges
    strawberries
    > remove ?
    Possible completions:
      item   Remove item from shopping list
    > remove item ?
    Possible completions:
      <item>   Item to remove
    > remove item apples
    Item not in list
    > remove item oranges
    > show list
    Items:
    bananas
    strawberries
    >

That works, but it would be great if we could tab-complete items when
removing them... and we can!  First, we need a function to list them (again,
it takes the ``JSH`` instance as the first argument, and any arbitrary string
arguments that preceed it in the command --- in this case, none):

.. code-block:: python

    def complete_items(cli):
        return shopping_list

And now we integrate this into the layout:

.. code-block:: python

    [...]
    'remove': {
        '?': 'Get rid of stuff',
        'item': {
            '?': 'Remove item from shopping list',
            '\t': complete_items,
            str: {
                '?': ('item', 'Item to remove'),
                None: remove_item
            }
        }
    },
    [...]

Here's what we have now:

::

    > add item carrots
    > add item courgettes
    > add item beetroot
    > show list
    Items:
    carrots
    courgettes
    beetroot
    > remove item ?
    Possible completions:
      <item>       Item to remove
      beetroot
      carrots
      courgettes
    > remove item c?
    Possible completions:
      <item>       Item to remove
      carrots
      courgettes
    > remove item carrots
    > show list
    Items:
    courgettes
    beetroot
    >

It's also possible for the completion function to return a dictionary.  In this
case, the keys are the possible completions and the corresponding values are
used as the descriptions in the help output.

If you want more fine-grained control over the input loop, you can separate
out reading the command and running it:

.. code-block:: python

    while True:
        try:
            command = cli.get_input()
        except EOFError:
            break

        if command:
            try:
                cli.run_command(command)
            except jsh.JSHError as err:
                print err
                
Argument Validation
-------------------

JSH allows you to validate that a user-defined token matches a format you expect. There are currently three built-in validators, but it is easy to write your own. Given the following layout:

.. code-block:: python

    layout = {
        'number': {
            '?': 'Enter a number',
            str: {
                '?': ('num', 'A number'),
                '_validate': jsh.validate_int,
            },
        },
    }
    
The user will now be unable to enter, or tab-complete, a value that is not a valid integer:

::

    > ?
    Possible completions:
      number    Enter a number
    > number ?
    Possible completions:
      num       A number
    > number foo
    Invalid argument: 'foo' is not a valid integer.
    > number 5
    
JSH provides three validators: ``JSH.validate_int``, ``JSH.validate_in(iterable)``, and ``JSH.validate_range(min, max)``. ``validate_in`` takes an interable of strings that the argument must be one of, and ``validate_range`` takes a ``min`` and ``max`` integer value that the argument must be between (inclusive).

You can easily write your own validators - just provide a function that takes two arguments (the CLI object, and the user-defined string) and returns either ``True``, or an error message.

Keyword Arguments to methods
----------------------------

By default, any user-defined arguments present in the command string will be passed in their original order to the final method that gets called when the command is submitted. To pass these as keyword arguments instead, provide an option ``_kwarg`` underneath the ``str`` layout:

.. code-block:: python

    layout = {
        'add': {
            '?': 'Add stuff',
            'item': {
                '?': 'Add item to shopping list',
                str: {
                    '?': ('item', 'Item description'),
                    None: add_item,
                    '_kwarg': 'item',
                }
            }
        },
    }
    
Now ``add_item`` will be called with ``add_item(cli, item=value)`` instead of just ``add_item(cli, value)``. This example doesn't make a difference, but with it allows you to untie your method signature from your command structure.

If you want the keyword argument name to be the same as the prior command token (as in the case above - the ``str`` follows the word 'item', and we want the keyword argument to be called ``item`` too), we can avoid defining it twice by using ``'_kwarg': True`` instead.

Sections
--------

Another feature, inspired not by the Junos CLI, but by the F5_ CLI is sections.
Sections let the user focus on a particular part of the CLI.  In our example,
we can focus on the items in the shopping list.

Let's add some commands to our layout to handle this:

.. code-block:: python

    layout = {
        '/': {
            '?': 'Go to top level',
            None: jsh.set_section(None)
        },
        '/item': {
            '?': 'Work on items',
            None: jsh.set_section('item')
        },
        'add': {
            '?': 'Add stuff',
            'item': {
                '?': 'Add item to shopping list',
                str: {
                    '?': ('item', 'Item description'),
                    None: add_item
                }
            }
        },
        'remove': {
            '?': 'Get rid of stuff',
            'item': {
                '?': 'Remove item from shopping list',
                '\t': complete_items,
                str: {
                    '?': ('item', 'Item to remove'),
                    None: remove_item
                }
            }
        },
        'show': {
            '?': 'Display various information',
            'list': {
                '?': 'Display shopping list',
                None: show_list
            },
            'pid': {
                '?': 'Display my PID',
                None: show_pid
            },
            'version': {
                '?': 'Display my version',
                None: show_version
            }
        },
        'exit': {
            '?': 'Quit this silly application',
            None: jsh.exit
        }
    }

This now lets us interact with the CLI like this:

::

    > ?
    Possible completions:
      /        Go to top level
      /item    Work on items
      add      Add stuff
      exit     Quit this silly application
      remove   Get rid of stuff
      show     Display various information
    > add ?
    Possible completions:
      item   Add item to shopping list
    > /item
    > add ?
    Possible completions:
      <item>   Item description
    > add carrots
    > add potatoes
    > show list
    Items:
    carrots
    potatoes
    > remove potatoes
    > show list
    Items:
    carrots
    >

Being inside the "item" section means that we can (and, in fact, must)
miss out the second word of a command when that word is ``item``.

Finally, it would be nice if the CLI told us which section we are currently
in.  We can do this by customising the prompt and including the string
``{section}`` in it, which will be replaced by the name of the current
section:

.. code-block:: python

    cli = jsh.JSH(
        layout,
        prompt='shopping{section}> '
    )

This gives us this:

::

    shopping> /item
    shopping(item)> /
    shopping>

We can customise the brackets around the section name, for example:

.. code-block:: python

    cli = jsh.JSH(
        layout,
        prompt='shopping{section}> ',
        section_delims=('/', '')
    )

This gives:

::

    shopping> /item
    shopping/item> /
    shopping>

However, section support is quite basic at the moment and needs more work.
It's currently nowhere near what the F5 CLI does.

Finally, there are two more settings that you can pass in when initialising
the ``JSH`` object: ``ignore_case`` (default ``False``), which controls whether
the CLI is case-sensitive and ``complete_on_space`` (default ``True``) which
controls whether command completion happens when the user presses space or
enter.

Enjoy!

.. _Junos: http://www.juniper.net/us/en/products-services/nos/junos/
.. _F5: https://f5.com/products/big-ip
