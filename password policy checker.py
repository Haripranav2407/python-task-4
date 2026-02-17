passwords = [
    "abc123",
    "hello@123",
    "password",
    "Admin#1",
    "test",
    "user$"
]
special_chars = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/"
valid = []
invalid = []
for pwd in passwords:
    has_digit = False
    has_special = False
    for ch in pwd:
        if ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True
    if has_digit and has_special:
        valid.append(pwd)
    else:
        invalid.append(pwd)
print("Valid passwords:")
print(valid)
print("\nInvalid passwords:")
print(invalid)