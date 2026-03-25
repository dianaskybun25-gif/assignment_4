def evaluate_polynomial(poly_dict, x):
    result = 0
    for i in poly_dict:
        result = result + poly_dict[i] * x**i
    return result



my_poly = {0: -10, 2: 3, 4: 1}

print(evaluate_polynomial(my_poly, 2))
print(evaluate_polynomial(my_poly, -1.5))