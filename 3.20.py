class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return min_val

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def _bubble_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] > self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break

    def _bubble_down(self, index):
        while index < len(self.heap):
            left_child_idx = 2 * index + 1
            right_child_idx = 2 * index + 2
            min_idx = index

            if left_child_idx < len(self.heap) and self.heap[left_child_idx] < self.heap[min_idx]:
                min_idx = left_child_idx
            if right_child_idx < len(self.heap) and self.heap[right_child_idx] < self.heap[min_idx]:
                min_idx = right_child_idx

            if min_idx != index:
                self.heap[min_idx], self.heap[index] = self.heap[index], self.heap[min_idx]
                index = min_idx
            else:
                break


# Example usage:
if __name__ == "__main__":
    heap = MinHeap()
    heap.push(5)
    heap.push(3)
    heap.push(7)
    heap.push(10)
    heap.push(9)

    print("Heap after pushing elements:", heap.heap)

    print("Peek:", heap.peek())

    print("Popped:", heap.pop())
    print("Heap after popping:", heap.heap)
