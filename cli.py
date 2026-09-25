"""
Command Line Interface for tech-balance-sheet.
Runs automated M&A due diligence audits and generates Board Technical Balance Sheets.
"""

from __future__ import annotations
import argparse
import json
import os
import sys
from typing import Any, Dict
from tech_balance_sheet.engine import TechBalanceSheetEngine
from tech_balance_sheet.reporters.cfo_balance_sheet_generator import CfoBalanceSheetReporter
from tech_balance_sheet.reporters.ic_memo_generator import ICMemoReporter


def get_demo_target_data() -> Tuple[str, Dict[str, float], Dict[str, Any]]:
    company_name = "CloudFlow Logistics Corp"
    financial_profile = {
        "ebitda_usd": 6_200_000.0,
        "baseline_ebitda_multiple": 14.0,  # Baseline valuation: $86.8M
        "annual_engineering_payroll_usd": 4_800_000.0,
        "top_3_customer_concentration": 0.42,  # 42% customer concentration
    }
    telemetry = {
        "security": {
            "critical_cves": 3,
            "high_cves": 7,
            "medium_cves": 18,
            "public_storage_buckets": 1,
            "post_quantum_fips_204_ready": False,
        },
        "licenses": [
            {"package": "legacy-pdf-renderer", "license": "AGPL-3.0"},
            {"package": "geo-routing-engine", "license": "GPL-3.0"},
            {"package": "fast-json", "license": "MIT"},
        ],
        "git": {
            "top_contributor_commit_ratio": 0.68,
            "top_contributor_name": "Marcus Vance (Co-Founder & VP Eng)",
            "active_contributors_count": 8,
            "annual_code_churn_percentage": 0.44,
        },
        "architecture": {
            "total_lines_of_code": 380_000,
            "test_coverage_ratio": 0.32,
            "is_modular_service_architecture": False,
            "legacy_frameworks_detected": ["Python 2.7", "AngularJS 1.6"],
            "circular_dependencies_count": 14,
        },
        "compliance": {
            "has_soc2_type2": False,
            "soc2_unqualified_opinion": False,
        },
    }
    return company_name, financial_profile, telemetry


def main():
    parser = argparse.ArgumentParser(
        description="Autonomous M&A Technical Diligence & Board-Level Software Balance Sheet OS"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # Demo command
    demo_parser = subparsers.add_parser("demo", help="Run full M&A Diligence & CFO Balance Sheet demo")
    demo_parser.add_argument("--outdir", default="./output_reports", help="Output directory for reports")

    # Audit command
    audit_parser = subparsers.add_parser("audit", help="Run audit on specific company profile")
    audit_parser.add_argument("--name", required=True, help="Target company name")
    audit_parser.add_argument("--ebitda", type=float, default=5_000_000.0, help="EBITDA in USD")
    audit_parser.add_argument("--multiple", type=float, default=12.0, help="Baseline EBITDA multiple")
    audit_parser.add_argument("--payroll", type=float, default=3_500_000.0, help="Annual engineering payroll")
    audit_parser.add_argument("--telemetry", help="Path to JSON file with telemetry data")
    audit_parser.add_argument("--outdir", default="./output_reports", help="Output directory for reports")

    args = parser.parse_args()

    if not args.command or args.command == "demo":
        company_name, financial_profile, telemetry = get_demo_target_data()
        outdir = getattr(args, "outdir", "./output_reports")
    elif args.command == "audit":
        company_name = args.name
        financial_profile = {
            "ebitda_usd": args.ebitda,
            "baseline_ebitda_multiple": args.multiple,
            "annual_engineering_payroll_usd": args.payroll,
        }
        if args.telemetry and os.path.exists(args.telemetry):
            with open(args.telemetry, "r", encoding="utf-8") as f:
                telemetry = json.load(f)
        else:
            _, _, telemetry = get_demo_target_data()
        outdir = args.outdir
    else:
        parser.print_help()
        sys.exit(1)

    os.makedirs(outdir, exist_ok=True)
    engine = TechBalanceSheetEngine()

    print(f"\n🚀 Running Autonomous Tech Diligence & Balance Sheet Audit for: {company_name}")
    print(f"   Baseline EBITDA: ${financial_profile['ebitda_usd']:,.2f} @ {financial_profile['baseline_ebitda_multiple']:.1f}x")
    print(f"   Baseline Enterprise Value: ${financial_profile['ebitda_usd'] * financial_profile['baseline_ebitda_multiple']:,.2f}\n")

    bs, income, diligence = engine.generate_full_audit(company_name, financial_profile, telemetry)

    # Render reports
    cfo_report_md = CfoBalanceSheetReporter.render_markdown(bs, income)
    ic_memo_md = ICMemoReporter.render_markdown(diligence, bs)

    cfo_path = os.path.join(outdir, "cfo_technical_balance_sheet.md")
    ic_path = os.path.join(outdir, "ic_due_diligence_memo.md")
    summary_path = os.path.join(outdir, "audit_summary.json")

    with open(cfo_path, "w", encoding="utf-8") as f:
        f.write(cfo_report_md)
    with open(ic_path, "w", encoding="utf-8") as f:
        f.write(ic_memo_md)
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "balance_sheet": bs.to_dict(),
                "income_statement": income.to_dict(),
                "diligence_report": diligence.to_dict(),
            },
            f,
            indent=2,
        )

    print("=" * 80)
    print("🏛️ PRIVATE EQUITY INVESTMENT COMMITTEE MEMO")
    print("=" * 80)
    print(f"Verdict: {diligence.deal_verdict}")
    print(f"Baseline Enterprise Value: ${diligence.baseline_enterprise_value_usd:,.2f}")
    print(f"Adjusted Enterprise Value: ${diligence.final_recommended_valuation_usd:,.2f}")
    print(f"Defensive Haircut Captured: ${diligence.total_valuation_haircut_usd:,.2f} (-{diligence.haircut_percentage:.1f}%)")
    print(f"Recommended Escrow Holdback: ${diligence.recommended_escrow_holdback_usd:,.2f}")
    print(f"Critical Red Flags Identified: {len(diligence.critical_deal_risks)}")

    print("\n" + "=" * 80)
    print("📊 BOARD OF DIRECTORS & CFO BALANCE SHEET")
    print("=" * 80)
    print(f"Total Technical Assets: ${bs.total_assets_usd:,.2f}")
    print(f"Total Technical Liabilities: ${bs.total_liabilities_usd:,.2f}")
    print(f"Net Technical Asset Value: ${bs.net_technical_asset_value_usd:,.2f}")
    print(f"Software Health Credit Grade: {bs.health_grade}")
    print(f"Annual Wasted Payroll on Tech Debt: ${income.annual_wasted_payroll_interest_usd:,.2f}/yr ({income.tech_debt_drag_percentage*100:.1f}%)")
    print(f"Projected 2-Year Remediation ROI: +{income.projected_2_year_roi_percentage:.1f}%")

    print("\n✅ Reports successfully generated:")
    print(f"   - {cfo_path}")
    print(f"   - {ic_path}")
    print(f"   - {summary_path}\n")


if __name__ == "__main__":
    main()
