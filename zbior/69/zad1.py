species_map = {}
with open("dane_geny.txt") as gen_file:
  for line in gen_file:
    genotype = line.strip()
    genotype_len = len(genotype)
    if genotype_len in species_map:
      species_map[genotype_len] += 1
    else:
      species_map[genotype_len] = 1

print(len(species_map.keys()))
max_gen = -1
for key in species_map:
  max_gen = max(species_map[key], max_gen)

print(max_gen)