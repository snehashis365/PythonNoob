def circle_area(radius):
    pie = 22 / 7
    return pie * (radius**2)
r=float(input("Enter Radius: "))
print(f"Area is: {circle_area(r)}")