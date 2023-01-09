#	Python Inheritance
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Ubuntu](htt    ps://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

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
		super().__init__(first_name=None, last_name=None)

person1 = Person("Taiwo", "Peter")
```

## Requirements
- ```#!/usr/bin/python3``` at the top of scripts to run them as executable files
- [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
