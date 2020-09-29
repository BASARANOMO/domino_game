"""
@Author: ZHANG Mofan
@Time: 09/28/2020 13:45-15:00

@Author2: XIE Ruiling
"""


def dominoes(int_couple_list):
    """ Display a list of dominoes

    Parameters
    ----------
    int_couple_list: list of dominoes (couples of integers)

    Returns
    -------

    """
    for idx in range(len(int_couple_list)):
        domino_str = domino_convert(int_couple_list[idx])
        domino_display(domino_str, idx+1)
    return


def domino_convert(int_couple):
    """ This method is used to convert a couple of integers to a string display

    Parameters
    ----------
    int_couple: tuple-like, a couple of integers, each between 0 and 6 (inclusive)

    Returns
    -------
    domino_str: list of lists, list having 2 elements, each element for one integer

    """
    domino_str = []
    str_list = [' '*5, ' '*5, '*    ', '    *', '*   *', '*   *', '* * *', '* * *']
    for num in int_couple:
        if (num & 1) == 0: # even number
            # num_str: list of strings, representing 3 lines of a display
            # num_str corresponds to the display of one integer of the domino
            num_str = [str_list[num], ' '*5, str_list[num+1]]
        else: # odd number
            num_str = [str_list[num-1], '  *  ', str_list[num]]
        domino_str.append(num_str) # num_str is element of domino_str
    return domino_str


def domino_display(domino_str, idx):
    """ Display one domino

    Parameters
    ----------
    domino_str: display of the domino
    idx: index of the domino

    Returns
    -------

    """
    index_part = [' '*3, f'({idx})', ' '*3]
    print(" "*3+"+-----|-----+")
    for i in range(3):
        print(index_part[i]+"|{}|{}|".format(domino_str[0][i], domino_str[1][i]))
    print(" "*3+"+-----|-----+")
    return

# Test
# dominoes([(1,2), (3,4), (5,6), (0,0)])
