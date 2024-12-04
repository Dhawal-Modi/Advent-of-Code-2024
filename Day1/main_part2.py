from collections import defaultdict


def main():
    list1 = []
    list2 = []
    with open("input.txt", 'r') as file:
        for line in file:
            splitline = line.split('   ')
            list1.append(splitline[0])
            list2.append(splitline[1].strip())

    list1.sort()
    list2.sort()

    similarity = []
    dict2 = defaultdict(int)
    for ele in list2:
        dict2[ele] += 1

    for k in list1:
        if k in dict2:
            print(k)
            print(dict2[k])
            similarity.append(int(k) * int(dict2[k]))
    print(sum(similarity))

    # for ele1,ele2 in zip(list1,dict2):
    #     if ele1 in dict2.keys():
    #         print(ele1)
    #         print(dict2[ele1])
    #         similarity.append(int(ele1) * int(dict2[ele1]))
    # print(sum(similarity))



if __name__ == "__main__":
    main()