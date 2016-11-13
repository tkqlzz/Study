class MaxHeap:
    def __init__(self):
        self.heapList = []

    def push(self, data):
        self.heapList.append(data)
        current = len(self.heapList) - 1
        parent = current - 1 >> 1
        self._siftDown(current, parent)

    def _siftDown(self, current, parent):  # current 에서 parent까지 체크, 변경
        while current > abs(parent):
            if self.heapList[current] > self.heapList[parent]:
                self._change(current, parent)
                current = parent
                parent = (parent - 1) >> 1
                continue
            break

    def pop(self):
        last = self.heapList.pop()
        if self.heapList:
            item = self.heapList[0]
            self.heapList[0] = last
            self._siftUp(0)
            return item
        return last

    def _siftUp(self, parent):  # parent 마지막 leaf 까지 한칸식 변경
        size = len(self.heapList)
        child = parent * 2 + 1
        while child < size:
            sibling = child + 1
            if sibling < size and self.heapList[child] < self.heapList[sibling]:
                child = sibling
            if self.heapList[child] > self.heapList[parent]:
                self._change(child, parent)
            else:
                break
            parent = child
            child = parent * 2 + 1

    def _change(self, child, parent):
        temp = self.heapList[child]
        self.heapList[child] = self.heapList[parent]
        self.heapList[parent] = temp

    def buildHeap(self, newList):
        self.heapList = newList
        for i in reversed(range(len(newList) // 2)):  # (마지막레벨-1.끝노드) ~ 루트까지
            self._siftUp(i)

    def sort(self):
        size = len(self.heapList)
        return [self.pop() for i in range(size)]


def arrPreorder(arr, i=0):
    if len(arr) > i:
        print(arr[i], end=" ")
        arrPreorder(arr, i * 2 + 1)
        arrPreorder(arr, i * 2 + 2)


def arrInorder(arr, i=0):
    if len(arr) > i:
        arrInorder(arr, i * 2 + 1)
        print(arr[i], end=" ")
        arrInorder(arr, i * 2 + 2)


def arrPostorder(arr, i=0):
    if len(arr) > i:
        arrPostorder(arr, i * 2 + 1)
        arrPostorder(arr, i * 2 + 2)
        print(arr[i], end=" ")


def arrShowTree(arr, i=0, depth=0):
    if len(arr) > i:
        arrShowTree(arr, i*2+2, depth+1)
        print(("   " * depth) + str(arr[i]))
        arrShowTree(arr, i*2+1, depth + 1)