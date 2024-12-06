import re

def find_pattern(input_string):
    result = []

    remove_pattern = re.compile(r"(?s)don't[(][)].*?do[(][)][^\w\s]*")
    eof_pattern = re.compile(r"don't[(][)].*")
    pattern = re.compile(r'mul[(]\d+[,]\d+[)]')

    matches_list = []

    clean_string = re.sub(remove_pattern, '',input_string).replace('\n','')
    cleaner_string = re.sub(eof_pattern, '',clean_string).replace('\n','')

    match = re.findall(pattern, cleaner_string)
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
    clean_inp = ''.join(inp)
    test_input = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]

    #print(find_pattern(test_input))
    print(find_pattern(clean_inp))
