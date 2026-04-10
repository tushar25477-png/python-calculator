import math
ans=0
while True:
    print("\nPrevious Answer:",round(ans,3))
    i=input("Choose: Add, Sub, Mult, Div, Root, Trig, Invtrig, Expo, Log, Pow, Fact, Avg, Prime, HCF (or Exit) → ").strip().title()
    if i=="Exit":
        break
    if i=="Add":
        numbers=[]
        while True:
            x=input("Enter a number (or 'ans' / nothing to stop): ")
            if x=='':
                break
            elif x=="ans":
                numbers.append(ans)
            else:
                numbers.append(float(x))
        ans=sum(numbers)
        print("Answer",ans)
    elif i=="Sub":
        numbers=[]
        while True:
            x=input("Enter a number (or 'ans' / nothing to stop): ")
            if x=='':
                break
            elif x=="ans":
                numbers.append(ans)
            else:
                numbers.append(float(x))
        if len(numbers)>0:
            ans=numbers[0]
            for j in range(1,len(numbers)):
                ans-=numbers[j]
            print("Answer",ans)
        else:
            print("No numbers entered")
    elif i=="Mult":
        numbers=[]
        while True:
            x=input("Enter a number (or 'ans' / nothing to stop): ")
            if x=='':
                break
            elif x=="ans":
                numbers.append(ans)
            else:
                numbers.append(float(x))
        if len(numbers)>0:
            ans=numbers[0]
            for j in range(1,len(numbers)):
                ans*=numbers[j]
            print("Answer",ans)
        else:
            print("No numbers entered")
    elif i=="Div":
        numbers=[]
        while True:
            x=input("Enter a number (or 'ans' / nothing to stop): ")
            if x=='':
                break
            elif x=="ans":
                numbers.append(ans)
            else:
                numbers.append(float(x))
        if len(numbers)>0:
            ans=numbers[0]
            for j in range(1,len(numbers)):
                if numbers[j]!=0:
                    ans/=numbers[j]
                else:
                    print("Cannot divide by zero")
                    break
            print("Answer",round(ans,3))
        else:
            print("No numbers entered")
    elif i=="Root":
        x=input("Enter number (or 'ans'): ")
        if x=="ans":
            x=ans
        else:
            x=float(x)
        p=input("'Squ' for Square root,'Cub' for Cube root: ")
        if p=="Squ":
            if x<0:
                print("Please enter positive number")
            else:
                ans=pow(x,1/2)
                print(round(ans,3))
        elif p=="Cub":
            ans=pow(x,1/3)
            print(round(ans,3))
        else:
            print("Invalid option")
    elif i=="Trig":
        x=input("Enter angle (or 'ans'): ")
        if x=="ans":
            x=ans
        else:
            x=float(x)
        p=input("Sin/Cos/Tan/Cosec/Sec/Cot: ")
        try:
            if p=="Sin":
                ans=math.sin(math.radians(x))
            elif p=="Cos":
                ans=math.cos(math.radians(x))
            elif p=="Tan":
                ans=math.tan(math.radians(x))
            elif p=="Cosec":
                ans=1/(math.sin(math.radians(x)))
            elif p=="Sec":
                ans=1/(math.cos(math.radians(x)))
            elif p=="Cot":
                ans=1/(math.tan(math.radians(x)))
            else:
                print("Invalid option")
                continue
            print(round(ans,3))
        except:
            print("Math error")
    elif i=="Invtrig":
        x=input("Enter number (or 'ans'): ")
        if x=="ans":
            x=ans
        else:
            x=float(x)
        p=input("Sininv/Cosinv/Taninv/Cosecinv/Secinv/Cotinv: ")
        try:
            if p=="Sininv" and -1<=x<=1:
                ans=math.degrees(math.asin(x))
            elif p=="Cosinv" and -1<=x<=1:
                ans=math.degrees(math.acos(x))
            elif p=="Taninv":
                ans=math.degrees(math.atan(x))
            elif p=="Cosecinv" and abs(x)>=1:
                ans=math.degrees(math.asin(1/x))
            elif p=="Secinv" and abs(x)>=1:
                ans=math.degrees(math.acos(1/x))
            elif p=="Cotinv" and x!=0:
                ans=math.degrees(math.atan(1/x))
            else:
                print("Invalid input")
                continue
            print(round(ans,2))
        except:
            print("Math error")
    elif i=="Expo":
        x=input("Enter number (or 'ans'): ")
        if x=="ans":
            x=ans
        else:
            x=float(x)
        ans=math.exp(x)
        print("e ^",round(x),"=",round(ans,2))
    elif i=="Log":
        x=input("Enter number (or 'ans'): ")
        if x=="ans":
            x=ans
        else:
            x=float(x)
        base=float(input("Enter base: "))
        if x>0 and base>0 and base!=1:
            ans=math.log(x,base)
            print("Answer:",round(ans,2))
        else:
            print("Invalid input")
    elif i=="Pow":
        x=input("Enter x (or 'ans'): ")
        if x=="ans":
            x=ans
        else:
            x=float(x)
        y=float(input("Enter y: "))
        ans=pow(x,y)
        print("Answer:",round(ans,2))
    elif i=="Fact":
        try:
            x=input("Enter number (or 'ans'): ")
            if x=="ans":
                x=int(ans)
            else:
                x=int(float(x))
            if x>=0:
                ans=math.factorial(x)
                print("Answer:",ans)
            else:
                print("Invalid input")
        except:
            print("Enter valid integer")
    elif i=="Avg":
        numbers=[]
        while True:
            x=input("Enter number (or 'ans' / nothing to stop): ")
            if x=='':
                break
            elif x=="ans":
                numbers.append(ans)
            else:
                numbers.append(float(x))
        if len(numbers)>0:
            ans=sum(numbers)/len(numbers)
            print("Average:",ans)
        else:
            print("No numbers entered")
    elif i=="Prime":
        x=int(input("Enter number: "))
        if x<2:
            print("Not Prime")
        else:
            for j in range(2,int(x**0.5)+1):
                if x%j==0:
                    print("Not Prime")
                    break
            else:
                print("Prime")
    elif i=="HCF":
        numbers=[]
        while True:
            x=input("Enter number (or press Enter to stop): ")
            if x=="":
                break
            numbers.append(int(x))
        if len(numbers)>0:
            result=numbers[0]
            for num in numbers[1:]:
                result=math.gcd(result,num)
            ans=result
            print("HCF =",ans)
        else:
            print("No numbers entered")
    else:
        print("Invalid option")