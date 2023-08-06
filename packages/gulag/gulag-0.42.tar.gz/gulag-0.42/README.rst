======
gulag
=======

`gulag` helps you leverage Mongo collections in Python/Django projects. Think Django model for MongoDB, but cruder.


Highlights:

- Declarative collections
- Auto-reconnect
- Readable exceptions


::
 
    import gulag

    class Task(gulag.nosql.MongoModel):
        """
        My Tasks

        == Schema ===================

        key : Cache key
        expires_utc : Expiry time
        b64: Encoded pickle
        """

        db_name = "my_database"
        col_name = "my_col"            # If not supplied, based on class name
        capped_size = 1024 * 1024      # 1 GB (omit for non-capped)

        index = [
            ("key", "is_active", "expires_utc", )
        ]

    TASK = Task()


    doc = TASK.find_one({"key": "unique"})



Installation
------------

pip install gulag


setting.py
---------
MONGO_URL      = "mongodb://127.0.0.1:27017"


Python use
----------

```
#!python

from gulag import nosql

import setting

nosql.conf.from_object(setting)


```

Contact: @jorjun