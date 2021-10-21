# -*- coding: utf-8 -*-
"""
    test.TestBeaconFilePersistence
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    TestBeaconFilePersistence class

    :copyright: Conceptual Vision Consulting LLC 2018-2021, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from service_beacons_python.persistence.BeaconsFilePersistence import BeaconsFilePersistence
from .BeaconsPersistenceFixture import BeaconsPersistenceFixture

class TestBeaconFilePersistence():
    @classmethod
    def setup_class(cls):
        cls.persistence = BeaconsFilePersistence("./data/beacons.test.json")
        cls.fixture = BeaconsPersistenceFixture(cls.persistence)

    def setup_method(self, method):
        self.persistence.clear(None)

    def test_crud_operations(self):
        self.fixture.test_crud_operations()

    def test_load_data(self):
        self.persistence.load(None)

    def test_get_with_filter(self):
        self.fixture.test_get_with_filter()
