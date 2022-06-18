class HashTable:
    # Constructor with optional initial capacity parameter
    # O(N) linear
    def __init__(self, capacity=10):
        # initialize the hash table with empty bucket list entries
        self.table = []
        for i in range(capacity):
            self.table.append([])

    # Inserts a new item into the hash table or updates existing item
    def insert(self, key, item):
        # get the bucket list for the item
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # if key is not present, append item to the end of bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for item with matching key in the hash table
    # Returns the value if found, or None if not found
    def search(self, key):
        # get the bucket list for the key
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for key in bucket list
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Removes item with matching key from the hash table
    def remove(self, key):
        # get the bucket list for the item
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove item from bucket list if it exists
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
