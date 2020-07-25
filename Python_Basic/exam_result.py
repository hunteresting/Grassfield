midterm = 40
final = 45
total = midterm + final

if total >= 90:
    print("You get an A.")
elif 80 <= total < 90:
    print("You get a B.")
elif 70 <= total < 80:
    print("You get a C.")
elif 60 <= total < 70:
    print("You get a D.")
else:
    print("You get an F.")