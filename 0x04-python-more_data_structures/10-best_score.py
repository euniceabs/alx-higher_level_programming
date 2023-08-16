#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_score_key = max(a_dictionary, key=lambda k: (
        a_dictionary[k] if isinstance(a_dictionary[k], int) else float('-inf')
    ))
    return best_score_key
