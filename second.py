import typing_extensions


name = "motaz"
age = 17
rank = 190
a, b, c =10, 20, 30

print(f"Hello my name is {name} and my age is {age} and finally my rank is {rank}")

print("Hello my is {} and my age is {} and finally my rank is {}".format(name,age,rank))

print("Heloo test {} {} {}".format(a, b, c))

print(f"Hello test {1:d} {2:d} {0:d}".format(a, b, c))

print("Hello test {2:.1f} {1:.2f} {0:.1f}".format(a, b, c))

mymoney = 500623501980

print("my money in bank is: {:d}".format(mymoney))
print("my money in bank is: {:,d}".format(mymoney))
print("my money in bank is: {:_d}".format(mymoney))

print(f"Hello my name is: {name} and my age is: {age} and my rank is: {rank}")

k = "I love python and php"
m = "motaz"

print(m.center(9,"#"))

