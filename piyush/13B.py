# Initialize an empty list to represent the queue
queue = []

# Function to enqueue (add) an element to the queue
def enqueue(item):
    queue.append(item)
    print(f"Enqueued: {item}")

# Function to dequeue (remove and return) an element from the queue
def dequeue():
    if not is_empty():
        item = queue.pop(0)
        print(f"Dequeued: {item}")
        return item
    else:
        print("Queue is empty.")
        return None

# Function to check if the queue is empty
def is_empty():
    return len(queue) == 0

# Function to display the elements in the queue
def display_queue():
    if not is_empty():
        print("Queue elements:", queue)
    else:
        print("Queue is empty.")

# Example usage
enqueue(1)
enqueue(2)
enqueue(3)
display_queue()
dequeue()
display_queue()