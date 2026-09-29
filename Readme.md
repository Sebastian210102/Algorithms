In this project i will study about the algorithms to improve my abilitys like a programmer and engineer. 
So lets begging 



17/09/2026 
# Chapter 1 
## Binary search
It's input is a sorted list of elements. If a elemente we are searching is in the list, binary search will return the position is located. Other wise binary serch return *Null*

For example, we have a list between 1 to 100. You have to try to guess the number in the fewest tries possible. For every try i'l tell you if es high, low or correct. 

You can think say 1, to low, meaby 2, to low..... so it will take too much tries guess the number, if my number is 99. 

#### So we have a better way to search

We can start with 50, too low, but we eliminated the half for the numbers. So next guess its 75. Now is too high. But again we cut the half of remaining numbers. So we can do this until guess the number. So we eliminated the half of the numbers for each search. 

General for any list for n, binary search will take log2 n steps to run in the worst of the cases 

**Very important** -> Binary search only wors in *SORTED LISTS* in alfabetical order 

Exercises 
1.1 Suppose you have a sorted list of 128 names, and you’re searching
through it using binary search. What’s the maximum number of
steps it would take?

In this lesson we leart that que number of steps for this algorithm is the *log2 num_total*

so -> log2 128 =  7 

1.2 Suppose you double the size of the list. What’s the maximum
number of steps now?

log2 (256) = 8

20/09/2026
## Runnig time 

Every time we talk about of runnig time, generally, you want to choose the most efficient algorithm wherever we want
to optimze for time of space. 

So binary search run in a log time, while in the example for guess number by number is called linear time 

- Binary search(O(logn))
- Simple search (O(n))


This terms makes us move to de next concept.

## Big O notation

This is a especial notation that tells you how fast your algorithm is. 

For exaple, imagine we have to do a program for search some kind of info,  you don't know what algorithm you can use
If every comparation will take 1ms, a comparation of 1 billion of inputs will take 11 days! 

But if we use binary seach will take only 30ms, this is a big diference.

Big O doesn’t tell you the speed inseconds. Big O notation lets you compare the number of operations. It
tells you how fast the algorithm grows.

O(n)

Where 
O = "Big O"
n = Number of operations

This notation will tells you the number of operations an algorith will makes 

### Big O establishes a worst-case run time

We can sopose you are searching a name in the phone book. You know that a simple search will take you O(N)
to run, if you find the name at the fisrt try is the best scenario, but for big O notation ypu will take the worst.

This are 5 big O run times that you'll encounter a lot. Sorted from the fastest to slowest:

* O(log n)Log time,  Example binary search
* O(n) Linear time, Example, simple search
* O(n * log n). Example: a fast sorting algorithm, like quicksort 
* O(n2). Example: a slow sorting algorithm, like selection sort
* O(n!). Example: a really slow algorithm, like the traveling salesperson

### Exercise
Give the run time for each of these scenarios in terms of big O.
1.3 You have a name, and you want to find the person’s phone number
in the phone book.

* R. O(log n)

1.4 You have a phone number, and you want to find the person’s name
in the phone book. (Hint: You’ll have to search through the whole
book!)

* R. O(n)

1.5 You want to read the numbers of every person in the phone book.
* R. O(n)

1.6 You want to read the numbers of just the As. (This is a tricky one!
It involves concepts that are covered more in chapter 4. Read the
answer—you may be surprised!)

* R. O(n)

## The traveling salesperson

Here is an examnple of a algorith with a very bad running time. This is a famus in computer science because, its growth is appalling and some very smart people think it can't be improved. It's called the travellin salesperson problem. 

You have a salesperson. This person has to go to five cities. Let's call Pancho, Pancho wants to hit all five cities while traveling the minimum distance. There are many ways to  try to visit each city.

He adds up the local distance and then picks the path with the lowest distance. There are 120 permutations with five cities.
For six cities will take 720 operations (there are 720 permutations). For seven cities will take 5040 permutations.
in general is a O(n!) time , or factorial time. Imagine you want to calculate for 100+ cities, the operation is impossible, the sun will collapse first. May be we need to seek for another way, but Does not exist!!
This is one of the problems in computer science, There is no fast kwown algorithm.  