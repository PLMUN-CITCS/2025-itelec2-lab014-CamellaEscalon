# Filename: nested_for_loop_multiplication_table.py

# Outer loop for rows (1 to 5)
for i in range(1, 6):
    # Inner loop for columns (1 to 5)
    for j in range(1, 6):
        # Calculate the product of the current row and column
        product = i * j
        # Print the product with formatting, ensuring consistent spacing
        print(f"{product:4}", end="")  # end="" prevents newline
    # Print a new line after each row to start the next row
    print()  # This moves the cursor to the next line after each row
