# CusTERM

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

CusTERM is a Python library for making your own bootleg command line!

## Installing

`pip install custerm`

## Usage

```python
# import the package
import custerm as ct

# define the functions
def command1():
	ct.log("Ran a command!")

# you can accept parameters
def command2(inp):
	ct.log("You wrote: "+inp)

# you can log as errors and warnings
def command3():
	# errors take an error type and a message
	ct.error("FakeError","This is an error!")
	# warnings take a message
	ct.warning("This is a warning!")

# you can make assertions that use ct errors
def command4():
	ct.assertion(0==0,"This is an assertion!")
	ct.assertion(0==0,"This is an assertion that raises a real error too!",hard=True)

# register the commands
ct.regcmd("cmd1",command1)
ct.regcmd("cmd2",command2)
ct.regcmd("cmd3",command3)
ct.regcmd("cmd4",command4)

# initialise the interface
ct.show()
ct.fetchroot().mainloop()
```
