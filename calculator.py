import sys

def sum(num1,num2):
    return num1+num2, num1-num2, num1*num2, num1/num2

if __name__=="__main__":
    print("---simple calculator---")

    if len(sys.argv)==3:
        num1=int(sys.argv[1])
        num2=int(sys.argv[2])
    else:
        num1=int(input("Enter number 1:"))
        num2=int(input("Enter number 2:"))
    
    print(f"num1:{num1}")
    print(f"num2:{num2}")

    add,sub,mul,div=sum(num1,num2)

    print("Addition:",add)
    print("Subtraction:",sub)
    print("Division:",div)
    print("Multiplication:",mul)
    