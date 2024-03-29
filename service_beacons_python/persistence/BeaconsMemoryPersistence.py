# -*- coding: utf-8 -*-
"""
    persistence.BeaconsMemoryPersistence
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    BeaconsMemoryPersistence class

    :copyright: Conceptual Vision Consulting LLC 2018-2021, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from typing import Optional, Any, Callable

from pip_services3_commons.data import FilterParams, DataPage, PagingParams
from pip_services3_data.persistence import IdentifiableMemoryPersistence

from .IBeaconsPersistence import IBeaconsPersistence
from ..data.version1 import BeaconV1


class BeaconsMemoryPersistence(IdentifiableMemoryPersistence, IBeaconsPersistence):

    def __init__(self):
        super(BeaconsMemoryPersistence, self).__init__()
        self._max_page_size = 1000

    def __compose_filter(self, filter: FilterParams) -> Callable:
        filter = filter if filter is not None else FilterParams()

        id = filter.get_as_nullable_string("id")
        site_id = filter.get_as_nullable_string("site_id")
        label = filter.get_as_nullable_string("label")
        udi = filter.get_as_nullable_string("udi")
        udis = filter.get_as_object("udis")
        if udis is not None and len(udis) > 0:
            udis = udis.split(",")

        def filter_beacons(item):
            if id is not None and item.id != id:
                return False
            if site_id is not None and item.site_id != site_id:
                return False
            if label is not None and item.label != label:
                return False
            if udi is not None and item.udi != udi:
                return False
            if udis is not None and item.udi not in udis:
                return False
            return True

        return filter_beacons

    def get_page_by_filter(self, correlation_id: Optional[str], filter: FilterParams, paging: PagingParams,
                           sort: Any = None, select: Any = None) -> DataPage:

        return super(BeaconsMemoryPersistence, self).get_page_by_filter(correlation_id,
                                                                        self.__compose_filter(filter), paging=paging)

    def get_one_by_udi(self, correlation_id: Optional[str], udi: str) -> Optional[BeaconV1]:
        if udi is None:
            return None
        for item in self._items:
            if udi == item.udi:
                return item
