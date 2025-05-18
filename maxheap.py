class heap_node:
    def __init__(self,ID,priority):
        self.id = ID
        self.priority = priority
class heap:
    def __init__(self):
        self.arr = [None]
        self.size = 0

    def swap(self , index1 , index2):
        temp = self.arr[index1]
        self.arr[index1] = self.arr[index2]
        self.arr[index2] = temp

    def max_heapify(self,index):
        left = 2 * index
        right = left + 1
        if left <= self.size and self.arr[left].priority > self.arr[index].priority:
            maximum_index = left
        else:
            maximum_index = index
        if right <= self.size and self.arr[right].priority >  self.arr[maximum_index].priority:
            maximum_index = right

        if maximum_index != index:
            self.swap(index , maximum_index)
            self.max_heapify(maximum_index)
            
    def increase_priority(self,ID,new_priority):
        index = None
        for i in range (1, self.size + 1):
            if ID == self.arr[i].id:
                index = i
        if index == None or self.arr[index].priority > new_priority:
            return
        else:
            self.arr[index].priority = new_priority
        parent = index // 2
        while index > 1 and self.arr[parent].priority < self.arr[index].priority:
            self.swap(index,parent)
            index = parent
            parent = index // 2

    def insert(self,id,priority):
        new_node = heap_node(id,priority)
        self.arr.append(new_node)
        self.size += 1
        index = self.size
        parent = index // 2
        while index > 1 and self.arr[parent].priority < self.arr[index].priority:
            self.swap(index,parent)
            index = parent
            parent = index // 2        
    
    def delete_maximum(self):
        if self.size == 0:
            return 
        maximum = self.arr[1]
        self.arr[1] = self.arr[self.size]
        self.arr.pop()
        self.size -= 1
        self.max_heapify(1)
        return maximum

    def process(self, bst=None):
        processed_node = self.delete_maximum()
        if processed_node and bst:
            bst.delete(processed_node)
        return processed_node
    
    def delete_by_id(self, ID):
        index = None
        for i in range (1, self.size + 1):
            if ID == self.arr[i].id:
                index = i
        if index == None:
            return
        self.arr[index] = self.arr[self.size]
        self.arr.pop()
        self.size -= 1
        self.max_heapify(index)
        parent = index // 2
        while index > 1 and self.arr[parent].priority < self.arr[index].priority:
            self.swap(index,parent)
            index = parent
            parent = index // 2 
        
    def level_order(self):
        for node in self.arr[1:]:
            print("ID:", node.id, '   priority:',node.priority)
        
    
    

            

