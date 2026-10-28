# ☕ Little Bean Coffee Analytics

A growing hands-on Python + Pandas project that teaches real data analysis skills through a single ongoing business story.

---

### 📌 Project Overview

This repository follows the daily sales of a small coffee shop called **Little Bean Coffee**.  
Instead of doing random disconnected exercises, we build **one continuous project** that gets more powerful with every lesson.

We start with simple hard-coded data and gradually turn it into a real analytics system.

---

### 🧠 Skills Covered So Far

| Lesson | Concept                          | Status       |
|--------|----------------------------------|--------------|
| 1      | Boolean Filtering + Aggregation  | ✅ Complete   |
| 2      | Creating New Columns (Revenue)   | ✅ Complete   |
| 3      | GroupBy                          | 🔄 In Progress |
| 4      | Functions with `return`          | ✅ Complete   |
| -      | Reading real CSV files           | Coming soon  |
| -      | Handling missing data            | Coming soon  |
| -      | Basic visualizations             | Coming soon  |

---

### 📊 Current Data

| date       | product              | category | cups_sold | price | revenue |
|------------|----------------------|----------|-----------|-------|---------|
| 2026-10-01 | Latte                | Coffee   | 45        | 4.50  | 202.50  |
| 2026-10-01 | Espresso             | Coffee   | 30        | 3.00  | 90.00   |
| 2026-10-01 | Blueberry Muffin     | Bakery   | 18        | 3.25  | 58.50   |
| 2026-10-02 | Latte                | Coffee   | 52        | 4.50  | 234.00  |
| 2026-10-02 | Espresso             | Coffee   | 28        | 3.00  | 84.00   |
| 2026-10-02 | Chocolate Croissant  | Bakery   | 22        | 3.75  | 82.50   |
| 2026-10-03 | Latte                | Coffee   | 38        | 4.50  | 171.00  |
| 2026-10-03 | Espresso             | Coffee   | 41        | 3.00  | 123.00  |
| 2026-10-03 | Blueberry Muffin     | Bakery   | 15        | 3.25  | 48.75   |

---

### ✨ Sample Output

```text
===== Little Bean Coffee Weekly Report =====
Total sales this week: $1093.75
Average daily sales:   $364.58
10% of sales (tip jar goal): $109.38
```

---

### 🛠️ How to Run

1. Make sure you have pandas installed:
   ```bash
   pip install pandas
   ```

2. Run the main script:
   ```bash
   python little_bean_coffee.py
   ```

---

### 📁 Project Structure

```text
little-bean-coffee/
│
├── README.md
├── little_bean_coffee.py      # Main analysis script
└── data/                      # (Future) CSV files will live here
```

---

### 🚀 What's Next

- Finish GroupBy lessons
- Load data from a real CSV file instead of hard-coding
- Add more days of sales data
- Calculate best-selling products
- Create simple charts
- Eventually turn this into a small dashboard

---

### ✍️ Author

Built while learning Python and Pandas step-by-step.  
This project is part of my journey into data analysis and junior Python development.

---

⭐ If you're also learning Pandas, feel free to fork this and follow along!
