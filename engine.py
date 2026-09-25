"""
Core Engine for Technical Balance Sheet and M&A Diligence OS.
Orchestrates forensic analyzers and synthesizes financial statements & IC memos.
"""

from __future__ import annotations
import datetime
import json
from typing import Any, Dict, List, Tuple
from tech_balance_sheet.analyzers.architecture_drift import ArchitectureDriftEngine
from tech_balance_sheet.analyzers.cve_actuary import CveActuarialEngine
from tech_balance_sheet.analyzers.git_forensics import GitForensicsEngine
from tech_balance_sheet.analyzers.license_scanner import LicenseForensicsEngine
from tech_balance_sheet.models import (
    MADiligenceReport,
    TechnicalAsset,
    TechnicalBalanceSheet,
    TechnicalIncomeStatement,
    TechnicalLiability,
)


class TechBalanceSheetEngine:
    """
    Synthesizes software codebase forensics into boardroom balance sheets,
    P&L tech debt statements, and private equity diligence reports.
    """

    def __init__(self):
        self.cve_engine = CveActuarialEngine()
        self.license_engine = LicenseForensicsEngine()
        self.git_engine = GitForensicsEngine()
        self.arch_engine = ArchitectureDriftEngine()

    def generate_full_audit(
        self,
        company_name: str,
        financial_profile: Dict[str, float],
        codebase_telemetry: Dict[str, Any],
        as_of_date: Optional[str] = None,
    ) -> Tuple[TechnicalBalanceSheet, TechnicalIncomeStatement, MADiligenceReport]:
        """
        Executes end-to-end multi-analyzer audit and outputs all three financial views.
        """
        date_str = as_of_date or datetime.date.today().isoformat()
        annual_payroll = financial_profile.get("annual_engineering_payroll_usd", 3_500_000.0)
        ebitda = financial_profile.get("ebitda_usd", 5_000_000.0)
        baseline_multiple = financial_profile.get("baseline_ebitda_multiple", 12.0)

        # 1. Run all forensic analyzers
        security_telemetry = codebase_telemetry.get("security", {})
        license_telemetry = codebase_telemetry.get("licenses", [])
        git_telemetry = codebase_telemetry.get("git", {})
        arch_telemetry = codebase_telemetry.get("architecture", {})
        compliance_telemetry = codebase_telemetry.get("compliance", {})

        cve_liabilities = self.cve_engine.analyze(security_telemetry)
        license_liabilities = self.license_engine.analyze(license_telemetry)
        git_liabilities = self.git_engine.analyze(git_telemetry)
        assets, arch_liabilities, tech_debt_drag_ratio = self.arch_engine.analyze_assets_and_liabilities(
            arch_telemetry, annual_payroll
        )

        all_liabilities = cve_liabilities + license_liabilities + git_liabilities + arch_liabilities

        # 2. Build Technical Balance Sheet
        total_assets = sum(a.net_book_value_usd for a in assets)
        total_liabilities = sum(l.estimated_remediation_cost_usd for l in all_liabilities)
        net_technical_equity = total_assets - total_liabilities
        debt_to_equity = (total_liabilities / total_assets) if total_assets > 0 else 99.9

        # Credit Grade
        if debt_to_equity <= 0.15:
            grade = "AAA"
        elif debt_to_equity <= 0.30:
            grade = "AA"
        elif debt_to_equity <= 0.50:
            grade = "A"
        elif debt_to_equity <= 0.75:
            grade = "BBB"
        elif debt_to_equity <= 1.00:
            grade = "BB"
        elif debt_to_equity <= 1.50:
            grade = "B"
        elif debt_to_equity <= 2.00:
            grade = "CCC"
        else:
            grade = "D"

        balance_sheet = TechnicalBalanceSheet(
            company_name=company_name,
            as_of_date=date_str,
            assets=assets,
            liabilities=all_liabilities,
            total_assets_usd=total_assets,
            total_liabilities_usd=total_liabilities,
            net_technical_asset_value_usd=net_technical_equity,
            debt_to_technical_equity_ratio=debt_to_equity,
            health_grade=grade,
        )

        # 3. Build Technical Income Statement (P&L Impact)
        wasted_payroll = annual_payroll * tech_debt_drag_ratio
        net_effective_capacity = annual_payroll - wasted_payroll
        recommended_capex = total_liabilities * 0.45  # Year 1 remediation budget
        velocity_dividend = wasted_payroll * 0.65  # Recovered productivity
        two_year_roi = (
            ((velocity_dividend * 2.0) - recommended_capex) / recommended_capex * 100.0
            if recommended_capex > 0
            else 0.0
        )

        income_statement = TechnicalIncomeStatement(
            company_name=company_name,
            period=f"LTM {date_str}",
            annual_engineering_payroll_usd=annual_payroll,
            tech_debt_drag_percentage=tech_debt_drag_ratio,
            annual_wasted_payroll_interest_usd=wasted_payroll,
            net_effective_rd_capacity_usd=net_effective_capacity,
            recommended_remediation_capex_usd=recommended_capex,
            projected_annual_velocity_dividend_usd=velocity_dividend,
            projected_2_year_roi_percentage=two_year_roi,
        )

        # 4. Build M&A Diligence & Valuation Haircut Report
        baseline_ev = ebitda * baseline_multiple
        multiple_discounts: Dict[str, float] = {}
        critical_risks: List[str] = []

        # Multiple Discount: Compliance & Certifications
        if not compliance_telemetry.get("has_soc2_type2", True):
            multiple_discounts["Missing SOC 2 Type II Certification"] = -0.10
            critical_risks.append("Missing SOC 2 Type II audit triggers enterprise contract churn.")
        elif not compliance_telemetry.get("soc2_unqualified_opinion", True):
            multiple_discounts["Qualified SOC 2 Audit Opinion"] = -0.05
            critical_risks.append("Qualified auditor findings in SOC 2 report.")

        # Multiple Discount: Copyleft License Contamination
        if any(l.category == "IP Contamination" for l in all_liabilities):
            multiple_discounts["Proprietary IP Contamination (GPL/AGPL)"] = -0.08
            critical_risks.append("Viral copyleft dependencies contaminate core proprietary software IP.")

        # Multiple Discount: Extreme Key-Person Risk
        if any(l.name.startswith("Extreme Key-Person Dependency") for l in all_liabilities):
            multiple_discounts["Single-Founder Bus Factor Liability"] = -0.06
            critical_risks.append("Over 65% of code committed by single person with retention risk.")

        # Multiple Discount: Monolithic Obsolescence
        if any(l.category == "Legacy Obsolescence" for l in all_liabilities):
            multiple_discounts["Legacy Framework Obsolescence"] = -0.05
            critical_risks.append("End-of-life runtime stack requires $180k+ re-platforming capex post-close.")

        # Customer Concentration Multiple Discount
        customer_conc = financial_profile.get("top_3_customer_concentration", 0.0)
        if customer_conc > 0.35:
            multiple_discounts[f"Customer Concentration ({customer_conc*100:.1f}% in Top 3)"] = -0.07
            critical_risks.append(f"Top 3 clients account for {customer_conc*100:.1f}% of recurring revenue.")

        total_multiple_discount = sum(multiple_discounts.values())
        adjusted_multiple = max(3.0, round(baseline_multiple * (1.0 + total_multiple_discount), 2))
        gross_adjusted_ev = ebitda * adjusted_multiple

        # Direct Dollar Liabilities deducted 1:1 from Enterprise Value
        direct_dollar_liabilities = total_liabilities
        final_valuation = max(0.0, gross_adjusted_ev - direct_dollar_liabilities)
        total_haircut = baseline_ev - final_valuation
        haircut_percentage = (total_haircut / baseline_ev * 100.0) if baseline_ev > 0 else 0.0

        # Escrow holdback recommendation (Hold back 150% of direct technical liabilities)
        recommended_escrow = round(direct_dollar_liabilities * 1.5, 2)

        # Verdict
        if haircut_percentage > 35.0:
            verdict = "WALK_AWAY"
        elif haircut_percentage > 20.0:
            verdict = "RENEGOTIATE_MAJOR_HAIRCUT"
        elif haircut_percentage > 8.0:
            verdict = "PROCEED_WITH_PRICE_ADJUSTMENT"
        else:
            verdict = "PROCEED_CLEAN"

        diligence_report = MADiligenceReport(
            target_company=company_name,
            analysis_date=date_str,
            ebitda_usd=ebitda,
            baseline_multiple=baseline_multiple,
            baseline_enterprise_value_usd=baseline_ev,
            multiple_adjustments=multiple_discounts,
            adjusted_multiple=adjusted_multiple,
            gross_adjusted_valuation_usd=gross_adjusted_ev,
            direct_balance_sheet_deductions_usd=direct_dollar_liabilities,
            final_recommended_valuation_usd=final_valuation,
            total_valuation_haircut_usd=total_haircut,
            haircut_percentage=haircut_percentage,
            recommended_escrow_holdback_usd=recommended_escrow,
            deal_verdict=verdict,
            critical_deal_risks=critical_risks,
        )

        return balance_sheet, income_statement, diligence_report
