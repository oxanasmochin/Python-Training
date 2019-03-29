def computepay(h,r):
    if h<=40 :
        gross=h*r
    else :
        gross=40*r+(h-40)*1.5*r
    return gross

hrs = input("Enter Hours:")
hrs = float(hrs)
rph =input("Enter pay per hour: ")
rph=float(rph)

p = computepay(hrs, rph)
print("Pay",p)
