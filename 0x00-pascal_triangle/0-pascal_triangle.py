#!/usr/bin/python3


def pascal_triangle(n):
    triangle = []
    i = 0
    
    while i < n :
        row = [0] * (i + 1)
        row[0] = 1
        row[-1] = 1
        
        if i > 1:
            j = 1
            while j < i:
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                j += 1
        
        triangle.append(row)
        i += 1
         
    return triangle