# import collections

# str1 = input('Enter a string : ')

# d = collections.defaultdict(int)

# for c in str1:
#     if c ==' ':
#         continue
#     d[c] += 1

# for c in sorted(d, key=d.get):
#     if d[c] > 1:
#         print('%s - %d' % (c, d[c]))
def count_repeated_characters(input_string):
    char_count = {}
    repeated_chars = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char, count in char_count.items():
        if count > 1:
            repeated_chars[char] = count

    for char, count in repeated_chars.items():
        print(f'{char}-{count}')

sample_string = 'thequickbrownfoxjumpsoverthelazydog'
count_repeated_characters(sample_string)