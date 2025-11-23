"""
===========================================================
      STUDENT PERFORMANCE TREND ANALYZER (MANUAL MODE)
===========================================================

This program allows the user to manually input marks for two
students across multiple subjects/exams/tests. After entering
the marks, it prints a detailed comparison, calculates averages,
finds who performed better overall, and generates a performance
trend plot.

The plot helps visualize how the students' marks increase or
decrease across test numbers.

Dependencies:
    - matplotlib (install using: pip install matplotlib)

===========================================================
"""

import matplotlib.pyplot as plt
import sys
import time

def line():
    print("="*60)

def slow_print(text, delay=0.02):
    """Print text with typing animation (for manual feel)."""
    for ch in text:
        print(ch, end="")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def welcome():
    line()
    slow_print("WELCOME TO THE STUDENT PERFORMANCE TREND ANALYZER")
    slow_print("This tool helps you compare marks between two students.")
    line()
    print()

def input_student_name(student_number):
    """Input student name manually."""
    name = input(f"Enter name of Student {student_number}: ").strip()
    while not name:
        print("Name cannot be empty. Please enter again.")
        name = input(f"Enter name of Student {student_number}: ").strip()
    return name

def input_number_of_tests():
    """Ask how many tests/subjects to compare."""
    while True:
        try:
            n = int(input("Enter number of tests/subjects: "))
            if n <= 0:
                print("Number must be positive!")
                continue
            return n
        except ValueError:
            print("Invalid input. Enter a valid number.")

def input_marks(student_name, count):
    """Input marks for a student for given number of tests."""
    slow_print(f"\nEnter marks for {student_name}:")
    marks = []

    for i in range(1, count + 1):
        while True:
            try:
                value = float(input(f"  Marks for Test {i}: "))
                if value < 0:
                    print("Marks cannot be negative!")
                    continue
                marks.append(value)
                break
            except ValueError:
                print("Invalid input. Enter a number.")
    
    return marks

def calculate_average(marks):
    return sum(marks) / len(marks)

def compare_marks(student1, marks1, student2, marks2):
    """Print detailed comparison."""
    line()
    slow_print("DETAILED PERFORMANCE COMPARISON:")
    line()

    for i, (m1, m2) in enumerate(zip(marks1, marks2), start=1):
        print(f"Test {i}:")
        print(f"  {student1}: {m1}")
        print(f"  {student2}: {m2}")

        if m1 > m2:
            print(f"  → {student1} performed better in Test {i}")
        elif m2 > m1:
            print(f"  → {student2} performed better in Test {i}")
        else:
            print("  → Both performed equally")
        print()

def final_summary(student1, marks1, student2, marks2):
    line()
    slow_print("FINAL SUMMARY:")
    line()

    avg1 = calculate_average(marks1)
    avg2 = calculate_average(marks2)

    print(f"{student1}'s Average Marks: {avg1:.2f}")
    print(f"{student2}'s Average Marks: {avg2:.2f}")
    print()

    if avg1 > avg2:
        slow_print(f"Overall Top Performer: {student1}")
    elif avg2 > avg1:
        slow_print(f"Overall Top Performer: {student2}")
    else:
        slow_print("Both students performed equally overall!")

def plot_trend(student1, marks1, student2, marks2):
    """Plot trend line graph."""
    line()
    slow_print("GENERATING PERFORMANCE TREND GRAPH...")
    line()

    tests = list(range(1, len(marks1) + 1))

    plt.figure(figsize=(12, 6))
    plt.plot(tests, marks1, marker='o', label=student1, linewidth=3)
    plt.plot(tests, marks2, marker='s', label=student2, linewidth=3)

    plt.title("Performance Trend Comparison", fontsize=18)
    plt.xlabel("Test Number", fontsize=14)
    plt.ylabel("Marks", fontsize=14)
    plt.grid(True)
    plt.legend(fontsize=14)
    plt.tight_layout()
    plt.show()

def main():
    welcome()

    # Step 1: Input names
    student1 = input_student_name(1)
    student2 = input_student_name(2)

    # Step 2: Number of tests
    num_tests = input_number_of_tests()

    # Step 3: Input marks
    marks1 = input_marks(student1, num_tests)
    marks2 = input_marks(student2, num_tests)

    # Step 4: Comparison
    compare_marks(student1, marks1, student2, marks2)

    # Step 5: Summary
    final_summary(student1, marks1, student2, marks2)

    # Step 6: Plot Trend Graph
    plot_trend(student1, marks1, student2, marks2)

    slow_print("\nPROCESS COMPLETE. THANK YOU FOR USING THE ANALYZER!")
    line()

if __name__ == "__main__":
    main()
