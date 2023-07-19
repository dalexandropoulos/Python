import unicodedata

# def write_unicode_characters_by_category():
#     categories = set()
    
#     # Get all the unique Unicode categories
#     for i in range(0x110000):
#         try:
#             char = chr(i)
#             category = unicodedata.category(char)
#             if category not in categories:
#                 categories.add(category)
#         except UnicodeEncodeError:
#             continue
    
#     # Write the characters to files based on their categories
#     for category in categories:
#         filename = f"{category}.txt"
#         with open(filename, "w", encoding="utf-8") as file:
#             file.write(f"Category: {category}\n\n")
#             count = 0
#             for i in range(0x110000):
#                 try:
#                     char = chr(i)
#                     if unicodedata.category(char) == category:
#                         file.write(f"{char} (U+{ord(char):04X}) ")
#                         count += 1
#                         if count % 5 == 0:
#                             file.write("\n")
#                 except UnicodeEncodeError:
#                     continue

# # Call the function to write the Unicode characters to files by category
# write_unicode_characters_by_category()

# def write_unicode_characters_by_size_and_category():
#     sizes = {
#         'Small': set(),
#         'Medium': set(),
#         'Large': set()
#     }

#     categories = set()

#     # Categorize Unicode characters by size and collect categories
#     for i in range(0x110000):
#         try:
#             char = chr(i)
#             if char.isprintable():
#                 category = unicodedata.category(char)
#                 categories.add(category)
#                 width = unicodedata.east_asian_width(char)
#                 if width == 'Na' or width == 'N':
#                     sizes['Small'].add(char)
#                 elif width == 'W' or width == 'F':
#                     sizes['Medium'].add(char)
#                 else:
#                     sizes['Large'].add(char)
#         except UnicodeEncodeError:
#             continue
    
#     # Sort the characters within each category
#     for category in categories:
#         sizes['Small'] = sorted(sizes['Small'], key=lambda x: (unicodedata.category(x), x))
#         sizes['Medium'] = sorted(sizes['Medium'], key=lambda x: (unicodedata.category(x), x))
#         sizes['Large'] = sorted(sizes['Large'], key=lambda x: (unicodedata.category(x), x))
    
#     # Write the characters to files by size, sorted by category
#     for size, characters in sizes.items():
#         filename = f"{size}_characters.txt"
#         with open(filename, "w", encoding="utf-8") as file:
#             file.write(f"Size: {size}\n\n")
            
#             # Write the characters in columns with fixed width
#             column_width = 10
#             for category in categories:
#                 file.write(f"Category: {category}\n")
#                 category_characters = [char for char in characters if unicodedata.category(char) == category]
#                 count = 0
#                 for char in category_characters:
#                     char_info = f"{char} (U+{ord(char):04X})"
#                     file.write(char_info.ljust(column_width))
#                     count += 1
#                     if count % (80 // column_width) == 0:
#                         file.write("\n")
#                 file.write("\n\n")

# # Call the function to write the Unicode characters to files by size and sorted by category
# write_unicode_characters_by_size_and_category()
