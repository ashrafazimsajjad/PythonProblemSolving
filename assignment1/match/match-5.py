# Take input from the user
ch = input("Enter a single character: ")

# Use match-case
match ch:
    # Check vowels
    case 'a' | 'e' | 'i' | 'o' | 'u' | 'A' | 'E' | 'I' | 'O' | 'U':
        print("Vowel")

    # Check digits
    case _ if ch.isdigit():
        print("Digit")

    # Check consonants (alphabet but not vowel)
    case _ if ch.isalpha():
        print("Consonant")

    # Other characters
    case _:
        print("Invalid input")