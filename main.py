elements = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }


def input_str():
    while True:
        s = input()
        if input_check(s) == True:
            return s 
    

def input_check(s):
    global elements
    if s == '':
        print('Input number again')
        return False
    else:
        for ch in s:
            if ch not in elements:
                print('Input number again')
                return False
        for i in range(3, len(s)):
            if s[i] == s[i-1] == s[i-2] == s[i-3] != 'I':
                print('Input number again')
                return False
        return True


def translate(s):
    num = []
    s = list(s)
    num.append(elements[s[0]])
    for i in range(1, len(s)):
        if elements[s[i-1]] < elements[s[i]] and elements[s[i]] <= (elements[s[i-1]] * 10):
            num.pop()
            num_m = elements[s[i]] - elements[s[i-1]]
            num.append(num_m)
        else:
            num.append(elements[s[i]])
    return sum(num)


def main():
    print('Input number')
    string = input_str()

    num = translate(string)
    print(f'Answer: {num}')
    

if __name__ == '__main__':
    main()