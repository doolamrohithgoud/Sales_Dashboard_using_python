# Extra insights from df.csv

This file summarizes additional analyses produced by `analysis_extra.py`.

- Outputs saved to `outputs/`:
  - `summary_metrics.csv` — total/avg/median order values and counts
  - `top_customers.csv` — customers ranked by total spend
  - `top_cities.csv` — sales by city
  - `category_sales.csv` — sales by category
  - `monthly_sales.csv` — sales per month
  - `day_of_week_sales.csv` — sales by weekday
  - `city_category_pivot.csv` — pivot table city × category
  - `high_value_orders.csv` — orders above 90th percentile by value
  - `monthly_sales.png`, `category_sales.png`, `top_cities.png`, `correlation.png`

Run:

```bash
python analysis_extra.py
```

Suggested next steps:
- Integrate the generated CSVs/plots into your Streamlit app.
- Add interactive filters (date range, city, category) to explore results.
