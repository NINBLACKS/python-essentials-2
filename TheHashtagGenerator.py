""" 
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.

Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""
# Check if the string is empty
# Split the string into words
# Capitalize the first letter of each word
# Put the word back on a string
# setting # at the beging of the string
# Check if the string is longer than 140 characters

phrase = "Learn how to speak English"
# Checking if the string is empty
if not len(phrase) == 0:
    cphrase = phrase.title()
    words = cphrase.split()
    fphrase = "#"+"" .join(map(str, words))
    print(fphrase)
else:
    print("False")
