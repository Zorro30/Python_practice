'''
Input:
3
4
..**
.**.
***.

Output:
ROWS:
2
2
3
COLUMNS:
1
2
3
1
'''

n = int(input())
m = int(input())
rows = []
columns = []
cols = []
columnss = []
for i in range(n):
    total = 0
    s = input()
    columns.append(s)
    rows.append(s.count('*'))

print('ROWS: {}'.format(rows))
for k in range(m):
    col = ''
    for i in range(n):
        col += str(columns[i][k])
    cols.append(col)
for i in cols:
    columnss.append(i.count('*'))
print('COLUMNS: {}'.format(columnss))