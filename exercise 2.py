fin = open('words.txt')

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

hi = fin.readline().strip()
i = 0
count = 0
total = 113809

while i < total:

    if has_no_e(hi):
        print hi
        count = count + 1
    hi = fin.readline().strip()
    i = i + 1

print (float(count)/float(total) *100.0 ),'% of the total words do not contain an e'
