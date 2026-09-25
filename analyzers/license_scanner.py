"""
License & IP Contamination Forensics.
Audits open-source dependencies for copyleft contagion (GPL/AGPL) in commercial closed-source M&A targets.
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional
from tech_balance_sheet.models import TechnicalLiability


import re

class LicenseForensicsEngine:
    """
    Quantifies proprietary IP contamination risks arising from viral open-source licenses.
    """

    VIRAL_LICENSES = {
        "AGPL-3.0": {"liability_usd": 250_000.0, "drag_usd": 35_000.0, "severity": "CRITICAL"},
        "GPL-3.0": {"liability_usd": 150_000.0, "drag_usd": 20_000.0, "severity": "HIGH"},
        "GPL-2.0": {"liability_usd": 100_000.0, "drag_usd": 15_000.0, "severity": "HIGH"},
        "SSPL-1.0": {"liability_usd": 180_000.0, "drag_usd": 25_000.0, "severity": "HIGH"},
    }

    def analyze(self, dependency_licenses: List[Dict[str, str]]) -> List[TechnicalLiability]:
        liabilities: List[TechnicalLiability] = []
        found_viral: Dict[str, List[str]] = {}

        for dep in dependency_licenses:
            pkg_name = dep.get("package", "unknown")
            license_id = dep.get("license", "").strip().upper()

            # Check AGPL first to avoid GPL partial match
            for viral_id in sorted(self.VIRAL_LICENSES.keys(), key=len, reverse=True):
                pattern = rf"(^|[^A-Z0-9]){re.escape(viral_id)}([^A-Z0-9]|$)"
                if re.search(pattern, license_id):
                    found_viral.setdefault(viral_id, []).append(pkg_name)
                    break

        for viral_id, packages in found_viral.items():
            meta = self.VIRAL_LICENSES[viral_id]
            pkg_list_str = ", ".join(packages[:3])
            if len(packages) > 3:
                pkg_list_str += f" (+{len(packages) - 3} more)"

            liabilities.append(
                TechnicalLiability(
                    name=f"Copyleft License Contamination ({viral_id})",
                    category="IP Contamination",
                    estimated_remediation_cost_usd=meta["liability_usd"] * len(packages),
                    annual_interest_drag_usd=meta["drag_usd"],
                    severity=meta["severity"],
                    description=(
                        f"Detected {len(packages)} proprietary module dependencies under viral copyleft license {viral_id} "
                        f"({pkg_list_str}). Threatens proprietary IP exclusivity and presents forced open-sourcing or commercial re-architecture liability."
                    ),
                )
            )

        return liabilities
