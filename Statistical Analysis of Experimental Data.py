import numpy as np

# Function to input a list of measurements from the user
def get_input_data():
    data = []
    while True:
        value = input("Enter a measurement (or 'done' to finish): ")
        if value.lower() == 'done':
            break
        try:
            data.append(float(value))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    return data

# Function to input a second dataset
def get_input_data2():
    data2 = []
    while True:
        value = input("Enter a measurement (or 'done' to finish): ")
        if value.lower() == 'done':
            break
        try:
            data2.append(float(value))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    return data2

# Function to calculate the mean of a dataset
def mean(data):
    return np.mean(data)

# Function to calculate the sample standard deviation of a dataset
def std_deviation(data):
    return np.std(data)

# Function to calculate the variance of a dataset
def variance(data):
    return np.var(data)

# Function to perform a one-sample t-test
def one_sample_t_test(data, hypothesis_mean):
    n = len(data)
    sample_mean = mean(data)
    sample_std_dev = std_deviation(data)

    t_stat = (sample_mean - hypothesis_mean) / (sample_std_dev / (n**0.5))
    return t_stat

# Function to perform a two-sample t-test
def two_sample_t_test(data1, data2):
    n1 = len(data1)
    n2 = len(data2)
    mean1 = mean(data1)
    mean2 = mean(data2)
    std_dev1 = std_deviation(data1)
    std_dev2 = std_deviation(data2)

    pooled_std_dev = ((std_dev1**2 * (n1 - 1) + std_dev2**2 * (n2 - 1)) / (n1 + n2 - 2))**0.5
    t_stat = (mean1 - mean2) / (pooled_std_dev * (1/n1 + 1/n2)**0.5)
    return t_stat

# Function to perform a chi-squared test
def chi_squared_test(observed, expected):
    chi_squared_stat = np.sum((observed - expected)**2 / expected)
    return chi_squared_stat

# Main program
print("Welcome to the Physics Statistical Analysis Tool!")

while True:
    data = get_input_data()

    if len(data) < 2:
        print("You need at least 2 data points for analysis.")
    else:
        print(f"Mean: {mean(data)}")
        print(f"Standard Deviation: {std_deviation(data)}")
        print(f"Variance: {variance(data)}")

        hypothesis_test = input("Perform a hypothesis test? (yes/no): ")
        if hypothesis_test == "yes":
            test_type = input("Select a test (one-sample t-test/two-sample t-test/chi-squared): ")
            if test_type == "one-sample t-test":
                hypothesis_mean = float(input("Enter the null hypothesis mean: "))
                t_stat = one_sample_t_test(data, hypothesis_mean)
                print(f"T-Statistic: {t_stat}")
            elif test_type == "two-sample t-test":
                data2 = get_input_data2()
                if len(data2) < 2:
                    print("You need at least 2 data points for the second dataset.")
                else:
                    t_stat = two_sample_t_test(data, data2)
                    print(f"T-Statistic: {t_stat}")
            elif test_type == "chi-squared":
                observed = np.array(data)
                expected = np.array([float(x) for x in input("Enter the expected values (comma-separated): ").split(",")])
                if len(data) != len(expected):
                    print("The number of observed and expected values must be the same.")
                else:
                    chi_squared_stat = chi_squared_test(observed, expected)
                    print(f"Chi-Squared Statistic: {chi_squared_stat}")
            else:
                print("Invalid test type. Please choose 'one-sample t-test', 'two-sample t-test', or 'chi-squared'.")
        repeat = input("Do you want to analyze another dataset? (yes/no): ")
        if repeat != "yes":
            break
