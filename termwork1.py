a, b, c = map(float, input("Enter 3 Integer which are sides Triangle : ").split())
print(f"a={a}, b={b}, c={c}")

#to check triangle or not triangle 

if a < b + c and b < a + c and c < a + b:
    is_triangle = 'yes'
else:
    is_triangle = 'no'

if is_triangle == 'yes':

    if a == b and b==c:
        print("equlateral triangle")
    elif a != b and a != c and b != c: 
        print("scalene triangle")

    else:
        print("isosceles Triangle")
else:
    print("triangle cant not form")

