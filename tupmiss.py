#create a list and input elements
#loop through each element 
#print the statement using end=""end will make output be together as one word
#Use .join to print the output in a striaght line with whitespace between" ".join(str(x)for i in x)
#sep="/n"output in each line
 # from re import I


def straightl(z):
    # for i in z:
        # print(i,end="")    
    print(*z)
    print(' '.join(str(i)for i in z ))
    # print(' '.join(map(str,z)))
straightl([5,6,7,8,0])
    #this is function that counts the elements of a list
#create function holding list
#using the len function
#the attribute of len function will be the list
#display output
#End function 
def count_s(z):
    #  z=[5,6,9,6,8,9]
    # print(len(z))
    countm=0                          #created adefaultvariableand assign it 0
    for p in range(len(z)):  #        #looped through the range of len to only deal with the integralpart,without len,we would be calculating sum
        countm+=1
    print(countm)        
        
count_s([5,6,7,8,9])
  #program to square each element in a list 
#create list with integral elements
#loop through each elemet 
#multiply each element with itself 
#display output
#call function
def square(nlist):
    for i in nlist:
        i*i
        print(' '.join(str(i)))
square([2,4,8])
#
    