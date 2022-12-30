#	Test Driven Development (doctest and unittests)
Test driven development is an important aspect of software engineering. I think of it as _virtual user use cases_. Now, we test softwares or code written to acertain that under realistic circumstances, the software will hold or still run. It means that as a software is written, the user is brought into perspective. You are writing the code as if the user is right in front of you using the software.

Imagine that you built an application to add only integers and floating-point numbers. I, as a user decide to input my name as a value. This isn't supposed to be a problem if there is a kind of error message displayed to me ```ONLY NUMBERS ALLOWED```. Now, that is an edge case, and you, who wrote the software have probably saved your company a lot of money; given that your application did not crash. The above is an example of the importance of  tests.

During testing of software, you will assume non-ideal or edge cases for the code, and write exceptions or handle errors to manage them.

This repository covers only unittests and doctests (interactive tests).

# Requirements
- ```#!/usr/bin/python3``` at the top of scripts to run them as executable files
- doctest  and unittest modules


## Example:
```
taiwop@Taiwo-avantgarde$ cat example_ezrapound.txt | tail -20
>>> text = "And New York is the most beautiful city in the world? \
... It is not far from it. No urban night is like the night there. \
... .. Squares after squares of flame, set up and cut into the aether. Here is our poetry: \
... For we have pulled down the stars to our will."
>>> text_indentation(text) #doctest: +REPORT_NDIFF, +NORMALIZE_WHITESPACE
And New York is the most beautiful city in the world?
<BLANKLINE>
It is not far from it.
<BLANKLINE>
No urban night is like the night there.
<BLANKLINE>
.
<BLANKLINE>
.
<BLANKLINE>
Squares after squares of flame, set up and cut into the aether.
<BLANKLINE>
Here is our poetry:
<BLANKLINE>
For we have pulled down the stars to our will.
<BLANKLINE>
taiwop@Taiwo-avantgarde$ python3 -m doctest -v tests/example_ezrapound.txt | tail -2
12 passed and 0 failed.
Test passed.
```
Reference for Ezra Pound poem: [Brainyquote.com](https://www.brainyquote.com/quotes/ezra_pound_164564)

## Note
- All tests were done on Ubuntu 20.04.
- Please check the [requirements.txt](https://github.com/Taiwopeter-babs/alx-higher_level_programming/blob/29b62115a8b060ddf9fc3c182f3395b8b27730de/0x07-python-test_driven_development/requirements.txt) for installations used.

## Author
Taiwo Babalola <babalolataiwop@gmail.com>
