Welcome to Infobase!
====================
This is a very minimalistic database module

General use
-----------------------

To create a database:

``>>>from infobase import infobase``

>>>data = infobase(name, [list, of, values])``

``>>>data.new_infobase()``

This will create a new database and store it

You can then add a row like so:

``>>>data.add_row([items, to, add])``

You can always print your data like so:

``>>>print data``

``| Num | list  | of | values |``

``| --- | ----- | -- | ------ |``

``|   1 | items | to | add    |``

Note: items will be closer together

Changelog
----------------------------------
- 0.8.Alpha

Notes for this release:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Added a changelog

If you have any bugs or ideas, or anything else:
------------------------------------------------
email me at shadow889566@gmail.com