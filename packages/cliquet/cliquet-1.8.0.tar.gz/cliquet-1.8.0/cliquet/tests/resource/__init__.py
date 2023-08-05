import mock

from cliquet.storage import memory
from cliquet.tests.support import unittest, DummyRequest
from cliquet.resource import BaseResource


class BaseTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(BaseTest, self).__init__(*args, **kwargs)
        self.storage = memory.Memory()

    def setUp(self):
        self.resource = BaseResource(self.get_request())
        self.patch_known_field = mock.patch.object(self.resource,
                                                   'is_known_field')

    def tearDown(self):
        mock.patch.stopall()

    def get_request(self):
        request = DummyRequest()
        request.registry.storage = self.storage
        return request

    @property
    def last_response(self):
        return self.resource.request.response
