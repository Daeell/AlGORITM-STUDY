from heapq import heappush, heappop

class DoublyHeapq:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.length = 0
    
    def insert(self, val):
        heappush(self.maxHeap, -val)
        heappush(self.minHeap, val)
        self.length += 1
    
    def deleteMax(self):
        if self.length == 0:
            return
        
        heappop(self.maxHeap)
        self.length -= 1
        
        if self.length <= 1:
            while len(self.minHeap) > 0:
                heappop(self.minHeap)
                
        if self.length == 1:
            heappush(self.minHeap, -self.maxHeap[0])
    
    def deleteMin(self):
        if self.length == 0:
            return
        
        heappop(self.minHeap)
        self.length -= 1
        
        if self.length <= 1:
            while len(self.maxHeap) > 0:
                heappop(self.maxHeap)
        
        if self.length == 1:
            heappush(self.maxHeap, -self.minHeap[0])
    
    def showMaxAndMin(self):
        if self.length == 0:
            return (0, 0)
        
        return (-heappop(self.maxHeap), heappop(self.minHeap))

    
def solution(operations):
    heap = DoublyHeapq()
    
    for operation in operations:
        command, val = operation.split()
        if command == 'I':
            heap.insert(int(val))
        else:
            if val == '1':
                heap.deleteMax()
            else:
                heap.deleteMin()
    
    return heap.showMaxAndMin()