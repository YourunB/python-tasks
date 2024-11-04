x1 = input()
x2 = input()
x3 = input()

if int(x1) > 0:
    new_x1 = x1.zfill(9)
    new_x1 = f'+{new_x1}'
else:
    new_x1 = x1.zfill(10)

new_x2 = f"{round(float(x2), 2):.2f}"
len_x2 = 10 - len(new_x2)
char = '#'
res_char = (char * len_x2) + new_x2

x3 = int(x3)
new_x3 = f"{x3:016b}"
new_x3 = '_'.join([new_x3[i:i+4] for i in range(0, len(new_x3), 4)])

print(new_x1)
print(res_char)
print(new_x3)