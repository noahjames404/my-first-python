#lambdas are small anonymous functions
#A lambda function can take any number of arguments, but can only have one expression.
#w3schools/python

hello = lambda name : "hello " + name

print(hello("noah"))

def complicated_task(x):
    print(x(300))


complicated_task(lambda n: n + 10)
