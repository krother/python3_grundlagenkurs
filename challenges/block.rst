
Blockchain
==========

We need:

1. A function that generates transactions (name1, name2, amount)
2. Block that consists of the checksum of the preceding block, some transactions, a checksum
3. All three are added to create a single hash
4. Tune the checksum until the hexdigest of the block ends with four zeroes

.. code:: python3

   import hashlib
   
   h = hashlib.sha256()
   h.update(text.encode())
   print(h.hexdigest())

