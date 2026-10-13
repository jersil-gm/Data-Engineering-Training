import os
import pandas as pd
import numpy as np

def run_expense_breakdown():
    # Resolve file paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file = os.path.join(base_dir, 'data', 'expenses.csv')
    summary_output_file = os.path.join(base_dir, 'data', 'cleaned_monthly_summaries.csv')

    print(f"Loading raw expense data from: {input_file}")
    df = pd.read_csv(input_file)

    # 1. Clean and standardize formats (amounts and dates)
    df['amount'] = df['amount'].replace(r'[\$,]', '', regex=True).astype(float)
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period('M')

    # 2. Use numpy to calculate monthly totals and averages
    amounts = df['amount'].to_numpy()
    overall_total = np.sum(amounts)
    overall_avg = np.mean(amounts)

    print("\n===== OVERALL METRICS (NUMPY) =====")
    print(f"Overall Total Spent:   ${overall_total:,.2f}")
    print(f"Overall Average Spend: ${overall_avg:,.2f}")

    print("\n===== MONTHLY METRICS (NUMPY) =====")
    for month, group in df.groupby('month'):
        monthly_amounts = group['amount'].to_numpy()
        m_total = np.sum(monthly_amounts)
        m_avg = np.mean(monthly_amounts)
        print(f"Month: {month} | Total: ${m_total:,.2f} | Average: ${m_avg:,.2f}")

    # 3. Use pandas to create a breakdown of expenses by category
    category_breakdown = (
        df.groupby(['month', 'category'])['amount']
        .sum()
        .unstack()
        .fillna(0.0)
    )

    print("\n===== CATEGORY BREAKDOWN =====")
    print(category_breakdown)

    # 4. Save cleaned dataset with monthly category summaries
    category_breakdown.to_csv(summary_output_file)
    print(f"\nSaved cleaned summary deliverable to: {summary_output_file}")

if __name__ == '__main__':
    run_expense_breakdown()