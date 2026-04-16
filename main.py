# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."

   return message


message = welcome_message("imaselko@calpoly.edu")
print(message)

#Evaluating Code with Conditionals
def smallest(n:float, m:float) -> float:
   if n < m:
      return n #which calls are evaluated for this statement? none
   else:
      return m

first = smallest(3,2) #What is the value of the first? return m: 2
second = smallest(2,2) #What is the value of the second? return m:2 is this is reasonable result, why? yes because there is not an "or equals to"
print(first)

def function2(a:int, b:int, c:int) -> int:
   if a > b and a > c:
      return a - b #when will a call evaluate this statement? when a is greater than b and c
   elif b > c:
      return b + c #when will a call evaluate this statement? when a is not greater than b and c and b is greater than c
   else:
      return 2 * c #when will call evaluate this statement? when a is not greater than b and c and b is not greater than c

answer1 = function2(3,2,1) #what is the answer: 1
answer2 = function2(2,3,1) #what is the answer: 4
answer3 = function2(2,1,3) #what is the answer: 6
print(answer3)
