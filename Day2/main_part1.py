def is_mono_increasing(stack):
    for i in range(1, len(stack)):
        if int(stack[i]) < int(stack[i - 1]):
            return False

        if (int(stack[i]) - int(stack[i-1])) < 1 or (int(stack[i]) - int(stack[i-1])) > 3:
            return False

    return True


def is_mono_decreasing(stack):
    for i in range(1, len(stack)):
        if int(stack[i]) > int(stack[i - 1]):
            return False

        if abs(int(stack[i]) - int(stack[i-1])) < 1 or abs(int(stack[i]) - int(stack[i-1])) > 3:
            return False

    return True

def reports(inp):
    safe_reports = []

    for li in inp:
        check1 = is_mono_increasing(li)
        check2 = is_mono_decreasing(li)
        if check1 or check2:
            safe_reports.append(1)

    return len(safe_reports)

if __name__ == "__main__":
    input_reports = []
    with open("input.txt", 'r') as file:
        for line in file:
            processed_line = (line.strip()).split()
            input_reports.append(processed_line)

    #print(input_reports)

    test_input = [['7','6','4','2','1'],
                  ['1' ,'2' ,'7', '8' ,'9'],
                  ['9', '7', '6', '2' ,'1'],
                  ['1' ,'3' ,'2' ,'4' ,'5'],
                  ['8', '6' ,'4', '4', '1'],
                  ['1' ,'3' ,'6', '7' ,'9']]

    ans = reports(input_reports)
    print(ans)