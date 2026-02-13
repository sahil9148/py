def number_to_words(num):
    words = {
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
        '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
    }

    result = []
    for digit in num:
        result.append(words[digit])

    return " ".join(result)


number = input("Enter number: ")
print(number_to_words(number))
