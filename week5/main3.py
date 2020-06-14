from common import print_tour, read_input, format_tour
import math

def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def change(result):
    for i in range(n-1):
        a,b,c = tour[result[i-1]],tour[result[i]],tour[result[i+1]]
        for j in range(i+2,n-1):
            d,e,f = tour[result[j-1]],tour[result[j]],tour[result[j+1]]
            if  distance(a,b) + distance(b,c) + distance(d,e) + distance(e,f) > distance(a,e) + distance(e,c) + distance(d,b) + distance(b,f):
                result[i],result[j] = result[j],result[i]
                print(i,j)
                return result, True
    return result, False



k = 6

result = [1959, 577, 1336, 932, 1827, 202, 362, 1160, 411, 1455, 1225, 739, 341, 1107, 780, 1451, 884, 1105, 534, 1271, 1270, 1748, 457, 854, 232, 847, 1727, 1769, 975, 56, 13, 131, 28, 468, 904, 1760, 84, 511, 1281, 1226, 1536, 557, 1408, 1274, 257, 1647, 1936, 1186, 833, 805, 418, 617, 70, 371, 1458, 947, 590, 1763, 1074, 1261, 1313, 784, 338, 924, 1399, 1726, 995, 553, 1413, 314, 323, 1053, 1481, 1918, 1294, 834, 1689, 171, 839, 1070, 517, 1121, 1860, 1807, 710, 959, 1376, 575, 1008, 796, 1881, 1558, 1916, 1236, 1346, 845, 963, 10, 772, 365, 1161, 1549, 1298, 1291, 1470, 1170, 1174, 1457, 1969, 825, 1416, 576, 36, 531, 843, 994, 966, 803, 1687, 770, 1259, 1339, 301, 599, 726, 1508, 568, 636, 1843, 217, 909, 1432, 1673, 1595, 1920, 50, 1295, 674, 388, 1424, 1093, 1588, 878, 1520, 1381, 771, 1497, 1891, 1208, 244, 693, 677, 1825, 669, 1355, 290, 119, 1794, 706, 350, 1386, 764, 1962, 395, 2039, 135, 1119, 72, 130, 680, 227, 1984, 1940, 393, 1400, 1921, 360, 1722, 903, 1833, 1988, 1453, 1476, 1144, 1148, 1014, 823, 1978, 1973, 615, 744, 1709, 2022, 1392, 819, 1264, 981, 1548, 1758, 0, 1994, 1762, 859, 563, 891, 417, 509, 355, 1606, 1776, 734, 1484, 79, 299, 8, 1179, 1573, 812, 1340, 359, 1152, 741, 1128, 580, 1830, 87, 752, 1541, 1243, 175, 2043, 1354, 1129, 1734, 765, 474, 1752, 364, 136, 1642, 682, 1000, 1046, 486, 912, 1177, 1785, 704, 1180, 666, 1728, 1102, 321, 1341, 1494, 562, 100, 1927, 587, 1839, 1615, 86, 156, 943, 2024, 671, 1680, 1618, 721, 420, 219, 1169, 1510, 1743, 458, 1168, 60, 875, 583, 1207, 127, 164, 1162, 675, 2020, 1900, 1903, 756, 935, 391, 1824, 1795, 311, 453, 1483, 802, 1884, 1992, 600, 1655, 1848, 1725, 1907, 1967, 1357, 993, 2012, 992, 1172, 1052, 627, 1095, 1532, 1201, 303, 497, 2011, 410, 470, 367, 1044, 1638, 207, 1480, 1165, 1710, 1415, 1649, 1798, 1888, 505, 746, 499, 566, 1981, 238, 1182, 312, 1414, 957, 958, 231, 529, 631, 134, 109, 667, 1637, 96, 81, 1477, 1247, 146, 1679, 1659, 1600, 57, 965, 1883, 985, 596, 293, 445, 1952, 1529, 1861, 1801, 1435, 885, 30, 66, 166, 1054, 1720, 117, 694, 1167, 565, 64, 632, 1488, 810, 2006, 1756, 337, 1322, 1587, 77, 1879, 1209, 216, 601, 1289, 427, 921, 1245, 696, 644, 653, 1782, 1653, 1173, 1525, 297, 1559, 204, 1970, 1887, 76, 1390, 310, 1865, 683, 1650, 1496, 373, 1715, 245, 1853, 322, 1154, 1184, 1311, 98, 1120, 139, 1222, 1511, 1972, 1790, 1802, 940, 1575, 163, 1327, 889, 1404, 725, 662, 400, 248, 339, 887, 971, 504, 1545, 2037, 733, 226, 942, 433, 848, 1845, 773, 867, 1733, 102, 1989, 898, 923, 385, 610, 1372, 1949, 1441, 607, 1736, 1278, 974, 702, 1862, 679, 487, 1292, 896, 501, 520, 212, 1913, 1885, 1393, 890, 1103, 1917, 1231, 1803, 237, 1206, 295, 688, 201, 946, 1204, 523, 1123, 25, 795, 830, 83, 1925, 588, 949, 1198, 121, 508, 526, 1568, 928, 387, 158, 640, 1337, 1227, 1535, 236, 44, 769, 376, 584, 296, 1068, 197, 1268, 16, 670, 549, 12, 1591, 1282, 868, 1939, 1806, 138, 1746, 149, 1275, 496, 551, 1851, 748, 1171, 1106, 2001, 99, 483, 1491, 826, 914, 736, 514, 931, 69, 1304, 871, 853, 892, 1745, 375, 816, 253, 332, 952, 155, 390, 1412, 1791, 1555, 1257, 1519, 1361, 861, 1473, 442, 1540, 637, 1602, 1450, 478, 1886, 1543, 944, 1255, 850, 1819, 15, 906, 288, 1492, 776, 1240, 1060, 1608, 856, 1035, 2036, 870, 1131, 763, 747, 506, 1498, 1043, 1686, 1262, 150, 1688, 1181, 1797, 104, 623, 1816, 1951, 1868, 2002, 2015, 256, 38, 1345, 657, 822, 1611, 838, 277, 650, 114, 1235, 394, 377, 1515, 1792, 1020, 591, 664, 243, 1832, 185, 95, 1086, 53, 727, 1431, 354, 456, 1670, 32, 1566, 564, 874, 266, 1596, 1446, 643, 908, 1966, 283, 1766, 1382, 1896, 882, 1676, 1932, 754, 1630, 1287, 955, 405, 883, 1397, 953, 1912, 507, 1640, 215, 668, 1364, 1088, 933, 828, 570, 633, 82, 1924, 1040, 1628, 1310, 1330, 990, 775, 482, 1136, 1383, 1556, 1963, 1866, 356, 441, 1593, 192, 574, 1826, 638, 718, 199, 1200, 1057, 1195, 14, 1109, 700, 252, 731, 641, 605, 1130, 1027, 1598, 984, 1840, 1420, 1401, 1157, 1489, 801, 1675, 1100, 1425, 798, 7, 1146, 1115, 270, 479, 1454, 452, 791, 707, 2033, 997, 917, 655, 1402, 488, 1096, 1616, 267, 334, 1279, 535, 448, 1439, 1564, 712, 723, 1707, 1856, 573, 1695, 223, 1017, 1870, 396, 1069, 945, 469, 1768, 108, 39, 1820, 42, 285, 1983, 490, 165, 241, 1219, 690, 835, 203, 1318, 1075, 555, 1876, 1892, 1466, 1248, 1919, 33, 282, 292, 461, 1251, 1590, 1149, 1783, 2040, 793, 1931, 646, 720, 1117, 421, 1284, 1434, 74, 1312, 806, 1320, 1430, 1942, 1579, 1316, 618, 345, 855, 1572, 3, 1976, 1438, 1452, 1501, 1500, 1333, 105, 2027, 1935, 785, 319, 681, 294, 1774, 425, 1447, 2018, 1560, 2032, 1315, 1809, 824, 1427, 1813, 278, 1362, 300, 206, 346, 595, 1875, 1953, 1156, 1546, 689, 1212, 1847, 1821, 740, 730, 1230, 1228, 1909, 873, 258, 317, 1199, 937, 1256, 329, 333, 1463, 954, 1754, 893, 383, 697, 1993, 1241, 1667, 246, 444, 973, 1389, 936, 401, 2038, 1388, 502, 1524, 1445, 472, 905, 1202, 1697, 348, 665, 1672, 525, 598, 1083, 1055, 262, 1775, 1614, 1732, 1690, 247, 1218, 169, 624, 1405, 586, 1037, 1210, 378, 1108, 621, 1871, 737, 1857, 956, 2009, 1965, 91, 440, 1301, 176, 858, 1042, 1418, 1613, 221, 1048, 120, 46, 1626, 239, 722, 1730, 1080, 59, 582, 1297, 713, 331, 374, 1641, 1922, 513, 398, 616, 1029, 972, 1269, 1460, 340, 209, 1468, 93, 750, 1479, 876, 450, 200, 1533, 1751, 1403, 1506, 880, 1837, 144, 1739, 2034, 2026, 1567, 1846, 1899, 841, 495, 397, 1474, 1661, 978, 1995, 1059, 1514, 1290, 116, 85, 1140, 1411, 1442, 1188, 1674, 20, 1145, 1753, 711, 1234, 1369, 1178, 182, 866, 1594, 786, 1705, 609, 1711, 399, 961, 894, 1379, 900, 361, 561, 26, 2019, 58, 1142, 177, 275, 480, 1237, 430, 1422, 1185, 1098, 1429, 274, 424, 1518, 691, 705, 103, 589, 1495, 1716, 1360, 446, 897, 381, 639, 465, 1302, 603, 494, 809, 1232, 1461, 320, 676, 1112, 404, 1349, 2031, 1804, 628, 799, 307, 1394, 1419, 1194, 1365, 269, 436, 1012, 47, 1669, 1283, 886, 107, 872, 2021, 1787, 419, 382, 24, 929, 1599, 1193, 416, 1242, 1351, 541, 738, 115, 2013, 546, 449, 1443, 622, 581, 569, 1788, 1694, 1982, 1633, 125, 1961, 1276, 829, 879, 915, 916, 1147, 619, 1114, 1863, 571, 759, 542, 521, 422, 1627, 715, 717, 126, 1009, 778, 23, 1380, 1723, 106, 1852, 1039, 539, 1308, 11, 154, 782, 1874, 1317, 1253, 1531, 2004, 716, 1660, 210, 986, 701, 1047, 811, 37, 1309, 1646, 437, 240, 2003, 147, 406, 1183, 899, 1808, 1811, 1574, 260, 152, 999, 306, 1350, 1789, 132, 1742, 1999, 1902, 224, 980, 1550, 1895, 141, 489, 837, 460, 426, 1344, 1869, 1724, 760, 635, 1437, 1898, 1947, 1325, 467, 1838, 1757, 168, 1708, 625, 1061, 1603, 220, 228, 1062, 989, 145, 475, 1387, 2046, 1737, 1260, 330, 1428, 1772, 930, 768, 1267, 1216, 1905, 2000, 45, 767, 1691, 1335, 1850, 336, 1741, 1077, 174, 9, 1901, 1211, 101, 1296, 2044, 368, 757, 90, 1472, 1635, 1303, 976, 1285, 1631, 1007, 1223, 1272, 1923, 698, 857, 484, 173, 559, 1750, 409, 948, 1005, 111, 1714, 1122, 1878, 2016, 709, 137, 172, 1864, 1779, 1073, 2030, 298, 1176, 2045, 451, 261, 5, 1527, 1307, 1006, 790, 184, 432, 1530, 1770, 2047, 1877, 2017, 259, 1547, 1683, 280, 1914, 1332, 363, 326, 967, 1175, 592, 225, 1475, 604, 463, 1478, 80, 1433, 48, 1738, 1526, 40, 1003, 242, 572, 724, 1781, 1300, 18, 1306, 276, 567, 1712, 1975, 218, 540, 1955, 647, 901, 2005, 863, 1189, 1509, 2029, 1065, 1721, 402, 1749, 606, 1187, 254, 613, 1135, 991, 1844, 1800, 287, 1625, 593, 512, 1097, 31, 180, 556, 1632, 2007, 836, 358, 357, 2042, 1423, 196, 214, 1323, 22, 1764, 629, 148, 968, 1565, 1589, 543, 661, 789, 78, 423, 792, 94, 464, 1605, 510, 1889, 408, 1153, 518, 1436, 208, 112, 1662, 1504, 1933, 428, 814, 1191, 1997, 1213, 1331, 1948, 29, 1571, 122, 1516, 1544, 2023, 1215, 1221, 1880, 1957, 1465, 191, 113, 1487, 2041, 170, 384, 1503, 907, 1831, 205, 157, 289, 851, 797, 560, 41, 1521, 235, 1348, 498, 1493, 1141, 1601, 1713, 1016, 1513, 1079, 1462, 1701, 807, 1926, 1263, 1368, 1464, 1229, 1396, 1700, 1321, 1391, 1371, 1459, 1456, 370, 167, 1771, 1375, 659, 1004, 1469, 1652, 751, 471, 485, 1938, 753, 1192, 1759, 1164, 926, 818, 1873, 844, 1623, 941, 1699, 342, 1648, 1908, 128, 1094, 732, 6, 755, 213, 1956, 1342, 1398, 1078, 910, 434, 530, 699, 895, 1634, 1286, 558, 178, 813, 1815, 1841, 1076, 1329, 1448, 1356, 335, 1056, 865, 1645, 1081, 1001, 304, 1622, 1986, 1025, 1377, 1849, 766, 1740, 1799, 1159, 1045, 1576, 519, 1658, 1051, 313, 1031, 372, 749, 1023, 804, 1929, 1214, 673, 63, 1, 1773, 1537, 614, 1562, 987, 1577, 1395, 1421, 1038, 492, 970, 881, 686, 1087, 88, 660, 403, 648, 328, 783, 1233, 1246, 1685, 1580, 777, 537, 1319, 1482, 1367, 1328, 1534, 1698, 927, 1205, 19, 1937, 1085, 1854, 477, 129, 481, 61, 1958, 1828, 827, 1266, 284, 1979, 1507, 2035, 1314, 1930, 1099, 431, 1911, 188, 162, 547, 1252, 1607, 251, 1696, 1585, 527, 1557, 594, 353, 369, 386, 309, 1293, 279, 1818, 1071, 1810, 1668, 379, 1110, 743, 1528, 1150, 658, 1717, 1729, 1998, 888, 1636, 877, 1378, 762, 1063, 1217, 1620, 92, 1197, 1133, 1002, 1971, 1654, 1777, 1347, 305, 1561, 1015, 1486, 821, 1836, 678, 536, 1985, 349, 1449, 1990, 1417, 1538, 389, 1894, 1829, 1138, 302, 982, 1872, 1617, 794, 308, 1126, 2028, 1024, 249, 831, 459, 1651, 1036, 327, 123, 51, 1643, 1897, 491, 1823, 849, 1166, 832, 1363, 1143, 1028, 919, 579, 250, 1305, 291, 545, 1719, 1113, 447, 815, 1671, 49, 1665, 1867, 862, 229, 351, 1224, 1050, 800, 1604, 1612, 714, 2025, 1964, 1467, 902, 1946, 347, 1041, 286, 1855, 1512, 1858, 1352, 1409, 1384, 68, 1132, 1784, 462, 1944, 1091, 977, 630, 554, 1906, 1610, 153, 271, 273, 781, 1950, 1890, 222, 1834, 1058, 1553, 1265, 1338, 925, 951, 2014, 1155, 758, 1517, 268, 964, 960, 1030, 728, 1943, 1374, 1111, 1703, 1644, 255, 687, 1444, 1134, 1084, 1817, 54, 503, 1158, 1101, 1793, 27, 443, 544, 439, 392, 1358, 52, 788, 1692, 1022, 1026, 2, 817, 194, 473, 183, 608, 742, 1666, 1805, 1334, 787, 438, 656, 1124, 950, 159, 672, 820, 234, 1092, 352, 264, 414, 634, 380, 195, 1426, 187, 272, 1127, 55, 142, 1987, 1032, 1137, 43, 918, 729, 626, 1542, 938, 962, 1406, 852, 983, 476, 1693, 1011, 34, 1343, 1941, 1744, 429, 552, 1033, 1324, 324, 774, 597, 1954, 454, 1522, 1767, 692, 1747, 1678, 1353, 1974, 538, 1551, 1277, 1410, 412, 550, 1034, 654, 1273, 1254, 1915, 1814, 1718, 1664, 703, 73, 1657, 198, 1569, 1629, 1299, 1934, 651, 1013, 1619, 1359, 548, 1010, 840, 315, 1968, 1570, 1704, 2008, 35, 493, 779, 1151, 233, 1977, 695, 281, 1842, 1249, 455, 366, 1104, 1499, 179, 996, 97, 1682, 1835, 71, 642, 1440, 500, 1910, 1859, 1067, 585, 645, 1072, 189, 528, 719, 1609, 1731, 263, 1765, 1066, 515, 1780, 1796, 1118, 1663, 1586, 1082, 1552, 920, 1116, 1812, 939, 1125, 1584, 620, 1190, 1706, 265, 1624, 846, 65, 1928, 143, 969, 1996, 1581, 1258, 17, 1326, 1523, 533, 1288, 1021, 1761, 684, 89, 1370, 186, 869, 160, 1090, 1220, 193, 1366, 318, 1280, 1244, 1583, 1049, 1882, 161, 181, 1578, 745, 343, 1945, 1385, 1639, 1778, 1089, 316, 1373, 1786, 708, 407, 1163, 1755, 1203, 735, 1980, 934, 1597, 1656, 1407, 1904, 1563, 860, 988, 1554, 611, 1490, 1893, 118, 4, 1822, 344, 1471, 1018, 761, 578, 133, 864, 685, 922, 1485, 913, 1505, 1677, 325, 211, 1582, 67, 1502, 1239, 1238, 1702, 649, 516, 652, 190, 979, 230, 435, 1064, 1539, 21, 602, 532, 1991, 413, 1196, 1681, 524, 124, 151, 1621, 663, 1250, 1684, 998, 1019, 1139, 612, 110, 911, 466, 808, 1960, 415, 2010, 842, 1735, 140, 75, 62, 1592, 522, 1959]
result.pop()
tour = read_input('input_'+str(k)+'.csv')
n = len(tour)
points = list(range(n))

changed = True
while changed:
    result, changed = change(result)


result.append(result[0])
print(result)
cities = read_input(f'input_{k}.csv')
name = 'random'
with open(f'sample/{name}_{k}.csv', 'w') as f:
    f.write(format_tour(result) + '\n')