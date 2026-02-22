
x = 5
print(f"{x:5}")   # min width = 5

x = 5

print(f"{x:<5}")   # left
print(f"{x:>5}")   # right
print(f"{x:^5}")   # center

x = 5

print(f"{x:*<5}")
print(f"{x:*>5}")
print(f"{x:*^5}")

#       012345
text = "HelloWorld"

print(f"{text:.5}")
print(f"{text[:5]}")

x = 42
print(f"{x:05}")

x = 10
y = -10

print(f"{x:+}")
print(f"{y:+}")

pi = 3.1415926

print(f"{pi:.2f}")
print(f"{pi:.4f}")

pi = 3.14159

print(f"{pi:8.2f}")

n = 123456789

print(f"{n:,}")

ratio = 0.375

print(f"{ratio:.2%}")