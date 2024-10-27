# Implement the FIFO queue manager using an in-memory queue with an arbitrary max size
# It contains helpful functions for managing the queue

from collections import deque
from .customer import Customer

class OrderQueueManager:
    def __init__(self, max_orders=10):
        self.queue = deque(maxlen=max_orders)

    def add_order(self, customer_data):
        if len(self.queue) >= self.queue.maxlen:
            raise OverflowError("The FIFO queue is full.")
        self.queue.append(customer_data)
    
    def get_next_order(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            raise IndexError("The FIFO queue is empty.")

    def queue_size(self):
        return len(self.queue)