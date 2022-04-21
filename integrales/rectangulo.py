def rectint(f,a,b,rectangles):
    cumulative_area=0

    a=float(a)
    b=float(b)
    rectangles=float(rectangles)

    i=(b-a)/rectangles

    trailing_x=a
    leading_x=a+i

    while (a<=leading_x<=b) or (a>=leading_x>=b):
        area=f((trailing_x+leading_x)/2)*i
        cumulative_area+=area

        leading_x+=i
        trailing_x+=i

    return cumulative_area