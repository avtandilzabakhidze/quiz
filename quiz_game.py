print("Welcome to my computer quiz!")

playing = input("Do you want to play ? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's play : ) ")

score = 0
#start 1
answer = input("What does cpu stand for ? ")

if answer.lower() == "central processing unit":
    print("correct ! ")
    score += 1
else:
    print("Incorrect ! ")
#end 1

#start 2
answer = input("What does RAM stand for ? ")

if answer.lower() == "random access memory":
    print("correct ! ")
    score += 1
else:
    print("Incorrect ! ")

#end 2

#start 3
answer = input("What does PSU stand for ? ")

if answer.lower() == "power suplay":
    print("correct ! ")
    score += 1
else:
    print("Incorrect ! ")
#end 3

print("You got " + str(score)+ " question correct ! ")



