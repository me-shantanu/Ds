#import Section
import SingleLL 
import DoubleLL
import CircularLL





#main code
print('''
     --|---------|        ----------         -------------      ----------       ----------     -----------  
       |         |        |                  |                 |          |     |     |    |    |
       |         |        |                  |                 |          |     |     |    |    |
       |         |        |--------          |                 |----------|     |     |    |    |---------
       |         |                 |         |    ------|      |          |     |          |    |
       |         |                 |         |          |      |          |     |          |    |
     --|---------| **      ---------- **     |-----------      |          |     |          |    |----------



      ''')

while True:
       print("---------------------------------------------------------------------------------")
       print("What Data Structure You wanna Play !!")
       print("---------------------------------------------------------------------------------")
       print("---------------------------------------------------------------------------------")
       print("1: Linked List")
       print("2: Stack")
       print("3: Queue")
       print("4: Trees")
       print("5: Graphs")
       print("6: hash ")
       print("7: Quite")
       print("---------------------------------------------------------------------------------")
       print("---------------------------------------------------------------------------------")
       First_input = int(input("Enter ther Number !! "))
       print("---------------------------------------------------------------------------------")
       if First_input == 1:
           while True:
                print("---------------------------------------------------------------------------------")
                print("Which LinkedList You wanna Play !!")
                print("---------------------------------------------------------------------------------")
                print("---------------------------------------------------------------------------------")
                print("1: Single Linked List")
                print("2: Double Linked List")
                print("3: Circular Linked List")
                print("4: Quite")
                print("---------------------------------------------------------------------------------")
                print("---------------------------------------------------------------------------------")
                sec_LL_input = int(input("Enter the Number !! "))
                print("---------------------------------------------------------------------------------")
                if sec_LL_input == 1:
                    list = SingleLL.SingleLinkedList()
                    list.create_list() 
                    while True:
                        print("---------------------------------------------------------------------------------")
                        print("1.Display List")
                        print("2. Count the Number of Nodes")
                        print("3.Search for an element")
                        print("4.Insert in an Empty List/Insert at the begging of the list")
                        print("5.Insert a Node at the end of the List")
                        print("6.Insert a node after a specific Node")
                        print("7.Insert a node before a specific Node")
                        print("8.Insert a node at a given Possition")
                        print("9.Delete First Node")
                        print("10.Delete last Node")
                        print("11.Delete any Node")
                        print("12.Reverse a List")
                        print("13.Bubble sort by exchanging Data")
                        print("14. Bubble sort by exchanging Links")
                        print("15.Merge sort")
                        print("16.Insert cycle")
                        print("17.Detect cycle")
                        print("18.Remove cycle")
                        print("19.Quite")
                        print("---------------------------------------------------------------------------------")
                        print("---------------------------------------------------------------------------------")
                        SLL_option = int (input("Enter Your Choice !! "))
                        print("---------------------------------------------------------------------------------")
                        if SLL_option == 1 :
                          list.display_list()
                        elif SLL_option == 2:
                          list.count_node()
                        elif SLL_option == 3:
                          data = int(input("Enter the Number want to search !! "))
                          list.search(data)
                        elif SLL_option == 4:
                          node_0= int(input("Enter the Node want to Insert !! "))
                          list.insert_in_beggning(node_0)
                        elif SLL_option == 5:
                          node_1 = int(input("Enter the Node want to be Inserted !! "))
                          list.insert_at_end(node_1)
                        elif SLL_option == 6:
                          x_0 = int(input("Enter the Node Where You want to !! "))
                          node_2 = int(input("Enter the Node want to be Inserted !! "))
                          list.insert_after(node_2,x_0)
                        elif SLL_option == 7:
                          x_1 = int(input("Enter the Node Where You want to !! "))
                          node_3 = int(input("Enter the Node want to be Inserted !! "))
                          list.insert_before(node_3,x_1)
                        elif SLL_option == 8:
                          x_2 = int(input("Enter the Possition Node Where You want to !! "))
                          node_4 = int(input("Enter the Node want to be Inserted !! "))
                          list.insert_at_possition(node_4,x_2)
                        elif SLL_option == 9:
                          list.delete_first_node()
                        elif SLL_option == 10:
                          list.delete_last_node()
                        elif SLL_option == 11:
                          node_5 = int(input("Enter the Node wanna Delete !! "))
                          list.delete_node(node_5)
                        elif SLL_option == 12:
                          list.reverse_list()
                        elif SLL_option == 13:
                          list.bubble_sort_exdata()
                        elif SLL_option == 14:
                          list.bubble_sort_exlink()
                        elif SLL_option == 15:
                          list.merge_sort()
                        elif SLL_option == 16:
                          data = int(input("Enter The Node where You wanna form a cycle !! "))
                          list.insert_cycle(data)
                        elif SLL_option == 17:
                          list.has_cycle()
                        elif SLL_option == 18:
                          list.remove_cycle()
                        elif SLL_option == 19:
                          break
                        else:
                          print("Please Make a valide choice between 1-19")
                        print()
                elif sec_LL_input == 2:
                  dlist = DoubleLL.DoubleLinkedList()
                  dlist.create_list()
                  while True:
                    print("---------------------------------------------------------------------------------")
                    print("1.Display List") 
                    print("2.Insert In empty List")
                    print("3.insert a node in the begining of the list")
                    print("4.Insert a node in the end of the list")
                    print("5.Insert a node after a specific node")
                    print("6.Insert a node before a specific node")
                    print("7.Delete First node")
                    print("8.delete last Node")
                    print("9.Delete any node")
                    print("10.Reverse a list") 
                    print("11.Quite")
                    print("---------------------------------------------------------------------------------")
                    print("---------------------------------------------------------------------------------")

                    DLL_option = int(input("Enter Your Choice !! ")) 
                    print("---------------------------------------------------------------------------------")
                    if DLL_option == 1:
                      dlist.Display_List()
                    elif DLL_option == 2:
                      data = int(input("Enter the value want to insert !! ")) 
                      dlist.insert_in_empty_list(data)
                    elif DLL_option == 3:
                      data = int(input("Enter the value want to insert !! "))
                      dlist.insert_in_begining(data)
                    elif DLL_option == 4:
                      data = int(input("Enter the value want to insert !! "))
                      dlist.insert_at_end(data)
                    elif DLL_option == 5:
                      data = int(input("Enter the value want to insert !! "))
                      x = int(input("Enter the possition !! "))
                      dlist.insert_after(data,x)
                    elif DLL_option == 6:
                      data = int(input("Enter the value want to insert !! "))
                      x = int(input("Enter the possition !! "))
                      dlist.insert_before(data,x)
                    elif DLL_option == 7:
                      dlist.delete_first_node()
                    elif DLL_option == 8:
                      dlist.delete_last_node()
                    elif DLL_option == 9:
                      x = int(input("Enter the node want to be deleted !! "))
                      dlist.delete_node(x)
                    elif DLL_option == 10:
                      dlist.reverse_list()
                    elif DLL_option == 11:
                      break
                    else:
                      print("Please Enter a Valide Number between 1-11 ") 
                    print()
                elif sec_LL_input == 3:
                  clist = CircularLL.CircularLinkedList()
                  clist.create_list()
                  while True:
                    print("---------------------------------------------------------------------------------")
                    print("1.Display list !! ")
                    print("2.Insert a node in a empty list !! ")
                    print("3.Insert a node in a begining of the list !! ")
                    print("4.Insert a node in the ende of the list !! ")
                    print("5.Insert a node after a specific node !! ")
                    print("6.Delete first node !! ")      
                    print("7.Delete last node !! ")
                    print("8.Delete any node !! ")
                    print("9.Quite ")
                    print("---------------------------------------------------------------------------------")
                    print("---------------------------------------------------------------------------------")
                    CLL_input = int(input("Choose the option !! "))
                    print("---------------------------------------------------------------------------------")
                    if CLL_input == 1:
                      clist.Display_list()
                    elif CLL_input == 2:
                      data = int(input("Enter the node wanna inserted !! "))
                      clist.insert_in_empty_list(data)
                    elif CLL_input == 3:
                      data = int(input("Enter the node wanna inserted !! "))
                      clist.insert_in_begining(data)
                    elif CLL_input == 4:
                      data = int(input("Enter the node wanna inserted !! "))
                      clist.inset_at_end(data)
                    elif CLL_input == 5:
                      data = int(input("Enter the node wanna inserted !! "))
                      x = int(input("Enter the possition !! "))
                      clist.insert_after(data,x)
                    elif CLL_input == 6:
                      clist.delete_first_node()
                    elif CLL_input == 7:
                      clist.delete_last_node()
                    elif CLL_input == 8:
                      x = int(input("Enter the node wanna delete !! "))
                      clist.delete_node(x)
                    elif CLL_input == 9:
                      break
                    else:
                      print("Please choose a valide option between 1-9 !! ")
                    print()
                elif sec_LL_input == 4:
                  break
                else:
                  print("Please choose a valide option between 1-4 !! ")


                         
                        