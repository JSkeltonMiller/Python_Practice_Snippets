import operator


dict1 = {}

def sortTriples(newList):  # make a dictionary with each triple as a tuple matched with the area
    for trl in newList:
        a = int(trl[0])
        b = int(trl[1])
        c = int(trl[2])
        test1 = str(a) +','+ str(b) +','+ str(c)
        dict1[test1] = a * b * .5

    sorted_dict1 = sorted(dict1.items(), key =operator.itemgetter(0), reverse = True)
    final_sorted = [triplet[0] for triplet in sorted_dict1]
    return final_sorted



sample = [(4, 3, 5), (12, 5, 13), (15, 8, 17)]
for triplet in sortTriples(sample):
    print triplet[0]

"""Desired Output:
[(4,3,5), ...etc. Pythagorean triple format
[("""