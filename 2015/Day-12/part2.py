# This part took quite a while to do, knew it had to somehow be done recursively, but 
# couldn't figure it out, cool problem

import json

def sum_item(json: dict):
    if type(json) == int:
        return json
    if type(json) == list:
        return sum(sum_item(json) for json in json)
    # has to be here because of some elements being of type str
    if type(json) != dict:
        return 0
    if 'red' in json.values():
        return 0
    return sum_item(list(json.values()))
        

src = open("./input.txt").read()
print(sum_item(json.loads(src)))

