"""
Week 3 Assignment - Discount Calculator
Author: [Rebecca Mulandi]
Description: This program calculates the final price after applying a discount
using a function that only applies discounts of 20% or higher.
"""
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    price (float): The original price of the item
    discount_percent (float): The discount percentage
    
    Returns:
    float: The final price after discount (if discount >= 20%) or original price
    """
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Calculate discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate final price
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

# Main program
print("Welcome to the Discount Calculator!")
print("-" * 35)

# Get input from user
try:
    # Ask user for original price
    original_price = float(input("Enter the original price of the item (numbers only): KSh "))
    
    # Ask user for discount percentage
    discount_percentage = float(input("Enter the discount percentage (numbers only): "))
    
    # Call the function to calculate final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Display results
    print("\n" + "=" * 40)
    print("CALCULATION RESULTS:")
    print("=" * 40)
    print(f"Original Price: KSh {original_price:.2f}")
    print(f"Discount Percentage: {discount_percentage}%")
    
    # Check if discount was applied
    if discount_percentage >= 20:
        discount_amount = original_price - final_price
        print(f"Discount Applied: KSh {discount_amount:.2f}")
        print(f"Final Price: KSh {final_price:.2f}")
        print("✓ Discount was applied!")
    else:
        print(f"Final Price: KSh {final_price:.2f}")
        print("✗ No discount applied (discount must be 20% or higher)")

except ValueError:
    print("Error: Please enter valid numbers for price and discount percentage.")
except Exception as e:
    print(f"An error occurred: {e}")

print("\nThank you for using the Discount Calculator!")