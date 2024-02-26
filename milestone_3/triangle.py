import sys

def get_triangle(n: int):
    rows = []
    for i in range(0, n):
        row = []
        if i <=2:
            row = [int(i) for i in str(11**i)]
        if i > 2:
            row = [1, 1]
            last_index = len(rows[i-1])
            for j in range(1, i+1):
                if j < last_index:
                    prev_el = rows[i-1][j-1]
                    next_el = rows[i-1][j]
                if j > 0 and j != i:
                    row.insert(j, prev_el + next_el)
        rows.append(row)

    return rows

def add_row_justified(s, slen):
    return s.center(slen, ' ')+'\n'


def analize_last_line(matrix):
    # Convert list of numbers to list of strings 
    matrix_str = [str(item) for item in matrix]
    matrix_len = len(matrix_str)
    max_item_len = 0
    for i in range(0, matrix_len):
        curr_item_str_len = len(str(matrix[i]))
        if curr_item_str_len > max_item_len:
            # Max length of string number
            max_item_len = curr_item_str_len
    # Calculate length of last line(largest line as a base of our triangle) including separator 
    matrix_line_len = len((' '*max_item_len).join(matrix_str))
    return matrix_line_len, max_item_len
    
def prepare_triangle(matrix):
    matrix_len = len(matrix)
    matrix_line_len, max_item_len = analize_last_line(matrix[matrix_len - 1])
    # Set separator with number of spaces
    sep = " "*max_item_len
    res = ''
    for i in range(0, matrix_len):
        str_arr = [str(item) for item in matrix[i]]
        curr_row = sep.join(str_arr)
        curr_row_len = len(curr_row)
        res += add_row_justified(curr_row, matrix_line_len)
    return res

arg = sys.argv[1:]
if len(arg) == 0:
    raise ValueError('Please enter number of rows argument')
num = int(arg[0])
if(num <= 0 or num >31):
    raise ValueError('Please enter number more than 0 and less than 31')

triangle_matrix = get_triangle(num)
print(prepare_triangle(triangle_matrix))
