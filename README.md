
<p align="center">
  <a href="http://cetrez.com/"><img src="./res/cetrez.svg" alt="Hack the Castle" align="center" width="400"></a>
</p>
<p align="center">
	<a href="http://cetrez.com/" rel="nofollow" class="rich-diff-level-one">Cetrez</a> | <a href="http://blog.cetrez.com/" rel="nofollow" class="rich-diff-level-one">Blog</a> | <a href="http://slides.com/hultner/python-dataclasses-gothpy-alexander-hultner/fullscreen" rel="nofollow" class="rich-diff-level-one">Presentation slides</a> | <a href="https://www.facebook.com/groups/nordiskpython/" rel="nofollow" class="rich-diff-level-one">Nordisk Python Community</a> | <a href="https://www.meetup.com/GothPy/events/249499024/" rel="nofollow" class="rich-diff-level-one">Meetup event</a> | <a href="https://twitter.com/ahultner" rel="nofollow" class="rich-diff-level-one">@ahultner</a>
	<hr>
</p>

# ♜ Python Dataclasses 
**By Alexander Hultnér** at GothPy 17th of May 2018.


## Dataclasses FAQ
**What's the requirements for using dataclasses?**   
Python 3.6+ (ordered dicts, type annotations) via `pip install dataclasses`   

**When can I use dataclasses without installing the package?**  
Dataclasses are native in 3.7  

**What similar patterns are used in older Python versions?**  
[Attrs](http://www.attrs.org/en/stable/) was a large insperation for dataclasses  
The misuse of NamedTuples (wouldn't recommend)   

## Quick Reference
```python
@dataclass
class A:
	a: str  # required, need to be first
	b: Optional[str] = None  # Optional value, “nullable”
	c: str = "default"  # Optional with default value
	d: str = datetime.now()  # Run at startup
	e: str = field(default_factory=lambda: f"Created: {datetime.now()}")  # Run at init
	
>>> A("Required value")
A(a='Required value', b=None, c='default', d=datetime.datetime(2018, 5, 24, 17, 50, 46, 555014), e='Created: 2018-05-24 17:51:07.782374')

```

## Links
- [GitHub – PEP draft & backport](https://github.com/ericvsmith/dataclasses)
- [Python.org PEP 557](https://www.python.org/dev/peps/pep-0557/)
- [A breif tour of Python 3.7 dataclasses](https://hackernoon.com/a-brief-tour-of-python-3-7-data-classes-22ee5e046517)
- [Raymond Hettinger - Dataclasses: The code generator to end all code generators - PyCon 2018](https://www.youtube.com/watch?v=T-TwcmT6Rcw)
- [The Ultimate Guide to Data Classes in Python 3.7](https://realpython.com/python-data-classes/)
