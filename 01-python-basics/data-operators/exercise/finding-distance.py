# Distance between two points
# Distance between the two points (x1, y1) and (x2, y2) is
# given by the formula:
# Distance = Square root of (((x2 - x1 )**2) + ((y2-y1)**2)))
# For instance, let point 1 is (3, 4), and point 2 is (7, 2).
# Then (x2-x1)**2=(7-3)**2 = 42 = 16 and (y2-y1)**2= (2
# 4)**2 = (-2)**2 = 4.
# now 16 + 4 =20, and the square root of 20 is 4.47.
# Therefore, the distance between (3, 4) and (7, 2) is 4.47.
# The program below finds the distance between two given
# points. The main function receives the coordinates of the
# two points and passes them to funcction dist, which finds the
# distance using the formula above


def dist(x1, y1, x2, y2):
    result = ((x2 - x1) ** 2) + ((y2 - y1) ** 2) ** 0.5
    print("distance between", (x1, y1), "and", (x2, y2), "is :", result)


def main():
    x1 = int(input("enter x1 : "))
    y1 = int(input("enter y1 : "))
    x2 = int(input("enter x2 : "))
    y2 = int(input("enter y2 : "))
    dist(x1, y1, x2, y2)


main()
