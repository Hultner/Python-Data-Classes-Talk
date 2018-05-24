
<p align="center">
  <a href="http://cetrez.com/"><img src="./res/cetrez.svg" alt="Hack the Castle" align="center" width="400"></a>
</p>
<p align="center">
	<a href="http://cetrez.com/" rel="nofollow" class="rich-diff-level-one">Cetrez</a> | <a href="http://blog.cetrez.com/" rel="nofollow" class="rich-diff-level-one">Blog</a> | <a href="http://slides.com/hultner/python-dataclasses-gothpy-alexander-hultner/fullscreen" rel="nofollow" class="rich-diff-level-one">Presentation slides</a> | <a href="https://www.facebook.com/groups/nordiskpython/" rel="nofollow" class="rich-diff-level-one">Nordisk Python Community</a> | <a href="https://www.meetup.com/GothPy/events/249499024/" rel="nofollow" class="rich-diff-level-one">Meetup event</a> | <a href="https://twitter.com/ahultner" rel="nofollow" class="rich-diff-level-one">@ahultner</a>
	<hr>
</p>

# ♜ Python Dataclasses 
**By Alexander Hultnér** at GothPy 17th of May 2018.


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
