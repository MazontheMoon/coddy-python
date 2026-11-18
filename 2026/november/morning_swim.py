def morning_swim(laps, energy_level):
    completed_laps = 0
    breaks = 0
    
    for lap in range(1, laps + 1):
        if energy_level == "medium" and lap % 3 == 0:
            breaks += 1
        if energy_level == "low":
            if lap % 4 == 0:
                breaks += 1
            if lap % 2 == 0:
                continue
        
        completed_laps += 1
    
    if energy_level == "high":
        comment = "Great job! You completed all laps without breaks."
    elif energy_level == "medium":
        comment = "Nice work! You took some breaks but still finished strong."
    else:
        comment = "Well done! You managed to swim despite low energy."
    
    return f"Laps completed: {completed_laps}, Breaks taken: {breaks}. {comment}"
