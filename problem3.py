"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """Get numbers from user until they type 'done'."""
    numbers = []
    while True:
        s = input("Enter a number (or 'done' to finish): ").strip().lower()
        if s == "done":
            break
        try:
            numbers.append(float(s))
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    return numbers


def analyze_numbers(numbers):
    """
    Return a dict with:
    count, sum, average, minimum, maximum, even_count, odd_count
    """
    if not numbers:
        return None

    count = len(numbers)
    total = sum(numbers)
    avg = total / count
    minimum = min(numbers)
    maximum = max(numbers)
    even_count = len([n for n in numbers if n % 2 == 0])
    odd_count  = len([n for n in numbers if n % 2 != 0])

    return {
        "count": count,
        "sum": total,
        "average": avg,
        "minimum": minimum,
        "maximum": maximum,
        "even_count": even_count,
        "odd_count": odd_count,
    }


def display_analysis(analysis):
    """Print the analysis nicely."""
    if not analysis:
        print("No analysis to display.")
        return
    print("\nAnalysis Results:")
    print("-" * 20)
    print(f"Count: {analysis['count']}")
    print(f"Sum: {analysis['sum']}")
    print(f"Average: {analysis['average']:.2f}")
    print(f"Minimum: {analysis['minimum']}")
    print(f"Maximum: {analysis['maximum']}")
    print(f"Even numbers: {analysis['even_count']}")
    print(f"Odd numbers:  {analysis['odd_count']}")


def main():
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.\n")
    numbers = get_numbers_from_user()
    if not numbers:
        print("No numbers entered!")
        return
    analysis = analyze_numbers(numbers)
    display_analysis(analysis)


if __name__ == "__main__":
    main()
