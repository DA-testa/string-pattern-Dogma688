#Maksims Makarskis 221RDB380

def read_input():
    type=input().strip().upper()
    if type == 'I':
        findtxt=input().strip()
        txt=input().strip()
    elif type == 'F':
        file ='tests/06'
        with open(file,'r') as f:
            findtxt = f.readline().strip()
            txt = f.readline().strip()
    return findtxt, txt

def print_occurrences(output):

    print(' '.join(map(str, output)))

def get_occurrences(findtxt, txt):

    occurrences = []
    find_len = len(findtxt)
    txt_len = len(txt)
    find_hesh = hash(findtxt)
    txt_hesh = hash(txt[:find_len])
    for i in range(txt_len - find_len +1):
        if find_hesh == txt_hesh and findtxt == txt[i:i+find_len]:
            occurrences.append(i)
        if i < txt_len - find_len:
            txt_hesh = hash(txt[i+1:i+find_len+1])
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
