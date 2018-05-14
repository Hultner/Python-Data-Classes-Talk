# python-dataclasses-meetup
Notes for my Python Dataclasses presentation

## Dataclasses 
Python 3.6+ for ordered dicts and type annotation support
Native in 3.7
Misuse of NamedTuples
Attrs – why in standard language?


Astuple asdict

Default, 
factories, 
```python
@dataclass
class A:
	d: Optional[str] = None  # Optional value, “nullable”
	d: str  # required 
	d: str = "default"  # Optional with default value
	d: str = lambda: f"Created: {now}"  # factory
```

## Links
https://github.com/ericvsmith/dataclasses  
https://www.python.org/dev/peps/pep-0557/  
https://hackernoon.com/a-brief-tour-of-python-3-7-data-classes-22ee5e046517  
