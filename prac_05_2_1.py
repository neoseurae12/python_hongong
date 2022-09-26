# 리스트 평탄화

output = []

def flatten(data):
    global output
    #print(output)

    for i in range(len(data)):
        if type(data[i]) == list:
            flatten(data[i])
        else:
            output.append(data[i])

    return output


example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))