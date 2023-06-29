def mountains_of_hoiyama(width):
    weight=0
    prev_number=0
    row_number=1
    for i in range(width,0,-2):
        weight+=row_number*i+prev_number
        prev_number+=row_number
        row_number+=2
    return weight