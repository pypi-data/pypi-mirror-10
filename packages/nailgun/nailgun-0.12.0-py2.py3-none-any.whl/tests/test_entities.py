"""Tests for :mod:`nailgun.entities`."""
from ddt import data, ddt, unpack
from fauxfactory import gen_integer
from nailgun import client, config, entities
from nailgun.entity_mixins import NoSuchPathError
from sys import version_info
from unittest import TestCase
import mock
# pylint:disable=too-many-public-methods


@ddt
class PathTestCase(TestCase):
    """Tests for extensions of :meth:`nailgun.entity_mixins.Entity.path`."""
    longMessage = True

    def setUp(self):  # pylint:disable=invalid-name
        """Set ``self.server_config`` and ``self.id_``."""
        self.server_config = config.ServerConfig('http://example.com')
        self.id_ = gen_integer(min_value=1)
        if version_info.major == 2:
            self.re_assertion = self.assertRegexpMatches
        else:
            self.re_assertion = self.assertRegex  # pylint:disable=no-member

    @data(
        (entities.AbstractDockerContainer, '/containers'),
        (entities.ActivationKey, '/activation_keys'),
        (entities.ConfigTemplate, '/config_templates'),
        (entities.ContentView, '/content_views'),
        (entities.ContentViewVersion, '/content_view_versions'),
        (entities.ForemanTask, '/tasks'),
        (entities.Organization, '/organizations'),
        (entities.Product, '/products'),
        (entities.Repository, '/repositories'),
        (entities.SmartProxy, '/smart_proxies'),
        (entities.System, '/systems'),
    )
    @unpack
    def test_path_without_which(self, entity, path):
        """Test what happens when the ``which`` argument is omitted.

        Assert that ``path`` returns a valid string when the ``which`` argument
        is omitted, regardless of whether an entity ID is provided.

        """
        # There is no API path for all foreman tasks.
        if entity != entities.ForemanTask:
            self.assertIn(path, entity(self.server_config).path(), entity)
        self.assertIn(
            '{0}/{1}'.format(path, self.id_),
            entity(self.server_config, id=self.id_).path(),
            entity
        )

    @data(
        (entities.AbstractDockerContainer, 'containers', 'logs'),
        (entities.AbstractDockerContainer, 'containers', 'power'),
        (entities.ActivationKey, '/activation_keys', 'add_subscriptions'),
        (entities.ActivationKey, '/activation_keys', 'content_override'),
        (entities.ActivationKey, '/activation_keys', 'releases'),
        (entities.ActivationKey, '/activation_keys', 'remove_subscriptions'),
        (entities.ContentView, '/content_views', 'available_puppet_module_names'),  # noqa pylint:disable=C0301
        (entities.ContentView, '/content_views', 'content_view_puppet_modules'),  # noqa pylint:disable=C0301
        (entities.ContentView, '/content_views', 'content_view_versions'),
        (entities.ContentView, '/content_views', 'copy'),
        (entities.ContentView, '/content_views', 'publish'),
        (entities.ContentViewVersion, '/content_view_versions', 'promote'),
        (entities.Organization, '/organizations', 'products'),
        (entities.Organization, '/organizations', 'subscriptions'),
        (entities.Organization, '/organizations', 'subscriptions/delete_manifest'),  # noqa pylint:disable=C0301
        (entities.Organization, '/organizations', 'subscriptions/refresh_manifest'),  # noqa pylint:disable=C0301
        (entities.Organization, '/organizations', 'subscriptions/upload'),
        (entities.Organization, '/organizations', 'sync_plans'),
        (entities.Product, '/products', 'repository_sets'),
        (entities.Product, '/products', 'repository_sets/2396/disable'),
        (entities.Product, '/products', 'repository_sets/2396/enable'),
        (entities.Repository, '/repositories', 'sync'),
        (entities.Repository, '/repositories', 'upload_content'),
    )
    @unpack
    def test_self_path_with_which(self, entity, path, which):
        """Test what happens when an entity ID is given and ``which=which``.

        Assert that when ``entity(id=<id>).path(which=which)`` is called, the
        resultant path contains the following string::

            'path/<id>/which'

        """
        gen_path = entity(self.server_config, id=self.id_).path(which=which)
        self.assertIn(
            '{0}/{1}/{2}'.format(path, self.id_, which),
            gen_path,
            entity.__name__
        )
        self.re_assertion(gen_path, '{0}$'.format(which), entity.__name__)

    @data(
        (entities.ConfigTemplate, '/config_templates', 'build_pxe_default'),
        (entities.ConfigTemplate, '/config_templates', 'revision'),
    )
    @unpack
    def test_base_path_with_which(self, entity, path, which):
        """Test what happens when no entity ID is given and ``which=which``.

        Assert that a path in the fllowing format is returned::

            {path}/{which}

        """
        gen_path = entity(self.server_config).path(which=which)
        self.assertIn('{0}/{1}'.format(path, which), gen_path, entity.__name__)
        self.re_assertion(gen_path, which + '$', entity.__name__)

    @data(
        (entities.ActivationKey, 'releases'),
        (entities.ContentView, 'available_puppet_module_names'),
        (entities.ContentView, 'content_view_puppet_modules'),
        (entities.ContentView, 'content_view_versions'),
        (entities.ContentView, 'publish'),
        (entities.ContentViewVersion, 'promote'),
        (entities.ForemanTask, 'self'),
        (entities.Organization, 'products'),
        (entities.Organization, 'self'),
        (entities.Organization, 'subscriptions'),
        (entities.Organization, 'subscriptions/delete_manifest'),
        (entities.Organization, 'subscriptions/refresh_manifest'),
        (entities.Organization, 'subscriptions/upload'),
        (entities.Organization, 'sync_plans'),
        (entities.Product, 'repository_sets'),
        (entities.Repository, 'sync'),
        (entities.Repository, 'upload_content'),
        (entities.SmartProxy, 'refresh'),
        (entities.System, 'self'),
    )
    @unpack
    def test_no_such_path(self, entity, path):
        """Test what happens when no entity ID is provided and ``which=path``.

        Assert that :class:`nailgun.entity_mixins.NoSuchPathError` is raised.

        """
        with self.assertRaises(NoSuchPathError):
            entity(self.server_config).path(which=path)

    def test_foremantask_path(self):
        """Test :meth:`nailgun.entities.ForemanTask.path`.

        Assert that correct paths are returned when:

        * an entity ID is provided and the ``which`` argument to ``path`` is
          omitted
        * ``which = 'bulk_search'``

        """
        self.assertIn(
            '/foreman_tasks/api/tasks/{0}'.format(self.id_),
            entities.ForemanTask(self.server_config, id=self.id_).path()
        )
        for gen_path in (
                entities.ForemanTask(self.server_config).path(
                    which='bulk_search'
                ),
                entities.ForemanTask(self.server_config, id=self.id_).path(
                    which='bulk_search'
                )
        ):
            self.assertIn('/foreman_tasks/api/tasks/bulk_search', gen_path)

    def test_syncplan_path(self):
        """Test :meth:`nailgun.entities.SyncPlan.path`.

        Assert that the correct paths are returned when the following paths are
        provided to :meth:`nailgun.entities.SyncPlan.path`:

        * ``add_products``
        * ``remove_products``

        """
        for which in ('add_products', 'remove_products'):
            path = entities.SyncPlan(
                self.server_config,
                id=2,
                organization=1,
            ).path(which)
            self.assertIn(
                'organizations/1/sync_plans/2/{0}'.format(which),
                path
            )
            self.re_assertion(path, '{0}$'.format(which))

    def test_system_path(self):
        """Test :meth:`nailgun.entities.System.path`.

        Assert that correct paths are returned when:

        * A UUID is provided and ``which`` is omitted.
        * A UUID is provided and ``which='self'``.
        * A UUID is omitted and ``which`` is omitted.
        * A UUID is omitted and ``which='base'``.

        """
        for gen_path in (
                entities.System(self.server_config, uuid=self.id_).path(),
                entities.System(self.server_config, uuid=self.id_).path(
                    which='self'
                )
        ):
            self.assertIn('/systems/{0}'.format(self.id_), gen_path)
            self.re_assertion(gen_path, '{0}$'.format(self.id_))
        for gen_path in (
                entities.System(self.server_config).path(),
                entities.System(self.server_config).path(which='base')):
            self.assertIn('/systems', gen_path)
            self.re_assertion(gen_path, 'systems$')


@ddt
class CreatePayloadTestCase(TestCase):
    """Tests for extensions of ``create_payload``.

    Several classes extend the ``create_payload`` method and make it do things
    like rename attributes or wrap the submitted dict of data in a second hash.
    It is possible to mess this up in a variety of ways. For example, an
    extended method could could try to rename an attribute that does not exist.
    This class attempts to find such issues by creating an entity, calling
    :meth:`nailgun.entity_mixins.EntityCreateMixin.create_payload` and
    asserting that a ``dict`` is returned.

    """

    @classmethod
    def setUpClass(cls):  # pylint:disable=invalid-name
        """Set ``cls.server_config``."""
        cls.server_config = config.ServerConfig('http://example.com')

    @data(
        entities.Architecture,
        entities.ConfigTemplate,
        entities.AbstractDockerContainer,
        entities.Domain,
        entities.HostCollection,
        entities.Host,
        entities.LifecycleEnvironment,
        entities.Location,
        entities.Media,
        entities.OperatingSystem,
        entities.Subnet,
        entities.UserGroup,
        entities.User,
    )
    def test_no_attributes(self, entity):
        """Create an entity with no attributes."""
        self.assertIsInstance(
            entity(self.server_config).create_payload(),
            dict
        )

    def test_sync_plan(self):
        """Create a :class:`nailgun.entities.SyncPlan`."""
        self.assertIsInstance(
            entities.SyncPlan(
                self.server_config,
                organization=1,
            ).create_payload(),
            dict
        )

    def test_content_view_puppet_module(self):
        """Create a :class:`nailgun.entities.ContentViewPuppetModule`."""
        self.assertIsInstance(
            entities.ContentViewPuppetModule(
                self.server_config,
                content_view=1,
            ).create_payload(),
            dict
        )


@ddt
class OrganizationTestCase(TestCase):
    """Tests for :class:`nailgun.entities.Organization`."""

    def setUp(self):  # pylint:disable=invalid-name
        """Set ``self.server_config`` and ``self.entity_id``."""
        self.server_config = config.ServerConfig(
            'http://example.com',
            auth=('foo', 'bar'),
            verify=False
        )
        self.entity_id = gen_integer(min_value=1)

    @data(200, 202)
    def test_delete_manifest(self, http_status_code):
        """Call :meth:`nailgun.entities.Organization.delete_manifest`.

        Assert that :meth:`nailgun.entities.Organization.delete_manifest`
        returns a dictionary when an HTTP 202 or some other success status code
        is returned.

        """
        # `client.post` will return this.
        post_return = mock.Mock()
        post_return.status_code = http_status_code
        post_return.raise_for_status.return_value = None
        post_return.json.return_value = {'id': gen_integer()}  # mock task ID

        # Start by patching `client.post` and `ForemanTask.poll`...
        # NOTE: Python 3 allows for better nested context managers.
        with mock.patch.object(client, 'post') as client_post:
            client_post.return_value = post_return
            with mock.patch.object(entities.ForemanTask, 'poll') as ft_poll:
                ft_poll.return_value = {}

                # ... then see if `delete_manifest` acts correctly.
                for synchronous in (True, False):
                    reply = entities.Organization(
                        self.server_config,
                        id=self.entity_id
                    ).delete_manifest(synchronous)
                    self.assertIsInstance(reply, dict)

    def test_subscriptions(self):
        """Call :meth:`nailgun.entities.Organization.subscriptions`.

        Asserts that :meth:`nailgun.entities.Organization.subscriptions`
        returns a list.

        """
        # Create a mock server response object.
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {u'results': []}

        with mock.patch.object(client, 'get') as mocked_client_get:
            mocked_client_get.return_value = mock_response
            # See if `subscriptions` behaves correctly.
            response = entities.Organization(
                self.server_config,
                id=self.entity_id,
            ).subscriptions()
            self.assertEqual(response, [])
