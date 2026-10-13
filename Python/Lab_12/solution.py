# Lab 12 - Document Analysis System
# Analyze sentence: words, vowels, consonants, digits, spaces, special chars

sentence = input("Enter a sentence: ")

words = sentence.split()
word_count = len(words)

vowels = "aeiouAEIOU"
vowel_count = sum(1 for c in sentence if c in vowels)
consonant_count = sum(1 for c in sentence if c.isalpha() and c not in vowels)
digit_count = sum(1 for c in sentence if c.isdigit())
space_count = sum(1 for c in sentence if c == ' ')
special_char_count = sum(1 for c in sentence if not c.isalnum() and not c.isspace())

total_letters = vowel_count + consonant_count
vowel_percentage = (vowel_count / total_letters * 100.0) if total_letters > 0 else 0.0

print("==================================================")
print("DOCUMENT ANALYSIS REPORT")
print("==================================================")
print(f"Sentence: {sentence}")
print(f"Total characters: {len(sentence)}")
print()
print("--- Character Breakdown ---")
print(f"Words:            {word_count}")
print(f"Vowels:           {vowel_count}")
print(f"Consonants:       {consonant_count}")
print(f"Digits:           {digit_count}")
print(f"Spaces:           {space_count}")
print(f"Special characters: {special_char_count}")
print()
print("--- Summary ---")
print(f"Total letters: {total_letters}")
print(f"Vowel percentage: {vowel_percentage:.1f}%")
print("==================================================")
print("Analysis Complete!")
print("==================================================")
