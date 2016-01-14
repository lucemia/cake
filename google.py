def findLongest(s):
    st_index = 0
    prev_number = s[0]

    output = []
    for index, number in enumerate(s): # index,number = 5,5
        if index == 0:
            continue
        if number > prev_number:
            # we are still good
            prev_number = number
            continue
        else:
            # a new subseq
            temp = s[st_index:index]  # s[0:2] -> [1,2]
            if len(temp) > len(output):
                output = temp  # [1,2]

            st_index = index # 2
            prev_number = number # 1

    temp = s[st_index:]
    if len(temp) > len(output):
        output = temp

    return output or s


print findLongest([2,7,3,4,7,5])
print findLongest([1,2,1,2,3])
print findLongest([1,2,3,4,5])
