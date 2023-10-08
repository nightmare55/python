#Write a python script to generate Fibonacci terms using generator function
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Create a generator object
fibonacci_gen = fibonacci_generator()

# Generate and print the first 10 Fibonacci terms
for i in range(10):
    fib_term = next(fibonacci_gen)
    print(fib_term)
