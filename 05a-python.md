# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Tuples are immutable whereas lists can be changed. Only tuples can
work as keys in dictionaries as they have a hash function

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are lists of unique elements, whereas lists can contain
multiple elements with the same value. A list could for example list all
the cards in a standard card deck with their ranks (4 cards per rank),
whereas the set would show unique ranks only (thus only 13 unique ranks)
.

>> I can imagine a set would be faster for finding an element as
there are only unique values in sets.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> A lambda allows the creation of a very short function, saving space
as an example you could use sorted('sequence', key = lamba x: x[2] to
sort by the third element in a sequence of tuples).


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions allow the creation of lists with a simple
expression. For example [x**2 for x in range(0,10)] would create a list
comprised of the squares of the numbers from 0 to 9.

>> You could do that with with map by using the following function:
map(lambda x: x**2, [x for x in range(0,10)]

>> Filter filters for elements that return True. For example, if I
wanted to create a list of all numbers divisible by 5 up to 50, I could
write the following function
filter(x%5 == 0, [x for x in range(0,51)]

>> Set and dictionary comprehensions would be very similar. For set
comprehensions, I could just use the set function on the above, whereas
for a dictionary, I could use a function with the following syntax:
d = dict((key,value) for (key, value) in iterable)


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





