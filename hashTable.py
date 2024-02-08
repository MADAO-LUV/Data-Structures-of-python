


class hashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size
    
    def put(self,key,data):
        hashvalue = self.hashfunction(key)

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue)
                while self.slots[nextslot] != None and\
                    self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)
                
        if self.slots[nextslot] == None:
            self.slots[nextslot] = key
            self.data[nextslot] = data
        else:
            self.data[nextslot] = data

    def hashfunction(self,key):
        return key%self.size

    def rehash(self,oldhash):
        return (oldhash+1)%self.size

    def get(self,key):
        startslot = self.hashfunction(key)

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True
        return data
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,data):
        return self.put(key,data)
    

    def length(self):
        count = 0
        position = 0
        for position in range(self.size):
            if self.slots[position] == None:
                count = count + 1

        count = self.size - count
        return count  

