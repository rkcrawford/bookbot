def get_num_words(text):
    word_list = text.split()
    return len(word_list)

def get_num_chars(text):
    totals_dict = {}
    for char in text:
        if char.lower() in totals_dict:
            totals_dict[char.lower()] += 1
        else:
            totals_dict[char.lower()] = 1
    return totals_dict

def sort_on(items):
    return items["num"]

def get_sorted_char_counts(d):
    d_list = []
    for kv in d:
        if kv.isalpha() == True:
            d_list.append({"char": kv, "num": d[kv]})
    d_list.sort(reverse=True, key=sort_on)
    return d_list
