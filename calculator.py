# === Advanced Calculator (Multi-number + Expression Mode) ===

# --- Simple Mode Functions ---

def add_numbers():
    """Add multiple numbers entered by the user (no symbols allowed)."""
    numbers = input("Enter numbers to add (separated by spaces): ").split()
    total = 0
    for num in numbers:
        # Block arithmetic symbols not allowed in addition
        if any(op in num for op in ['+', '-', '*', '/', '×', '÷']):
            print(f"⚠️ Invalid input '{num}' — please enter only plain numbers (e.g., 10 20 30).")
            return "❌ Error! Symbols are not allowed in addition section."
        try:
            total += float(num)
        except ValueError:
            print(f"⚠️ '{num}' is not a valid number, skipping it.")
    return total


def subtract_numbers():
    """Subtract multiple numbers entered by the user (no +, *, / allowed)."""
    numbers = input("Enter numbers to subtract (separated by spaces): ").split()
    if not numbers:
        return "⚠️ No numbers entered!"
    for num in numbers:
        if any(op in num for op in ['+', '*', '/', '×', '÷']):
            print(f"⚠️ Invalid input '{num}' — please enter only plain numbers (e.g., 50 20 10).")
            return "❌ Error! Symbols are not allowed in subtraction section."
    try:
        nums = [float(num) for num in numbers]
        result = nums[0]
        for num in nums[1:]:
            result -= num
        return result
    except ValueError:
        return "⚠️ Invalid input! Please enter numeric values only."


def multiply_numbers():
    """Multiply multiple numbers entered by the user (no +, -, / allowed)."""
    numbers = input("Enter numbers to multiply (separated by spaces): ").split()
    if not numbers:
        return "⚠️ No numbers entered!"
    for num in numbers:
        if any(op in num for op in ['+', '-', '/', '÷']):
            print(f"⚠️ Invalid input '{num}' — please enter only plain numbers (e.g., 2 3 4).")
            return "❌ Error! Symbols are not allowed in multiplication section."
    try:
        nums = [float(num) for num in numbers]
        result = 1
        for num in nums:
            result *= num
        return result
    except ValueError:
        return "⚠️ Invalid input! Please enter numeric values only."


def divide_numbers():
    """Divide multiple numbers entered by the user (no +, -, * allowed)."""
    numbers = input("Enter numbers to divide (separated by spaces): ").split()
    if not numbers:
        return "⚠️ No numbers entered!"
    for num in numbers:
        if any(op in num for op in ['+', '-', '*', '×']):
            print(f"⚠️ Invalid input '{num}' — please enter only plain numbers (e.g., 100 5 2).")
            return "❌ Error! Symbols are not allowed in division section."
    try:
        nums = [float(num) for num in numbers]
        result = nums[0]
        for num in nums[1:]:
            if num == 0:
                return "❌ Error! Division by zero."
            result /= num
        return result
    except ValueError:
        return "⚠️ Invalid input! Please enter numeric values only."


# --- Expression Mode Function ---

def calculate_expression():
    """Evaluate a full mathematical expression like 10 + 20 - 5 * 2."""
    expression = input("Enter your expression (e.g., 10 + 20 - 5 * 2 / 5): ")

    try:
        # Allow ÷ and × as symbols too
        expression = expression.replace('÷', '/').replace('×', '*')
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "❌ Error! Division by zero."
    except Exception:
        return "⚠️ Invalid expression! Please enter a valid math expression."


# --- Display Menus ---

def display_main_menu():
    print("\n" + "="*38)
    print("        🧮 ADVANCED CALCULATOR MENU")
    print("="*38)
    print("1️⃣  Simple Mode (step-by-step input)")
    print("2️⃣  Expression Mode (type full equation)")
    print("3️⃣  Exit")
    print("="*38)


def display_simple_menu():
    print("\n" + "-"*38)
    print("       🔢 SIMPLE CALCULATOR MENU")
    print("-"*38)
    print("1. ➕ Add multiple numbers")
    print("2. ➖ Subtract multiple numbers")
    print("3. ✖️ Multiply multiple numbers")
    print("4. ➗ Divide multiple numbers")
    print("5. 🔙 Back to Main Menu")
    print("-"*38)


# --- Main Program Loop ---

while True:
    display_main_menu()
    mode = input("👉 Choose mode (1/2/3): ").strip()

    # Exit program
    if mode == '3':
        print("\n👋 Exiting the calculator. Goodbye!")
        break

    # Simple mode
    elif mode == '1':
        while True:
            display_simple_menu()
            choice = input("👉 Choose operation (1/2/3/4/5): ").strip()

            if choice == '5':
                print("🔙 Returning to main menu...")
                break
            elif choice == '1':
                result = add_numbers()
                print(f"\n✅ Result: The total sum is {result}")
            elif choice == '2':
                result = subtract_numbers()
                print(f"\n✅ Result: The final difference is {result}")
            elif choice == '3':
                result = multiply_numbers()
                print(f"\n✅ Result: The total product is {result}")
            elif choice == '4':
                result = divide_numbers()
                print(f"\n✅ Result: The final quotient is {result}")
            else:
                print("⚠️ Invalid choice! Please select 1–5.")
                continue

            again = input("\n🔁 Do another simple calculation? (y/n): ").lower()
            if again != 'y':
                break

    # Expression mode
    elif mode == '2':
        while True:
            result = calculate_expression()
            print(f"\n✅ Result: {result}")
            again = input("\n🔁 Do another expression calculation? (y/n): ").lower()
            if again != 'y':
                break

    else:
        print("⚠️ Invalid option! Please choose 1, 2, or 3.")
