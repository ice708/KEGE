text = '1'*81

while ('11111' in text) or ('888' in text):
    if '11111' in text:
        text = text.replace('11111','88', 1)
    else:
        text = text.replace('888','8', 1)

print(text)

print("")