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

# Chapter 2
## How your memory works?

Imagine you go to a show and need to check your things. A ches of drawers is available.
Each drawwer can hold one element. You want to store 2 things so you ask for 2 drawers. 
Your computer looks like a giant set of drawers, and each drawer has an address.

for example: fe0ffeeb is the address of a slot in memory

## Arrays and Liked lists

Sometimes we need to store a list of elements in memory. Suppose you are doing a app for your do-to, you'll want
to store the to-do list in memory. 

Should you use an array or a linked list?
Using an **array** means all your tasked are stored contiguosly (right next to each other) in memory.

Meaby you have a array with 3 items, but the fourth space is bussy for another thing in memory. So if you want to add a 
new item, you cant add because there already taken up by someone else's stuff. It's like going to a movie with your friends and finding a place to sit but another friend joins you, and there is no place for them. 
In this case you need to ask your computer for a different chunck of memory that can fit your tasks. Then you need to move all your task there. 

Some times we can asked for a specific number of space in the computer. For example you can asked for 10 spaces, and if you want to add another item you dont need to move your tasks. 
But what if you don used all these 10 spaces, it is wasted memory.
And what happend if you want you need more than 10?

Well this problem is fixed by linked lists.

### Linked list

With linked lists, the items can be anywhere in memory.

Each iteam stores the address of the next item in the list. A bunch of random memory addresses are linked together. 
Is like a tresure hunt, when you go to the first addresses it says, the next item can be found in the adress 6484.
Adding an item to a linked list is easy: you stick it anywhere in memory and store the address in the previous item. 


We  avoid another problem, We don't need that the date is together, so your computer is not searching a spaces with 1000 slots, like works in arrays, this linked lists split in the memory, so if you have space in memory you can have a linked list. 


So what are arrays good for?

### Ararys 

Linked list have a problem, suppose you need to read the last element in a linked list. You cant just read it, because you dont know the address of this item. Instead you have to go  to item 1 to go to item 2 and so on... until get the last item. 

* Linked list are great ig you're going to read all the items one at time, but if you want to going to keep jumping around, is teerible. 

Arrays are different, You know the addres of each item, for example we know that the fisrt position of your array is 00, so what item is in the position 05? Is easy.

* Arrays are great when you want to select or get some random position instantly. 

### Terminology. 

The elements in an array are numbered, This numbering starts at 0. 
This position of an element is called index. 
Here are the run times for common operations on a arrays and lists

         Arrays      Lists
Reading    O(1)      O(n)
Insertion  O(n)      O(1)

### Exercise
Suppose you're bulding an app to keep track of your finances
1. Groceries
2. Movie
3. Memberships 

At the final of the month you need to review and sum the total of your expenses. Should you use a
linked list or a array?
R. I will use a linked list becouse the finale of the app is sum all your expenses and you need to insert a new value
every day. So it is more optimizable use a linked list, and if you want to see something meaby has more time, but the final goal is the sum and the insertion of values.  But if the final goal is that the user can see, and meaby acces to any value from this expenses list, meaby the better option is a array. 

### Inserting into the middle of a list

Whats is better if you want to insert elements ib the middleÑ arrays or lists?
With list it's as easy as chagening what the previuos elemnt points to
But for arrays you have to shift all the rest of elements down. And if there is not space you might have to copy everything in a different location. 

**List are better if you want to insert in the middle**


#### Pointers
We use pointers when we have a linked list and you *point to the next item*. With each item in your linked list, you use a little bit of memory to store address of the next item. This is called **pointer**. 


### Deletions 

Again when we want to delte a item is better in linked list, because you only need to change de element you points to. 

#### Run times for Common operations on arrays and linked lists


|Operation|Arrays|Linked Lists|
|---------|-------|------------|
|Reading|O(1)|O(n)|
|Insertion|O(n)|O(1)|
|Deltion|O(n)|O(1)|


It's aa common practice to keep track of the first and last items in a linked listm so it would take only O(1) time to delete those