def p_np_solver():
    # today we will solve the p vs np problem through brute force
    p = 0
    n = 0
    np = n * p
    while (p != np):
        p += 1
        while (p != np):
            n += 1
    # the loop will end if we have found the solution to p vs np
    return (n, p)

# if you run this function, it will terminate. Therefore, p = np. QED.
