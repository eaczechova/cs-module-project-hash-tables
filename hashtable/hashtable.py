class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY ):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0
       
      
    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here

        return len(self.array)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size/self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for char in key:
            # ord() function returns an integer representing the Unicode character
            hash += (hash * 33) + ord(char)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        key_index = self.hash_index(key)
        current_node = self.array[key_index]
        new_node = HashTableEntry(key, value)
        # if there is nothing on that index, just add new_node
        if current_node is None:
            self.array[key_index] = new_node
            self.size += 1
        else:
        # add it to the beginning of the list by moving current node next
            new_node.next = current_node
            self.array[key_index] = new_node
        self.size += 1
        
    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        """

        key_index  = self.hash_index(key) 
        current_node = self.array[key_index]

        
        prev_node = None

        while current_node is not None and current_node.key is not key:
            prev_node = current_node
            current_node = current_node.next
        
        # when key was not found
        if current_node is None:
            return None
        
        else: 
            deleted_node = current_node.value
            # index key is at the first position
            if prev_node is None:
                # key index points to next node
                self.array[key_index] = current_node.next
                self.size -= 1
            else:
                prev_node.next = current_node.next

            return deleted_node

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        key_index  = self.hash_index(key)
        current_node = self.array[key_index]

        while current_node is not None and current_node.key is not key:
            current_node = current_node.next
            if current_node is None:
                return None
        
        if current_node is not None:
            return current_node.value 
     

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")
