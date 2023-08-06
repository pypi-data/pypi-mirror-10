ripozo-cassandra
================

.. image:: https://travis-ci.org/vertical-knowledge/ripozo-cassandra.svg?branch=master&style=flat
    :target: https://travis-ci.org/vertical-knowledge/ripozo-cassandra?style=flat
    :alt: test status

.. image:: https://coveralls.io/repos/vertical-knowledge/ripozo-cassandra/badge.svg?branch=master&style=flat
    :target: https://coveralls.io/r/vertical-knowledge/ripozo-cassandra?branch=master&style=flat
    :alt: test coverage

.. image:: https://readthedocs.org/projects/ripozo-cassandra/badge/?version=latest&style=flat
    :target: https://ripozo-cassandra.readthedocs.org/?style=flat
    :alt: documentation


ripozo-cassandra is a ripozo-extension that provides a Manager that
integrates cqlengine (and thereby Cassandra) with ripozo.  It provides
convience functions for generating resources.  In particular it focues
on creating shortcuts for CRUD+L type operations.  It fully implements
the BaseManager_ class that is provided in the ripozo_ package.

Example
=======

This is the minimal example of creating ripozo managers with
ripozo-cassandra and integrating them with a resource. As
you can see in the example, there are only three functional
lines of code.

.. code-block:: python

    from cqlengine.models import Model
    from cqlengine import columns, connection
    from cqlengine.management import create_keyspace, sync_table, delete_keyspace

    from ripozo_cassandra import CQLManager

    from uuid import uuid4

    # Define your model
    class Person(Model):
        id = columns.UUID(primary_key=True, default=lambda:uuid4())
        first_name = columns.Text()
        last_name = columns.Text()

    # Setup cqlengine and sync the person table
    keyspace_name = 'mykeyspace'
    connection.setup(['192.168.56.102'], keyspace_name)
    create_keyspace(keyspace_name)
    sync_table(Person)

    # This is where you define your manager
    class PersonManageR(CQLManager):
        model = Person  # Assign the cqlengin model to the manager
        fields = ('id', 'first_name', 'last_name',) # Specify the fields to use for this manager

    # This is the ripozo specific part.
    # This creates a resource class that can be given
    # to a dispatcher (e.g. the flask-ripozo package's FlaskDispatcher)
    class PersonResource(ResourceBase):
        manager = PersonManager
        pks = ['id']

        # A retrieval method that will operate on the '/api/person' route
        # It retrieves the id, first_name, and last_name properties
        @apimethod(methods=['GET'])
        def get_person(cls, request):
            properties = self.manager.retrieve(request.url_params)
            return cls(properties=properties)




.. _BaseManager: https://ripozo.readthedocs.org/en/latest/API/ripozo.managers.html#ripozo.managers.base.BaseManager

.. _ripozo: https://ripozo.readthedocs.org/