# Lab 03 - Loops, Strings, and Lists

In this lab, we'll learn how to use loops, including for processing both lists and strings.

## Getting Started

Be sure that you have accepted the assignment invitation within GitHub Classroom (by clicking on the link provided in the lab assignment on Canvas), before you proceed.  You want to clone your own copy of the repository (not the original, since you can't write to that repository).  The command to do so will look something like this:

```
git clone https://github.com/CSCI1030U/lab03-rana-muniz
```

Be sure to change directory to a place where the rest of your CSCI1030U labs are stored, first, so that this command copies your lab assignment starter code into the proper place.

## Instructions

In this lab, you will edit the `lab03.py` file so that it meets the requirements described in the following sections.


### Part 1

The `lab03.py` file declares a variable called `pets`, as well as two more variables `count` and `pet_name_lengths`.  Your first task is to count the number of pet names in `pets` using a for loop, putting the count into `count`.  Your second task is to, for each pet name, count the number of letters in the pet name using a for loop, putting each pet name into a list variable called `word_lengths`, using the `append()` function to add to the list.  

Sample output has been given, below:

```
There are 6 pets in the list.
The word lengths of each pet name are [4, 5, 16, 5, 6, 4].
```

_**Note:** The output has to match exactly, so be sure to put exactly one space on each side of the `=` sign, and there will be a newline after each variable output (as is the default for `print()`)._

### Part 2

Given in the `lab03.py` file are a list of words.  Use a loop to go through this list of words, and for each word count the number of vowels (`a`, `e`, `i`, `o`, or `u`) and the number of consonants (any other character, for simplicity).  You can assume that the words will be strictly lowercase letters.  Finally, form a list of the ratios (`vowel_count / consonant_count`) for all of the words, in the same order as the words in the list.

Sample output has been given, below:

```
The vowel to consonant ratios of each word are [0.5, 0.6666666666666666, 0.25, 0.5, 0.5, 1.0, 0.5, 0.3333333333333333, 0.5].
```

## Verifying Correctness

Run the pre-written tests that verify that your lab assignment code passes, using the following command:

```
pytest --capture=sys
```

Examine the output closely.  There should be hints about what went wrong, if any of the tests fail.  If you are struggling to figure it out, you can always ask for help (see __Getting Help__ for details).


## Getting Help

If your code does not work, there is always a lab instructor present during your lab period for assistance.  Them not having to mark lab assignment submissions means that they should have plenty of time to ensure that you are able to get your lab assignment submission working by the end of the lab period.

_**Note:** The lab instructor is likely to help you figure out what is wrong with your code, rather than tell you how to fix it directly.  The goal is for you to learn how to diagnose and fix your bugs on your own._



## How to Submit

First, ensure that your code passes the tests (see the section __Verifying Correctness__ for details).  If you are certain that your code passes all of the tests, then you can submit your work using the following commands:

```
git add --all
git commit -m "Lab 03 completed code"
git push origin main
```

Once you have submitted your work, you can also double check that your auto-grading was successful by clicking on the `Actions` tab in your repository page on GitHub.  Sometimes, this takes a few minutes to complete, so please be patient.
