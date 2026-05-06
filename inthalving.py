from decimal import Decimal, ROUND_HALF_UP
degarr=[]
coefarr=[]
streq=""

# Keep in mind that this implementaion I have done assumes the question gives minima.

#For creating the halves and analysing which case to follow.
def halvetana(interA,interB):
    val1,val2,val3=Decimal(0),Decimal(0),Decimal(0)
    leng=Decimal(abs(interB-interA))
    mainmidpnt=Decimal(interA+(leng/2))
    midpntA=Decimal(interA+(leng/4))
    midpntB=Decimal(interB-(leng/4))

    #Calculating the f(x) for the 3 equidistant midpoints.
    for i in range(len(degarr)):
        val1+=Decimal((midpntA**degarr[i])*coefarr[i])
        val2+=Decimal((mainmidpnt**degarr[i])*coefarr[i])
        val3+=Decimal((midpntB**degarr[i])*coefarr[i])
    if val1>val2 and val2>val3:
        return 1
    elif val1<val2 and val2<val3:
        return 2
    #The elif statement below only considers the case of "cup" not the case of an "upside down cup". IYKYK. I mean literally too, not just the joke.
    elif val1>val2 and val2<val3:
        return 3
#Representing a univariate equation using two arrays(lists), one for recording coefficients and the other for recording the variable's powers.
#The equation is basically divided into operators and operands where the operator would always be the + symbol connecting the coefficient, variable+variable power pair.
degnum=int(input("Enter the total number operands in the equation:"))
for i in range(degnum):
    x=int(input(f"Enter the power for operand-var {i}:"))
    degarr.append(Decimal(x))
    y=int(input("Enter the coefficient for the corresponding:"))
    coefarr.append(Decimal(y))
print("The equation is: ")

#For formating and representing the equation.
for i in range(degnum):
    streq=streq+"+"+str(degarr[i])[::-1]+"^x"+str(coefarr[i])[::-1]+" "

print(streq[:0:-1])

inps=[i for i in input("Enter the interval values:").split()]


STEP = Decimal('0.0001')
HALF = Decimal('2')
QUART = Decimal('4')

interA=Decimal(inps[0])
interB=Decimal(inps[1])
print(type(interA))
print(type(interB))
iters=int(input("Enter the number of iterations:"))

for i in range(0,iters):
    x=halvetana(interA,interB)
    if i!=iters-1:
        if x==1:
            print("Case 1 called for iteration ",i)
            interA=interA+((abs(interB-interA))/Decimal('2'))
            print(interA,interB,"\n")
        elif x==2:
            print("Case 2 called for iteration ",i)
            interB=interB-((abs(interB-interA))/Decimal('2'))
            print(interA,interB,"\n")


        elif x==3:
            print("Case 3 called for iteration ",i)
            k=interA
            interA=interA+((abs(interB-interA))/Decimal('4'))
            interB=interB-((abs(interB-k))/Decimal('4'))
            print(interA,interB,"\n")

    else:
        if x==1:
            print(interA,interB)
            optpos=interB-((abs(interB-interA))/QUART)
            optpos = optpos.quantize(STEP, rounding=ROUND_HALF_UP)
            optval=0
            for j in range(len(degarr)):
                optval+=(optpos**degarr[j])*coefarr[j]

            print("The optimum minima is at the position x= ",optpos,"\nwhere for f(x)= ",streq[:0:-1],f" f({optpos})= ",optval)

        elif x==2:
            print(interA,interB)
            optpos=interA+((abs(interB-interA))/QUART)
            optpos = optpos.quantize(STEP, rounding=ROUND_HALF_UP)
            optval=0
            for j in range(len(degarr)):
                optval+=(optpos**degarr[j])*coefarr[j]

            print("The optimum minima after ",iters," iterations is at the position x= ",optpos,"\nwhere for f(x)= ",streq[:0:-1],f" f({optpos})= ",optval)
        
        #The reason I'm not putting else is because the "upside down cup" can arise. Not the "cup".
        elif x==3:
            print(interA,interB)
            optpos=interA+((abs(interB-interA))/HALF)
            optpos = optpos.quantize(STEP, rounding=ROUND_HALF_UP)
            optval=0
            for j in range(len(degarr)):
                optval+=(optpos**degarr[j])*coefarr[j]

            print("The optimum minima after ",iters," iterations is at the position x= ",optpos,"\nwhere for f(x)= ",streq[:0:-1],f" f({optpos})= ",optval)


"""
Updates to be made:
Floating point correction.
    1. The current code is just an intuistic implementation of mine which has to be debugged.
    2. It assumes that the user only gives question for minimization, so for maximizing, complement of the equation has to be implemented.
    3. The upside down cup solution if possible.
    4. The graphical representation of the equation would make it look even more cooler.
"""
