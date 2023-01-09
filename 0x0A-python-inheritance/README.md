#	Python Inheritance

## Note
All python scripts have ```#!usr/bin/python3``` as the first line and can be run with shell scripts


```py
#!/usr/bin/python3
class User():
	def __init__(self, first_name=None, last_name=None):
		self.first_name = first_name
		self.last_name = last_name

	def __str__(self):
		return "My name is {} {}".format(self.first_name, self.last_name)

class Person(User):
	def __init__(self):
		super().__init__(self, first_name=None, last_name=None)

person1 = Person("Taiwo", "Peter")
```
