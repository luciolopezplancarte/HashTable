"""
Lucio Plancarte 
"""

import math
class HashTable:
    C = 0.65 # HASH FUNCTION CONSTANT

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
        self._buckets = buckets
        self.array = [None] * buckets
        self._size = 0
        self._load_factor_threshold = load_factor
        self._resize_multiplier = resize_by
        self._del_marker = del_token

        print(f"Initialzing Hashtable with {self._buckets} buckets")


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
        index = math.floor(self._buckets * ((key * self.C) % 1))
        return index

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
        #load factor = number of items in list/ number of available slots
        #simpler implementation: (h(key) + i^2)%(tablesize)


        load_factor = self._size /(self._buckets)
        if load_factor > self._load_factor_threshold:
            #resize
            self._resize() 
            print("Resizing...")
        index = self.hash_function(key)
        if self.get(key):
            #UPDATE
            #https://stackoverflow.com/questions/11458239/how-to-change-values-in-a-tuple
            temp= list(self.array[index])
            temp[0] = key
            temp[1] = value
            self.array[index] = tuple(temp)

            return

        i = 0
        if self.array[index] is not None:
            #print("COLLISION")
            #print("PROBING")
            new_index = index
            while True:
            #while self.array[new_index] is not None:
                new_index = (index + (i*i))%self._buckets
                #print(f"Probing Index{new_index}")
                i +=1
                if self.array[new_index] is None or self.array[new_index] == self._del_marker:
                    index = new_index
                    break
            
        self.array[index] = (key,value)
        #print(f"Inserting into index:{index}")
        self._size +=1
        





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
        #Check if the item exists
        if not self.search(key):
            return None
        
        index_toGet = self.hash_function(key)
        index_toProbe  = index_toGet
        for i in range(self._buckets):
            if self.array[index_toProbe]:
                if self.array[index_toProbe][0] == key:
                    return self.array[index_toGet][1]
                else:
                    index_toProbe = (index_toGet + (i * i))% self._buckets
        
        return None


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
        index_toSearch = self.hash_function(key)
        index_toProbe  = index_toSearch
        for i in range(self._buckets):
            if self.array[index_toProbe]:
                if self.array[index_toProbe][0] == key:
                    return True
                else:
                    index_toProbe = (index_toSearch + (i * i))% self._buckets
        return None
                    

        

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
        if not self.get(key):
            print(f"{key} does not exist")
            return

        index_toRemove = self.hash_function(key)
        index_toProbe  = index_toRemove
        for i in range(self._buckets):
            if self.array[index_toProbe]:
                if self.array[index_toProbe][0] == key:
                    self.array[index_toProbe] = self._del_marker
                    self._size -= 1
                    return
                else:
                    index_toProbe = (index_toRemove + (i * i))% self._buckets
        

        

    def _resize(self):
        """
        This private method resizes the hash table and PUTS the element from the old table
        to their new corresponding buckets in the new larger table based on the new
        hash computation.
        """
        
        self._buckets= self._resize_multiplier * self._buckets
        #new_array = [None] * self._buckets
        temp_array = self.array
        self.array = [None] * self._buckets

        for i in range(len(temp_array)):
            j = 0
            if temp_array[i]:
                #self.put(temp_array[i][0], temp_array[i][1])
                index = self.hash_function(temp_array[i][0])
                new_index = index
                while True:
                    new_index = (index + (j*j))%self._buckets
                    j +=1
                    if self.array[new_index] is None or self.array[new_index] == self._del_marker:
                        index = new_index
                        break
                self.array[index] = temp_array[i]
            


    def __len__(self):
        """
        Method to return the VALID number of elements of the hash table
        """
        return self._size

    def is_empty(self):
        """
        Method to check if the hash table is empty or not.
        It returns a boolean value
        """
        return self._size == 0

    def __str__(self):
        """
        Method to show the content of the hash table including the None and DELETED values.
        For the deleted elements use the word "DELETED"
        It returns a string to be used by the "print" function.
        If the table is empty, it returs "Hash Table is Empty"
        """
        result = ""
        for i in range(self._buckets):
            if self.array[i] == self._del_marker:
                result += f"{i}: DELETED\n"
            else:
                result += f"{i}: {self.array[i]} \n"

        return result


