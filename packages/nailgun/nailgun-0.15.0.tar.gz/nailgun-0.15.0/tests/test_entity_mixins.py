"""Tests for :mod:`nailgun.entity_mixins`."""
# pylint:disable=too-many-public-methods
#
# Python 3.3 and later includes module `ipaddress` in the standard library. If
# Robottelo ever moves past Python 2.x, that module should be used instead of
# `socket`.
from fauxfactory import gen_integer
from nailgun import client, config, entity_mixins
from nailgun.entity_fields import (
    IntegerField,
    OneToManyField,
    OneToOneField,
    StringField,
)
import mock
import unittest


class SampleEntity(entity_mixins.Entity):
    """Sample entity to be used in the tests"""

    def __init__(self, server_config=None, **kwargs):
        self._fields = {'name': StringField(), 'number': IntegerField()}
        self._meta = {'api_path': 'foo'}
        super(SampleEntity, self).__init__(server_config, **kwargs)


class ManyRelatedEntity(entity_mixins.Entity):
    """An entity with a :class:`nailgun.entity_fields.OneToManyField`.

    The ``OneToOneField`` on this entity points to
    :class:`tests.test_entity_mixins.SampleEntity`.

    """

    def __init__(self, server_config=None, **kwargs):
        self._fields = {'entities': OneToManyField(SampleEntity)}
        super(ManyRelatedEntity, self).__init__(server_config, **kwargs)


class EntityWithDelete(entity_mixins.Entity, entity_mixins.EntityDeleteMixin):
    """An entity that can be deleted.

    This entity inherits from :class:`nailgun.entity_mixins.EntityDeleteMixin`.

    """

    def __init__(self, server_config=None, **kwargs):
        self._meta = {'api_path': ''}
        super(EntityWithDelete, self).__init__(server_config, **kwargs)


class EntityWithRead(entity_mixins.Entity, entity_mixins.EntityReadMixin):
    """An entity that can be read.

    This entity inherits from :class:`nailgun.entity_mixins.EntityReadMixin`.

    """

    def __init__(self, server_config=None, **kwargs):
        self._fields = {
            'one_to_one': OneToOneField(SampleEntity),
            'one_to_many': OneToManyField(SampleEntity),
        }
        self._meta = {'api_path': ''}
        super(EntityWithRead, self).__init__(server_config, **kwargs)


class EntityWithCreateRead(
        entity_mixins.Entity,
        entity_mixins.EntityCreateMixin,
        entity_mixins.EntityReadMixin):
    """An entity that can be created and read.

    This entity inherits from :class:`nailgun.entity_mixins.EntityCreateMixin`
    and :class:`nailgun.entity_mixins.EntityReadMixin`.

    """

    def __init__(self, server_config=None, **kwargs):
        self._fields = {'integer_field': IntegerField()}
        self._meta = {'api_path': ''}
        super(EntityWithCreateRead, self).__init__(server_config, **kwargs)


# -----------------------------------------------------------------------------


class MakeEntityFromIdTestCase(unittest.TestCase):
    """Tests for :func:`nailgun.entity_mixins._make_entity_from_id`."""
    # pylint:disable=protected-access

    def setUp(self):
        """Set ``self.server_config``."""
        self.server_config = config.ServerConfig('example.com')

    def test_pass_in_entity_obj(self):
        """Pass in an entity class and an entity."""
        self.assertIsInstance(
            entity_mixins._make_entity_from_id(
                SampleEntity,
                SampleEntity(self.server_config),
                self.server_config
            ),
            SampleEntity
        )

    def test_pass_in_entity_id(self):
        """Pass in an entity class and an entity ID."""
        entity_id = gen_integer(min_value=1)
        entity_obj = entity_mixins._make_entity_from_id(
            SampleEntity,
            entity_id,
            self.server_config
        )
        self.assertIsInstance(entity_obj, SampleEntity)
        self.assertEqual(entity_obj.id, entity_id)  # pylint:disable=no-member


class MakeEntitiesFromIdsTestCase(unittest.TestCase):
    """Tests for ``_make_entity_from_ids``."""
    # pylint:disable=protected-access

    def setUp(self):
        """Set ``self.server_config``."""
        self.server_config = config.ServerConfig('example.com')

    def test_pass_in_emtpy_iterable(self):
        """Pass in an entity class and an empty iterable."""
        for iterable in ([], tuple()):
            self.assertEqual(
                [],
                entity_mixins._make_entities_from_ids(
                    SampleEntity,
                    iterable,
                    self.server_config
                )
            )

    def test_pass_in_entity_obj(self):
        """Pass in an entity class and an iterable containing entities."""
        for num_entities in range(4):
            input_entities = [
                SampleEntity(self.server_config) for _ in range(num_entities)
            ]
            output_entities = entity_mixins._make_entities_from_ids(
                SampleEntity,
                input_entities,
                self.server_config
            )
            self.assertEqual(num_entities, len(output_entities))
            for output_entity in output_entities:
                self.assertIsInstance(output_entity, SampleEntity)

    def test_pass_in_entity_ids(self):
        """Pass in an entity class and an iterable containing entity IDs."""
        for num_entities in range(4):
            entity_ids = [
                gen_integer(min_value=1) for _ in range(num_entities)
            ]
            entities = entity_mixins._make_entities_from_ids(
                SampleEntity,
                entity_ids,
                self.server_config
            )
            self.assertEqual(len(entities), len(entity_ids))
            for i in range(len(entity_ids)):
                self.assertIsInstance(entities[i], SampleEntity)
                self.assertEqual(entities[i].id, entity_ids[i])

    def test_pass_in_both(self):
        """Pass in an entity class and an iterable with entities and IDs."""
        entities = entity_mixins._make_entities_from_ids(
            SampleEntity,
            [SampleEntity(self.server_config), 5],
            self.server_config
        )
        self.assertEqual(len(entities), 2)
        for entity in entities:
            self.assertIsInstance(entity, SampleEntity)


class EntityTestCase(unittest.TestCase):
    """Tests for :class:`nailgun.entity_mixins.Entity`."""

    def setUp(self):
        """Set ``self.server_config``."""
        self.server_config = config.ServerConfig('http://example.com')

    def test_entity_get_fields(self):
        """Test :meth:`nailgun.entity_mixins.Entity.get_fields`."""
        fields = SampleEntity(self.server_config).get_fields()

        self.assertIn('name', fields)
        self.assertIn('number', fields)

        self.assertIsInstance(fields['name'], StringField)
        self.assertIsInstance(fields['number'], IntegerField)

    def test_entity_get_values(self):
        """Test :meth:`nailgun.entity_mixins.Entity.get_values`."""
        self.assertEqual(SampleEntity(self.server_config).get_values(), {})
        self.assertEqual(
            SampleEntity(self.server_config, name='Alice').get_values(),
            {'name': 'Alice'}
        )
        self.assertDictEqual(
            SampleEntity(self.server_config, name='Ed', number=2).get_values(),
            {'name': 'Ed', 'number': 2}
        )
        self.assertDictEqual(
            SampleEntity(self.server_config, number=3).get_values(),
            {'number': 3}
        )

    def test_path(self):
        """Test :meth:`nailgun.entity_mixins.Entity.path`."""
        base_path = '{0}/{1}'.format(
            self.server_config.url,
            # pylint:disable=protected-access
            SampleEntity(self.server_config)._meta['api_path']
        )
        self.assertEqual(SampleEntity(self.server_config).path(), base_path)
        self.assertEqual(
            SampleEntity(self.server_config, id=5).path(),
            base_path + '/5',
        )
        self.assertEqual(
            SampleEntity(self.server_config, id=5).path('base'),
            base_path,
        )
        with self.assertRaises(entity_mixins.NoSuchPathError):
            SampleEntity(self.server_config).path('self')

    def test_no_such_field_error(self):
        """Try to raise a :class:`nailgun.entity_mixins.NoSuchFieldError`."""
        SampleEntity(self.server_config, name='Alice')
        with self.assertRaises(entity_mixins.NoSuchFieldError):
            SampleEntity(self.server_config, namee='Alice')

    def test_bad_value_error(self):
        """Try to raise a :class:`nailgun.entity_mixins.BadValueError`."""
        ManyRelatedEntity(self.server_config, entities=[1])
        with self.assertRaises(entity_mixins.BadValueError):
            ManyRelatedEntity(self.server_config, entities=1)

    def test_repr_v1(self):
        """Test method ``nailgun.entity_mixins.Entity.__repr__``.

        Assert that ``__repr__`` works correctly when no arguments are passed
        to an entity.

        """
        entity = ManyRelatedEntity(self.server_config)
        target = 'tests.test_entity_mixins.ManyRelatedEntity({0})'.format(
            repr(self.server_config)
        )
        self.assertEqual(repr(entity), target)
        import nailgun  # noqa pylint:disable=unused-variable
        import tests  # noqa pylint:disable=unused-variable
        # pylint:disable=eval-used
        self.assertEqual(repr(eval(repr(entity))), target)

    def test_repr_v2(self):
        """Test method ``nailgun.entity_mixins.Entity.__repr__``.

        Assert that ``__repr__`` works correctly when an ID is passed to an
        entity.

        """
        entity = ManyRelatedEntity(self.server_config, id=gen_integer())
        target = (
            'tests.test_entity_mixins.ManyRelatedEntity({0}, id={1})'
            .format(
                repr(self.server_config),
                entity.id  # pylint:disable=no-member
            )
        )
        self.assertEqual(repr(entity), target)
        import nailgun  # noqa pylint:disable=unused-variable
        import tests  # noqa pylint:disable=unused-variable
        # pylint:disable=eval-used
        self.assertEqual(repr(eval(repr(entity))), target)

    def test_repr_v3(self):
        """Test method ``nailgun.entity_mixins.Entity.__repr__``.

        Assert that ``__repr__`` works correctly when one entity has a foreign
        key relationship to a second entity.

        """
        entity_id = gen_integer()
        target = (
            'tests.test_entity_mixins.ManyRelatedEntity('
            '{0}, '
            'entities=[tests.test_entity_mixins.SampleEntity({0}, id={1})]'
            ')'
            .format(self.server_config, entity_id)
        )
        entity = ManyRelatedEntity(
            self.server_config,
            entities=[SampleEntity(self.server_config, id=entity_id)]
        )
        self.assertEqual(repr(entity), target)
        import nailgun  # noqa pylint:disable=unused-variable
        import tests  # noqa pylint:disable=unused-variable
        # pylint:disable=eval-used
        self.assertEqual(repr(eval(repr(entity))), target)


class EntityDeleteMixinTestCase(unittest.TestCase):
    """Tests for entity mixin classes."""

    def setUp(self):
        """Set ``self.server_config`` and ``self.entity_id``."""
        # Example usage: SomeEntity(server_config, id=self.entity_id)
        self.server_config = config.ServerConfig(
            'example.com',
            auth=('Alice', 'hackme'),
            verify=True,
        )
        self.entity_id = gen_integer(min_value=1)

    def test_delete_200(self):
        """Test :meth:`nailgun.entity_mixins.EntityDeleteMixin.delete`.

        Assert that ``delete`` returns a JSON-decoded response from the server
        when an HTTP 200 status code is returned.

        """
        delete_return = mock.Mock()
        delete_return.status_code = 200
        delete_return.json.return_value = {'9501743': '14697417'}  # arbitrary
        with mock.patch.object(client, 'delete') as client_delete:
            client_delete.return_value = delete_return
            self.assertEqual(
                EntityWithDelete(
                    self.server_config,
                    id=self.entity_id
                ).delete(),
                delete_return.json.return_value
            )

    def test_delete_202(self):
        """Test :meth:`nailgun.entity_mixins.EntityDeleteMixin.delete`.

        Assert that ``delete`` returns information about a foreman task when an
        HTTP 202 status code is returned.

        """
        delete_return = mock.Mock()
        delete_return.status_code = 202
        delete_return.json.return_value = {'id': gen_integer()}  # mock task ID
        with mock.patch.object(client, 'delete') as client_delete:
            client_delete.return_value = delete_return
            with mock.patch.object(entity_mixins, '_poll_task') as poller:
                poller.return_value = {'324171': '59601212'}  # arbitrary
                self.assertEqual(
                    EntityWithDelete(
                        self.server_config,
                        id=self.entity_id
                    ).delete(),
                    poller.return_value
                )

    def test__poll_task_failed_task(self):
        """Test what happens when an asynchronous task completes and fails.

        Assert that a :class:`nailgun.entity_mixins.TaskFailedError` exception
        is raised.

        """
        get_return = mock.Mock()
        get_return.json.return_value = {
            'state': 'not running',
            'result': 'not success',
            'humanized': {'errors': 'bogus error'},
        }
        with mock.patch.object(client, 'get') as client_get:
            client_get.return_value = get_return
            with self.assertRaises(entity_mixins.TaskFailedError):
                # pylint:disable=protected-access
                entity_mixins._poll_task(gen_integer(), self.server_config)

    def test_read(self):
        """Test :meth:`nailgun.entity_mixins.EntityReadMixin.read`  and
        :meth:`nailgun.entity_mixins.EntityReadMixin.read_json`.

        Assert that ``EntityReadMixin.read_json`` returns the server's
        response, with all JSON decoded.

        Assert that ``EntityReadMixin.read`` returns an object with correctly
        populated attributes.

        """
        # Create a mock server response object.
        mock_response = mock.Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            u'id': self.entity_id,
            u'one_to_one': {'id': 123},
            u'one_to_manys': [{'id': 234}, {'id': 345}],
        }

        # Make `client.get` return the above object.
        with mock.patch.object(client, 'get') as client_get:
            client_get.return_value = mock_response

            # See if EntityReadMixin.read_json behaves correctly.
            self.assertEqual(
                EntityWithRead(
                    self.server_config,
                    id=self.entity_id
                ).read_json(),
                mock_response.json.return_value,
            )

            # See if EntityReadMixin.read behaves correctly.
            entity = EntityWithRead(
                self.server_config,
                id=self.entity_id
            ).read()
            self.assertEqual(entity.id, self.entity_id)
            self.assertIsInstance(entity.one_to_one, SampleEntity)
            self.assertEqual(entity.one_to_one.id, 123)
            self.assertEqual(len(entity.one_to_many), 2)
            for entity_ in entity.one_to_many:
                self.assertIsInstance(entity_, SampleEntity)
                self.assertIn(entity_.id, [234, 345])

    def test_create(self):
        """Test :meth:`nailgun.entity_mixins.EntityCreateMixin.create`.

        Assert that the object returned is a specialized object and that it has
        the attributes returned by
        :meth:`nailgun.entity_mixins.EntityCreateMixin.create_json`.

        """
        arbitrary_integer = gen_integer()
        with mock.patch.object(
            entity_mixins.EntityCreateMixin,
            'create_json'
        ) as create_json:
            create_json.return_value = {
                u'id': self.entity_id,
                u'integer_field': arbitrary_integer,
            }
            entity = EntityWithCreateRead(self.server_config).create()
            self.assertIsInstance(entity, EntityWithCreateRead)
            self.assertEqual(entity.id, self.entity_id)
            self.assertEqual(entity.integer_field, arbitrary_integer)

    def test_create_missing(self):
        """Test :meth:`nailgun.entity_mixins.EntityCreateMixin.create_missing`.

        Assert that ``create_missing`` passes ``self._server_config`` to
        generated entities.

        """

        class FKEntityWithCreateRead(
                entity_mixins.Entity,
                entity_mixins.EntityCreateMixin,
                entity_mixins.EntityReadMixin):
            """An entity that can be created and read and has a FK field."""

            def __init__(self, server_config=None, **kwargs):
                self._fields = {
                    'one_to_many': OneToManyField(SampleEntity, required=True),
                    'one_to_one': OneToOneField(SampleEntity, required=True),
                }
                super(FKEntityWithCreateRead, self).__init__(
                    server_config,
                    **kwargs
                )

        entity = FKEntityWithCreateRead(self.server_config)
        with mock.patch.object(OneToOneField, 'gen_value') as gen_value_1:
            with mock.patch.object(OneToManyField, 'gen_value') as gen_value_2:
                entity.create_missing()
        for mock_gen_value in (gen_value_1, gen_value_2):
            self.assertEqual(
                mock_gen_value.mock_calls,
                [
                    mock.call(),  # gen_value() returns a class. The class is
                    mock.call()(self.server_config),  # instantiated, and
                    mock.call()().create(True),  # create(True) is called.
                ]
            )
