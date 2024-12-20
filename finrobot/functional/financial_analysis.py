import pandas as pd

def calculate_financial_ratios(financial_data: pd.DataFrame) -> str:
    """
    Calculates key financial ratios from a company's financial data.

    Args:
        financial_data: A pandas DataFrame containing financial data.
            It should have columns like 'Revenue', 'Cost of Goods Sold', 'Net Income',
            'Total Assets', 'Total Liabilities', 'Total Equity'.

    Returns:
        A string containing the calculated financial ratios.
    """
    if financial_data.empty:
        return "No financial data provided."

    try:
        revenue = financial_data['Revenue'].iloc[0]
        cost_of_goods_sold = financial_data['Cost of Goods Sold'].iloc[0]
        net_income = financial_data['Net Income'].iloc[0]
        total_assets = financial_data['Total Assets'].iloc[0]
        total_liabilities = financial_data['Total Liabilities'].iloc[0]
        total_equity = financial_data['Total Equity'].iloc[0]

        gross_profit_margin = (revenue - cost_of_goods_sold) / revenue if revenue != 0 else 0
        net_profit_margin = net_income / revenue if revenue != 0 else 0
        return_on_equity = net_income / total_equity if total_equity != 0 else 0
        debt_to_equity = total_liabilities / total_equity if total_equity != 0 else 0
        return_on_assets = net_income / total_assets if total_assets != 0 else 0

        results = f"""
        Gross Profit Margin: {gross_profit_margin:.2f}
        Net Profit Margin: {net_profit_margin:.2f}
        Return on Equity: {return_on_equity:.2f}
        Debt to Equity: {debt_to_equity:.2f}
        Return on Assets: {return_on_assets:.2f}
        """
        return results
    except KeyError as e:
        return f"Error: Missing required column in financial data: {e}"
    except Exception as e:
        return f"An error occurred: {e}"