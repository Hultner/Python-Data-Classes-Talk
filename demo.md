# Demo 
I forgot to save some of the interpeter output from the demo, this is what
I managed to salvage.  
However the code we used are available in [demo.py](./demo.py).

```python
bpython version 0.17.1 on top of Python 3.6.5 /Users/hultner/.local/share/virtualenvs/python-dataclasses-meetup-qfN_94ua/bin/python3.6
>>> from example_1 import *
>>> our_event = Event("Dataclasses")
>>> our_event
Event(title='Dataclasses', hosts=[], day=datetime.date(2018, 5, 17))
>>> our_event = Event("Dataclasses", host_collection, date(2018,5,18))
>>> our_event
Event(title='Dataclasses', hosts=[Host(name='Alexander Hultnér', nickname='Hultnér'), Host(name='Emily Bache', nickname=None)], day=datetime.date(2018, 5, 18))
>>> json_dataclass(our_event)
'{"title": "Dataclasses", "hosts": [{"name": "Alexander Hultn\\u00e9r", "nickname": "Hultn\\u00e9r"}, {"name": "Emily Bache", "nickname": null}], "day": "2018-05-18"}'
>>> EventHacky("Dataclasses", [Host(**host) for host in host_collection], date(2018, 5, 17))
EventBad(title='Dataclasses', hosts=[Host(name='Alexander Hultnér', nickname='Hultnér'), Host(name='Emily Bache', nickname=None)], day=datetime.date(2018, 5,17))
>>> EventConventionalVerbose("Dataclasses")
EventConventionalVerbose(title='Dataclasses', hosts=[], day=datetime.date(2018, 5, 17))
>>> EventConventionalVerbose("Dataclasses")
EventConventionalVerbose(title='Dataclasses', hosts=[], day=datetime.date(2018, 5, 17))
>>> EventConventionalVerbose("Dataclasses", host_collection)
EventConventionalVerbose(title='Dataclasses', hosts=[Host(name='Alexander Hultnér', nickname='Hultnér'), Host(name='Emily Bache', nickname=None)], day=datetime.date(2018, 5, 17))
>>> EventConventionalVerbose("Dataclasses", host_collection, date(2018,5, 18))
EventConventionalVerbose(title='Dataclasses', hosts=[Host(name='Alexander Hultnér', nickname='Hultnér'), Host(name='Emily Bache', nickname=None)], day=datetime.date(2018, 5, 18))
>>> host_collection
[{'name': 'Alexander Hultnér', 'nickname': 'Hultnér'}, {'name': 'Emily Bache'}]
>>>
```
