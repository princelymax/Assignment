sandwich_orders = ['tuna','pastrami','chicken','pastrami','veggie','pastrami','beef']
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches that were made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")