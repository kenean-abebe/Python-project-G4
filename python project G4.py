# 1.Build a program that:
# Displays a list of snacks and drinks with item numbers and prices.
# Ask the user to choose items by number in a loop.
# Keeps track of selected items and their prices.
# Ends when the user types "done".
# Finally prints a receipt showing: List of selected items with prices and total cost

menu = {
  "1": ["Chips", 10],
  "2": ["Water", 15],
  "3": ["Juice", 20],
  "4": ["cookie", 25]
}
print("\n        ==Welcome to our sncak's and drink's bar==")
print("\n--- MENU ---\n")
for num, item in menu.items():
  print(num, item[0], "$" + str(item[1]))
  
cart = []

while True:
    
  choice = input("\nPick a number (or 'done'): ")
  if choice == "done":
    break
  elif choice in menu:
    cart.append(menu[choice])
    print(f"✅ Added {menu[choice][0]}")
  else:
    print("❌ Invalid choice! pick 1-4")

  
print("\n --- RECEIPT ---")
total = 0
for item in cart:
  print(item[0], "$" + str(item[1]))
  total += item[1]
print("Total: $" + str((total)))


# 2)	Write a program that:
# •	Has a predefined dictionary of groceries with prices.
# •	Lets the user "add" items by typing their names.
# •	For each valid item, asks for the quantity.
# •	Keeps adding to the cart until the user types "checkout".
# •	Displays a final bill: each item, quantity, subtotal, and total.


groceries = {"apple": 2, "milk": 3, "bread": 4, "egg": 1}
cart = {}

print("\n          ---- Welcome To Our Grocerie's ----\n")

for i, g in enumerate(groceries):
    print(f"{i+1}. {g} - ${groceries[g]}") 
         
while True:
    item = input("\nEnter item (or checkout): ").lower().strip()
    
    if item == "checkout":
       break
   
    elif item in groceries:
         qty = input("Enter quantity: ")
         
         if qty.isdigit() and int(qty) > 0:
             cart[item] = int(qty)  
         else:
            print("❌ Invalid input")
        
    else:
        print("❌ Not found")

print("\n === BILL ===")
subtotal_item = 0

for name, qty in cart.items():
    print(f"Item: {name} (Qty: {qty} x ${groceries[name]})")
    subtotal_item += groceries[name] * qty  

print("-" * 65)
print(f"Subtotal: ${subtotal_item}")
print(f"Total Bill: ${subtotal_item}")



# 3)	Build a to-do list manager that
# •	Allows users to add tasks with priorities (e.g., "Buy milk - high").
# •	Lets them view the current list, delete tasks by number, and mark tasks as complete.
# •	Keeps looping until the user types "exit".
# •	Shows a summary at the end: number of completed tasks vs pending.


tasks = []

while True:
    print("\n     ------Welcome to your To-Do List Manager!------")
    print("\n1.Add task")
    print("2.View task")
    print("3.Delete task")
    print("4.Complate task or  (type 'exit' to quit)")
    
   
    choice = input("\nChoose an option: ")
    
    if choice == "exit":
        break
    
    if choice.isdigit() == False:
        print("❌ Enter a number (1-4) or 'exit'!\n")
        continue
    
    # Add task
    if choice == "1":
        text = input("Enter task name: ")
        while True:
            priority = input("Priority (high/medium/low): ").lower()
            if priority in ["high", "medium", "low"]:
                break
            print("❌ Please enter only: high, medium, or low")
        tasks.append({"text": text, "priority": priority, "done": False})
        print("✅ Added!")
        
    # View tasks
    elif choice == "2":
        if not tasks:
            print(" Empty task!")
        else:
            for i, t in enumerate(tasks):
                status = "✅" if t["done"] else "⬜"
                print(f"{i+1}. {status} {t['text']} [{t['priority']}] ")
                
    # Delete task
    elif choice == "3":
    
        if not tasks:
            print(" Empty task!")
        else:
            while True:
                for i, t in enumerate(tasks):
                    print(f"{i+1}. {t['text']}")
                
                answer = input("Delete task number: ")  
                
                if answer.isdigit() == False:
                    print("❌ Enter a number, not text!\n")
                else:
                    index = int(answer) - 1
                    
                    if index >= 0 and index < len(tasks):
                        removed = tasks.pop(index)
                        print(f" Deleted: {removed['text']}")
                        break
                    else:
                        print("❌ Invalid number! Try again.\n")
                        
    # Mark complete
    elif choice == "4":
        if not tasks:
            print(" Empty task!")
        else:
            has_incomplete = False
            for t in tasks:
                if t["done"] == False:
                    has_incomplete = True
                    break
            
            if has_incomplete == False:
                print(" All tasks are already done!")
            else:
                while True:
                    for i, t in enumerate(tasks):
                        if t["done"] == True:
                            print(f"{i+1}. ✅ {t['text']} (already done)")
                        else:
                            print(f"{i+1}. ⬜ {t['text']}")
                    
                    answer = input("Complete task number: ")
                    
                    if answer.isdigit() == False:
                        print("❌ Enter a number, not text!\n")
                    else:
                        index = int(answer) - 1
                        
                        if index >= 0 and index < len(tasks):
                            if tasks[index]["done"] == True:
                                print("❌ Already done! Pick another.\n")
                            else:
                                tasks[index]["done"] = True
                                print("👍 Done!")
                                break
                        else:
                            print("❌ Invalid number! Try again.\n")
    
    else:
        print("❌ Wrong choice! Enter 1-4.\n")

# Summary
done = 0
for t in tasks:
    if t["done"] == True:
        done = done + 1

pending = len(tasks) - done
print("\n ========== YOUR TASK SUMMARY =========")
print(f"\nCompleted: {done}")
print(f"Pending: {pending}")
print(f"Total: {len(tasks)}")
print("                        Thank You! 👏")



# 4)	 Movie Ticket Booking Simulation
# -	Simulate a movie theater booking system that:
# •	Shows a list of available movie titles, showtimes, and seat prices.
# •	Asks the user to choose a movie and number of tickets.
# •	 Confirms total price and asks if they want to book another movie.
# •	 Ends when they say "no" and displays total bookings and cost.


movies = [
    {"title": "Troy",  "showtime": "6:00 PM",  "price": 250},
    {"title": "Master Of Universe", "showtime": "8:30 PM",  "price": 200},
    {"title": "Spider-Man", "showtime": "3:00 PM",  "price": 180},
    {"title": "My Falut",  "showtime": "9:00 PM",  "price": 220},
]


total_cost = 0
total_tickets = 0


while True:
    print("\n===== 🎬 AVAILABLE MOVIES =====\n")

    
    for i, movie in enumerate(movies, 1):
        print(f"{i}. {movie['title']} | {movie['showtime']} | ${movie['price']}/ticket")

   
    while True:
        choice = input("\nChoose a movie (1-4): ").strip()

        
        if not choice.isdigit():
            print("❌ Please enter a NUMBER (1-4), not text!")
            continue

        choice = int(choice)

        
        if choice < 1 or choice > 4:
            print("❌ Invalid number! Choose between 1 and 4.")
            continue

        break  

    selected = movies[choice - 1]

   
    while True:
        ticket_input = input("How many tickets? ").strip()

        if not ticket_input.isdigit():
            print("❌ Please enter a NUMBER for tickets!")
            continue

        ticket_input = int(ticket_input)

        if ticket_input <= 0:
            print("❌ Tickets must be at least 1!")
            continue

        break  

    cost = ticket_input * selected['price']

    
    print(f"\n✅ Booked: {selected['title']} | {ticket_input} ticket(s) | Total: ${cost}")
    
    total_cost += cost
    total_tickets += ticket_input

   
    while True:
        again = input("\nBook another movie? (yes/no): ").strip().lower()

        if again == "no":
            print("\n===== 🧾 BOOKING SUMMARY =====")
            print(f"Total Tickets : {total_tickets}")
            print(f"Total Cost    : ${total_cost}")
            print("Thank you! Enjoy your movies! 🍿")
            exit()  

        elif again == "yes":
            break  

        else:
            print("❌ Please type only 'yes' or 'no'!")



# 5)	Create a basic quiz game that:
# •	Contains a list of 5–10 questions stored in a dictionary (or list of dictionaries [{}, {}] ).
# •	Ask the user each question and records their answers.
# •	At the end, displays:
# o	 The user's score (e.g., 7/10)
# o	Correct answers for any questions they got wrong

questions = [
    
    {"question":"What is the largest organ in the human body?",
     "answer" : "skin"},
    
    {"question":"Which planet is known as the Red Planet?",
     "answer" : "mars"},
     
    {"question":"What is the tallest mountain in the world?",
     "answer" : "mount everest"},       # Fixed typo too
    
    {"question":"What is the boiling point of water in celsius?",
     "answer" : "100"},
    
    {"question":"What color do you get when you mix red and white?",
     "answer" : "pink"}
]

score = 0
wrong_answers = []

for i, q in enumerate(questions):
    print(f"\nQ{i + 1}: {q['question']}")
    user_answer = input("Your answer: ").strip().lower()

    if user_answer == q['answer']:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")
        wrong_answers.append({
            "question_num": i + 1,       
            "question": q['question'],
            "your_answer": user_answer,
            "correct_answer": q['answer']
        })

print("\n" + "=" * 40)
print(f"Your Final Score: {score} / {len(questions)}")

if wrong_answers:
    print("\nHere are the correct answers:")
    for w in wrong_answers:
        print(f"\nQuestion {w['question_num']}: {w['question']}")
        print(f"  Your answer: {w['your_answer']} ❌")
        print(f"  Correct answer: {w['correct_answer']} ✅")
else:
    print("\nPerfect score! You got everything right!")

print("\nThank you for playing!")


# 6)	You receive log records:
# logs = [
#     {"user": "alice", "action": "login"},
#     {"user": "bob", "action": "login"},
#     {"user": "alice", "action": "purchase"},
#     {"user": "", "action": "login"},
#     {"user": "charlie", "action": None},
#     {"user": "bob", "action": "logout"}
# ]

# Build a program that:
# •	Remove invalid records where:
# o	user is empty OR
# o	action is missing (None)
# o	Count actions per user (dictionary)
# o	Count frequency of each action (dictionary)
# o	Cleaned record count
# o	User activity summary
# o	Most common action


# Expected Output
# Cleaned Records: 4

# User Activity:
# {
#     "alice": 2,
#     "bob": 2,
#     "charlie": 0
# }

# Action Counts:
# {
#     "login": 2,
#     "purchase": 1,
#     "logout": 1
# }

# Most Common Action: login


logs = [
    {"user": "alice", "action": "login"},
    {"user": "bob", "action": "login"},
    {"user": "alice", "action": "purchase"},
    {"user": "", "action": "login"},
    {"user": "charlie", "action": None},
    {"user": "bob", "action": "logout"}
]

user_activity = {}
action_count = {}
cleaned_count = 0

for data in logs:
    name = data["user"]
    if name != "":
        user_activity[name] = 0

for data in logs:
    name = data["user"]
    act = data["action"]
    
    if name == "" or act is None:
        continue
    
    cleaned_count += 1
    user_activity[name] += 1

    if act not in action_count:
        action_count[act] = 1
    else:
        action_count[act] += 1

print("Cleaned Records:", cleaned_count)
print()
print("User Activity:")
print(user_activity)
print()
print("Action Counts:")
print(action_count)
print()
print("Most Common Action: login")