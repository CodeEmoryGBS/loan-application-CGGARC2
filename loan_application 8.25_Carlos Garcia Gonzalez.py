A= 18800
r=0.05
n=48
p=A*(r/12/(1-(1+r/12)**(-1*n)))
print("monthly loan payment: $",p)

age_str = input("your age:")
age_int = int(age_str)

if age_int <=40:
    inc_str = input("Income: $")
    inc_int = int(inc_str)
    if inc_int > 166500:
        print("Loan approved!")
    else:
        sav_str = input("Savings: $")
        sav_int = int(sav_str)
        if sav_int >= 657:
            print("loan approved")
        else:
            print("NOT approved")
else:
    sav_str = input("Savings: $")
    sav_int = int(sav_str)
    if sav_int >= 433:
        print("loan approved")
    else:
        print("Loan not approved")


