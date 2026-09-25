"""
Git Forensics & Key-Person Risk Engine.
Quantifies team entropy, bus factor concentration, and organizational knowledge debt.
"""

from __future__ import annotations
from typing import Any, Dict, List
from tech_balance_sheet.models import TechnicalLiability


class GitForensicsEngine:
    """
    Evaluates key-person risk, author concentration, and engineering turnover liabilities.
    """

    KEY_PERSON_REPLACEMENT_COST_USD = 120_000.0
    HIGH_CHURN_REFACTOR_COST_USD = 45_000.0

    def analyze(self, git_telemetry: Dict[str, Any]) -> List[TechnicalLiability]:
        liabilities: List[TechnicalLiability] = []

        top_author_share = git_telemetry.get("top_contributor_commit_ratio", 0.0)
        top_author_name = git_telemetry.get("top_contributor_name", "Primary Lead")
        active_committers = git_telemetry.get("active_contributors_count", 1)
        code_churn_rate = git_telemetry.get("annual_code_churn_percentage", 0.0)

        # Bus Factor / Key Person Risk
        if top_author_share >= 0.65 or active_committers <= 1:
            severity = "CRITICAL" if active_committers <= 1 else "HIGH"
            liabilities.append(
                TechnicalLiability(
                    name="Extreme Key-Person Dependency (Bus Factor = 1)",
                    category="Key-Person Risk",
                    estimated_remediation_cost_usd=self.KEY_PERSON_REPLACEMENT_COST_USD,
                    annual_interest_drag_usd=35_000.0,
                    severity=severity,
                    description=(
                        f"{top_author_name} authored {top_author_share*100:.1f}% of total codebase commits. "
                        f"Target business faces catastrophic operational disruption upon key-person departure post-close."
                    ),
                )
            )
        elif top_author_share >= 0.45:
            liabilities.append(
                TechnicalLiability(
                    name="Elevated Author Concentration Risk",
                    category="Key-Person Risk",
                    estimated_remediation_cost_usd=60_000.0,
                    annual_interest_drag_usd=18_000.0,
                    severity="MEDIUM",
                    description=(
                        f"Top contributor holds {top_author_share*100:.1f}% commit share. "
                        f"Requires immediate knowledge transfer documentation and team redundancy onboarding."
                    ),
                )
            )

        # High Churn / Architectural Instability
        if code_churn_rate >= 0.40:
            liabilities.append(
                TechnicalLiability(
                    name="High Code Churn & Architectural Instability",
                    category="Architectural Drag",
                    estimated_remediation_cost_usd=self.HIGH_CHURN_REFACTOR_COST_USD,
                    annual_interest_drag_usd=25_000.0,
                    severity="HIGH",
                    description=(
                        f"Annual codebase churn is {code_churn_rate*100:.1f}%, indicating frequent rewrites, "
                        f"brittle abstractions, and high regression probability during integration."
                    ),
                )
            )

        return liabilities
