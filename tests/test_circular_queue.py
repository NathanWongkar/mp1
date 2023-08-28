
from questions.circular_queue import MyCircularQueue

def test_basic_functionality():
    queue = MyCircularQueue(3)
    
    assert queue.enQueue(1) == True
    assert queue.enQueue(2) == True
    assert queue.enQueue(3) == True
    assert queue.enQueue(4) == False  # Queue is full now
    
    assert queue.Rear() == 3
    assert queue.isFull() == True
    
    assert queue.deQueue() == True
    assert queue.enQueue(4) == True
    assert queue.Rear() == 4

def test_empty_queue():
    queue = MyCircularQueue(3)
    
    assert queue.isEmpty() == True
    assert queue.Front() == -1
    assert queue.Rear() == -1

def test_full_queue():
    queue = MyCircularQueue(2)
    
    assert queue.enQueue(1) == True
    assert queue.enQueue(2) == True
    assert queue.enQueue(3) == False  # Should fail since the queue is full
    
    assert queue.isFull() == True
    
    assert queue.deQueue() == True
    assert queue.isFull() == False

def test_dequeue_empty():
    queue = MyCircularQueue(3)
    
    # Attempting to dequeue from an empty queue should return False
    assert queue.deQueue() == False

def test_circular_behavior():
    queue = MyCircularQueue(3)
    
    assert queue.enQueue(1) == True
    assert queue.enQueue(2) == True
    assert queue.enQueue(3) == True
    assert queue.deQueue() == True  # Remove 1
    assert queue.enQueue(4) == True
    
    assert queue.Front() == 2
    assert queue.Rear() == 4
    
    # Making sure the queue behaves in a circular fashion
    assert queue.deQueue() == True  # Remove 2
    assert queue.deQueue() == True  # Remove 3
    assert queue.enQueue(5) == True
    assert queue.enQueue(6) == True
    
    assert queue.Front() == 4
    assert queue.Rear() == 6

