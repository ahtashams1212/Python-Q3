#     STRING AND FSTRING


name: str = 'Ahtasham Shafique'

print ("My name is", name)
print ("I am student of DAE Automobiles")
print ('I am student of PIAIC')
print ('''
       G
        C
         T 
          Student'''
       )
print ('"By Zia Khan"')

print ('PIAIC','Generative AI','Cloud Applied', sep='---')

# for inline words spacing use ( end='   '  )
print('PIAIC', end='   ')
print('Generative AI', end='   ')
print('Cloud Applied')
print()



#     OPERATORS



a : int = 7
b : int = 2

print(a + b) # addtition

print()

print(a - b) # subtraction

print()


print(a * b)

print()


print(a / b) # division
print()





#       LIST-ITS-METHOD




# ->                    0        1         2
names : list[str] = ["Qasim","Sir Zia", "Sir Inam",
                     "Apple","Mango", "Cheery"]
# <-                    -3     -2          -1

print(names[-2])
print(names[2])
print(names[-3])
print(names[-1])
print(names[1])
print(names[0])

print()

print(names[1:6])

print()

print(names[-3:-5]) # Answer is empty because it does not support backword it only support forward position.
 
print()

print(names[0::3])

print()

print
names.sort()  
print(names)

names_list = list(names)
names_list.append("watermelon")
names = tuple(names_list)
print(names)



print ()
 
#   LOOP

x: int = 0
while x <= 10:
    print('Ahtasham')


# FOR LOOP

y: int = 0
for y in  range(11):
    print ('Shafique')