n = int(input())
room = []
count_row = 0 #가로
count_col = 0 #세로
bed_row = 0 #누울 수 있는 자리(가로)
bed_col = 0 #(세로)
for i in range(n):
    room.append(input())
for i in range(n):
    count_row = 0
    for j in range(n):
        if room[i][j] == '.':
            count_row += 1
        else: #room[i][j] == 'X'
            if count_row >= 2:
                bed_row += 1
                count_row = 0
                continue
            else:
                count_row = 0
    if count_row >= 2:
        bed_row += 1
for j in range(n):
    count_col = 0
    for i in range(n):
        if room[i][j] == '.':
            count_col += 1
        else: #room[i][j] == 'X'
            if count_col >= 2:
                bed_col += 1
                count_col = 0
                continue
            else:
                count_col = 0
    if count_col >= 2:
        bed_col += 1
print(bed_row, bed_col)