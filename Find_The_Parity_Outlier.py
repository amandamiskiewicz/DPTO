def find_outlier(integers):
    even_numbers = []
    odd_numbers = []

    for num in integers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    if len(even_numbers) == 1:
        return even_numbers[0]
    else:
        return odd_numbers[0]