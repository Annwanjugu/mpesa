math = int(input("math: "))
if math > 100 and math < 0:
    print("invalid input")
eng = int(input("eng; "))
if eng > 100 and eng < 0:
    print("invalid input")
kis = int(input("kis; "))
if kis > 100 and kis < 0:
    print("inalid input")
bio = int(input("bio: "))
if bio > 100 and bio < 0:
    print("invalid input")
chem = int(input("chem: "))
if chem > 100 and chem < 0:
    print("invalid input")

avg = (math+eng+kis+bio+chem)/5
print(f"The average is {avg}")



if avg <= 39 and avg > 0:
    print("the grade is E")

if avg <=50 and avg >40:
    print("the average is D")

if avg <=60 and avg >50:
    print("The average is C")

if avg <=70 and avg >60:
    print("the average is B")

if avg <=100 and avg >70:
    print("the average is A")

if avg > 100:
    print("invalid")
