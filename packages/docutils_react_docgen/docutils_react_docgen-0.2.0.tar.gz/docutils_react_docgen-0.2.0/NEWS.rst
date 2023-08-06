*************
 Change Log
*************

0.0.1 (2015-04-23)
==================

* initial release

0.0.2 (2015-04-27)
==================

* __init__.py: import from .docutils_react_docgen
* Converter and Formatter are subclasses of object.

0.1.0 (2015-04-30)
==================

This release is not backward compatible as some options have been removed.

* Improved display of module. 
* Infer CommonJS module name from bower.json or package.json if available.
* Thanks to Andrey Popp for adding CommonJS support!
* Removed options\:
  missing, 
  module_dict_key_emphasis, 
  module_prop_emphasis
* Added options\:
  module_description_missing, 
  module_prop_description_missing, 
  tab_size, 
  use_commonjs_module_name, 
* Added formatter_class attribute to ReactDocgen to facilitate sub-classing.

0.1.1 (2015-05-18)
==================

* Fix react_docgen() doc string, add link in README.rst

0.2.0 (2015-05-31)
==================

react_docgen() has always referenced the initial value of REACT_DOCGEN.
With this change you can now set 
which react-docgen command to run 
within conf.py.


* Added SETTINGS

* Use run_react_docgen() instead of react_docgen().

* Deprecate REACT_DOCGEN, use SETTINGS['react_docgen'] instead.
  The next major release will not include REACT_DOCGEN. 

