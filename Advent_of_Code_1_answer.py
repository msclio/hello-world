
'''
This function takes a list as input and outputs the product of the two entries
that add up to 2020. I named my variables "expense_entries" for the list of
numbers that the user provides, and "multiplied" for the product of the two
numbers adding up to 2020, but you can rename these variables if you'd like.

Some example lists to try copy-pasting as user input are at the bottom of
this file.
'''

def main():
    expense_list = [1483, 1193, 1213, 1692, 1589, 1840, 1544, 2009, 305, 1493, 702, 251, 1568,
1382, 1170, 1273, 96, 146, 324, 1992, 602, 1262, 922, 1805, 1968, 561, 44,
1837, 1545, 1017, 1153, 1131, 1244, 1969, 677, 602, 1953, 1057, 709, 239, 911,
1384, 864, 1408, 295, 1066, 396, 311, 1941, 156, 1538, 1016, 557, 455, 1238,
1940, 296, 965, 272, 1514, 1993, 1249, 497, 1103, 1084, 171, 1521, 753, 1208,
1452, 1590, 1319, 464, 702, 473, 438, 910, 1298, 609, 627, 1314, 1286, 944,
1700, 1580, 654, 872, 1720, 1651, 1186, 999, 581, 990, 631, 1626, 1664, 111,
1667, 1841, 501]
    answer = report_repair(expense_list)
    print("The answer is " + str(answer))

def report_repair(expense_entries):
    multiplied = 0
    i = 0
    j = 0
##    count = [0]
##
##    for k in range(len(expense_entries)):
##        for l in range(len(expense_entries)):
##            if expense_entries[k] + expense_entries[l] == 2020:
##                count[0] += 1
##                count.append(k)
##                count.append(l)

    while multiplied == 0:
        if i != j and expense_entries[i] + expense_entries[j] == 2020:
            multiplied = expense_entries[i] * expense_entries[j]
        else:
            i += 1
            if i == len(expense_entries):
                i = 0
                j += 1

##    print(count)
    return multiplied

main()



'''
Example lists to input and try:

[199,346,1258,639,2002,567,298,547,394,278,985,398,824,1987,1563,1381]

answer = 882459

[1382, 1908, 610, 415, 36, 702, 1825, 575, 443, 1181, 1855, 1175, 1951,
579, 1413, 1910, 966, 2018, 1750, 132, 1651, 1092, 225, 1367, 1354, 268,
1668, 360, 161, 1060, 1072, 864, 261, 652, 1535, 346, 1446, 1842, 1148,
701, 1128, 662, 1057, 331, 904, 344, 84, 120, 1424, 1562, 530, 1233, 1020,
244, 1645, 431, 1475, 360, 721, 340, 838, 1324, 1904, 1427, 715, 737, 1217,
1756, 298, 65, 1504, 931, 242, 1589, 1504, 420, 1976, 1179, 300, 1908, 926, 879,
1323, 586, 1366, 1377, 902, 411, 691, 507, 1963, 59, 949, 1242, 365,
472, 1457, 608, 712]

answer = 986611

[1483, 1193, 1213, 1692, 1589, 1840, 1544, 2009, 305, 1493, 702, 251, 1568,
1382, 1170, 1273, 96, 146, 324, 1992, 602, 1262, 922, 1805, 1968, 561, 44,
1837, 1545, 1017, 1153, 1131, 1244, 1969, 677, 602, 1953, 1057, 709, 239, 911,
1384, 864, 1408, 295, 1066, 396, 311, 1941, 156, 1538, 1016, 557, 455, 1238,
1940, 296, 965, 272, 1514, 1993, 1249, 497, 1103, 1084, 171, 1521, 753, 1208,
1452, 1590, 1319, 464, 702, 473, 438, 910, 1298, 609, 627, 1314, 1286, 944,
1700, 1580, 654, 872, 1720, 1651, 1186, 999, 581, 990, 631, 1626, 1664, 111,
1667, 1841, 501]

answer = 22099
'''
