def get_grade(score):
    """Return grade based on score."""
    if score >= 95:
        return 'A+'
    elif score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'c'
    elif score >= 60:
        return 'D'
    elif score >= 50:
        return 'E'
    else:
        return 'F'

def get_grade_description(grade):
    """Return description for grade."""
    descriptions = {
        'A+': 'Outstanding - Exceptional performance',
        'A': 'Excellent - Very Good performance',
        'B': 'Good - Above average performance',
        'C': 'Average - Satisfactory performance',
        'D': 'Below Average - Passing performance',
        'F': 'Fail - Needs improvement'
    }
    return descriptions.get(grade, 'Unknown grade')

def main():
    """Main program to check student grades."""
    print("\n" + "="*50)
    print("       STUDENT GRADE CHECKER")
    print("="*50 + "\n")
    
    try:
        student_name = input("Enter student name: ")
        score = float(input("Enter student score (0-100): "))
        
        if 0 <= score <= 100:
            grade = get_grade(score)
            description = get_grade_description(grade)
            print(f"\n{'='*50}")
            print(f"Student: {student_name}")
            print(f"Score: {score}")
            print(f"Grade: {grade}")
            print(f"Description: {description}")
            print(f"{'='*50}\n")
        else:
            print("Invalid score! Please enter a score between 0 and 100.")
    except ValueError:
        print("Invalid input! Please enter valid data.")

if __name__ == "__main__":
    main()