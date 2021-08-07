# https://www.codewars.com/kata/5202ef17a402dd033c000009
# Best Solution
def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])

# My Solution
import string
def title_case(title, minor_words=''):
    if minor_words:
        title_list = title.lower().capitalize().split()
        for index, word in enumerate(title_list):
            if not word.lower() in minor_words.lower().split():
                title_list[index] = word.capitalize()
        return ' '.join([str(word) for word in title_list])
    else:
        return string.capwords(title)