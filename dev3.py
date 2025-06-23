# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----- NumPy -----
print("🔹 NumPy Array Operations")

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

# Basic operations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))

# ----- Pandas -----
print("\n🔹 Pandas DataFrame Operations")

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Marks': [85, 92, 78, 88]
}
df = pd.DataFrame(data)

# Show DataFrame
print(df)

# Add a new column
df['Passed'] = df['Marks'] >= 80
print("\nUpdated DataFrame with Passed column:")
print(df)

# ----- Matplotlib -----
print("\n🔹 Data Visualization with Matplotlib")

# Plot Marks as a bar chart
plt.bar(df['Name'], df['Marks'], color='skyblue')
plt.title("Student Marks")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.grid(True)
plt.show()
