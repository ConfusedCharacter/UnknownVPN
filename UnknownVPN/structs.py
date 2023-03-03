from typing import NamedTuple

class AccountDetails(NamedTuple):
    balance         : float
    services_count  : int
    userid          : int
    username        : str

class GetServiceLicense(NamedTuple):
    license         : str
    service_id      : str


class ChangeLicense(NamedTuple):
    license         : str
    service_id      : str

class BuyService(NamedTuple):
    license         : str
    service_id      : str

class GetInfo(NamedTuple):
    createdTime     : str
    enabled         : bool
    expired         : bool
    expiryTime      : float
    free            : bool
    id              : str
    license         : str
    name            : str
    plan            : str
    price           : int
    protocol        : str
    remain_size     : float
    server_id       : str
    server_name     : str
    size            : float
    subscription_id : str
    type            : str
    used_size       : float
    users_count     : int
    banned          : bool

class GetLinks(NamedTuple):
    direct          : str
    nimbaha         : str

