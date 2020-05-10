with_mutation_count = 0

with open("dane_geny.txt") as gen_file:
  for line in gen_file:
    genotype = line.strip()
    gen = ""
    for letter in genotype:
      if len(gen) <= 1 and letter == "A":
        gen += "A"
      elif len(gen) == 1 and letter != "A":
        gen = ""
      elif len(gen) >= 2:
        gen += letter
        if gen[-1] == "B" and gen[-2] == "B":
          if "BCDDC" in gen:
            with_mutation_count += 1
            break
          else:
            gen = ""

print(with_mutation_count)