# https://www.interviewcake.com/question/python/reverse-string-in-place

def reverse(string_list):
    string_list = list(string_list)
    i = 0
    j = len(string_list) - 1

    while i < j:
        string_list[i], string_list[j] = string_list[j], string_list[i]
        i += 1
        j -= 1

    return ''.join(string_list)


assert reverse('abc') == 'cba'
assert reverse('ab') == 'ba'
assert reverse('abcd') == 'dcba'
assert reverse('abcde') == 'edcba'
