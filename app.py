print("Title of program: Encouragement bot")
print()
while True:
  description = input("How are you feeling?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("sending you a virtual hug and keep your head up ok? you will get over this !")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append(",great to see that you are feeling happy!")
      counter += 2
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you are stronger than you think")
      counter += 1
    if each_word == "bad":
      feelings_list.append("bad")
      encouragement_list.append("the most beautiful thing in the world is now and i promise that everything us going to get better ")
      counter += 1
    if each_word == "angry":
      feelings_list.append("angry")
      encouragement_list.append("dont take it out on yourself or others, be careful")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". go take a break and take good care of yourself, "+ encouragement_list[0] + "! Hope you feel better :)"  
      
  elif counter == 2:
    
      output = " It seems that you are feeling quite " + feelings_list[0] + encouragement_list[0] 

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
