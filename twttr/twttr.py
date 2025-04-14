s = input("Input: ").strip()
print ("Output: ", end="")

for c in s:
    if c.lower() not in ['a', 'e', 'i', 'o', 'u']:
        print(c, end = "")
print()
