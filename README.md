# Number Guessing Game Using The Concept Of Binary Search

Theoretically, this is a simple game that covers how to guess a number using the concept behind the binary search algorithm. In reality, the code is a bit more complex and covers a wide range of topics. Within this project, you will see classes, dictionaries, lists, type conversions, and simple command line arguments. You'll also see the SOLID and DRY principles being used.

## Requirements
Python 3.6 or newer

## How to play
Run `python3 main.py` in your terminal and follow the prompts. Note: you may need to use `python` instead of `python3` depending on your setup. There are 2 additional arguments that can be passed in any order.

The `hints` argument. This will display additional information through the game play to help understand what your next guess should be.
Example: `python3 main.py hints`

The `auto` argument. This will still require you to answer the prompt of how must items should be in the list, but it will automatically guess for you. If you use this argument, it is recommended, but not required, to also use the hints argument with it.
Example: `python3 main.py hints auto` or `python3 main.py auto hints`

## What is binary search?
Binary search is a faster way of searching for an item within a **sorted** list/array. (NOTE: the list MUST BE sorted). It works by starting at the middle of the list and then determining if you're high or low (or correct). If the mid point is too high, then we know everything from that point upwards can be disgarded. The inverse is true if the mid point was too low. We keep cutting the list in half until we get to the answer. The benefit to this approach is that on very large lists, the max number of guesses (or operations) is relatively low. The increase in operations is log n. Here's a small table showing how it grows based in the list size:

| List size     | Operations |
| ------------- | ---------- |
| 10            | 4          |
| 100           | 7          |
| 1,000         | 10         |
| 10,000        | 14         |
| 100,000       | 17         |
| 1,000,000     | 20         |
| 10,000,000    | 24         |
| 100,000,000   | 27         |
| 1,000,000,000 | 30         |

It might be hard to believe that if someone asked you to pick a number between 1 and 1 billion, that you could definitively guess it within 30 guesses, but it's true! Thirty guesses is also the worse case, it's possible you guess in less than that. To get to a worse case of 100 operations, your list size would need to be 1 nonillion ( 1 plus 30 zeros - 1,000,000,000,000,000,000,000,000,000,000.)