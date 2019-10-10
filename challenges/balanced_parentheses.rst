Balanced Parentheses
====================

Write a function that detects whether
all open parentheses in a string are closed and vice versa.

The input is a non-empty string
 consisting only of ( and )

.. code:: python3

   assert balanced("()") == True
   assert balanced(")(") == False
   assert balanced("((()))") == True
   assert balanced("(((") == False
   assert balanced("(()())") == True
   assert balanced("(()") == False
   assert balanced("") == True
   assert balanced("(" * 100000 + ")" * 100000) == True
   assert balanced(")") == False
