#Two examples of Decorators.

# One (Converts array of strings to camelCase strings!)
def deco_camelcase(func):

    def inner(list_of_values):

        return [func(string) for string in list_of_values]
    return inner

@deco_camelcase
def camelcase(string):

    string = ''.join(one.capitalize() for one in string.split('_'))
    return string

names = [
    "hello_world",
    "with_name",
    "snoop_dogg"
]


# Two (Converts a unsecure function to secure!)

def secure_function(func):

    def inner(key, pwd=None):
        if pwd == "hello":
            return func(key)
        else:
            return "Not allowed to access!!!"
    
    return inner

@secure_function
def unsecure_function(key):

    dict_val = {
        "rohan" : 8799118910,
        "mohan" : 1234987543,
        "Sodhan" : 9876543210
    }
    if key in dict_val:
        return dict_val[key]
    else:
        return "Not found"
