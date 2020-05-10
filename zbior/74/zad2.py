passwords = []
with open("hasla.txt") as passwords_file:
  for line in passwords_file:
    password = line.strip()
    passwords.append(password)

duplicate_passwords = []
for i in range(0, len(passwords)):
  for j in range(0, len(passwords)):
    if i == j:
      continue
    if passwords[i] == passwords[j]:
      if passwords[i] not in duplicate_passwords:
        duplicate_passwords.append(passwords[i])
      continue



print(sorted(duplicate_passwords))
