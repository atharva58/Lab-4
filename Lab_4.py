# file handling
x=input("Enter a file name in .txt: \n")
f_hand=open(x)

def capital(a): #to print the file in capital letter and strip down the extra spaces
  for i in f_hand:
    i=i.strip()
    z=i.lower()
    print(z)

def lst(b): # splitting the .txt file in list of strings or chars
  bart=list()
  x = []
  #return(f_hand.read().strip().split()) #this is correct
  for i in f_hand:
    i=i.strip()
    i=i.strip('\n')
    i=i.split()
    x += i
  return(x)

#print(lst(x))

def count_char(c): #to count number of items in the list
  count =0
  temp=list()
  temp=lst(x)
  for i in temp:
    count+=1
  print(count)

count_char(x)
