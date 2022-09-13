def get_magic_triangle(numRows):
    '''Print Pascal's triangle with numRows.'''
    if numRows == 1:
        return [[1]] # base case is reached!
    else:
        res_arr = get_magic_triangle(numRows-1) # recursive call to pascal_tri
        # use previous row to calculate current row
        cur_row = [1] # every row starts with 1
        prev_row = res_arr[-1]
        for i in range(len(prev_row)-1):
            # sum of 2 entries directly above
            cur_row.append(prev_row[i] + prev_row[i+1])
        cur_row += [1] # every row ends with 1
        res_arr.append(cur_row)
        print(res_arr)



get_magic_triangle(5)

# това е решение с рекурсия, но не работи