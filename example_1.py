from dataclasses import dataclass, asdict, astuple
import collections


@dataclass
class Event:
    pass


# Named tuple approach
EventBad = collections.namedtuple("EventBad", [])


class EventVerbose:
    pass
