#!/usr/bin/python3
'''comment goes here'''


def canUnlockAll(boxes):
    '''Checks if all boxes can be unlocked'''
    keyset = [0]
    for key in keyset:
        for content in boxes[key]:
            if content not in keyset and content < len(boxes):
                keyset.append(content)

    return len(keyset) == len(boxes)
