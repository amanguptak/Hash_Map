class Mapnode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class Map:
    def __init__(self):
        self.bucketsize=5
        self.bucket=[None for i in range(self.bucketsize)]
        self.count=0


    #for genrating the hash code if key will be a string
    def hash_code(self,key):
        code=0
        coffecint=1
        for i in reversed(key):
            #code=code+ord(i)coffecient
            code+=ord(i)*coffecint
            code=code%self.bucketsize
            coffecint=3
            coffecint=coffecint%self.bucketsize
            return code%self.bucketsize

    def size(self):

        return self.count

#rehash method for decreasing the time complexity of code
    def rehash(self):
        #storing value of previous list in temp
        temp= self.bucket
        #creatng new bucket with double size and intializing with None
        self.bucket= [None for i in range(2*self.bucketsize)]
        self.bucketsize= 2* self.bucketsize
        self.count=0
        for head in temp:
            while head is not None:
                self.insert(head.key,head.value)
                head=head.next


    def getLoadfactor(self):
        loadfactor=self.count/self.bucketsize
        return loadfactor

    #inserting a keyvalue pair in hashmap
    def insert(self,key,value):
        index=self.hash_code(key)
        head=self.bucket[index]
        while head is not None:
            if head.key==key:
                head.value=value
            return
            head=head.next
        newnode=Mapnode(key,value)
        newnode.next=head
        self.bucket[index]=newnode
        self.count+=1
        loadfactor=self.count/self.bucketsize
        if loadfactor>0.7:
            self.rehash()

     #printing value  of respected key

    def printkey(self,key):
        index = self.hash_code(key)
        head=self.bucket[index]
        while head is not None:
            if head.key==key:

             return (head.value)
            head=head.next

        return None
    #remove element from hash
    def remove(self,key):
         index=self.hash_code(key)
         head=self.bucket[index]
         prev=None
         while head is not None:

            if head.key==key:
                if prev  is None:
                    self.bucket[index]=head.next
                else:

                    prev.next=head.next

                return head.value

            prev=head
            head=head.next
         return None


if __name__=="__main__":
    map=Map()
    #for checking the loadfactor
    for i in range(10):
        map.insert("dvc"+str(i),i)
        print(map.getLoadfactor())
    print(map.size()
      #if you want to insert a key or remove a key use below commented code

    '''print(map.printkey("kumar"))
    print(map.printkey("gupta"))
    print(map.printkey("aman"))
    print(map.remove("aman"))
    print(map.printkey("aman"))'
    '''

