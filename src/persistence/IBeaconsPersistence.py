# -*- coding: utf-8 -*-
"""
    persistence.IBeaconsPersistence
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    IBeaconsPersistence class

    :copyright: Conceptual Vision Consulting LLC 2018-2021, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from typing import Optional

from pip_services3_commons.data import PagingParams, FilterParams, DataPage

from src.data.version1 import BeaconV1


class IBeaconsPersistence:

    def get_page_by_filter(self, correlation_id: Optional[str], filter: FilterParams, paging: PagingParams) -> DataPage:
        raise NotImplementedError('Method from interface definition')

    def get_one_by_id(self, correlation_id: Optional[str], id: str) -> dict:
        raise NotImplementedError('Method from interface definition')

    def get_one_by_udi(self, correlation_id: Optional[str], udi: str) -> dict:
        raise NotImplementedError('Method from interface definition')

    def create(self, correlation_id: Optional[str], entity: BeaconV1) -> dict:
        raise NotImplementedError('Method from interface definition')

    def update(self, correlation_id: Optional[str], entity: BeaconV1) -> dict:
        raise NotImplementedError('Method from interface definition')

    def delete_by_id(self, correlation_id: Optional[str], id: str) -> dict:
        raise NotImplementedError('Method from interface definition')
