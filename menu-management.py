def add_item(menu, item):
    if item not in menu:
        menu.append(item)

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} is not in the menu.")
def check_item(menu, item):
    return f"{item} is available" if item in menu else f"{item} is not available"
menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item(menu, "Tacos")
remove_item(menu, "Salad")
availability = check_item(menu, "Pizza")
print(f"Updated menu: {menu}")
print(f"Availability: {availability}")
