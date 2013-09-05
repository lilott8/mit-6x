def integrate(f, a, b, parts):
    spacing = float(b-a)/parts
    current = 0
    for i in range(parts):
        current += spacing * f(a+ i*spacing)
    return current
    
    