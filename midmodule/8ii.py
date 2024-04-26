def space_after_periods(text):

    corrected_text = []
    skip = False
    for i, char in enumerate(text):
        if not skip:
            corrected_text.append(char)
        skip = False
        if char == '.':
            if i < len(text - 1) and text[i + 1] != ' ':
                corrected_text.append(" ")
            elif i < len(text) - 2 and text[i + 2] == ' ':
                skip = True

    return " ". join(corrected_text)

print(space_after_periods("Hello mr. blue sky"))