with open("tekst.txt") as txt_file:
  for line in txt_file:
    words = line.strip().split()
    for word in words:
      if word[0] == "d" and word[-1] == "d":
        print(word)