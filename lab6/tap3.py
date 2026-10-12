def is_passed(score):
    if score<0 or score>100:
        return None
    return score>=50
print(is_passed(50))