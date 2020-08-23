# def accum(s):
#     s = list(s)
#     accum_s = ""
#     accum_s2 = ""
#     for x,y in enumerate(s):
#         accum_s2 = accum_s2 + y * (int(x) + 1)
#         accum_s2 = accum_s2.capitalize()
#         if (x + 1 == len(s)):
#             accum_s = accum_s + accum_s2
#         else:
#             accum_s = accum_s + accum_s2 + "-"
#         accum_s2 = ""
#         print(accum_s)

def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

print(accum("ZpglnRxqenU"))