def single_root_words(root_word, *other_words):
    same_words = []
    s = 0
    for i in range(len(other_words)):
        s += i
        if str.upper(root_word) in str.upper(other_words[i]):
            same_words.append(other_words[i])
        elif str.lower(root_word) in str.upper(other_words[i]):
            same_words.append(other_words[i])
        elif str.upper(root_word) in str.lower(other_words[i]):
            same_words.append(other_words[i])
        elif str.lower(root_word) in str.lower(other_words[i]):
            same_words.append(other_words[i])
    return same_words

print(single_root_words("Book", "Edelbrok", "Paperbook", "KingsBook"))
print(single_root_words("SONIC", "Supersonic", "Ultrasonic", "Psysonic", "Paperbook"))