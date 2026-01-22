# Simple program: count how many vowels are in a sentence
# (This code has a few intentional errors in it)

def count_vowels(text):
    # List of vowels we want to count
    vowels = ["a", "e", "i", "o", "u"]

    # Start our counter at 0
    count = 0

    # Loop through every character in the text
    for ch in text:
        # Make the character lowercase so 'A' counts like 'a'
        ch = ch.lower()

        # If the character is a vowel, add 1 to the count
        if ch in vowels:
            count += 1

    # Return the final count
    return count


# Ask the user for a sentence
sentence = input("Type a sentence: ")

# Print the result
print("Number of vowels:", count_vowels(sentence))
