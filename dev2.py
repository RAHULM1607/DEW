import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample email-like data (as a dictionary)
data = {
    'Email_ID': [1, 2, 3, 4, 5],
    'Sender': ['alice@mail.com', 'bob@mail.com', 'alice@mail.com', 'carol@mail.com', 'bob@mail.com'],
    'Spam': [0, 1, 0, 1, 0],
    'Content_Length': [120, 350, 180, 400, 150]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display the data
print("Dataset:")
print(df)

# Basic Info
print("\nInfo:")
print(df.info())

# Summary
print("\nSummary Statistics:")
print(df.describe())

# Spam vs Not Spam Count
sns.countplot(x='Spam', data=df)
plt.title("Spam vs Not Spam")
plt.xticks([0, 1], ['Not Spam', 'Spam'])
plt.show()

# Content Length Distribution
sns.histplot(df['Content_Length'], bins=5, kde=True)
plt.title("Content Length Distribution")
plt.xlabel("Content Length")
plt.show()
