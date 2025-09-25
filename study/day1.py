def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

limit = int(input("Enter the upper limit: "))
print("/tPrime numbers up to", limit, ":")
for num in range(2, limit + 1):
    if is_prime(num):
        print(num)


message = input('What kid of car do you like?') 
print("Let me see if I can find you a " + message)


prompt = 'Welcome to the pizza parlor!'
prompt += '\nHow many people are in your group? '
message = input(prompt)
people = int(message)
if people > 8:
    print('You will have to wait for a table.')
else:
    print('Your table is ready.')


current_number = 1
while current_number <= 20:
    if current_number % 2 == 0:
        print(str(current_number) + " is even")
    else:
        print(str(current_number) + " is odd")
    current_number += 1


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)


unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print('--results--')
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")  


sandwich_orders = ['pastrami', 'tuna', 'ham', 'cheese', 'veggie', 'pastrami', 'chicken', 'pastrami']
finished_sandwiches = [] 
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')   
    print(sandwich_orders)
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)


def greet_users(names):
    names = ['hannah', 'ty', 'margot']
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
greet_users('names')