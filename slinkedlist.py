class node(object):
    def __init__(self,data, next_node=None):
        self.data=data
        self.next_node = next_node

    def get_content(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self,new_next):
        self.next_node = new_next


def print_list(l):
    current=l.head
    while(current):
        print current.data
        current= current.get_next()

class List:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.set_next(self.head)
            self.head=new_node

    def delete(self,data):
        if data==self.head.data:
            self.head=self.head.get_next()
            return
        prev=self.head
        current=prev.get_next()
        while current!=None:
            if current.data==data:
                prev.set_next(current.get_next())
                return
            else:
                prev=current
                current=current.get_next()
        if current==None:
            print "data not found"
            return

    def size(self):
        count=0
        current=self.head
        while current!=None:
            count+=1
            current=current.get_next()

        return count

    def search(self,data):
        current=self.head
        while current!=None:
            if current.data==data:
                return data
            else:
                current=current.get_next()
        if current==None:
            print "data not found"
            return





def main():
    l=List()
    l.insert(1)
    l.insert(3)
    l.delete(3)
    l.delete(2)
    l.insert(1)
    l.insert(23)
    l.insert(2)
    print_list(l)
    print l.size()
    print l.search(23)

if __name__ == '__main__':
    main()



