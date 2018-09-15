class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
    
    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node
     
    def printAllValues(self, msg=""):
        runner = self.head          # create a runner     
        print("\n\nhead points to ", id(self.head))
        print("Printing the values in the list ---", msg,"---")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next        
        print(id(runner), runner.value, id(runner.next))t 
        runner.next = node

    def removeNode(self,value):
        if target==head:
            head.next = self.head
            target.next = None
        return(self)
        
    def removeFront(self,value):
        if self.head = None:
            return None
        else:
            temp = self.head
            self.head=self.head.next
            return temp