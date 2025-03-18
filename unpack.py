
def f(a,b):
    print(a, b)


A=[88]
B={ "b":99}
f(*A,  **B)

C={"b":102, "a":99}
f(**C)

f(a=111, b=222)

D=[1,2]
f(*D)
