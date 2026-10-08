A = int(input(""))
B = int(input(""))
if((A==1 or A==0)and(B==0 or B==1)):
    if(A or B):
        print("OR=1")
    else:
        print("OR=0")
    if(A and B):
        print("AND=1")
    else:
        print("AND=0")
    if((A and (not B)) or (not A) and B):
        print("XOR=1")
    else:
        print("XOR=0")
else:
    print("輸入錯誤")