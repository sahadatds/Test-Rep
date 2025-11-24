import random
random_number = random.randint(1,100)
guess_number = int(input("Please guess a number : "))

counter = 1
while guess_number != random_number:

  if guess_number < random_number:
    print("Plz, Guess higher.")
  else:
    print("Plz guess lower number.")
  
  guess_number = int(input("Please guess a number : "))
  counter+=1

print("Correct Guess. Your Guess number is : ", guess_number)
print("Total number of steps took, ",counter)