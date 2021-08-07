def solution(args):
    return_string = ''
    ranges = []
    pre_ranges = []
    args.append('end')
    for index, number in enumerate(args):
        if number != 'end':
            if number + 1 == args[index+1]:
                pre_ranges.append(number)
            else:
                if pre_ranges:
                    pre_ranges.append(number)
                    if len(pre_ranges) >= 3:
                        ranges.append(pre_ranges)
                    else:
                        for x in pre_ranges:
                            ranges.append(x)
                    pre_ranges = []
                else:
                    ranges.append(number)
    for x in ranges:
        if isinstance(x, int):
            return_string += f'{x},'
        else:
            return_string += f'{x[0]}-{x[-1]},'
    return return_string[:-1]


print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]) == '-6,-3-1,3-5,7-11,14,15,17-20')