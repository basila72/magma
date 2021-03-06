#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from functools import partial
from typing import Any, Callable, List, Mapping, Optional

from dataclasses_json import dataclass_json
from marshmallow import fields as marshmallow_fields

from .datetime_utils import fromisoformat


DATETIME_FIELD = field(
    metadata={
        "dataclasses_json": {
            "encoder": datetime.isoformat,
            "decoder": fromisoformat,
            "mm_field": marshmallow_fields.DateTime(format="iso"),
        }
    }
)


@dataclass_json
@dataclass
class AddServiceLinkMutation:
    __QUERY__ = """
    mutation AddServiceLinkMutation($id: ID!, $linkId: ID!) {
  addServiceLink(id: $id, linkId: $linkId) {
    id
    name
    externalId
    customer {
      id
      name
      externalId
    }
    terminationPoints {
      id
      name
    }
    links {
      id
    }
  }
}

    """

    @dataclass_json
    @dataclass
    class AddServiceLinkMutationData:
        @dataclass_json
        @dataclass
        class Service:
            @dataclass_json
            @dataclass
            class Customer:
                id: str
                name: str
                externalId: Optional[str] = None

            @dataclass_json
            @dataclass
            class Equipment:
                id: str
                name: str

            @dataclass_json
            @dataclass
            class Link:
                id: str

            id: str
            name: str
            terminationPoints: List[Equipment]
            links: List[Link]
            externalId: Optional[str] = None
            customer: Optional[Customer] = None

        addServiceLink: Optional[Service] = None

    data: Optional[AddServiceLinkMutationData] = None
    errors: Any = None

    @classmethod
    # fmt: off
    def execute(cls, client, id: str, linkId: str):
        # fmt: off
        variables = {"id": id, "linkId": linkId}
        response_text = client.call(cls.__QUERY__, variables=variables)
        return cls.from_json(response_text).data
