QMS
===

Query Made Simple

Dependencies
------------

* PyMysql

Features
--------

* Provides SQL Query Builer

Todo
----

* Provide a better way to define qms.json (and an alternative)
* Installation process
* Any other kind of queries (update, delete, show...)
* Tests

Usage
-----

.. code-block:: bash

    from qms import *
    load_qms_config('qms.json')
    query = Query.select('some, field', 'table_name').where("field", Query.LIKE, '%a value%').orWhere("some_other_field", Query.EQUAL, "another_value");
    print(query.get())
    results = query.execute("my_handler")
    print(results)