print("KAUN BANEGA CROREPATI") 

score = 0

print("\nQ1: What is the capital of India")
print("1. Delhi")
print("2. Kolkata")
print("3. Mumbai")
print("4. Chennai")

x = int(input("Enter your option (1-4): "))

if x == 1:
    print(" Correct!")
    score = score + 1
else:
    print(" Wrong! Correct answer is Delhi ")


# Question 2
print("\nQ2: Which planet is known as the Red Planet?")
print("1. Venus")
print("2. Earth")
print("3. Jupiter")
print("4. Mars")

y = int(input("Enter your option (1-4): "))

if y == 4:
    print("Correct!")
    score += 1
else:
    print(" Wrong! Correct answer is Mars ")


# Question 3
print("\nQ3: Which gas do plants absorb from the atmosphere ?")
print("1. Carbon Dioxide")
print("2. Hydrogen")
print("3. Oxygen")
print("4. Nitrogen")

z = int(input("Enter your option (1-4): "))

if z == 1:
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is Carbon Dioxide")

print("\n Your Final Score:", score, "/ 3")

if score == 3:
    print("🏆 Excellent! You are a genius!")
elif score == 2:
    print("👍 Good job!")
else:
    print("😅 Better luck next time!")
