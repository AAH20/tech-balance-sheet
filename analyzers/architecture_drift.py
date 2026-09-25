"""
Architecture Drift & Tech Debt Drag Engine.
Quantifies monolithic coupling, framework obsolescence, and test capital.
"""

from __future__ import annotations
from typing import Any, Dict, List, Tuple
from tech_balance_sheet.models import TechnicalAsset, TechnicalLiability


class ArchitectureDriftEngine:
    """
    Evaluates architectural health, modularity, framework obsolescence, and test capital.
    """

    def analyze_assets_and_liabilities(
        self,
        architecture_telemetry: Dict[str, Any],
        annual_engineering_payroll_usd: float,
    ) -> Tuple[List[TechnicalAsset], List[TechnicalLiability], float]:
        """
        Returns (assets, liabilities, overall_drag_percentage).
        """
        assets: List[TechnicalAsset] = []
        liabilities: List[TechnicalLiability] = []

        total_lines_of_code = architecture_telemetry.get("total_lines_of_code", 100_000)
        test_coverage_ratio = architecture_telemetry.get("test_coverage_ratio", 0.50)
        has_modular_architecture = architecture_telemetry.get("is_modular_service_architecture", False)
        legacy_frameworks = architecture_telemetry.get("legacy_frameworks_detected", [])
        circular_dependencies_count = architecture_telemetry.get("circular_dependencies_count", 0)

        # 1. Assets: Core IP Capital (Valued at baseline replacement cost ~$15/LOC gross)
        gross_ip_value = total_lines_of_code * 15.0
        # Depreciation based on age / unmaintained percentage
        deprecated_ratio = 0.35 if legacy_frameworks else 0.15
        accumulated_depreciation = gross_ip_value * deprecated_ratio
        net_ip_value = gross_ip_value - accumulated_depreciation

        assets.append(
            TechnicalAsset(
                name="Proprietary Codebase & Domain IP",
                category="Core IP",
                gross_value_usd=gross_ip_value,
                accumulated_depreciation_usd=accumulated_depreciation,
                net_book_value_usd=net_ip_value,
                description=f"Valuation of {total_lines_of_code:,} proprietary lines of code across domain logic and proprietary workflows.",
            )
        )

        # 2. Assets: Test Coverage Capital
        # High test coverage acts as an insurance asset protecting against regressions
        test_asset_gross = (total_lines_of_code * test_coverage_ratio) * 8.0
        test_depreciation = test_asset_gross * (1.0 - test_coverage_ratio)
        net_test_asset = max(0.0, test_asset_gross - test_depreciation)

        assets.append(
            TechnicalAsset(
                name="Automated Test Coverage Capital",
                category="Test Coverage Capital",
                gross_value_usd=test_asset_gross,
                accumulated_depreciation_usd=test_depreciation,
                net_book_value_usd=net_test_asset,
                description=f"Automated verification asset covering {test_coverage_ratio*100:.1f}% of production logic paths.",
            )
        )

        if has_modular_architecture:
            assets.append(
                TechnicalAsset(
                    name="Decoupled Modular Architecture",
                    category="Architecture Modularity",
                    gross_value_usd=250_000.0,
                    accumulated_depreciation_usd=25_000.0,
                    net_book_value_usd=225_000.0,
                    description="Standardized interface contracts allowing independent service scaling and agile team deployment.",
                )
            )

        # 3. Liabilities: Legacy Framework Obsolescence
        if legacy_frameworks:
            framework_list_str = ", ".join(legacy_frameworks)
            replatforming_cost = len(legacy_frameworks) * 90_000.0
            liabilities.append(
                TechnicalLiability(
                    name=f"End-of-Life Runtime & Framework Obsolescence ({framework_list_str})",
                    category="Legacy Obsolescence",
                    estimated_remediation_cost_usd=replatforming_cost,
                    annual_interest_drag_usd=replatforming_cost * 0.35,
                    severity="CRITICAL" if len(legacy_frameworks) > 1 else "HIGH",
                    description=(
                        f"Target relies on deprecated runtimes/libraries ({framework_list_str}) that no longer receive security patches, "
                        f"requiring mandatory re-platforming capex."
                    ),
                )
            )

        # 4. Liabilities: Circular Dependencies & Monolithic Coupling
        if circular_dependencies_count > 5:
            coupling_remediation = circular_dependencies_count * 5_000.0
            liabilities.append(
                TechnicalLiability(
                    name=f"High Architectural Coupling ({circular_dependencies_count} Circular Imports)",
                    category="Architectural Drag",
                    estimated_remediation_cost_usd=coupling_remediation,
                    annual_interest_drag_usd=coupling_remediation * 0.40,
                    severity="HIGH",
                    description="Severe entanglement between core domain and infrastructure layers, obstructing CI/CD velocity.",
                )
            )

        # 5. Compute Tech Debt Drag Percentage
        base_drag = 0.12  # Base friction
        if legacy_frameworks:
            base_drag += 0.10 * len(legacy_frameworks)
        if test_coverage_ratio < 0.40:
            base_drag += 0.08
        if circular_dependencies_count > 5:
            base_drag += 0.06

        drag_percentage = min(0.55, base_drag)  # Cap at 55%

        return assets, liabilities, drag_percentage
