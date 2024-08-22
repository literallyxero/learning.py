def first_last_name(first, last, middle=""):
    """Makes a nice formatted name"""
    if middle:
        name = f"{first} {middle} {last}"
    else:
        name = f"{first} {last}"
    return name.title()
        
