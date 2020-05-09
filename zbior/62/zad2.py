first_longest_element = 0
longest_element_count = 0

numbers = []

with open("liczby2.txt") as num_file:
  for line in num_file:
    num = int(line.strip())
    numbers.append(num)

for i, start_number in enumerate(numbers):
  curr_first_element = start_number
  curr_element_count = 1

  for j in range(i, len(numbers) - 1):
    if numbers[j + 1] >= numbers[j]:
      curr_element_count += 1
    else:
      break
  
  if curr_element_count > longest_element_count:
    longest_element_count = curr_element_count
    first_longest_element = curr_first_element
  
print(first_longest_element)
print(longest_element_count)
    
