"""
Lucio Plancarte 
"""


class HashTable:

    def __init__(self, buckets = 10,
                        load_factor = 0.75,
                        resize_by = 2,
                        del_token = "#DEL#"):
        """
        The Constructor for this hashtable.
        It initializes:
        The default amount of buckets
        The array to be used as hashtable.
            You can use the builtin Python list to create a list with initial
            None values.
            The table has a capacity of the number of buckets.
        The initial size for the hash table (number of elements)
        The load factor threshold
        The multiplier for the resizing operation.
            (we won't reduce the table in this assignment)
        The special variable to be used as the marker for deleted items
        The constant 'C' for the hash function with a value 0.65
        It prints the message "Initialzing HashTable with ______ buckets"
        """

    def hash_function(self, key):
        """
        Returns the bucket for the element in the hash table.
        It implements a MULTIPLICATIVE hash function.
        In the multiplication method, a constant ( (0 < C < 1) is used to
        multiply the key. The fractional part of the product is then 
        multiplied by the number of buckets to get the hash value (the indec).
        It uses the equation:
        h(k) = floor(buckets * (key * C mod 1 ) )
        """

    def put(self, key, value):
        """
        Inserts OR Updates a tuple (key-value) pair in hash table.
        This method uses QUADRATIC probing with lazy deletion to handle collisions.
        When a new element needs to be inserted, this method computes the load factor
        of the hash table. If it is equal than or greater than the load factor threshold,
        then it resizes the table.
        It prints "Resizing..."
        
        Parameters:
        -key: The key to be inserts or updated.
        -value: The value associated with the key.

        Consider:
        1. If the key already exists, its value is UPDATED.
        2. If the key doesn't exist, and the bucket is empty then a new Python
            tuple (key, value) pair is inserted. If the bucket is occupied, then
            a QUADRATIC probing is needed.
            Use the QUADRATIC probe equation, not just a simple loop.
            Use the equation in the one presented in class as "Simpler implementation"
            for the quadratic probing.
            Consider a circular table
        3. If a deleted slot, marked with the special token is encountered during the
            QUADRATIC probing, it can be reused for insertion.
        4. The size of the hash table is incremented only for new insertions, not for updates.
        """


    def get(self, key):
        """
        Method that returns the value for a given key
        If the key does not exist it returns None
        When using QUADRATIC probing the key might be stored in a different slot.
        Therefore, the method should start searching from the slot corresponding
        to the key and continue until it finds an empty bucket using the QUADRATIC
        probing technique. It is not a simple loop through the table!
        Also consider a circular table for the probing.
        """

    def search(self, key):
        """
        Method to search for an item. It recieves the key for that item
        It returns True if the item exists in the table.
        Otherwise it returns None
        When using QUADRATIC probing the key might be stored in a different slot.
        Therefore, the method should start searching from the slot corresponding 
        to the key and continue until it finds an empty bucket using the QUADRATIC
        probing technique. It is not a simple loops through the table!
        Also consider a circular table for the probing.
        """

    def remove(self, key):
        """
        Removes a key-value pair from the hash table.
        This method uses QUADRATIC probing to find the key and marks the slot as 
        DELETED instead of removing it entirely.

        Parameters:
            -key: The key of the item to be removed.

        If the key is found, it marks the slot as deleted and decrements the size.
        If the key is not found or if an empty slot (None) is encountered, it prints:
            "___ does not exist"
        The DELETED marker allows the slot to be reused for future insertions while
        preventing the search algorithm from terminating prematurely.

        The method should start searching from the slot corresponding to the key and
        continue until it finds an empty bucket using the QUADRATIC probing technique.
        It is not a simple loop through the table!

        In this activity, for simplicity we are NOT shrinking the table.
        """

    def _resize(self):
        """
        This private method resizes the hash table and PUTS the element from the old table
        to their new corresponding buckets in the new larger table based on the new
        hash computation.
        """

    def __len__(self):
        """
        Method to return the VALID number of elements of the hash table
        """

    def is_empty(self):
        """
        Method to check if the hash table is empty or not.
        It returns a boolean value
        """
    def __str__(self):
        """
        Method to show the content of the hash table including the None and DELETED values.
        For the deleted elements use the word "DELETED"
        It returns a string to be used by the "print" function.
        If the table is empty, it returs "Hash Table is Empty"
        """


