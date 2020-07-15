import SingleLL

node = SingleLL.Node
singlelinkedlist = SingleLL.SingleLinkedList()
def merge1(self,list2):
    merge_list = singlelinkedlist()
    merge_list.start =self._merge1(self.start,list1.start)
    return merge_list

def _merge1(self,p1,p2):
    if p1.info <= p2.info:
        startM = node(p1.info)
        p1=p1.link; 
    else:
        startM = node(p1.info)
        p2= p2.link; 
    pM = startM
    while p1 is not None and p2 is not None:
        if p1.info <= p2.info:
            pM.link = node(p1.info)
            p1 = p1.link 
        else:
            pM.link = node(p2.info)
            p2=p2.link 
    #id second list is finish then add elemsnt of frist list to main list
    while p1 is not None:
        pM.link = node(p1.info)
        p1=p1.link 
        pM = pM.link
    #if first list is fiish thne add element of second list in main list
    while p2 is not None:
        pM.link = node(p2.info)
        p2=p2.link 
        pM = pM.link

def merge2(self,list2):
    merge_list = singlelinkedlist()
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

list1 = SingleLL.SingleLinkedList()
list2 = SingleLL.SingleLinkedList()
list1.create_list()
list2.create_list()
list1.bubble_sort_exdata()
list2.bubble_sort_exdata()
print("first List - ", list1.display_list())
print("sec list - "); list2.display_list()
list3 = list1.merge1(list2)
print("merged list is - "); list3.display_list()

print("first List - "); list1.display_list()
print("sec list - "); list2.display_list()
list3 = list1.merge2(list2)
print("merged list is - "); list3.display_list()
print("first List - "); list1.display_list()
print("sec list - "); list2.display_list()

