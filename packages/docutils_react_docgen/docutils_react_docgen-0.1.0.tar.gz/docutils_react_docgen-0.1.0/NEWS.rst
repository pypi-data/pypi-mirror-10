*************
 Change Log
*************

.. contents:: Table of Contents


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

