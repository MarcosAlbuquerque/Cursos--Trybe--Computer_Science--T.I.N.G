class Queue:
    queue = []

    def __init__(self):
        self.queue.clear()
        self.queue

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        return self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def search(self, index):
        if index >= 0 and index < len(self.queue):
            return self.queue[index]
        raise IndexError()
