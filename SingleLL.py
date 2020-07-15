class Node:
    def __init__(self,value):
        self.info = value
        self.link = None

class SingleLinkedList:
    def __init__(self):
        self.start = None
    def display_list(self):
        if self.start is None:
            print("Emoty")
        else:
            print("List is ")
            p = self.start
            while p is not None:
                print(p.info," ",end='')
                p = p.link
            print()
    def count_node(self):
        p = self.start
        n =0
        while p is not None:
            n+=1
            p = p.link
        print("Number of Nodes is this Single List is ",n)

    def search(self,x):
        pos = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print(x," is at possition ",pos)
                return True
            pos+=1
            p=p.link
            
        print(x," is not in the List ")
        return False
    def insert_in_beggning(self,data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
        else:
            temp.link = self.start
            self.start=temp
    def insert_at_end(self,data):
        temp = Node(data)
        if self.start is None:
            self.start=temp
            return
        else:
            p = self.start
            while p.link is not None:
                p = p.link
            p.link = temp
    def create_list(self):
        n = int(input("Enter the Number of Node !! "))
        if n <= 0:
            return
        for i in range(n):
            data = int(input("Enter the Element !! "))
            self.insert_at_end(data)
    def insert_after(self,data,x):
        temp = Node(data)
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.link
        if p is None:
            print(x," is not present in list ")
        else:
            temp.link = p.link
            p.link = temp
    def insert_before(self,data,x):
        temp = Node(data)
        #if list is empty
        if self.start == None:
            print("List is Empty")
            return
        #if x is First Node and New node has to insert before x
        if self.start.info == x:
            temp.link = self.start
            self.start = temp
            return
        #find the predesesor of x and insert a new node after that
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link
        if p.link is None:
            print(x," is not present in the list")
            return 
        else:
            temp.link = p.link
            p.link = temp
    def insert_at_possition(self,data,x):
        temp = Node(data)
        if x == 1:
            temp.link = self.start
            self.start = temp
            return
        p = self.start
        i = 1
        while i < k-1 and p is not None:
            i+=1
            p = p.link
        if p is None:
            print(x," possition is not valide !! ")
            return
        else:
            temp.link = p.link
            p.link = temp 
    def delete_node(self,x):
        if self.start is None:
            print("List is empty !!")
            return
        if self.start.info == x :
            self.start = self.start.link
            return

        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link
        if p.link is None:
            print(x," is not prasent in list")
        else:
            p.link = p.link.link
    def delete_first_node(self):
        if self.start is None:
            print("List is Empty")
            return
        else:
            self.start =self.start.link
    def delete_last_node(self):
        if self.start is None:
            print("List is Empty")
            return
        elif self.start.link is None:
            self.start = None
            return
        else:
            p = self.start
            while p.link.link is not None:
                p = p.link
            p.link = None
    def reverse_list(self):
        prev = None
        p = self.start
        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p = next
        self.start = prev
    def bubble_sort_exdata(self):
        end = None
        while end != self.start.link:
            p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.info , q.info =q.info , p.info
                p=p.link
            end = p

    def bubble_sort_exlink(self):
        end = None
        while end != self.start.link:
            r = p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.link = q.link
                    q.link = p
                    if p != self.start:
                        r.link = q
                    else:
                        self.start = q
                    p,q=q,p
                r = p
                p = p.link
            end = p

    def has_cycle(self):
        if self.find_cycle() is None:
            return False
        else:
            return True
    def find_cycle(self):
        if self.start is None or self.start.link is None:
            return True
        slowR = self.start
        fastR = self.start
        while fastR is not None and fastR.link is not None:
            slowR = slowR.link
            fastR = fastR.link.link 
            if slowR == fastR:
                return slowR
        return None
    def remove_cycle(self):
        c = self.find_cycle()
        if c is None:
            return
        print("Node of which cycle was deleted is ", c.info)
        p = c
        q = c
        len_cycle = 0
        while True:
            len_cycle += 1
            q = q.link 
            if p == q:
                break; 
        print("length of cycle is : ",len_cycle)
        len_remaning_list = 0
        p = self.start
        while p != q:
            len_remaning_list += 1
            p = p.link
            q = q.link 
        print("Number of Nodes not includded in the Cycle are : ", len_remaning_list)
        lenght_list = len_cycle+ len_remaning_list
        print("Length os the list is : ",lenght_list)
        p = self.start
        for i in range(lenght_list - 1):
            p = p.link
        p.link = None
    def insert_cycle(self,x):
        if self.start is None:
            return
        p = self.start
        px = None
        prev = None
        while p is not None:
            if p.info == x:
                px = p
            prev = p
            p = p.link
        if px is not None:
            prev.link = px
        else:
            print(x," is Not present is the list ")
    def merge2(self,list2):
        merge_list = SingleLinkedList()
        merge_list.start = self._merge2(self.start,list2.start)
        return merge_list

    def _merge2(self,p1,p2):
        if p1.info <= p2.info:
            startM = p1
            p1= p1.link 
        else:
            startM = p2
            p2 = p2.link 
        pM = startM
        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pM.link = p1
                pM = pM.link 
                p1 = p1.link 
            else:
                pM.link = p2
                pM = pM.link 
                p2 = p2.link 
        if p1 is None:
            pM.link = p2
        if p2 is None:
            pM.link = p1
        return startM
    def merge_sort(self):
        self.start = self._merge_sort_rec(self.start)
    def _merge_sort_rec(self,list_start):
        #is list is empty or has no elements
        if list_start is None or list_start.link is None:
            return list_start
        #if more than one element are there
        start1 = list_start
        start2 = self._divide_list(list_start)
        start1 = self._merge_sort_rec(start1)
        start2 = self._merge_sort_rec(start2)
        startM = self._merge2(start1,start2)
        return startM
        
    def _divide_list(self,p):
        q = p.link.link
        while q is not None and q.link is not None:
            p = p.link
            q = q.link.link 

        start2 =p.link
        p.link = None
        return start2
