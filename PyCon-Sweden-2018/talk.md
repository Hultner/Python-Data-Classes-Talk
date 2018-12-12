## Title
Data Classes, in Python 3.6 and beyond

## Conference
Pycon Sweden, December 12, 2018 (10:45-11:20), Stockholm

## Talk Format
Presentation, 35 minutes

## Description
Python 3.7 is here and the @dataclass-decorator is a major new feature 
simplifying class-creation. In this talk, we will learn to use the power of 
data classes to make our codebases cleaner and leaner in a pythonic way.

We will also learn how to use the backport in Python 3.6 codebases before 
upgrading.

## Audience Level
Intermediate, intended to be interesting for all audiences.

## Outline
 - Intoruction and outline (3 minutes, 3 total)
   - Quick introduction of myself and Cetrez
   - Outline of the talk
   - Why
 - Why
 - Data Classes in two minutes (2 minutes, 5 total)
   - Base on slide from previous talk
 - History (2 minutes, 7 total)
   - Named Tuple
   - Attrs
   - ORM-libraries
 - Usage (3 minutes, 10 total)
   - `pip install dataclasses` in Python 3.6
   - `from dataclasses import dataclasses`
   - `@dataclass` decorator
   - Small example
 - Example (2 minutes, 12 total)
   - Bigger example
   - `__post_init__()`
   - `field()`, `default_factory`
 - Utility functions (2 minutes, 14 total)
   - `asdict`
   - `astuple`
   - etc...
 - JSON Conversion (2 minutes, 16 total)
   - asdict & json.dumps
   - (show JSONEncoder in demo)
 - ...
 - Demo/Interactive Session (14 minutes, 30 total)
   - Use JupyterLab/notebook
 - Final thoughs (2 minutes, 32 total)
 - Questions (3 minutes, 35 total)
   - Links
   - Bio

## Additional notes
[Slides PyCon SE 2018](https://slides.com/hultner/pycon-se-18/)

### GothPy
I had a similar but slightly shorter talk at GothPy (the Gothenburg Python user
group). 
 - [Event](https://www.meetup.com/GothPy/events/249499024/)
 - [Slides](https://slides.com/hultner/python-dataclasses-gothpy-alexander-hultner#/)

## Bio
...

