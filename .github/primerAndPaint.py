l=float(input("Please give the length in feet"))
w=float(input("Please give the width in feet"))
h=float(input("Please give the height in feet"))

area = l*w*2 +l*h*2 +w*h*2
primer = area/200
paint = area/350

print("the total area is " + str(area) + " squared feet")
print("the amount of primer needed is %.2f gallons" % round(primer,2))
print("the amount of paint needed is %.2f gallons"% round(paint,2))