word = input("Enter a word: ")

word_count = len(word)


numbers = []
for i in range(word_count):
    num = int(input(f"Enter number: "))
 

print(numbers)
print("The length of the word is", word_count)


def ave(nums):
    total = 0
    count = 0
    for n in nums:
        total += n
        count += 1
    return total / count

aveword = ave(numbers)
print(f"The average of the numbers is {aveword}")


def match(word, word_count, aveword):
    if word_count > aveword:
        print(f"The length of the word '{word}' is greater than the average")
    elif word_count < aveword:
        print(f"The length of the word '{word}' is less than the average")
    else:
        print(f"The length of the word '{word}' is equal to the average")

match(word, word_count, aveword)
