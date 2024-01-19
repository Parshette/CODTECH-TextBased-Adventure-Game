
print("welcome to the hunted mansion!")
print(" You are  a distant  famil member o a rih  millionaire who has  just passed way,leaving this mansion to you.")
print(" As the  newfound owner,you deside yo pay a visit to the mansion.")
print("the house is dated ,creaky and falling apart .you walk  to the front door.")
print("Do you wnatto enter the living room or dinig room")

roomChoice = input(">")

if(roomChoice =="living room"):
    print("You enter the living room.")
    print("As you walk in you see a sleeping pitbull guarding some gold ewelry.")
    print("Do you want to steal the jewelry rom the pitbull?")
    pitBullChoice ==input(">") 
    if(pitBullChoice =="yes"):
       print(" You attempt to steal the ewelry , but it wakes up and rips you to shreds.")
       print("You are now dead")
    elif(pitBullChoice =="No"):
       print("You decide to not steal the dog's jewelry ")
       print(" You turn around and leave the house safely")
    else:
        print(" Invalid choice .please enter yes or no.")
elif(roomChoice == "dining room"):
    print(" you chose to go into dining room. ")
    print("As you walk in , you see a shiny vase on the table.")
    print("DO you want to open the vase?")
    vaseChoice = input(">")
    if(vaseChoice =="Yes"):
      print(" You open the vase and find a pile of bones!")
    elif(vaseChoice =="No"):
     print("You decide not to open the shiny vase")
     print("As you turnto leave, you hear a cracking sound coming from the corner.")
     print("A dark figure with glowing red eyes launches at you , knocking you unconcious")  
     print(" You wake up in your bed. It was alla dream ") 
    else:
     print(" Invalid choice .please enter yes or no.")
else:
   print("Invalid choice, please enter living room or dining room.")             
   