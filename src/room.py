# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.desc = description
        self.n_to = "none"
        self.s_to = "none"
        self.e_to = "none"
        self.w_to = "none"
        self.items = items
