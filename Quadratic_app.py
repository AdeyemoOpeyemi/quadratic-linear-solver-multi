import streamlit as st
import numpy as np

# ---------------- Solver Function ----------------

def quadratic_solver(a, b, c):
    """
    Solve quadratic or linear equations.
    Returns roots as two-number pairs for each root:
    - Real roots: two numbers per root (root1, root2)
    - Complex roots: two lines with (real, imag) for each root
    - Linear: (root, None)
    """
    roots = []
    
    for ai, bi, ci in zip(a, b, c):
        if ai == 0 and bi == 0:
            roots.append([[None, None]])
        elif ai == 0:
            x = -ci / bi
            roots.append([[x, None]])
        else:
            discriminant = bi**2 - 4*ai*ci
            if discriminant >= 0:
                x1 = (-bi + np.sqrt(discriminant)) / (2*ai)
                x2 = (-bi - np.sqrt(discriminant)) / (2*ai)
                roots.append([[x1, x2]])
            else:
                x_real = -bi / (2*ai)
                x_imag = np.sqrt(-discriminant) / (2*ai)
                # Two complex roots as separate two-number lines
                roots.append([[x_real, x_imag], [x_real, -x_imag]])
    
    return roots

# ---------------- Streamlit App ----------------

st.title("🧮 Quadratic & Linear Solver - Two Numbers per Root")

st.markdown("""
- Real roots: `root1, root2`  
- Complex roots: each root as `real_part, imag_part` on separate lines  
- Linear: `root, None`
""")

# ---------------- Single Equation ----------------
st.header("Single Equation Solver")
a = st.number_input("Enter coefficient a:", value=1.0, format="%.6f")
b = st.number_input("Enter coefficient b:", value=1.0, format="%.6f")
c = st.number_input("Enter coefficient c:", value=1.0, format="%.6f")

if st.button("Solve Single Equation"):
    roots_list = quadratic_solver([a], [b], [c])
    st.subheader("Roots:")
    for roots in roots_list:
        for pair in roots:
            st.write(", ".join(str(round(x,6)) if x is not None else "None" for x in pair))

# ---------------- Batch Equations ----------------
st.header("Batch Equation Solver")
st.markdown("Enter multiple coefficients separated by commas (e.g., 1,0,2)")

a_list_input = st.text_input("a values:", "1,3,0")
b_list_input = st.text_input("b values:", "4,4,2")
c_list_input = st.text_input("c values:", "5,5,8")

if st.button("Solve Batch"):
    try:
        a_list = [float(x.strip()) for x in a_list_input.split(",")]
        b_list = [float(x.strip()) for x in b_list_input.split(",")]
        c_list = [float(x.strip()) for x in c_list_input.split(",")]
        
        roots_list = quadratic_solver(a_list, b_list, c_list)
        
        st.subheader("Roots:")
        for idx, roots in enumerate(roots_list):
            st.write(f"Equation {idx+1}:")
            for pair in roots:
                st.write(", ".join(str(round(x,6)) if x is not None else "None" for x in pair))
        
    except ValueError:
        st.error("⚠️ Please enter valid numbers separated by commas.")
