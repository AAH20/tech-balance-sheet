"""
Investment Committee Technical Due Diligence Memo Generator.
Formats pre-LOI and buyout tech diligence findings for Private Equity deal teams.
"""

from __future__ import annotations
from tech_balance_sheet.models import MADiligenceReport, TechnicalBalanceSheet


class ICMemoReporter:
    """
    Renders formal Investment Committee (IC) Technical Due Diligence Risk Memos.
    """

    @staticmethod
    def render_markdown(
        report: MADiligenceReport,
        balance_sheet: TechnicalBalanceSheet,
    ) -> str:
        lines = [
            f"# 🏛️ PRIVATE EQUITY INVESTMENT COMMITTEE: TECHNICAL DUE DILIGENCE MEMO",
            f"**CONFIDENTIAL // DEAL TEAM EYES ONLY**",
            f"**Target Company:** {report.target_company} | **Evaluation Date:** {report.analysis_date}",
            f"**Deal Verdict:** `{report.deal_verdict}` | **Total Haircut:** `${report.total_valuation_haircut_usd:,.2f}` (`-{report.haircut_percentage:.1f}%`)",
            "",
            "---",
            "",
            "## 1. Executive Deal Summary & Recommendation",
            f"Based on automated algorithmic forensic analysis across target source code repositories, licensing dependencies, cloud infrastructure, and organizational git history, the engineering diligence team issues a recommendation to **`{report.deal_verdict}`**.",
            "",
            f"* **Baseline EBITDA:** `${report.ebitda_usd:,.2f}`",
            f"* **Agreed Baseline Multiple:** `{report.baseline_multiple:.1f}x EBITDA` $\\to$ **Baseline Enterprise Value: `${report.baseline_enterprise_value_usd:,.2f}`**",
            f"* **Adjusted Diligence Multiple:** `{report.adjusted_multiple:.2f}x EBITDA` $\\to$ **Multiple-Adjusted EV: `${report.gross_adjusted_valuation_usd:,.2f}`**",
            f"* **Direct Balance Sheet Liabilities Deducted:** `(${report.direct_balance_sheet_deductions_usd:,.2f})`",
            f"* **Final Recommended Target Valuation:** **`${report.final_recommended_valuation_usd:,.2f}`**",
            f"* **Recommended Escrow Holdback:** **`${report.recommended_escrow_holdback_usd:,.2f}`**",
            "",
            "---",
            "",
            "## 2. Valuation Haircut Waterfall",
            "",
            "| Valuation Step / Adjustment | Metric / Basis | Enterprise Value Impact (USD) |",
            "| :--- | :--- | :--- |",
            f"| Baseline Enterprise Value | {report.baseline_multiple:.1f}x on ${report.ebitda_usd:,.2f} EBITDA | **${report.baseline_enterprise_value_usd:,.2f}** |",
        ]

        for desc, discount in report.multiple_adjustments.items():
            discount_val = report.ebitda_usd * (report.baseline_multiple * abs(discount))
            lines.append(
                f"| Multiple Discount: {desc} | {discount*100:.1f}% multiple drag | (${discount_val:,.2f}) |"
            )

        lines.extend(
            [
                f"| **Subtotal: Multiple-Adjusted Valuation** | **{report.adjusted_multiple:.2f}x EBITDA** | **${report.gross_adjusted_valuation_usd:,.2f}** |",
                f"| Direct Technical & CVE Remediation Deduction | 1:1 Net Liability Deductions | (${report.direct_balance_sheet_deductions_usd:,.2f}) |",
                f"| **FINAL RECOMMENDED OFFER CEILING** | **NET VALUATION** | **${report.final_recommended_valuation_usd:,.2f}** |",
                f"| **TOTAL DEFENSIVE HAIRCUT CAPTURED** | **PURCHASE PRICE REDUCTION** | **${report.total_valuation_haircut_usd:,.2f} (-{report.haircut_percentage:.1f}%)** |",
                "",
                "---",
                "",
                "## 3. Critical Red Flags & Deal Breakers",
            ]
        )

        for i, risk in enumerate(report.critical_deal_risks, 1):
            lines.append(f"{i}. 🛑 **{risk}**")

        lines.extend(
            [
                "",
                "---",
                "",
                "## 4. Remediation Schedule & Escrow Holdback Requirement",
                f"Deal team should require an escrow holdback of **`${report.recommended_escrow_holdback_usd:,.2f}`** (150% of direct liability cost) to be released in tranches over 12 months subject to:",
                "1. Clean remediation of all Critical and High CVEs without service disruption.",
                "2. Replacement or commercial isolation of all viral copyleft (GPL/AGPL) dependencies.",
                "3. Completion of un-qualified SOC 2 Type II audit certification.",
                "4. Formal key-person redundancy agreements and IP assignment confirmations.",
                "",
            ]
        )

        return "\n".join(lines)
