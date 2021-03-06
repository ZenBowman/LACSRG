## 11/18/2012
## Prasan Samtani
## ZenBowman@gmail.com

def parent(i):
    return i/2
def left(i):
    return 2*i
def right( i):
    return (2*i)+1

class Heap:
    def __init__(self, data):
        self.data = ["IntentionalBlank"] + data

    def max_heapify(self, i):
        l = left(i)
        r = right(i)
        largest = i
        if (l < len(self.data)) and (self.data[l] > self.data[i]):
            largest = l
        if (r < len(self.data)) and (self.data[r] > self.data[largest]):
            largest = r

        if (largest != i):
            tmp = self.data[i]
            self.data[i] = self.data[largest]
            self.data[largest] = tmp
            self.max_heapify(largest)
