"""
Comprehensive Unit Tests for tech-balance-sheet.
Validates financial balance sheet equation, actuarial liability calculations,
valuation haircut waterfall, and executive memo rendering.
"""

from __future__ import annotations
import unittest
from tech_balance_sheet.analyzers.architecture_drift import ArchitectureDriftEngine
from tech_balance_sheet.analyzers.cve_actuary import CveActuarialEngine
from tech_balance_sheet.analyzers.git_forensics import GitForensicsEngine
from tech_balance_sheet.analyzers.license_scanner import LicenseForensicsEngine
from tech_balance_sheet.engine import TechBalanceSheetEngine
from tech_balance_sheet.reporters.cfo_balance_sheet_generator import CfoBalanceSheetReporter
from tech_balance_sheet.reporters.ic_memo_generator import ICMemoReporter


class TestTechBalanceSheet(unittest.TestCase):
    def setUp(self):
        self.engine = TechBalanceSheetEngine()

    def test_cve_actuarial_engine(self):
        cve_engine = CveActuarialEngine()
        telemetry = {
            "critical_cves": 2,
            "high_cves": 3,
            "medium_cves": 5,
            "public_storage_buckets": 1,
            "post_quantum_fips_204_ready": False,
        }
        liabilities = cve_engine.analyze(telemetry)
        self.assertEqual(len(liabilities), 5)

        total_cost = sum(l.estimated_remediation_cost_usd for l in liabilities)
        # 2*25k + 3*8k + 5*2k + 75k + 120k = 50k + 24k + 10k + 75k + 120k = 279k
        self.assertEqual(total_cost, 279_000.0)

    def test_license_forensics_copyleft(self):
        lic_engine = LicenseForensicsEngine()
        deps = [
            {"package": "foo-lib", "license": "MIT"},
            {"package": "agpl-tool", "license": "AGPL-3.0"},
            {"package": "gpl-core", "license": "GPL-2.0"},
        ]
        liabilities = lic_engine.analyze(deps)
        self.assertEqual(len(liabilities), 2)
        categories = [l.category for l in liabilities]
        self.assertTrue(all(c == "IP Contamination" for c in categories))

    def test_git_forensics_bus_factor(self):
        git_engine = GitForensicsEngine()
        telemetry = {
            "top_contributor_commit_ratio": 0.75,
            "top_contributor_name": "Solo Founder",
            "active_contributors_count": 1,
            "annual_code_churn_percentage": 0.50,
        }
        liabilities = git_engine.analyze(telemetry)
        self.assertEqual(len(liabilities), 2)
        names = [l.name for l in liabilities]
        self.assertTrue(any("Bus Factor = 1" in n for n in names))
        self.assertTrue(any("High Code Churn" in n for n in names))

    def test_full_engine_accounting_invariants(self):
        company = "SaaS Analytics Inc"
        financials = {
            "ebitda_usd": 4_000_000.0,
            "baseline_ebitda_multiple": 10.0,  # $40M EV
            "annual_engineering_payroll_usd": 2_500_000.0,
            "top_3_customer_concentration": 0.20,
        }
        telemetry = {
            "security": {"critical_cves": 0, "high_cves": 2, "medium_cves": 4},
            "licenses": [{"package": "lodash", "license": "MIT"}],
            "git": {"top_contributor_commit_ratio": 0.30, "active_contributors_count": 6},
            "architecture": {
                "total_lines_of_code": 150_000,
                "test_coverage_ratio": 0.65,
                "is_modular_service_architecture": True,
            },
            "compliance": {"has_soc2_type2": True, "soc2_unqualified_opinion": True},
        }

        bs, income, diligence = self.engine.generate_full_audit(company, financials, telemetry)

        # 1. Fundamental Accounting Invariant: Net Technical Asset Value = Total Assets - Total Liabilities
        expected_ntav = bs.total_assets_usd - bs.total_liabilities_usd
        self.assertAlmostEqual(bs.net_technical_asset_value_usd, expected_ntav, places=2)

        # 2. P&L Invariant: Wasted Payroll + Net Effective Capacity = Total Engineering Payroll
        reconciled_payroll = income.annual_wasted_payroll_interest_usd + income.net_effective_rd_capacity_usd
        self.assertAlmostEqual(reconciled_payroll, income.annual_engineering_payroll_usd, places=2)

        # 3. Valuation Haircut Invariant: Final Valuation + Total Haircut = Baseline EV
        self.assertAlmostEqual(
            diligence.final_recommended_valuation_usd + diligence.total_valuation_haircut_usd,
            diligence.baseline_enterprise_value_usd,
            places=2,
        )

        # 4. Diligence Verdict
        self.assertEqual(diligence.deal_verdict, "PROCEED_CLEAN")
        self.assertIn(bs.health_grade, ["AAA", "AA", "A"])

    def test_reporters_render_clean_markdown(self):
        company = "HealthTech Pro"
        financials = {
            "ebitda_usd": 3_000_000.0,
            "baseline_ebitda_multiple": 11.0,
            "annual_engineering_payroll_usd": 2_000_000.0,
        }
        telemetry = {
            "security": {"critical_cves": 1, "public_storage_buckets": 1},
            "licenses": [{"package": "agpl-lib", "license": "AGPL-3.0"}],
            "git": {"top_contributor_commit_ratio": 0.70},
            "architecture": {"total_lines_of_code": 80_000, "legacy_frameworks_detected": ["Python 2.7"]},
            "compliance": {"has_soc2_type2": False},
        }

        bs, income, diligence = self.engine.generate_full_audit(company, financials, telemetry)

        cfo_md = CfoBalanceSheetReporter.render_markdown(bs, income)
        ic_md = ICMemoReporter.render_markdown(diligence, bs)

        self.assertIn("BOARD OF DIRECTORS: TECHNICAL BALANCE SHEET", cfo_md)
        self.assertIn("Net Technical Asset Value", cfo_md)
        self.assertIn("PRIVATE EQUITY INVESTMENT COMMITTEE", ic_md)
        self.assertIn("Valuation Haircut Waterfall", ic_md)
        self.assertIn(diligence.deal_verdict, ic_md)


if __name__ == "__main__":
    unittest.main()
