nums=int(input("enter your num:"))
while True:
    option=input("davam etmek isteyirsen q yaz eks halda y::")
    print("#"*20)
    if option=="q":
        operator=input("Operator(*,-,+,/):")
        num=int(input("enter your num:"))
        if operator=="+":
            nums+=num
            print(nums)
        elif operator=="-":
            nums-=num
            print(nums)
        elif operator=="*":
            nums*=num
            print(nums)
        elif operator=="/":
            nums/=num
        else:
            print("Duzgun operator daxil edin")
            break
    else:
        print("#"*20)
        print(nums)  
        break   
        