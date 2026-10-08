num = int(input(""))
if(num<0 or num>15):
        print("輸入錯誤")
else:
    a = num%2
    b = num//2%2
    c = num//4%2
    d = num//8%2
    print("二進制=",end="")
    print(d,end="")
    print(c,end="")
    print(b,end="")
    print(a)
    e = num%8
    f = num//8%8
    print("八進制=",end="")
    print(f,end="")
    print(e)
    print("十六進制=",end="")
    if(num>9):
        temp = num-9
        match temp:
            case 1:
                print("A")
            case 2:
                        print("B")
            case 3:
                        print("C")
            case 4:
                        print("D")
            case 5:
                        print("E")
            case 6:
                        print("F")
    else:
        print(num)
