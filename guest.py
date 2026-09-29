class Guest:
    def __init__(self, guest_id, name, phone):
        self.guest_id = guest_id
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.guest_id} {self.name} {self.phone}"
