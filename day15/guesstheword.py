word="hello"
char_list=list(word)
print(char_list)
gussed_list=['_' for _ in char_list]
print(gussed_list)  
dictionary={}
count=0
while count<10:
  user_input=input("guess a word:")
  if len(user_input)>1:
    print("you can guess only one letter")
  elif user_input in char_list:
    position=[]
    for i,letter in enumerate(word):
      if letter==user_input:
        position.append(i)
    
    dictionary[user_input]=position
    print("yes")  
    for x in position:
      gussed_list[x]=user_input
    print(gussed_list)

  else:
    print("no")
    count+=1
    print(10-count,"chances left")
