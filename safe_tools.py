def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

def safe_number(text):
    try:
        # Return text converted with int()
        return int(text)
    except ValueError:
        # Return the text "Not a number"
        return "Not a number"

def get_field(learner, key):
    try:
        # Return the value at that key
        return learner[key]
    except KeyError:
        # Return the text "Field not found"
        return "Field not found"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_number("42"))
print(safe_number("abc"))

learner = {"name": "Amina", "score": 82}
print(get_field(learner, "score"))
print(get_field(learner, "email"))