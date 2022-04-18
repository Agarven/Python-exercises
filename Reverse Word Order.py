def reverse(sentence):
    splitted_sentence = sentence.split()
    lenght = len(splitted_sentence)
    id = 0
    reversed_sentence = []
    while id < lenght:
        reversed_sentence.append(splitted_sentence[(lenght - 1 - id)])
        id += 1
    return " ".join(reversed_sentence)

input = input("Type a sentance and I will reverse it.")
print(reverse(input))
