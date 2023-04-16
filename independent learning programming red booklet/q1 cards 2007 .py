def sum15(list):
    score = 0
    for i in range(0, len(list)):
        for j in range(i, len(list)):
            sum = 0
            for k in range(i, j+1):
                sum = sum + list[k]
            if sum == 15:
                score += 1
    return score


def duplicate(list):
    checked = []
    score = 0
    for i in range(0, len(list)):
        count = 0
        item = list[i]

        if item not in checked:
            for j in range(0, len(list)):
                if list[j] == item:
                    count += 1
            if count > 1:
                score += count
            checked.append(item)
    return score



def main():
    list = []
    for i in range(0, 5):
        x = int(input("input a number"))
        list.append(x)

    print(sum15(list) + duplicate(list))

main()
