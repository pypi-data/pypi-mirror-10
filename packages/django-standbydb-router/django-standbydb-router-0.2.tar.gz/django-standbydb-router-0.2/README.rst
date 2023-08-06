``standby`` provides a Django database router useful in master-standby deployments.


MasterStandbyRouter
-----------------

With ``standbydb.MasterStandbyRouter`` all read queries will go to a standby
database;  all inserts, updates, and deletes will go to the ``default``
database.

First, define ``STANDBY_DATABASES`` in your settings.  It should be a list of
database aliases that can be found in ``DATABASES``::

    DATABASES = {
        'default': {...},
        'standby-1': {...},
        'standby-2': {...},
    }
    STANDBY_DATABASES = ['standby-1', 'standby-2']

Then put ``standbydb.MasterStandbyRouter`` into DATABASE_ROUTERS::

    DATABASE_ROUTERS = ('standbydb.MasterStandbyRouter',)

The standby databases will be chosen in round-robin fashion.

If you want to get a connection to a standby in your app, use
``standbydb.get_standby``::

    from django.db import connections
    import standbydb

    connection = connections[standbydb.get_standby()]


Running the Tests
-----------------

To run the tests, you'll need to install the development requirements::

    pip install -r requirements.txt
    ./run.sh test
