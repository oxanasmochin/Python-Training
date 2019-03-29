hrs = input("Enter Hours:")
hrs = float(hrs)
rph =input("Enter pay per hour: ")
rph=float(rph)
incr=1.5

if hrs<=40 :
    gross_pay=hrs*rph
else:
    gross_pay=40*rph+(hrs-40)*incr*rph
print("Pay: ", gross_pay)
