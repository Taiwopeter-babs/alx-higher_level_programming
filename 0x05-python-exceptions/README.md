#	Python Exceptions

## Note
All python scripts have ```#!usr/bin/python3``` as the first line and can be run with shell scripts

## Exceptions
- try clause
- except clause
- else and;
- finally

```py
#!/usr/bin/python3

try:
    # execute statement(s)
except (Exception(s)):
	# do stuff about exception
    raise # useful when exceptions are to be re-raised 
else:
    # executes when there is no exception
finally:
    # excecutes regardless
```
## Notes on else statements
I observed that some else statements in try/except except blocks are unnecessary. For example
```py
def print_integer(val):

	try:
	    print("{:d}".format(value))
	except (TypeError, ValueError):
	    return (False)
	else:		# Unecessary else statement
            return (True)
```
Instead, the boolean value should just be returned after the code in the ```try``` block sucessfully executes
like this
```py
	try:
	    print("{:d}".format(value))
	except (TypeError, ValueError):
	    return (False)

	return (True) # returns if no exception is caught.
```
