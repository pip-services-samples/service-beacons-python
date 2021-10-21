# -*- coding: utf-8 -*-
"""
    data.version1.BeaconV1Schema
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    BeaconV1Schema class

    :copyright: Conceptual Vision Consulting LLC 2018-2021, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services3_commons.convert.TypeCode import TypeCode
from pip_services3_commons.validate.ObjectSchema import ObjectSchema


class BeaconV1Schema(ObjectSchema):
    def __init__(self):
        super().__init__()

        self.with_optional_property("id", TypeCode.String)
        self.with_required_property("site_id", TypeCode.String)
        self.with_optional_property("type", TypeCode.String)
        self.with_required_property("udi", TypeCode.String)
        self.with_optional_property("label", TypeCode.String)
        self.with_optional_property("center", TypeCode.Map)
        self.with_optional_property("radius", TypeCode.Float)
