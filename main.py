def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  num_chars = get_char_count(text)
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{num_words} words found in the document")
  print()
  for entry in num_chars:
    char = entry["char"]
    num = entry["num"]
    print(f"The {char} character was found {num} times")
  print("--- End report ---")

def sort_on(dict):
  return dict["num"]

def get_char_count(text):
  chars = {}
  chars_list = []
  for char in text.lower():
    if char not in chars:
      if char.isalpha():
        chars[char] = 1
    else:
      chars[char] += 1

  for char, num in chars.items():
    chars_list.append({"char": char, "num": num})
  
  chars_list.sort(reverse=True, key=sort_on)
  return chars_list

def get_num_words(text):
  words = text.split()
  return len(words)
  
def get_book_text(path):  
  with open(path) as f:
    return f.read()

main()