# rle-encode.py

def rle_encode(data):
    encoding = ''
    prev_num = 0
    count = 1

    if not data: return ''

    for i in range(1, len(data)):
        item = data[i]
        if item != prev_num:
            if prev_num:
                encoding += str(count) + str(prev_num)
            count = 1
            prev_num = item

        else:
            count += 1

    else:
        encoding += str(count) + str(prev_num)
        return encoding


print(rle_encode("111111444444222"))