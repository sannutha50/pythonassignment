def calculate_positive_feedback_percentage(ratings):
    if len(ratings) == 0:
        return 0.0
    positive_count = sum(1 for rating in ratings if rating >= 4)
    positive_percentage = (positive_count / len(ratings)) * 100
    return positive_percentage
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
positive_feedback_percentage = calculate_positive_feedback_percentage(ratings)
print(f"Positive Feedback: {positive_feedback_percentage:.1f}%")
