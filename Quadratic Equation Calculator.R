## QUADRATIC EQUATION
# Quadratic Equation formular

quadratic <- function() {
  # Prompt user for input only if not provided
  a <- as.numeric(readline("Enter the value for a: "))
  b <- as.numeric(readline("Enter the value for b: "))
  c <- as.numeric(readline("Enter the value for c: "))
  # Check if a is zero
  if (a == 0) {
    cat("This is not a quadratic equation because 'a' cannot be zero:\n")
    return(NULL)
  }
  # Calculate the discriminant
  equation <- b^2 - 4 * a * c
  
  # Solve based on the discriminant
  if (equation > 0) {
    x1 <- (-b + sqrt(equation)) / (2 * a)
    x2 <- (-b - sqrt(equation)) / (2 * a)
    cat("The equation has two distinct real roots:\n")
    return(c(x1 = x1, x2 = x2))
    
  } else if (equation == 0) {
    x <- -b / (2 * a)
    cat("The equation has one real repeated root:\n")
    return(c(x = x))
    
  } else {
    real_part <- -b / (2 * a)
    imaginary_part <- sqrt(abs(equation)) / (2 * a)
    root1 <- real_part + imaginary_part * 1i
    root2 <- real_part - imaginary_part * 1i
    cat("The equation has two complex roots:\n")
    return(c(root1 = root1, root2 = root2))
  }
}

quadratic()


