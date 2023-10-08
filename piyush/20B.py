n = int(input("Enter the value of n: "))  # Input the value of 'n'
result = {}

for x in range(1, n + 1):
    result[x] = x * x

print("Dictionary (n={}):".format(n))
print(result)