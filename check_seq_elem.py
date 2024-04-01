'''
You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

Array can contain numbers or strings. X can be either.

Return true if the array contains the value, false if not.
'''

def check(seq: list, elem: [str | int]) -> bool:
    '''
    Checks if element exist in giben sequence
    :param seq: list to check
    :param elem: element to look for.
    :return: True if element exists in sequence, else False.
    '''
    return elem in seq