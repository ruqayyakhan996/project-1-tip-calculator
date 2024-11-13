# Function to calculate the tip
def calculate_tip(total_bill, tip_percentage):
    tip_amount = (total_bill * tip_percentage) / 100
    total_amount = total_bill + tip_amount
    return tip_amount, total_amount

# Input from the user
print("Welcome to the Tip Calculator!")
total_bill = float(input("Enter the total bill amount: "))
tip_percentage = float(input("Enter the tip percentage: "))

# Calculate tip and total amount
tip_amount, total_amount = calculate_tip(total_bill, tip_percentage)

# Display the results
print(f"\nTip Amount: ${tip_amount:.2f}")
print(f"Total Amount (including tip): ${total_amount:.2f}")

# Project Contributors
print("\nProject Developed by: Ruqayya, Saliha, Shamila")