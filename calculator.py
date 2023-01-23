while(True):
    print("1/standard mode ")
    print("2/programmer mode")
    x=(input("choice your mode :"))
    if x =="1":
        print("1-Addition")
        print("2-subtration")
        print("3-multiply")
        print("4-Division")
        operator= input("enter operator : ")
        num_1=float(input("enter first number: "))
        num_2=float(input("enter second number: "))

        if operator == "1":
            print(num_1 ,"+",num_2,"=",num_1+num_2)
            
        elif operator == "2":
            print(num_1 ,"-",num_2,num_1-num_2)
        elif operator == "3":
            print(num_1 ,"*",num_2,"=",num_1*num_2)
        else :
            if num_2 ==0:
                print("wrong process")
            else:
                print(num_1 ,"/",num_2,num_1/num_2)
    elif x =="2":
            #programmer mode 
            print("1-AND")
            print("2-OR")
            print("3-XOR")
            print("4-NOT")
            print("5-Shift Right")
            print("6-Shift Left")

            choice= input("enter operator : ")
            num_1 =int(input("enter first number: "))
            num_2 =int(input("enter second number: "))
            if choice =="1":
                result= num_1&num_2
                print(num_1,"&",num_2,"=",bin(result))
                
            elif choice =="2":
                result= num_1|num_2
                print(num_1,"|",num_2,"=",bin(result))
                
            elif choice =="3":
                result= num_1^num_2
                print(num_1,"^",num_2,"=",bin(result))
                
            elif choice =="4":
                result= ~ num_1
                print(num_1,"=",bin(result))
                
            elif choice == "5":
                result= num_1>>num_2
                print(num_1,"=",bin(result))
                
            else:
                result= num_1<<num_2
                print(num_1,"=",bin(result))
    else:
        print("wrong mode")    
            
