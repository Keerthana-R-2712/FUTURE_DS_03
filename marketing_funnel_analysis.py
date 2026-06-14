import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_excel("marketing_campaign.xlsx")

# Basic Information
print("Dataset Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

# Total Campaign Acceptance
df['TotalCampaignAccepted'] = (
    df['AcceptedCmp1'] +
    df['AcceptedCmp2'] +
    df['AcceptedCmp3'] +
    df['AcceptedCmp4'] +
    df['AcceptedCmp5']
)

# Conversion Rate
conversion_rate = (df['Response'].sum() / len(df)) * 100
print(f"\nOverall Conversion Rate: {conversion_rate:.2f}%")

# Funnel Data
visitors = df['NumWebVisitsMonth'].sum()
purchases = df['NumWebPurchases'].sum()
customers = df['Response'].sum()

funnel = pd.DataFrame({
    'Stage': ['Website Visits', 'Web Purchases', 'Converted Customers'],
    'Count': [visitors, purchases, customers]
})

print("\nFunnel Data:")
print(funnel)

# Funnel Chart
plt.figure(figsize=(8,5))
plt.bar(funnel['Stage'], funnel['Count'])
plt.title('Marketing Funnel Analysis')
plt.ylabel('Count')
plt.show()

# Campaign Performance
campaigns = df[['AcceptedCmp1',
                'AcceptedCmp2',
                'AcceptedCmp3',
                'AcceptedCmp4',
                'AcceptedCmp5']].sum()

plt.figure(figsize=(8,5))
campaigns.plot(kind='bar')
plt.title('Campaign Performance')
plt.ylabel('Accepted Customers')
plt.show()

# Education vs Conversion
edu_conversion = df.groupby('Education')['Response'].mean() * 100

plt.figure(figsize=(8,5))
edu_conversion.sort_values().plot(kind='bar')
plt.title('Education vs Conversion Rate')
plt.ylabel('Conversion Rate (%)')
plt.show()

# Marital Status vs Conversion
marital_conversion = df.groupby('Marital_Status')['Response'].mean() * 100

plt.figure(figsize=(8,5))
marital_conversion.sort_values().plot(kind='bar')
plt.title('Marital Status vs Conversion Rate')
plt.ylabel('Conversion Rate (%)')
plt.show()

# Top Insights
print("\n===== KEY INSIGHTS =====")
print(f"Total Customers: {len(df)}")
print(f"Converted Customers: {customers}")
print(f"Overall Conversion Rate: {conversion_rate:.2f}%")
print("Campaign analysis and conversion charts generated successfully.")