full_name = input("Enter your full name (First, Middle, Last): ")

first_name, middle_name, last_name = full_name.split(", ")

first_name = first_name.capitalize()
middle_name = middle_name[0].capitalize() + "."
last_name = last_name.capitalize()

formatted_name = f"{last_name}, {first_name} {middle_name}"

print("Formatted Name:", formatted_name)