import re
from collections import defaultdict
def trump_detector(trump_speech):
    count = 0
    trump_list = []
    trump_speech = trump_speech + 'L'
    for index, letter in enumerate(trump_speech.lower()):
        if letter in 'aeiou':
            if trump_speech.lower()[index+1] == letter:
                count += 1
            else:
                trump_list.append(letter*count)
                count = 0
    print(trump_list)
    lens = 0
    for item in trump_list:
        lens += len(item)
    print(round(lens/len(trump_list), 2))
    return round(lens/len(trump_list), 2)







#trump_detector("I will build a huge wall")
#trump_detector("America NUUUUUKEEEE Oooobaaaamaaaaa")
def test_trump_detector():
    assert trump_detector("I will build a huge wall") == 0
    Test.assert_equals(trump_detector("HUUUUUGEEEE WAAAAAALL"), 4)
    Test.assert_equals(trump_detector("MEXICAAAAAAAANS GOOOO HOOOMEEEE"), 2.5)
    Test.assert_equals(trump_detector("America NUUUUUKEEEE Oooobaaaamaaaaa"), 1.89)
    Test.assert_equals(trump_detector("listen migrants: IIII KIIIDD YOOOUUU NOOOOOOTTT"), 1.56)