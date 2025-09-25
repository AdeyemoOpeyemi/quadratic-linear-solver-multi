import numpy as np

# ---------------- Solver Function ----------------

def quadratic_solver(a, b, c):
    """
    Solve quadratic or linear equations.
    Always returns two numbers for each equation:
    - Real roots: two numbers
    - Complex roots: real part and imaginary part of first root
    """
    roots = []
    
    for ai, bi, ci in zip(a, b, c):
        if ai == 0 and bi == 0:
            # Invalid equation
            roots.append([None, None])
        elif ai == 0:
            # Linear equation
            x = -ci / bi
            roots.append([x, None])
        else:
            discriminant = bi**2 - 4*ai*ci
            if discriminant >= 0:
                x1 = (-bi + np.sqrt(discriminant)) / (2*ai)
                x2 = (-bi - np.sqrt(discriminant)) / (2*ai)
                roots.append([x1, x2])
            else:
                # Complex roots: show as two numbers
                x_real = -bi / (2*ai)
                x_imag = np.sqrt(-discriminant) / (2*ai)
                roots.append([x_real, x_imag])  # first number = real, second = imag
    
    return roots

# ---------------- Interactive Terminal ----------------

def main():
    print("Quadratic/Linear Solver - Two Number Output")
    print("Enter 'q' to quit.\n")
    
    while True:
        a = input("Enter coefficient a: ")
        if a.lower() == 'q':
            break
        b = input("Enter coefficient b: ")
        if b.lower() == 'q':
            break
        c = input("Enter coefficient c: ")
        if c.lower() == 'q':
            break
        
        try:
            a_val = float(a)
            b_val = float(b)
            c_val = float(c)
        except ValueError:
            print("Please enter valid numbers.")
            continue
        
        roots_list = quadratic_solver([a_val], [b_val], [c_val])
        
        for roots in roots_list:
            # Print two numbers only
            print(", ".join(str(round(x, 6)) if x is not None else "None" for x in roots))
        print("-" * 30)

if __name__ == "__main__":
    main()
