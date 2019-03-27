
<p align="center">
  <a href="https://hultner.se/"><img src="https://hultner.se/img/logo/logo_black-01.svg" alt="Hultnér Technologies" align="center" width="200"></a>
</p>
<p align="center">
	<a href="https://hultner.se/" rel="nofollow" class="rich-diff-level-one">Hultnér Technologies AB</a> | <a href="http://alexander.hultner.se" rel="nofollow" class="rich-diff-level-one">Blog</a> | <a href="https://slides.com/hultner/pycon-se-18/fullscreen" rel="nofollow" class="rich-diff-level-one">Slides, PyCon SE 18</a> | <a href="https://www.facebook.com/groups/nordiskpython/" rel="nofollow" class="rich-diff-level-one">Nordisk Python Community</a> | <a href="https://twitter.com/ahultner" rel="nofollow" class="rich-diff-level-one">@ahultner</a>
	<hr>
</p>

# ♜ Python Data Classes 
*Data Classes, in Python 3.6 and beyond.*

## PyCon Sweden, December 12, 2018 (Stockholm)
[**Data Classes, in Python 3.6 and beyond** (youtube video)](http://youtube.com/watch?v=nwjWOaxWMes)  
Python 3.7 is here and the @dataclass-decorator is a major new feature 
simplifying class-creation. In this talk, we will learn to use the power of 
data classes to make our codebases cleaner and leaner in a pythonic way.

We will also learn how to use the backport in Python 3.6 codebases before 
upgrading.

- [Video Recording](http://youtube.com/watch?v=nwjWOaxWMes)
- [Slides](https://slides.com/hultner/pycon-se-18/fullscreen)
- [Jupyter Lab Notebook](PyCon-Sweden-2018/demo.ipynb)

## GothPy, May 17, 2018
**By Alexander Hultnér** at GothPy 17th of May 2018.  
A talk about *data classes* and how you can use them today.
The code we experimented with in the demo is available in [demo.py](./demo.py).

- [Slides](http://slides.com/hultner/python-dataclasses-gothpy-alexander-hultner/fullscreen)
- [Meetup Event](https://www.meetup.com/GothPy/events/249499024/)

## ♜ Dataclasses FAQ
**What's the requirements for using data classes?**   
Python 3.6+ (ordered dicts, type annotations) via `pip install dataclasses`   

**When can I use data classes without installing the package?**  
Dataclasses are native in 3.7  

**What similar patterns are used in older Python versions?**  
[Attrs](http://www.attrs.org/en/stable/) was a large inspiration for data classes  
NamedTuples, based on tuples, regretted design choices have been improved in dataclasses. 
Got a Dataclasses-style syntax recently.  
ORMs, SQLAlchemy, Djangon ORM, PeeWee, etc.

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
- [Dataclasses, Python Docs](https://docs.python.org/3/library/dataclasses.html)
