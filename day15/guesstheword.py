

def string_to_char_array(word):
  char_list=list(word)
  print(char_list)
  return char_list


def get_char_position_in_array(word, user_gussed_char):
  position=[]
  if user_gussed_char in char_list:
    for i,letter in enumerate(word):
      if letter==user_gussed_char:
        position.append(i)
  return position


def is_valid_input(user_gussed_char):
    if len(user_gussed_char)>1:
      print("you can guess only one letter")
      return False
    return True


def fill_guesses(position,user_gussed_char,gussed_list):
  for x in position:
    gussed_list[x]=user_gussed_char
  return gussed_list


def wrong_guess(count):
      print("no")
      count+=1
      print(10-count,"chances left")
      return count 

word ="hello"
char_list= string_to_char_array(word)
gussed_list=['_' for _ in char_list]
dictionary={}
count=0
while count<10:
  user_gussed_char=input("guess a word:")
  if is_valid_input(user_gussed_char):
    position = get_char_position_in_array(word, user_gussed_char)
    if position:
      dictionary[user_gussed_char]=position
      print(fill_guesses(position,user_gussed_char,gussed_list))
    else:
      count = wrong_guess(count)

