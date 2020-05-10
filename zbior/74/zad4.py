passwords = []
with open("hasla.txt") as passwords_file:
  for line in passwords_file:
    password = line.strip()
    passwords.append(password)

small_letters = "abcdefghijklmnopqrstuvwxyz"
big_letters = small_letters.upper()
numbers = "0123456789"

strong_passwords_count = 0
for password in passwords:
  has_small_letter = False
  has_big_letter = False
  has_number = False
  for letter in password:
    if letter in small_letters:
      has_small_letter = True
    elif letter in big_letters:
      has_big_letter = True
    elif letter in numbers:
      has_number = True
  if has_big_letter and has_number and has_small_letter:
    strong_passwords_count += 1

print(strong_passwords_count)
