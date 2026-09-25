"""
Financial & Mathematical Models for Technical Balance Sheet and M&A Diligence.
Unifies software codebase liabilities with corporate valuation and GAAP-adjacent balance sheets.
"""

from __future__ import annotations
import json
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class TechnicalAsset:
    name: str
    category: str  # "Core IP", "Test Coverage Capital", "Architecture Modularity"
    gross_value_usd: float
    accumulated_depreciation_usd: float
    net_book_value_usd: float
    description: str


@dataclass
class TechnicalLiability:
    name: str
    category: str  # "Legacy Obsolescence", "Security / CVE", "IP Contamination", "Key-Person Risk", "Architectural Drag"
    estimated_remediation_cost_usd: float
    annual_interest_drag_usd: float  # Annual engineering payroll wasted servicing this debt
    severity: str  # "CRITICAL", "HIGH", "MEDIUM", "LOW"
    description: str


@dataclass
class TechnicalBalanceSheet:
    company_name: str
    as_of_date: str
    assets: List[TechnicalAsset]
    liabilities: List[TechnicalLiability]
    total_assets_usd: float
    total_liabilities_usd: float
    net_technical_asset_value_usd: float
    debt_to_technical_equity_ratio: float
    health_grade: str  # "AAA", "AA", "A", "BBB", "BB", "B", "CCC", "D"

    def to_dict(self) -> dict:
        return {
            "company_name": self.company_name,
            "as_of_date": self.as_of_date,
            "total_assets_usd": round(self.total_assets_usd, 2),
            "total_liabilities_usd": round(self.total_liabilities_usd, 2),
            "net_technical_asset_value_usd": round(self.net_technical_asset_value_usd, 2),
            "debt_to_technical_equity_ratio": round(self.debt_to_technical_equity_ratio, 2),
            "health_grade": self.health_grade,
            "assets": [
                {
                    "name": a.name,
                    "category": a.category,
                    "gross_value_usd": round(a.gross_value_usd, 2),
                    "depreciation_usd": round(a.accumulated_depreciation_usd, 2),
                    "net_book_value_usd": round(a.net_book_value_usd, 2),
                }
                for a in self.assets
            ],
            "liabilities": [
                {
                    "name": l.name,
                    "category": l.category,
                    "remediation_cost_usd": round(l.estimated_remediation_cost_usd, 2),
                    "annual_interest_drag_usd": round(l.annual_interest_drag_usd, 2),
                    "severity": l.severity,
                }
                for l in self.liabilities
            ],
        }


@dataclass
class TechnicalIncomeStatement:
    company_name: str
    period: str
    annual_engineering_payroll_usd: float
    tech_debt_drag_percentage: float  # e.g., 28.5%
    annual_wasted_payroll_interest_usd: float
    net_effective_rd_capacity_usd: float
    recommended_remediation_capex_usd: float
    projected_annual_velocity_dividend_usd: float
    projected_2_year_roi_percentage: float

    def to_dict(self) -> dict:
        return {
            "company_name": self.company_name,
            "period": self.period,
            "annual_engineering_payroll_usd": round(self.annual_engineering_payroll_usd, 2),
            "tech_debt_drag_percentage": round(self.tech_debt_drag_percentage * 100, 1),
            "annual_wasted_payroll_interest_usd": round(self.annual_wasted_payroll_interest_usd, 2),
            "net_effective_rd_capacity_usd": round(self.net_effective_rd_capacity_usd, 2),
            "recommended_remediation_capex_usd": round(self.recommended_remediation_capex_usd, 2),
            "projected_annual_velocity_dividend_usd": round(self.projected_annual_velocity_dividend_usd, 2),
            "projected_2_year_roi_percentage": round(self.projected_2_year_roi_percentage, 1),
        }


@dataclass
class MADiligenceReport:
    target_company: str
    analysis_date: str
    ebitda_usd: float
    baseline_multiple: float
    baseline_enterprise_value_usd: float
    multiple_adjustments: Dict[str, float]
    adjusted_multiple: float
    gross_adjusted_valuation_usd: float
    direct_balance_sheet_deductions_usd: float
    final_recommended_valuation_usd: float
    total_valuation_haircut_usd: float
    haircut_percentage: float
    recommended_escrow_holdback_usd: float
    deal_verdict: str  # "PROCEED_CLEAN", "PROCEED_WITH_PRICE_ADJUSTMENT", "RENEGOTIATE_MAJOR_HAIRCUT", "WALK_AWAY"
    critical_deal_risks: List[str]

    def to_dict(self) -> dict:
        return {
            "target_company": self.target_company,
            "analysis_date": self.analysis_date,
            "financial_baseline": {
                "ebitda_usd": round(self.ebitda_usd, 2),
                "baseline_multiple": self.baseline_multiple,
                "baseline_enterprise_value_usd": round(self.baseline_enterprise_value_usd, 2),
            },
            "valuation_adjustments": {
                "multiple_adjustments": self.multiple_adjustments,
                "adjusted_multiple": self.adjusted_multiple,
                "gross_adjusted_valuation_usd": round(self.gross_adjusted_valuation_usd, 2),
                "direct_balance_sheet_deductions_usd": round(self.direct_balance_sheet_deductions_usd, 2),
                "final_recommended_valuation_usd": round(self.final_recommended_valuation_usd, 2),
                "total_valuation_haircut_usd": round(self.total_valuation_haircut_usd, 2),
                "haircut_percentage": round(self.haircut_percentage, 2),
                "recommended_escrow_holdback_usd": round(self.recommended_escrow_holdback_usd, 2),
            },
            "deal_verdict": self.deal_verdict,
            "critical_deal_risks": self.critical_deal_risks,
        }
