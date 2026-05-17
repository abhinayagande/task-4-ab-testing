
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Load dataset
df = pd.read_csv("marketing_AB.csv")

# Convert converted column into integer
df["converted"] = df["converted"].astype(int)

# Calculate conversion rate
conversion = df.groupby("test group")["converted"].mean()

print("Conversion Rate")
print(conversion)

# Separate control and test groups
control = df[df["test group"] == "psa"]["converted"]
test = df[df["test group"] == "ad"]["converted"]

# Perform T-Test
t_stat, p_value = ttest_ind(test, control)

print("\nT-Test Result")
print("T-statistic:", t_stat)
print("P-value:", p_value)

# Decision
if p_value < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")

# Plot conversion rates
conversion.plot(kind="bar")
plt.title("Conversion Rate by Test Group")
plt.xlabel("Test Group")
plt.ylabel("Conversion Rate")
plt.show()
