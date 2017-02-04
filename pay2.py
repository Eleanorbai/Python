try:
    hrs = raw_input("Enter Hours:")
    h = float(hrs)
    rats = raw_input("Enter rates:")
    r = float(rats)
except:
    print "Error, please enter numeric input"
    quit()
if h <= 40:
    pay = h * r
    print pay
elif h > 40:
    pay = 40 * r + (h-40) * 1.5 * r
    print pay