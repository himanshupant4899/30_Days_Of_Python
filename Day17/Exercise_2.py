#Create a function that accepts any number of positional and keyword arguments, and that prints them
#back to the user.Your output should indicate which values were provided as positional arguments,
#and which were provided as keyword arguments.

def foo(*args, **kwargs):
    print(f'positional args: {args}')
    print(f'positional args: {kwargs}')

foo(1,2,"hello",3,4,a=5,b=6)