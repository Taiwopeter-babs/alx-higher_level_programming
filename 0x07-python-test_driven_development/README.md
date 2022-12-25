#	Test Driven Development (doctest and unittests)

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


## Author
Taiwo Babalola <babalolataiwop@gmail.com>
