questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 3],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
    ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
    ["What is the square root of 64?", "8", "10", "6", "12", 1],
    ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3],
    ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3],
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2]
]
prizes = [100000, 320000, 400000, 450000,  500000, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000]

i=0
for question in questions:
   print(question[0])
   print(f"a. {question[1]}")
   print(f"b. {question[2]}")
   print(f"c. {question[3]}")
   print(f"d. {question[4]}")

   a = input("Enter your answer: 1 for a,2 for b,3 for c,4 for d\n")
 
   if(question[5]==a):
        print("Correct answer")
        print(f"You won {prizes[i]} ")
        i+=1
        
   else:
        print(f"Incorrect answer!, The correct answer was {question[5]}")   
        print("Better luck next time....")
        print(f"The prize money you won is {prizes[i-1]}")
        break  

if i == len(questions):
    print("\n Congratulations! You have completed the game!")
    print(f"💰 You won the grand prize of ₹{prizes[-1]} 🎊")
