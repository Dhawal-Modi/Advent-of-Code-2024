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

    distances = []
    for e1,e2 in zip(list1,list2):
        distance = abs(int(e1) - int(e2))
        distances.append(distance)
    print(distances)

    assert len(distances) == len(list1)
    assert len(distances) == len(list2)

    result = sum(distances)

    print(result)

if __name__ == "__main__":
    main()