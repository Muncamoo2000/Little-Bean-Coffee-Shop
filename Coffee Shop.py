import pandas as pd
#PART 1 AVG
#create the database
data = {
        "date":["2026-10-01", "2026-10-01", "2026-10-01","2026-10-02", "2026-10-02", "2026-10-02", "2026-10-03", "2026-10-03", "2026-10-03"],
        "product": ["Latte", "Espresso", "Blueberry Muffin", "Latte", "Espresso", "Chocolate Croissant", "Latte", "Espresso", "Blueberry Muffin"],
        "category": ["Coffee", "Coffee", "Bakery", "Coffee", "Coffee", "Bakery", "Coffee", "Coffee", "Bakery"],
        "cups_sold": [45, 30, 18, 52, 28, 22, 38, 41, 15],
        "price": [4.50, 3.00, 3.25, 4.50, 3.00, 3.75, 4.50, 3.00, 3.25]
        }
df = pd.DataFrame(data)

# Use bool mask to print out average number of cups sold in the Bakery
avg_cups = df.loc[df["category"] == "Bakery", "cups_sold"].mean()
print(avg_cups)

# PART 2 CALCULATING REVENUE
# Create a new column called "revenue"

df["revenue"] = df["cups_sold"] * df["price"]


# Find total revenue from all coffee items
sum_revenue = df.loc[df["category"] == "Coffee", "revenue"].sum()
print(sum_revenue)