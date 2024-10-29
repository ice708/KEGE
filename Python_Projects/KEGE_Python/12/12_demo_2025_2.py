text = '1'*81

while text.find('11111') != -1 or text.find('888') != -1:
    if text.find('11111') != -1:
        text = text.replace('11111','88', 1)
    else:
        text = text.replace('888','8', 1)

print(text)