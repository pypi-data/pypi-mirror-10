=====================
docutils_react_docgen
=====================

.. contents::


Overview
========

docutils extension for documenting React modules.
Requires react-docgen

Example
-------

Here is the restructured text to display all of the
React modules in `static/js/lib/my`.  Source links 
to each module are relative to the `src` option::
 
    My JS/React Library
    ===================

    .. contents:: Table of Contents

    .. reactdocgen:: static/js/lib/my
            :src: https://bitbucket.org/.../my/src/tip

Installation
============

From PyPi
::

    $ pip install docutils-react-docgen 

From source
::

    $ hg clone ssh://hg@bitbucket.org/pwexler/docutils_react_docgen
    $ pip install -e docutils_react_docgen/

The installation is successful if you can import docutils_react_docgen.  
The following command must produce no errors::

    $ python -c 'import docutils_react_docgen'


Usage
-----

In your `conf.py` you must import docutils_react_docgen::

    import docutils_react_docgen
    
In your restructured text document(s) include the `reactdocgen` directive,
and the react-docgen command on the same line,
followed by zero or more option lines, 
followed by a blank line::

    .. reactdocgen::  /path/to/your/react/modules/ [react-docgen options]
        :option: value             
        
This will convert the output of::

    react-docgen /path/to/your/react/modules/ [react-docgen options]

into restructured text and insert it in place of the directive.

react-docgen lets you filter which modules to extract meta data from.
See::

    react-docgen --help

for an explanation of the react-docgen command line options.

Each module is displayed with a heading
showing the module name
(which can appear in the table of contents), 
optionally followed by a link to its source code,
followed by its description, 
followed by its properties shown alphabetically in a definition list.  

Options
-------

Each option is shown with its default value.

`module_description_missing`  
  default: Module doc string is missing!

  The string to display whenever a module's 'description' key value is empty.

`module_prop_description_missing`  
  default: Property doc string is missing!

  The string to display whenever a property's 'description' key value is empty.

`module_underline_character`  
  default: \-

  The underline character for the module heading.

`src`  
  default: 

  If empty, no link is displayed for each module.

  If not empty, it is the prefix used when linking to the source code.
  The url is the prefix followed by '/' followed by the module filename.

`tab_size`  
  default: 4

  The number of space characters to replace each tab character with.

`use_commonjs_module_name`   
  default: True

  If True, 
  a search for the CommonJS package proceeds 
  recursively starting with the given directory
  and working up the directory tree towards the root.

  If False, 
  or (if True and) no bower.json or package.json can be found,
  the module name will appear as its filename instead of its 
  CommonJS Module name.

  
Changing Default Options
------------------------

The default values of all the options 
may be changed directly.  
For example::

    import docutils_react_docgen
    docutils_react_docgen.DEFAULT_OPTIONS['module_description_missing'] = ''

Providing a Custom Formatter
----------------------------

Proceed by creating a module,
sub-classing both Formatter and ReactDocgen,
and registering your directive::

    import docutils_react_docgen
    from docutils.parsers import rst
    
    class MyFormatter(docutils_react_docgen.Formatter):
        ... overwrite methods as necessary 
        
    class MyDirective(docutils_react_docgen.ReactDocgen):
        formatter_class = MyFormatter

    rst.directives.register_directive('mydirective', MyDirective)

The formatter_class will be invoked as follows::

    rst = self.formatter_class(options, dirname).run(doc_dict)

options
    A dict of the directive options.

dirname
    The path to search for the CommonJS package.

doc_dict
    A dict of module metadata 
    such as returned by `docutils_react_docgen.react_docgen()`_

The run() method must return a string 
containing the desired restructured text.

Finally, insure that the module containing your directive is imported 
by conf.py

.. _`docutils_react_docgen.react_docgen()`: reference.html#docutils_react_docgen.docutils_react_docgen.react_docgen

