expression = input("Expression: ")

if '+' in expression:
    x, y = expression.split("+")
    z= float(x) + float(y)
    print (z)

elif '-' in expression:
    x, y = expression.split("-")
    z= float(x) - float(y)
    print (z)

elif '*' in expression:
    x, y = expression.split("*")
    z= float(x) * float(y)
    print (z)

elif '/' in expression:
    x, y = expression.split("/")
    z= float(x) / float(y)
    print (z)
