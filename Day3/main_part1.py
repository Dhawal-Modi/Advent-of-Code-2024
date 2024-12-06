import re

def find_pattern(input_string):
    result = []
    pattern = re.compile(r'mul[(]\d+[,]\d+[)]')

    matches_list = []
    for string in input_string:
        match = re.findall(pattern, string)
        matches_list.append(match)

    matches = sum(matches_list, [])

    num_pattern = re.compile(r'\d+')
    for i in matches:
        mul_match = re.findall(num_pattern, i)
        mul_result = int(mul_match[0]) * int(mul_match[1])
        result.append(mul_result)

    return sum(result)

if __name__ == "__main__":
    inp = []
    with open("input.txt", 'r') as file:
        for line in file:
            inp.append(line)

    #print(inp)

    print(find_pattern(inp))
