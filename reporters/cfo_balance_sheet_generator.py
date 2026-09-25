"""
CFO & Board of Directors Technical Balance Sheet Reporter.
Renders GAAP-adjacent technical assets, liabilities, and P&L drag statements.
"""

from __future__ import annotations
from tech_balance_sheet.models import TechnicalBalanceSheet, TechnicalIncomeStatement


class CfoBalanceSheetReporter:
    """
    Formats the Technical Balance Sheet and Income Statement for executive boardrooms and CFO reviews.
    """

    @staticmethod
    def render_markdown(
        balance_sheet: TechnicalBalanceSheet,
        income_statement: TechnicalIncomeStatement,
    ) -> str:
        lines = [
            f"# 📊 BOARD OF DIRECTORS: TECHNICAL BALANCE SHEET & P&L STATEMENT",
            f"**Entity:** {balance_sheet.company_name} | **As of Date:** {balance_sheet.as_of_date}",
            f"**Software Health Rating:** `{balance_sheet.health_grade}` | **Tech Debt / Equity Ratio:** `{balance_sheet.debt_to_technical_equity_ratio:.2f}`",
            "",
            "---",
            "",
            "## 1. Technical Balance Sheet",
            "",
            "### ASSETS (Capitalized Software Assets)",
            "| Asset Name | Category | Gross Value (USD) | Accumulated Depreciation | Net Book Value (USD) |",
            "| :--- | :--- | :--- | :--- | :--- |",
        ]

        for a in balance_sheet.assets:
            lines.append(
                f"| {a.name} | {a.category} | ${a.gross_value_usd:,.2f} | (${a.accumulated_depreciation_usd:,.2f}) | **${a.net_book_value_usd:,.2f}** |"
            )

        lines.extend(
            [
                f"| **TOTAL TECHNICAL ASSETS** | | | | **${balance_sheet.total_assets_usd:,.2f}** |",
                "",
                "### LIABILITIES (Accrued Technical Debt Obligations)",
                "| Liability Obligation | Category | Severity | Remediation Capital | Annual Interest Drag |",
                "| :--- | :--- | :--- | :--- | :--- |",
            ]
        )

        for l in balance_sheet.liabilities:
            lines.append(
                f"| {l.name} | {l.category} | `{l.severity}` | ${l.estimated_remediation_cost_usd:,.2f} | ${l.annual_interest_drag_usd:,.2f}/yr |"
            )

        lines.extend(
            [
                f"| **TOTAL TECHNICAL LIABILITIES** | | | **${balance_sheet.total_liabilities_usd:,.2f}** | |",
                "",
                "### NET TECHNICAL POSITION",
                f"* **Net Technical Asset Value (NTAV):** `${balance_sheet.net_technical_asset_value_usd:,.2f}`",
                f"* **Solvency & Health Grade:** `{balance_sheet.health_grade}`",
                "",
                "---",
                "",
                "## 2. Technical Income Statement (P&L Drag Analysis)",
                "",
                f"| Financial Metric | Amount (USD) | % of Engineering Payroll |",
                f"| :--- | :--- | :--- |",
                f"| Total Annual Engineering Payroll | ${income_statement.annual_engineering_payroll_usd:,.2f} | 100.0% |",
                f"| **Technical Debt Friction & Drag** | **(${income_statement.annual_wasted_payroll_interest_usd:,.2f})** | **{income_statement.tech_debt_drag_percentage*100:.1f}%** |",
                f"| **Net Productive R&D Innovation Capacity** | **${income_statement.net_effective_rd_capacity_usd:,.2f}** | **{100.0 - (income_statement.tech_debt_drag_percentage*100):.1f}%** |",
                "",
                "### Remediation Capital Allocation & ROI Forecast",
                f"* **Recommended Year 1 Remediation Capex:** `${income_statement.recommended_remediation_capex_usd:,.2f}`",
                f"* **Projected Annual Velocity Dividend:** `${income_statement.projected_annual_velocity_dividend_usd:,.2f}/year` in unlocked engineering output",
                f"* **Projected 2-Year Remediation ROI:** **`+{income_statement.projected_2_year_roi_percentage:.1f}%`**",
                "",
            ]
        )

        return "\n".join(lines)
