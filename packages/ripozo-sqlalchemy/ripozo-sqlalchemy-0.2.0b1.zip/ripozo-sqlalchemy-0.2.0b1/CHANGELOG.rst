0.2.0b1 (2015-06-05)
====================

- Breaking Change: You are now required to inject a session handler on instantiation of the manager.


0.1.6b1 (2015-06-04)
====================

- Sessions are only grabbed once in any given method.  This allows you to safely return a new session every time
- Added a method for after a CRUD statement has been called.


0.1.5 (2015-04-28)
==================

- Optimization for retrieving lists using ``AlchemyManager.list_fields`` property for retrieving lists
- Retrieve list now properly applies filters.
- meta links updated in retrieve_list.  They now are contained in the links dictionary
- previous linked rename to prev in retrieve_list meta information


0.1.4 (2015-03-26)
==================

- Nothing changed yet.


0.1.3 (2015-03-26)
==================

- Nothing changed yet.


0.1.2 (2015-03-24)
==================

- NotFoundException raised when retrieve is called and no model is found.


0.1.1 (2015-03-15)
==================

- Added convience attribute for using all of the columns on the model.