"""
CVE & Cyber Risk Actuarial Engine.
Translates software vulnerabilities and cloud misconfigurations into actuarial dollar liabilities.
"""

from __future__ import annotations
from typing import Any, Dict, List
from tech_balance_sheet.models import TechnicalLiability


class CveActuarialEngine:
    """
    Computes actuarial balance-sheet liabilities and annual interest drag
    for software CVEs, infrastructure leaks, and Post-Quantum cryptographic gaps.
    """

    CRITICAL_CVE_REMEDIATION_USD = 25_000.0
    CRITICAL_CVE_ANNUAL_DRAG_USD = 12_500.0

    HIGH_CVE_REMEDIATION_USD = 8_000.0
    HIGH_CVE_ANNUAL_DRAG_USD = 3_500.0

    MEDIUM_CVE_REMEDIATION_USD = 2_000.0
    MEDIUM_CVE_ANNUAL_DRAG_USD = 500.0

    PUBLIC_BUCKET_REMEDIATION_USD = 75_000.0
    POST_QUANTUM_DEFICIT_REMEDIATION_USD = 120_000.0

    def analyze(self, security_telemetry: Dict[str, Any]) -> List[TechnicalLiability]:
        liabilities: List[TechnicalLiability] = []

        critical_cves = security_telemetry.get("critical_cves", 0)
        high_cves = security_telemetry.get("high_cves", 0)
        medium_cves = security_telemetry.get("medium_cves", 0)
        public_buckets = security_telemetry.get("public_storage_buckets", 0)
        pqc_ready = security_telemetry.get("post_quantum_fips_204_ready", True)

        if critical_cves > 0:
            total_remediation = critical_cves * self.CRITICAL_CVE_REMEDIATION_USD
            annual_drag = critical_cves * self.CRITICAL_CVE_ANNUAL_DRAG_USD
            liabilities.append(
                TechnicalLiability(
                    name=f"Critical CVSS 9.0+ Vulnerabilities ({critical_cves} CVEs)",
                    category="Security / CVE",
                    estimated_remediation_cost_usd=total_remediation,
                    annual_interest_drag_usd=annual_drag,
                    severity="CRITICAL",
                    description=f"{critical_cves} remotely exploitable critical vulnerabilities requiring immediate hot-patching and security audit.",
                )
            )

        if high_cves > 0:
            total_remediation = high_cves * self.HIGH_CVE_REMEDIATION_USD
            annual_drag = high_cves * self.HIGH_CVE_ANNUAL_DRAG_USD
            liabilities.append(
                TechnicalLiability(
                    name=f"High CVSS 7.0-8.9 Vulnerabilities ({high_cves} CVEs)",
                    category="Security / CVE",
                    estimated_remediation_cost_usd=total_remediation,
                    annual_interest_drag_usd=annual_drag,
                    severity="HIGH",
                    description=f"{high_cves} high-severity CVEs presenting supply-chain or unauthorized access risk.",
                )
            )

        if medium_cves > 0:
            total_remediation = medium_cves * self.MEDIUM_CVE_REMEDIATION_USD
            annual_drag = medium_cves * self.MEDIUM_CVE_ANNUAL_DRAG_USD
            liabilities.append(
                TechnicalLiability(
                    name=f"Medium Severity CVE Backlog ({medium_cves} CVEs)",
                    category="Security / CVE",
                    estimated_remediation_cost_usd=total_remediation,
                    annual_interest_drag_usd=annual_drag,
                    severity="MEDIUM",
                    description=f"Accumulated unpatched library versions and dependencies with known vulnerabilities.",
                )
            )

        if public_buckets > 0:
            liabilities.append(
                TechnicalLiability(
                    name="Public Cloud Storage Exposure",
                    category="Security / CVE",
                    estimated_remediation_cost_usd=public_buckets * self.PUBLIC_BUCKET_REMEDIATION_USD,
                    annual_interest_drag_usd=25_000.0,
                    severity="CRITICAL",
                    description=f"{public_buckets} public AWS S3 / GCP buckets detected with unauthenticated object read access.",
                )
            )

        if not pqc_ready:
            liabilities.append(
                TechnicalLiability(
                    name="Post-Quantum Cryptography Deficit (NIST FIPS 203/204)",
                    category="Security / CVE",
                    estimated_remediation_cost_usd=self.POST_QUANTUM_DEFICIT_REMEDIATION_USD,
                    annual_interest_drag_usd=15_000.0,
                    severity="MEDIUM",
                    description="Absence of quantum-resistant algorithm agility, triggering compliance friction under emerging federal standards.",
                )
            )

        return liabilities
