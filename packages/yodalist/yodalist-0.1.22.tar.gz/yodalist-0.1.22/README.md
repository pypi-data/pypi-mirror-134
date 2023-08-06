# yodalist pre-release

Yoda-indexed lists in Python.

Yoda-indexing follows this pattern: 0, 4, 5, 6, 1, 2, 3, 7, 8, 9, etc. Inspired by the ordering used in the 

## TODOS:

```
0. Stress the importance of zero-indexing: We're not savages here.
4. Add functionality tests
5. Add RaisesError tests
6. Package to a wheel, etc. 
1. Add to pip, conda, other package managers.
2. Add install instructions
3. Add something else snarky here
7. Post to HackerNews or ProgrammerHumor or something, because this is how career-building works in 2022
```

## Install

There are three ways to use this package:

1. Simply copy-and-paste the `src/yodalist.py` file to your project.

2. (todo) Install via PIP

3. (todo) Build and install on your own.

## Usage

```
>>> from yodalist import yodalist
>>> mylist = yodalist(['hello', 'world', 'i', 'am', 'a', 'yoda', 'list', '!!!'])
>>> for ii in range(len(mylist)):
...     print(ii, mylist[ii])
... 
0 hello
1 a
2 yoda
3 list
4 world
5 i
6 am
7 !!!
```
