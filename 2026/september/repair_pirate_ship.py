def repair_pirate_ship(wood_planks, nails, damage_size):
    required_planks = damage_size * 5
    required_nails = required_planks * 2
    
    if wood_planks >= required_planks and nails >= required_nails:
        return True
    else:
        return False