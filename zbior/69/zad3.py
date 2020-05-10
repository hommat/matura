max_gen_in_one_person = 0
max_gen_len = 0

with open("dane_geny.txt") as gen_file:
  for line in gen_file:
    genotype = line.strip()
    gens = []
    gen = ""
    for letter in genotype:
      if len(gen) <= 1 and letter == "A":
        gen += "A"
      elif len(gen) == 1 and letter != "A":
        gen = ""
      elif len(gen) >= 2:
        gen += letter
        if gen[-1] == "B" and gen[-2] == "B":
            gens.append(gen)
            max_gen_len = max(max_gen_len, len(gen))
            gen = ""
    max_gen_in_one_person = max(max_gen_in_one_person, len(gens))

print(max_gen_in_one_person)
print(max_gen_len)