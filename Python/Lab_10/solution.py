# Lab 10 - Text Processing Tool
# Develop a Python program for a Document Text Processing Utility.

print("==================================================")
print("               TEXT PROCESSING TOOL               ")
print("==================================================")

sentence = input("Enter a sentence: ")

print()
print("--- Processing Results ---")
pos = int(input("Enter position for indexing: "))
char_at_pos = sentence[pos]
print(f"Character at position {pos}  : '{char_at_pos}'")

start_idx = int(input("Enter start index for slicing : "))
end_idx = int(input("Enter end index for slicing   : "))
sliced_str = sentence[start_idx:end_idx]
print(f"Sliced string [{start_idx}:{end_idx}]        : '{sliced_str}'")

print(f"Uppercase                      : {sentence.upper()}")
print(f"Lowercase                      : {sentence.lower()}")

word_to_replace = input("Enter word to replace          : ")
replacement_word = input("Enter replacement word         : ")
after_replace = sentence.replace(word_to_replace, replacement_word)
print(f"After replace                  : {after_replace}")
print(f"Length of sentence             : {len(sentence)}")

print()
print("==================================================")
print("Analysis Complete!")
print("==================================================")
