# Professor Review and Analysis System
# Simple Python project using basic conditionals and loops

print("Welcome to the Professor Review & Analysis System!")


# Create an empty dictionary to store professor ratings
professors = {}

# Take input for how many professors to review
num = int(input("How many professors do you want to review? "))

for i in range(num):
    name = input(f"Enter the name of Professor {i+1}: ")
    rating = float(input("Enter rating for the professor (1 to 5): "))

    # Store professor and rating
    professors[name] = rating

print("Review Summary:")
for name, rating in professors.items():
    # Conditional analysis based on rating
    if rating >= 4.5:
        feedback = "Excellent performance! Highly appreciated."
    elif rating >= 3.5:
        feedback = "Good and consistent teaching."
    elif rating >= 2.5:
        feedback = "Average, needs improvement."
    else:
        feedback = "Poor performance, needs attention."

    print(f"{name}: Rating = {rating} → {feedback}")

# Calculate average rating across professors
avg_rating = sum(professors.values()) / len(professors)
print(f"Overall average rating: {avg_rating:.2f}")


# Give overall analysis
if avg_rating >= 4.5:
    print("Overall Analysis: Outstanding teaching quality across professors.")
elif avg_rating >= 3.5:
    print("Overall Analysis: Generally good teaching quality.")
elif avg_rating >= 2.5:
    print("Overall Analysis: Mixed performance, some improvements needed.")
else:
    print("Overall Analysis: Teaching quality must be improved.")