# Function to check voter eligibility
def check_voter_eligibility(age):
    # Check if the age is 18 or above
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

# Get user's age
age = int(input("Enter your age: "))

# Check eligibility
result = check_voter_eligibility(age)
print(result)

