def decorator_function(func):
    def inner_function():
        print('I got decorated!')
        func()
    return inner_function

@decorator_function  #decorator tag, In simple terms decorator function adds additional functionality to a function already present.
def simple_function():
    print('I am simple function.')
    
simple_function()