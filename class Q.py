class Queue:
    def __init__(self): #self is used as a subtitute of this
        self.items = []
        
    def is_empty(self):
            return len (self.items) == 0
        
    def enqueue(self,item):
            self.items.append(item)
            
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is Empty.")
                
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("queue is empty")
                
    def size(self):
        return len(self.items)
                
my_queue=Queue()
my_queue.enqueue[1]
my_queue.enqueue[2]                     
my_queue.enqueue[3]
                
print("Queue Front",my_queue.front())
print("Queue size" , my_queue.size ())
                
while not my_queue.is_empty():
    print("Dequeue", my_queue.dequeue())