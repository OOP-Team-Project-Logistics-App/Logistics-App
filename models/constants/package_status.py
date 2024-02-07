from enum import Enum


class PackageStatus(Enum):
    NOT_ASSIGNED = "Not assigned"
    EN_ROUTE = "En route"
    DELIVERED = "Delivered"