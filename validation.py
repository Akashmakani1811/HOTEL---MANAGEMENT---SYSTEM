def get_non_empty(prompt):
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Invalid input")

def get_positive_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val > 0:
                return val
            print("Invalid number")
        except ValueError:
            print("Invalid input")
