"""
Find Cost of Tile to Cover W x H Floor –
Calculate the total cost of tile it would take to cover a floor plan of
width and height, using a cost entered by the user.
"""


def cost_to_cover(width, height, price_pm):
    """
    :param width:
    :param height:
    :param price_pm:
    :return:
    """
    return width * height * price_pm


print(cost_to_cover(50, 100, 0.5))


def find_max_comb(seq):
    """
    Find max combination of 2 numbering in a sequence - n^2
    """
    temp = 0
    for i, num in enumerate(seq):
        for y_axis in seq[i + 1:]:
            temp = max(temp, num + y_axis)
    return temp


print(find_max_comb([1, 7, 3, 1, 3, 5, 4]))
