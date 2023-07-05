
# def collatz(n):
#     root = [n]
#     while n != 1:
#         n = int(n/2) if n%2==0 else 3*n+1
#         root.append(n)
#     return root

def collatz(n):
    return [n] + collatz(int(n/2)) if n%2==0 else [n] + collatz(3*n+1) if n != 1 else [1]


# example
print(collatz(100))



