def shortcut(message):
    S = []
    for char in "ALGORYTM":
        S.append(ord(char))

    while len(message) % 8 != 0:
        message += "."

    for i, char in enumerate(message):
        S[i % 8] = (S[i % 8] + ord(char)) % 128

    w = ""
    for i in range(0, 8):
        w += chr(65 + S[i] % 26)

    return w

def A(nums, d, n):
    w = ""
    for y in nums:
        w += chr((y*d % n))
    return w

messages = []
signatures = []

with open("wiadomosci.txt") as messages_file:
    for line in messages_file:
        message = line.strip()
        messages.append(message)

with open("podpisy.txt") as signatures_file:
    for line in signatures_file:
        nums = line.strip().split()
        for i, num in enumerate(nums):
            nums[i] = int(num)
        signatures.append(nums)

for i in range(0, len(messages)):
    message = messages[i]
    signature = signatures[i]
    if shortcut(message) == A(signature, 3, 200):
        print(i +1, end=" " )
print()