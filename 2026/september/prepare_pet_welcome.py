def prepare_pet_welcome(pet_name, pet_type, initial_supplies):
    welcome_message = "Welcome home, " + pet_name + " the " + pet_type + "!"
    
    supplies = initial_supplies.copy()
    
    if pet_type.lower() == "dog":
        supplies.extend(["leash", "dog food", "chew toy"])
    elif pet_type.lower() == "cat":
        supplies.extend(["litter box", "cat food", "scratching post"])
    else:
        supplies.extend(["cage", "food", "toys"])
    
    return {"welcome_message": welcome_message, "supplies": supplies}
