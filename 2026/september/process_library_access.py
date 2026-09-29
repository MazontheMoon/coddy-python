def process_library_access(member_level, current_checkouts, book_available):
    # Increment checkout count based on member level
    if member_level == "premium":
        updated_checkouts = current_checkouts + 1
        limit = 10
    elif member_level == "standard":
        updated_checkouts = current_checkouts + 2
        limit = 5
    else:  # basic
        updated_checkouts = current_checkouts
        limit = 3
    
    # Check if checkout is approved
    return book_available and updated_checkouts <= limit