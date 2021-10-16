#ano -> identitycardno = 12 dob -> dateofbirth , comorbidity
def vaccine_drive(ano, dob,como):
    #Remove spaces from the ano
    space_ano = ano.replace(" ","")
    if ((len(space_ano)== 12 and len(dob) == 10) and ( como == "yes" or como == "no")):
        p = dob.split("/")
        age = 2021- int(p[-1])
        if (age >=60 or como == "yes"):
            print("1")
        elif(age >=45):
            print("2")
        elif(age >=30):
            print("3")
        else:
            print("Invalid Input")
    else:
        print("Invalid Input (ano,dob,c)")
vaccine_drive("1234 4523 4522", "13/12/1972", "yes")
