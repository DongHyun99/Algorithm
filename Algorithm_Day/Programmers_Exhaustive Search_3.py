def solution(brown, yellow):

    answer = []
    y_row = yellow
    y_columns = 1

    while y_columns <= y_row:
        if yellow != y_row * y_columns:
            y_columns = y_columns+1
            y_row = yellow // y_columns
            continue
        elif brown == (y_row+y_columns+2)*2:
            return [y_row+2,y_columns+2]
        y_columns = y_columns+1
        y_row = yellow // y_columns