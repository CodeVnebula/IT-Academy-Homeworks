def midpoint(x1, y1, x2, y2):
    middle_point = ((x1 + x2) / 2, (y1 + y2) / 2)
    middle_point_x = middle_point[0]
    middle_point_y = middle_point[1]
    return middle_point_x, middle_point_y

def main():
    x, y = midpoint(0, 0, 4, 4)  # Expected output: (2.0, 2.0)
    print(f"Point xy({x, y})")
    
    x, y = midpoint(-3, 5, 7, -2)  # Expected output: (2.0, 1.5)
    print(f"Point xy({x}, {y})")
    
    x, y = midpoint(-10, -5, 10, 5)  # Expected output: (0.0, 0.0)
    print(f"Point xy({x}, {y})")

    x, y = midpoint(1, 1, 9, 1)  # Expected output: (5.0, 1.0)
    print(f"Point xy({x}, {y})")

    x, y = midpoint(3, 7, 3, -5)  # Expected output: (3.0, 1.0)
    print(f"Point xy({x}, {y})")

if __name__ == "__main__":
    main()
