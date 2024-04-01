'''
Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

Use conditionals to return the proper message:

case	return
name equals owner	'Hello boss'
otherwise	'Hello guest'

'''

def greet(name: str, owner: str) -> str:
    '''

    :param name: Person to greet
    :param owner: Person who owns?
    :return: A greeting
    '''
    return f"Hello {'boss' if name == owner else 'guest'}"