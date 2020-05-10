passwords = []
with open("hasla.txt") as passwords_file:
  for line in passwords_file:
    password = line.strip()
    passwords.append(password)

only_numeric_password_count = 0
for password in passwords:
  is_only_numeric = True
  for letter in password:
    if letter not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      is_only_numeric = False
      break
  if is_only_numeric:
    only_numeric_password_count += 1

print(only_numeric_password_count)
