#I’m going to be using raw_input. But remember that hands a string in so
#I’m going to have to use float.
inp = raw_input("Enter your work hour:")
hour = float(inp)
inp = raw_input("Enter your work rate:")
rate = float(inp)
pay = hour * rate
print pay
