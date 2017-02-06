def computepay(h,r):
    if h <= 40:
        inp = h * r
    elif h >= 40:
        inp = 40 * r + (h - 40) * 1.5 * r
    return inp

hrs = raw_input("Enter Hours:")
h = float(hrs)
rats = raw_input("Enter Rates:")
r = float(rats)
p = computepay(h,r)
print "Pay",p