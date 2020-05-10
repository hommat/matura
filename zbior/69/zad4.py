import math

resistant_genotype_count = 0
strong_resistant_genotype_count = 0

def is_palidrome(n):
  for i in range(0, math.floor(len(n)/2)):
    if n[i] != n[-i-1]:
      return False
  return True

def get_gens(genotype):
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
          gen = ""
  return gens

with open("dane_geny.txt") as gen_file:
  for line in gen_file:
    genotype = line.strip()
    if is_palidrome(genotype):
      strong_resistant_genotype_count += 1
      resistant_genotype_count += 1
    else:
      gens = get_gens(genotype)
      reversed_gens = get_gens(reversed(genotype))

      if len(gens) == len(reversed_gens):
        are_the_same = True
        for i in range(0, len(gens)):
          if gens[i] != reversed_gens[i]:
            are_the_same = False
            break
        if are_the_same:
          resistant_genotype_count += 1

print(resistant_genotype_count)
print(strong_resistant_genotype_count)