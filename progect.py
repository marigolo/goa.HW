# #MATE
# import random
# import turtle
# import datetime

# class Currency:
#     RATES = {
#         "USD": 0.37,  
#         "EUR": 0.34, 
#         "GBP": 0.29   
#     }

#     def change_currency(self, current_balance: float):
#         print("\n--- ვალუტის კონვერტაცია ---")
#         if current_balance <= 0:
#             print("❌ თქვენს ბალანსზე არ არის საკმარისი თანხა კონვერტაციისთვის.")
#             return

#         print(f"💰 თქვენი მიმდინარე ბალანსი: {current_balance} ₾")
#         change = input("გსურთ ვალუტის შეცვლა/კონვერტაცია? (yes/no): ").strip().lower()

#         if change == "yes":
#             target_currency = input("რომელ ვალუტაში გსურთ გადაყვანა? (USD/EUR/GBP): ").strip().upper()
            
#             if target_currency not in self.RATES:
#                 print("❌ არასწორი ვალუტა. აირჩიეთ USD, EUR ან GBP.")
#                 return

#             try:
#                 amount_gel = float(input(f"რამდენი ლარის (₾) კონვერტაცია გსურთ? (მაქს: {current_balance} ₾): "))
#             except ValueError:
#                 print("❌ შეცდომა: შეიყვანეთ ვალიდური რიცხვი.")
#                 return

#             if amount_gel <= 0:
#                 print("❌ თანხა უნდა იყოს 0-ზე მეტი.")
#                 return

#             if amount_gel > current_balance:
#                 print("❌ შეცდომა: შეყვანილი თანხა აღემატება თქვენს ბალანსს!")
#                 return

#             converted_amount = round(amount_gel * self.RATES[target_currency], 2)
#             print(f"✅ {amount_gel} ₾ = {converted_amount} {target_currency} (კურსი: 1 GEL = {self.RATES[target_currency]} {target_currency})")
#         else:
#             print("თქვენ უარი განაცხადეთ ვალუტის კონვერტაციაზე.")


# def generate_account_number() -> str:
#     """გენერირებს რანდომულ საბანკო ანგარიშის ნომერს"""
#     random_digits = "".join([str(random.randint(0, 9)) for _ in range(6)])
#     return f"GE29GOA{random_digits}"
# #MATE
# #MARI

# def draw_receipt(action_type: str, amount: float, balance: float, account_number: str, owner_name: str):
#     """ხატავს საბანკო ჩეკს turtle მოდულის გამოყენებით"""
#     try:
#         try:
#             turtle.bye()
#         except Exception:
#             pass

#         screen = turtle.Screen()
#         screen.title("GOA Bank - ტრანზაქციის ჩეკი")
#         screen.bgcolor("#f0f0f0")
#         screen.setup(400, 550)
        
#         t = turtle.Turtle()
#         t.speed(0)
#         t.hideturtle()
        
#         # ჩეკის თეთრი ფონის მართკუთხედი
#         t.penup()
#         t.goto(-160, 240)
#         t.pendown()
#         t.color("black", "white")
#         t.begin_fill()
#         for _ in range(2):
#             t.forward(320)
#             t.right(90)
#             t.forward(480)
#             t.right(90)
#         t.end_fill()
        
#         # 🏛️ GOA Bank თავი და ლოგოს სტილი
#         t.penup()
#         t.goto(0, 200)
#         t.color("#111111")
#         t.write("🏛️ GOA BANK", align="center", font=("Arial", 16, "bold"))
        
#         t.goto(0, 175)
#         t.color("#00aa00")
#         t.write("[ G - O - A ] SYSTEM", align="center", font=("Arial", 10, "bold"))
        
#         # გამყოფი ხაზი
#         t.goto(-140, 150)
#         t.pendown()
#         t.color("gray")
#         t.pensize(1)
#         t.forward(280)
#         t.penup()
        
#         # ტრანზაქციის დეტალები
#         current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        
#         details = [
#             f"თარიღი: {current_time}",
#             f"მფლობელი: {owner_name}",
#             f"ანგარიში: {account_number}",
#             f"ოპერაცია: {action_type}",
#             f"თანხა: {amount} ₾",
#             f"მიმდინარე ბალანსი: {balance} ₾"
#         ]
        
#         y_pos = 110
#         for text in details:
#             t.goto(-130, y_pos)
#             t.color("black")
#             t.write(text, font=("Arial", 9, "normal"))
#             y_pos -= 35
            
#         # ქვედა გამყოფი ხაზი
#         t.goto(-140, -100)
#         t.pendown()
#         t.color("gray")
#         t.forward(280)
#         t.penup()
        
#         # ფუტერი
#         t.goto(0, -135)
#         t.color("#00aa00")
#         t.write("CHAD DEVELOPER APPROVED", align="center", font=("Arial", 9, "bold"))
        
#         t.goto(0, -165)
#         t.color("gray")
#         t.write("*** მადლობა რომ სარგებლობთ GOA-თი! ***", align="center", font=("Arial", 8, "italic"))
        
#         print("✨ ჩეკი წარმატებით დაიხატა ახალ ფანჯარაში!")
#         screen.exitonclick()
#     except (turtle.Terminator, Exception):
#         pass


# def draw_welcome_screen():
#     """ხატავს მისასალმებელ Turtle Bank ფანჯარს წარმატებული ლოგინის შემდეგ"""
#     try:
#         try:
#             turtle.bye()
#         except Exception:
#             pass

#         screen = turtle.Screen()
#         screen.setup(850, 650)
#         screen.bgcolor("#10243A")
#         screen.title("Welcome to Goa Bank")

#         pen = turtle.Turtle()
#         pen.hideturtle()
#         pen.speed(0)
        
#         # Welcome text
#         pen.penup()
#         pen.goto(0, 200)
#         pen.color("gold")
#         pen.write("WELCOME TO", align="center", font=("Arial", 25, "bold"))

#         pen.goto(0, 150)
#         pen.color("white")
#         pen.write("GOA BANK", align="center", font=("Arial", 35, "bold"))
        
#         # Draw a bank building
#         pen.goto(-100, -100)
#         pen.color("white")
#         pen.pendown()
#         pen.begin_fill()

#         for i in range(2):
#             pen.forward(200)
#             pen.left(90)
#             pen.forward(120)
#             pen.left(90)

#         pen.end_fill()
#         pen.penup()
        
#         # Draw the roof
#         pen.goto(-120, 20)
#         pen.color("gold")
#         pen.pendown()
#         pen.begin_fill()
#         pen.goto(0, 100)
#         pen.goto(120, 20)
#         pen.goto(-120, 20)
#         pen.end_fill()
#         pen.penup()
        
#         # Draw columns
#         for x in [-70, -25, 20, 65]:
#             pen.goto(x, -90)
#             pen.color("#10243A")
#             pen.pendown()
#             pen.begin_fill()

#             for i in range(2):
#                 pen.forward(15)
#                 pen.left(90)
#                 pen.forward(90)
#                 pen.left(90)

#             pen.end_fill()
#             pen.penup()
            
#         # Coins
#         for x, y in [(-200, -120), (200, -120)]:
#             pen.goto(x, y)
#             pen.dot(50, "gold")
#             pen.goto(x, y - 12)
#             pen.color("white")
#             pen.write("$", align="center", font=("Arial", 20, "bold"))

#         pen.goto(0, -200)
#         pen.color("gold")
#         pen.write("Your Money, Your Future!", align="center", font=("Arial", 18, "bold"))

#         screen.exitonclick()
#     except (turtle.Terminator, Exception):
#         pass


# class BankAccount:
#     def __init__(self, account_number: str, owner: str, initial_balance: float = 0.0):
#         self.account_number = account_number
#         self.owner = owner
#         self.balance = initial_balance  
#         self.transaction_history = [f"ანგარიში შეიქმნა საწყისი ბალანსით: {initial_balance}₾"]

#     def deposit(self, amount: float):
#         if amount <= 0:
#             print("❌ შეცდომა: შეტანილი თანხა უნდა იყოს 0-ზე მეტი.")
#             return
#         self.balance += amount
#         self.transaction_history.append(f"შეტანა: +{amount}₾ | ბალანსი: {self.balance}₾")
#         print(f"✅ წარმატებით ჩაირიცხა {amount}₾. ახალი ბალანსი: {self.balance}₾")
#         draw_receipt("თანხის შეტანა", amount, self.balance, self.account_number, self.owner)

#     def withdraw(self, amount: float):
#         if amount <= 0:
#             print("❌ შეცდომა: გატანის თანხა უნდა იყოს 0-ზე მეტი.")
#             return
#         if amount > self.balance:
#             print("❌ შეცდომა: ანგარიშზე არ არის საკმარისი თანხა.")
#             return
#         self.balance -= amount
#         self.transaction_history.append(f"გატანა: -{amount}₾ | ბალანსი: {self.balance}₾")
#         print(f"✅ წარმატებით გაიტანეთ {amount}₾. დარჩენილი ბალანსი: {self.balance}₾")
#         draw_receipt("თანხის გამოტანა", amount, self.balance, self.account_number, self.owner)

#     def show_history(self):
#         print(f"\n--- ტრანზაქციების ისტორია ({self.account_number}) ---")
#         if not self.transaction_history:
#             print("ტრანზაქციები არ მოიძებნება.")
#         else:
#             for tx in self.transaction_history:
#                 print(tx)
# #MARI
# #NIKA
# class User:
#     def __init__(self, first_name: str, last_name: str, personal_id: str, username: str, pin: str, account_number: str):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.personal_id = personal_id
#         self.username = username
#         self.pin = pin
#         self.account = BankAccount(account_number, f"{first_name} {last_name}", 0.0)


# class GOABank(Currency):
#     def __init__(self):
#         super().__init__()
#         self.name = "GOA Bank"
#         self.users = {}  
#         self.all_accounts = {}  
#         self.current_user = None  
#         self.lang = "ka"  # საწყისი ენა არის ქართული ("ka" ან "en")

#     def register(self):
#         if self.lang == "ka":
#             print("\n--- GOA Bank - რეგისტრაცია ---")
#             while True:
#                 first_name = input("შეიყვანეთ სახელი (მხოლოდ ასოები): ").strip()
#                 if first_name.isalpha():
#                     break
#                 print("❌ შეცდომა: სახელი უნდა შეიცავდეს მხოლოდ ასოებს.")

#             while True:
#                 last_name = input("შეიყვანეთ გვარი (მხოლოდ ასოები): ").strip()
#                 if last_name.isalpha():
#                     break
#                 print("❌ შეცდომა: გვარი უნდა შეიცავდეს მხოლოდ ასოებს.")

#             while True:
#                 personal_id = input("შეიყვანეთ პირადი ნომერი (მხოლოდ რიცხვები): ").strip()
#                 if personal_id.isdigit():
#                     break
#                 print("❌ შეცდომა: პირადი ნომერი უნდა შედგებოდეს მხოლოდ რიცხვებისგან.")
            
#             username = input("შეიყვანეთ მომხმარებლის უნიკალური სახელი (username): ").strip()
#             if username in self.users:
#                 print("❌ ეს სახელი უკვე დაკავებულია!")
#                 return
            
#             while True:
#                 pin = input("შეიყვანეთ PIN კოდი (მხოლოდ რიცხვები): ").strip()
#                 if pin.isdigit():
#                     break
#                 print("❌ შეცდომა: PIN კოდი უნდა შედგებოდეს მხოლოდ რიცხვებისგან.")
#         else:
#             print("\n--- GOA Bank - Registration ---")
#             while True:
#                 first_name = input("Enter first name (letters only): ").strip()
#                 if first_name.isalpha():
#                     break
#                 print("❌ Error: First name must contain only letters.")

#             while True:
#                 last_name = input("Enter last name (letters only): ").strip()
#                 if last_name.isalpha():
#                     break
#                 print("❌ Error: Last name must contain only letters.")

#             while True:
#                 personal_id = input("Enter personal ID (numbers only): ").strip()
#                 if personal_id.isdigit():
#                     break
#                 print("❌ Error: Personal ID must contain only numbers.")
            
#             username = input("Enter unique username: ").strip()
#             if username in self.users:
#                 print("❌ This username is already taken!")
#                 return
            
#             while True:
#                 pin = input("Enter PIN code (numbers only): ").strip()
#                 if pin.isdigit():
#                     break
#                 print("❌ Error: PIN must contain only numbers.")
        
#         acc_num = generate_account_number()
#         while acc_num in self.all_accounts:
#             acc_num = generate_account_number()

#         new_user = User(first_name, last_name, personal_id, username, pin, acc_num)
#         self.users[username] = new_user
#         self.all_accounts[acc_num] = new_user.account

#         if self.lang == "ka":
#             print(f"\n🎉 რეგისტრაცია წარმატებით დასრულდა!")
#             print(f"💳 შენი გენერირებული საბანკო ანგარიშის ნომერია: {acc_num}")
#         else:
#             print(f"\n🎉 Registration completed successfully!")
#             print(f"💳 Your generated account number is: {acc_num}")

#     def login(self):
#         if self.lang == "ka":
#             print("\n--- GOA Bank - სისტემაში შესვლა ---")
#             username = input("მომხმარებლის სახელი: ").strip()
#             pin = input("PIN კოდი: ").strip()
#         else:
#             print("\n--- GOA Bank - Login ---")
#             username = input("Username: ").strip()
#             pin = input("PIN code: ").strip()

#         if username in self.users and self.users[username].pin == pin:
#             self.current_user = self.users[username]
#             if self.lang == "ka":
#                 print(f"👋 მოგესალმები, {self.current_user.first_name}! წარმატებით შეხვედი სისტემაში.")
#             else:
#                 print(f"👋 Welcome, {self.current_user.first_name}! Logged in successfully.")
#             draw_welcome_screen()
#         else:
#             if self.lang == "ka":
#                 print("❌ შეცდომა: არასწორი სახელი ან PIN კოდი.")
#             else:
#                 print("❌ Error: Incorrect username or PIN.")

#     def logout(self):
#         if self.lang == "ka":
#             print(f"\n🚪 {self.current_user.username} გამოვიდა სისტემიდან.")
#         else:
#             print(f"\n🚪 {self.current_user.username} logged out.")
#         self.current_user = None

#     def show_profile(self):
#         if not self.current_user:
#             print("❌ ჯერ უნდა შეხვიდე სისტემაში!" if self.lang == "ka" else "❌ You must log in first!")
#             return
        
#         acc = self.current_user.account
#         if self.lang == "ka":
#             print("\n==============================")
#             print("        👤 მომხმარებელი        ")
#             print("==============================")
#             print(f" სახელი და გვარი: {self.current_user.first_name} {self.current_user.last_name}")
#             print(f" პირადი ნომერი (პნ): {self.current_user.personal_id}")
#             print(f" Username: {self.current_user.username}")
#             print(f" ანგარიშის ნომერი: {acc.account_number}")
#             print(f" მიმდინარე ბალანსი: {acc.balance}₾")
#             print("==============================")
#             input("\nგაგრძელებისთვის დააჭირე Enter-ს...")
#         else:
#             print("\n==============================")
#             print("        👤 User Profile        ")
#             print("==============================")
#             print(f" Full Name: {self.current_user.first_name} {self.current_user.last_name}")
#             print(f" Personal ID: {self.current_user.personal_id}")
#             print(f" Username: {self.current_user.username}")
#             print(f" Account Number: {acc.account_number}")
#             print(f" Current Balance: {acc.balance}₾")
#             print("==============================")
#             input("\nPress Enter to continue...")
#     #NIKA        
#     #LUKA
#     def transfer_money(self):
#         if not self.current_user:
#             print("❌ ჯერ უნდა შეხვიდე სისტემაში!" if self.lang == "ka" else "❌ You must log in first!")
#             return

#         sender_account = self.current_user.account
#         if self.lang == "ka":
#             print(f"\n--- თანხის გადარიცხვა ---")
#             print(f"შენი ანგარიში: {sender_account.account_number} (ბალანსი: {sender_account.balance}₾)")
#             to_acc = input("მიმღები ანგარიშის ნომერი: ").strip()
#         else:
#             print(f"\n--- Money Transfer ---")
#             print(f"Your Account: {sender_account.account_number} (Balance: {sender_account.balance}₾)")
#             to_acc = input("Recipient account number: ").strip()

#         if to_acc not in self.all_accounts:
#             print("❌ მიმღები ანგარიში ვერ მოიძებნა ბანკში." if self.lang == "ka" else "❌ Recipient account not found.")
#             return
        
#         if sender_account.account_number == to_acc:
#             print("❌ საკუთარ თავს ვერ გადაურიცხავ." if self.lang == "ka" else "❌ Cannot transfer to yourself.")
#             return

#         try:
#             amount = float(input("გადასარიცხი თანხა (₾): " if self.lang == "ka" else "Amount to transfer (₾): "))
#         except ValueError:
#             print("❌ არასწორი თანხა." if self.lang == "ka" else "❌ Invalid amount.")
#             return

#         receiver_account = self.all_accounts[to_acc]

#         if amount <= 0:
#             print("❌ თანხა უნდა იყოს 0-ზე მეტი." if self.lang == "ka" else "❌ Amount must be greater than 0.")
#             return

#         if amount > sender_account.balance:
#             print("❌ ანგარიშზე არ არის საკმარისი თანხა!" if self.lang == "ka" else "❌ Insufficient funds!")
#             return

#         sender_account.balance -= amount
#         sender_account.transaction_history.append(f"გადარიცხვა ({to_acc}-ზე): -{amount}₾ | ბალანსი: {sender_account.balance}₾")

#         receiver_account.balance += amount
#         receiver_account.transaction_history.append(f"გადმორიცხვა ({sender_account.account_number}-დან): +{amount}₾ | ბალანსი: {receiver_account.balance}₾")

#         if self.lang == "ka":
#             print(f"✅ გადარიცხვა წარმატებით დასრულდა! გადაირიცხა {amount}₾.")
#         else:
#             print(f"✅ Transfer successful! Transferred {amount}₾.")
#         draw_receipt("თანხის გადარიცხვა", amount, sender_account.balance, sender_account.account_number, sender_account.owner)
#     #LUKA  
#     # გიორგი
#     def run(self):
#         while True:
#             print("\n==============================")
#             print("        🏛️ GOA BANK SYSTEM        ")
#             print("==============================")
            
#             # მთავარი მენიუ (დაულოგინებელი მომხმარებელი)
#             if not self.current_user:
#                 if self.lang == "ka":
#                     print("1. რეგისტრაცია")
#                     print("2. სისტემაში შესვლა (Login)")
#                     print("3. ენის შეცვლა / Change Language (English)")
#                     print("4. პროგრამიდან გასვლა")
#                     choice = input("\nაირჩიეთ მოქმედება (1-4): ").strip()
#                 else:
#                     print("1. Register")
#                     print("2. Login")
#                     print("3. Change Language / ენის შეცვლა (ქართული)")
#                     print("4. Exit")
#                     choice = input("\nChoose an action (1-4): ").strip()

#                 if choice == "1":
#                     self.register()
#                 elif choice == "2":
#                     self.login()
#                 elif choice == "3":
#                     self.lang = "en" if self.lang == "ka" else "ka"
#                     print("🌐 Language changed to English!" if self.lang == "en" else "🌐 ენა შეიცვალა ქართულით!")
#                 elif choice == "4":
#                     print("ნახვამდის! / Goodbye!")
#                     break
#                 else:
#                     print("❌ არასწორი არჩევანი, სცადე თავიდან." if self.lang == "ka" else "❌ Invalid choice, try again.")
            
#             # მენიუ დალოგინებული მომხმარებლისთვის
#             else:
#                 if self.lang == "ka":
#                     print(f"\n👤 შემოსული ხარ როგორც: [{self.current_user.username}]")
#                     print("1. პროფილისა და ბალანსის ნახვა")
#                     print("2. თანხის შეტანა ანგარიშზე")
#                     print("3. თანხის გამოტანა (მოხსნა)")
#                     print("4. თანხის გადარიცხვა სხვა ანგარიშზე")
#                     print("5. ტრანზაქციების ისტორიის ნახვა")
#                     print("6. ვალუტის კონვერტაცია (ბალანსიდან)")
#                     print("7. გასვლა ექაუნთიდან (Logout)")
#                     choice = input("\nაირჩიეთ მოქმედება (1-7): ").strip()
#                 else:
#                     print(f"\n👤 Logged in as: [{self.current_user.username}]")
#                     print("1. View Profile and Balance")
#                     print("2. Deposit Money")
#                     print("3. Withdraw Money")
#                     print("4. Transfer Money")
#                     print("5. View Transaction History")
#                     print("6. Currency Conversion (From Balance)")
#                     print("7. Logout")
#                     choice = input("\nChoose an action (1-7): ").strip()

#                 if choice == "1":
#                     self.show_profile()
#                 elif choice == "2":
#                     try:
#                         amt = float(input("შესატანი თანხა: " if self.lang == "ka" else "Deposit amount: "))
#                         self.current_user.account.deposit(amt)
#                     except ValueError:
#                         print("❌ არასწორი ფორმატი." if self.lang == "ka" else "❌ Invalid format.")
#                 elif choice == "3":
#                     try:
#                         amt = float(input("გასატანი თანხა: " if self.lang == "ka" else "Withdraw amount: "))
#                         self.current_user.account.withdraw(amt)
#                     except ValueError:
#                         print("❌ არასწორი ფორმატი." if self.lang == "ka" else "❌ Invalid format.")
#                 elif choice == "4":
#                     self.transfer_money()
#                 elif choice == "5":
#                     self.current_user.account.show_history()
#                     input("\nგაგრძელებისთვის დააჭირე Enter-ს..." if self.lang == "ka" else "\nPress Enter to continue...")
#                 elif choice == "6":
#                     # გადაეცემა მიმდინარე დალოგინებული მომხმარებლის ბალანსი
#                     self.change_currency(self.current_user.account.balance)
#                     input("\nგაგრძელებისთვის დააჭირე Enter-ს..." if self.lang == "ka" else "\nPress Enter to continue...")
#                 elif choice == "7":
#                     self.logout()
#                 else:
#                     print("❌ არასწორი არჩევანი, სცადე თავიდან." if self.lang == "ka" else "❌ Invalid choice, try again.")
#                     input("\nგაგრძელებისთვის დააჭირე Enter-ს..." if self.lang == "ka" else "\nPress Enter to continue...")


# if __name__ == "__main__":
#     bank = GOABank()
#     bank.run()