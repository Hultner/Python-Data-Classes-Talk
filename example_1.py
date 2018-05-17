import collections
from datetime import date
from typing import List, Optional
from dataclasses import dataclass, field, asdict, astuple
import jsondate as json

@dataclass
class Host:
    name: str  # Required field
    nickname: Optional[str] = None  # Not required


@dataclass
class Event:
    title: str  # Required field

    # Mutable objects requires a factory, otherwise they'll share state just
    # like conventional Python classes. A suggestion to change this was rejected.
    hosts: List[Host] = field(default_factory=list)
    day: date = date.today()

    # Executes after init, good for *validation* and *post processing*
    def __post_init__(self):

        # Transform host dict/mappings to instances of host class
        self.hosts = [Host(**hoster) for hoster in self.hosts]


# Named tuple approach
EventHacky = collections.namedtuple("EventBad", ["title", "hosts", "day"])


class EventConventionalVerbose:

    def __init__(self, title: str, hosts: Host = None, day: date = None):
        self.title = title
        # Can't set mutable objects as default argument
        if hosts is None:
            self.hosts = []
        else:
            self.hosts = [Host(**hoster) for hoster in hosts]
        if day is None:
            self.day = date.today()
        else:
            self.day = day

    def __repr__(self):
        return f"EventConventionalVerbose(title={self.title!r}, hosts={self.hosts!r}, day={self.day!r})"

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.title, self.hosts, self.day) == (
                other.title, other.hosts, other.day
            )
        return NotImplemented

    def __ne__(self, other):
        if other.__class__ is self.__class__:
            return (self.title, self.hosts, self.day) != (
                other.title, other.hosts, other.day
            )
        return NotImplemented

    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return (self.title, self.hosts, self.day) < (
                other.title, other.hosts, other.day
            )
        return NotImplemented

    def __le__(self, other):
        if other.__class__ is self.__class__:
            return (self.title, self.hosts, self.day) <= (
                other.title, other.hosts, other.day
            )
        return NotImplemented

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return (self.title, self.hosts, self.day) > (
                other.title, other.hosts, other.day
            )
        return NotImplemented

    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return (self.title, self.hosts, self.day) >= (
                other.title, other.hosts, other.day
            )
        return NotImplemented

def json_dataclass(data):
    return json.dumps(asdict(data))

host_collection = [
    {"name": "Alexander Hultnér", "nickname": "Hultnér"}, {"name": "Emily Bache"}
]
