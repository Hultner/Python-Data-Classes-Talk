
<p align="center">
  <a href="http://cetrez.com/"><img src="./res/cetrez.svg" alt="Hack the Castle" align="center" width="400"></a>
</p>
<p align="center">
	<a href="http://cetrez.com/" rel="nofollow" class="rich-diff-level-one">Cetrez</a> | <a href="http://blog.cetrez.com/" rel="nofollow" class="rich-diff-level-one">Blog</a> | <a href="http://slides.com/hultner/python-dataclasses-gothpy-alexander-hultner/fullscreen" rel="nofollow" class="rich-diff-level-one">Presentation slides</a> | <a href="https://www.facebook.com/groups/nordiskpython/" rel="nofollow" class="rich-diff-level-one">Nordisk Python Community</a> | <a href="https://www.meetup.com/GothPy/events/249499024/" rel="nofollow" class="rich-diff-level-one">Meetup event</a> | <a href="https://twitter.com/ahultner" rel="nofollow" class="rich-diff-level-one">@ahultner</a>
	<hr>
</p>

# ♜ Python Data Classes 
*Data Classes, in Python 3.6 and beyond…*

## PyCon Sweden, December 12, 2018 (Stockholm)
**Data Classes, in Python 3.6 and beyond**  
Python 3.7 is here and the @dataclass-decorator is a major new feature 
simplifying class-creation. In this talk, we will learn to use the power of 
data classes to make our codebases cleaner and leaner in a pythonic way.

We will also learn how to use the backport in Python 3.6 codebases before 
upgrading.

…

## GothPy, May 17, 2018
**By Alexander Hultnér** at GothPy 17th of May 2018.  
A talk about *data classes* and how you can use them today.
The code we experimented with in the demo is available in [demo.py](./demo.py).

## ♜ Dataclasses FAQ
**What's the requirements for using data classes?**   
Python 3.6+ (ordered dicts, type annotations) via `pip install dataclasses`   

**When can I use data classes without installing the package?**  
Dataclasses are native in 3.7  

**What similar patterns are used in older Python versions?**  
[Attrs](http://www.attrs.org/en/stable/) was a large inspiration for data classes  
The misuse of NamedTuples (wouldn't recommend)   

## ♜ Quick Reference
```python
@dataclass
class A:
	# Required, need to be first; just like in function signatures
	a: str
	
	# Optional value, “nullable”
	b: Optional[str] = None
	
	# Optional with default value
	c: str = "default"
	
	# Executed at startup
	d: str = str(datetime.now())
	
	# Executed when creating class instance
	e: str = field(default_factory=lambda: f"Created: {datetime.now()}") 
	
>>> A("Required value")
A(a='Required value', b=None, c='default', d='2018-05-24 20:39:19.930841', e='Created: 2018-05-24 20:40:05.762934')


```

## ♜ Links
- [GitHub – PEP draft & backport](https://github.com/ericvsmith/dataclasses)
- [Python.org PEP 557](https://www.python.org/dev/peps/pep-0557/)
- [A breif tour of Python 3.7 dataclasses](https://hackernoon.com/a-brief-tour-of-python-3-7-data-classes-22ee5e046517)
- [Raymond Hettinger - Dataclasses: The code generator to end all code generators - PyCon 2018](https://www.youtube.com/watch?v=T-TwcmT6Rcw)
- [The Ultimate Guide to Data Classes in Python 3.7](https://realpython.com/python-data-classes/)
