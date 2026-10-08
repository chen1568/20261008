A = int(input(""))
B = int(input(""))
if((A==1 or A==0)and(B==0 or B==1)):
    if((A and (not B)) or (not A) and B):
        middle = 1
    else:
        middle = 0
    S = int(input(""))
    if(S and middle):
        start = 1
    else:
        start = 0
    print("第一個閘輸出={}".format(middle))
    print("允許啟動={}".format(start))
else:
    print("輸入錯誤")