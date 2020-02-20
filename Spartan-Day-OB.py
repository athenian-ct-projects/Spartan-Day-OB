print("Spartan Day Program \nby OB '23")
print("""
First you will pick a number from 1-5. It wil ask you to enter a number. Once you have done that,
it will ask you to pick a number to decide the name of that part of the course. It will make you do 
each of those 3 times. Once you have 3 objectives with their respective names you will give them to 
the teacher so they know that you have completed the task. Then you will add the tasks into the race.
""")

def incorrect():
    print ("sorry not the right number")
for x in range (1,4,1):
  print(x)
else:
  print("Please Start the game")
print("once you have picked 3 numbers with their names give them to your teacher so they know you completed your task") 
#you will have to choose a number 3 times (they have to be different numbers)
#I am defining each number and added a while loop so I makes you pick a number 3 times.
x=0
while x<3 :
  num = int(input("enter a number 1-5: "))
  if num == 1 :
    print (" you have to incorperate an obstacle you have to jump over")
  elif num == 2 :
    print (" you have to do 5 pushups before starting the race")
  elif num == 3 :
    print (" you have to weave throught 4 poles")
  elif num == 4 :
    print (" you have to go through a tube")
  elif num == 5 :
    print (" you have to add a part of the coarse where you can not touch the ground ") 
  else:
    incorrect()
  name = int(input("now pick a number that will determine the name of this objective from 6-11: "))
  #now you will name each number
  #what ever number goes with the name is what that object has to be called
  if name == 6 :
    print (" tarantula")
  if name == 7 :
    print (" Superstar")
  if name == 8 :
    print (" crab cakes")
  if name == 9 :
    print (" dog cave")
  if name == 10 :
    print (" pole bender")
  if name == 11 :
    print (" kangaroo")
  x = x+1 
print ("if one of your answers was wrong you must restart to make sure you have 3 of each")
print (" now that you are done, go back to the top to read the rest of the instructions ")
