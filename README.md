# 🏛️ tech-balance-sheet
> **Autonomous M&A Technical Due Diligence & Board-Level Software Balance Sheet OS**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-5%2F5%20Passing-brightgreen.svg)]()
[![Target Buyers](https://img.shields.io/badge/Buyers-PE%20Buyout%20Funds%20%7C%20CFOs%20%7C%20Boards-purple.svg)]()
[![P&L Drag](https://img.shields.io/badge/Financial%20Audit-GAAP--Adjacent-gold.svg)]()

`tech-balance-sheet` is an enterprise financial-forensic platform that translates source code repositories, software architecture, security vulnerabilities, and team dynamics into **defensible M&A valuation haircuts** for Private Equity deal teams and **GAAP-adjacent Technical Balance Sheets** for corporate Boards and CFOs.

---

## The Strategic Thesis

Every CFO and Board of Directors understands financial debt, depreciation schedules, and capital expenditures. But they have **zero visibility into technical liabilities** until a $20M re-platforming project fails, an outage makes the news, or an acquirer walks away from a deal.

Simultaneously, in software M&A, Private Equity buyout funds pay **$75,000 to $150,000 per deal** to advisory firms (Alvarez & Marsal, West Monroe, Deloitte) for 3-week manual IT due diligence slide decks that lack mathematical leverage during price negotiations.

`tech-balance-sheet` bridges this gap with an algorithmic valuation and balance-sheet engine:
1. **For Buy-Side M&A / Private Equity:** Ingests target data rooms and codebases to output a quantitative **Investment Committee Tech Diligence Memo** with an exact purchase price haircut calculation and escrow holdback clauses within 24 hours.
2. **For Corporate CFOs & Boards:** Generates a quarterly **Technical Balance Sheet and P&L Statement**, translating tech debt interest into wasted engineering payroll and establishing a software credit rating (AAA down to D).

---

## High-Level System Architecture

```mermaid
flowchart TD
    subgraph Ingestion ["1. Forensic Ingestion Enclave"]
        REPO["Source Repositories\n(Git Log, Churn, Bus Factor)"]
        DEPS["Dependency Tree\n(GPL/AGPL License Scanner)"]
        VULN["Security Telemetry\n(CVSS v3/v4 & Actuarial CVEs)"]
        ARCH["Architecture Topology\n(Monoliths, Circular Imports, Test Capital)"]
    end

    subgraph Engine ["2. Forensic Financial Engine (tech-balance-sheet)"]
        ACTUARY["CVE & Cyber Actuary Engine\n(NVD Remediation Cost + Annual Drag)"]
        IP_SCAN["License Forensics Engine\n(Viral Copyleft Contamination Risk)"]
        BUS_SCAN["Git Forensics Engine\n(Key-Person Risk & Team Turnover)"]
        DRIFT_SCAN["Architecture Drift Engine\n(Legacy Obsolescence & Test Assets)"]

        INGESTION_ORCH["TechBalanceSheetEngine"]
        ACTUARY --> INGESTION_ORCH
        IP_SCAN --> INGESTION_ORCH
        BUS_SCAN --> INGESTION_ORCH
        DRIFT_SCAN --> INGESTION_ORCH
    end

    subgraph DualOutput ["3. Executive & Deal Team Synthesis"]
        subgraph PE_Track ["Track A: M&A / Private Equity Deal Teams"]
            IC_GEN["ICMemoReporter"]
            IC_MEMO["Investment Committee Tech Diligence Memo\n(Markdown, HTML, PDF)"]
            HAIRCUT["Defensible Valuation Haircut\n(Purchase Price Reduction)"]
            IC_GEN --> IC_MEMO
            IC_GEN --> HAIRCUT
        end

        subgraph CFO_Track ["Track B: CFOs & Board of Directors"]
            CFO_GEN["CfoBalanceSheetReporter"]
            BS_STMT["Board Technical Balance Sheet\n(Assets, Liabilities, Solvency Grade)"]
            PL_STMT["Technical Income Statement\n(Wasted Engineering Payroll & ROI)"]
            CFO_GEN --> BS_STMT
            CFO_GEN --> PL_STMT
        end
    end

    REPO --> INGESTION_ORCH
    DEPS --> INGESTION_ORCH
    VULN --> INGESTION_ORCH
    ARCH --> INGESTION_ORCH

    INGESTION_ORCH --> PE_Track
    INGESTION_ORCH --> CFO_Track
```

---

## The Technical Balance Sheet Equation

Just like GAAP financial accounting, the software codebase is modeled as a capital structure:

$$\mathbf{Net\ Technical\ Asset\ Value\ (NTAV)} = \mathbf{Technical\ Assets} - \mathbf{Technical\ Liabilities}$$

```mermaid
graph LR
    subgraph Assets ["Technical Assets (Capitalized Code Base)"]
        A1["Proprietary Core IP ($15/LOC gross)"]
        A2["Automated Test Coverage Capital (Insurance Value)"]
        A3["Modular Decoupled Architecture Asset"]
    end

    subgraph Liabilities ["Technical Liabilities (Accrued Debt)"]
        L1["Security & CVE Remediation (CVSS Actuarial Cost)"]
        L2["Copyleft License Contamination (AGPL/GPL IP Risk)"]
        L3["Key-Person Bus Factor Exposure (Retention Deficit)"]
        L4["Legacy Framework Obsolescence (Re-platforming Capex)"]
        L5["Architectural Drag & Circular Coupling"]
    end

    subgraph Solvency ["Capital Position & Credit Grade"]
        NET["Net Technical Asset Value (NTAV)"]
        RATIO["Debt-to-Technical-Equity Ratio"]
        GRADE["Software Health Grade (AAA to D)"]
    end

    Assets --> NET
    Liabilities --> NET
    NET --> RATIO
    RATIO --> GRADE
```

---

## M&A Valuation Haircut Waterfall

In buyout transactions, valuation is adjusted systematically across two primary levers: **Multiple Compression** and **Direct Dollar-for-Dollar Deductions**:

$$\text{Final\ Valuation} = \left[\text{EBITDA} \times (\text{Multiple}_{base} + \sum \Delta \text{Multiple})\right] - \sum \text{Direct\ Liabilities}$$

```mermaid
flowchart LR
    A["Baseline Enterprise Value\n(e.g., $6.2M EBITDA @ 14.0x = $86.8M)"] --> B{"Multiple Drag\nAdjustments"}
    B -->|"-10% Missing SOC 2"| C1["Compliance Penalty"]
    B -->|"-8% Copyleft Contamination"| C2["IP Risk Penalty"]
    B -->|"-7% Customer Concentration"| C3["Concentration Penalty"]
    B -->|"-6% Bus Factor Dependency"| C4["Key-Person Penalty"]
    B -->|"-5% Legacy Runtime Obsolescence"| C5["Obsolescence Penalty"]

    C1 & C2 & C3 & C4 & C5 --> D["Subtotal: Multiple-Adjusted EV\n($55.5M @ 8.96x)"]
    D --> E{"Direct Dollar Deductions\n(1:1 Balance Sheet Liabilities)"}
    E -->|"-$279k CVE Hot-Patching"| F1["Cyber Remediation"]
    E -->|"-$400k AGPL Re-Licensing"| F2["IP Settlement"]
    E -->|"-$180k Re-Platforming Capex"| F3["Legacy Capex"]

    F1 & F2 & F3 --> G["Final Recommended Valuation\n($54.2M)"]
    G --> H["Total Defensive Haircut Captured:\n$32,575,000.00 (-37.5%)"]
```

---

## Track 1: Private Equity 24-Hour Diligence Workflow

The following sequence diagram details how the automated diligence engine interfaces with the target's Virtual Data Room (VDR), executes forensic analyzers, and arms the PE Deal Team with an Investment Committee memo before signing the LOI:

```mermaid
sequenceDiagram
    autonumber
    actor DealTeam as PE Deal Team / Investment Committee
    participant VDR as Target VDR & Codebase
    participant Diligence as tech-balance-sheet Engine
    participant Actuary as Forensic Actuarial Suite
    actor TargetFounder as Target Company Founders

    DealTeam->>VDR: Grant Ephemeral Access (Read-Only Git/Cloud)
    VDR->>Diligence: Ingest Git Log, Dependencies & Telemetry
    par Parallel Forensic Scans
        Diligence->>Actuary: CVE & Cloud Exposure Audit
        Diligence->>Actuary: Copyleft IP Contamination Scan (AGPL/GPL)
        Diligence->>Actuary: Git Author Entropy & Bus-Factor Check
        Diligence->>Actuary: Architectural Obsolescence & Test Capital
    end
    Actuary-->>Diligence: Raw Forensic Liabilities & Risk Ratios
    Diligence->>Diligence: Compute Multiple Compression & Direct Dollar Deductions
    Diligence->>Diligence: Formulate Escrow Holdback (150% of Direct Liabilities)
    Diligence-->>DealTeam: Deliver IC Due Diligence Memo & Haircut Report
    DealTeam->>TargetFounder: Present Re-negotiated Valuation & Escrow Clauses
    Note over DealTeam,TargetFounder: Deal team captures $10M-$30M defensive purchase price reduction before signing LOI
```

---

## Track 3: The Board & CFO Tech Debt P&L Drag Loop

The following architectural model illustrates how technical debt acts as an uncapitalized tax on engineering payroll, and how targeted remediation unlocks a multi-year velocity dividend:

```mermaid
flowchart TD
    subgraph Payroll ["Corporate P&L Budget Allocation"]
        GROSS_PAYROLL["Total Engineering Payroll\n(e.g., $4.8M / year)"]
    end

    subgraph DebtDrag ["The Hidden Debt Interest Tax"]
        DRAG_RATIO{"Technical Debt Drag Ratio\n(28.5% - 46.0%)"}
        WASTED_CASH["Wasted Engineering Payroll\n($1.3M - $2.2M / year in friction)"]
        EFFECTIVE_RD["Net Productive R&D Innovation\n(Remaining $2.6M - $3.4M capacity)"]
        
        GROSS_PAYROLL --> DRAG_RATIO
        DRAG_RATIO -->|"Friction Loss"| WASTED_CASH
        DRAG_RATIO -->|"Actual Velocity"| EFFECTIVE_RD
    end

    subgraph CFO_Action ["Board Capital Allocation Decision"]
        AUDIT["tech-balance-sheet Audit\n(Identifies High-ROI Remediation Hotspots)"]
        CAPEX["Targeted Year 1 Remediation Capex\n(e.g., $280k - $320k budget)"]
        DIVIDEND["Annual Velocity Dividend\n(+$880k/year in unlocked developer capacity)"]
        ROI["Projected 2-Year ROI: +380% to +530%"]

        WASTED_CASH --> AUDIT
        AUDIT --> CAPEX
        CAPEX --> DIVIDEND
        DIVIDEND --> ROI
        ROI -->|"Reinvest in Core IP Assets"| GROSS_PAYROLL
    end
```

---

### 1. Board Technical Balance Sheet
```text
================================================================================
📊 BOARD OF DIRECTORS: TECHNICAL BALANCE SHEET
================================================================================
ASSETS (Capitalized Software Assets)
* Proprietary Codebase & Domain IP:       $2,470,000.00 (Net Book Value)
* Automated Test Coverage Capital:          $480,000.00 (Net Book Value)
* Modular Architecture Capital:             $225,000.00 (Net Book Value)
TOTAL TECHNICAL ASSETS:                   $3,175,000.00

LIABILITIES (Accrued Technical Debt Obligations)
* Critical CVSS 9.0+ Vulnerabilities:       $75,000.00 ($37,500/yr drag)
* Copyleft License Contamination (AGPL):   $250,000.00 ($35,000/yr drag)
* Extreme Key-Person Dependency:           $120,000.00 ($35,000/yr drag)
* End-of-Life Runtime (Python 2.7):        $180,000.00 ($63,000/yr drag)
TOTAL TECHNICAL LIABILITIES:                $625,000.00

NET TECHNICAL POSITION
* Net Technical Asset Value (NTAV):       $2,550,000.00
* Software Health Rating:                 AA (Solvent, manageable debt)
```

### 2. CFO Technical Income Statement (P&L Drag)
```text
================================================================================
📈 TECHNICAL INCOME STATEMENT (P&L DRAG ANALYSIS)
================================================================================
Total Annual Engineering Payroll:         $4,800,000.00
Technical Debt Drag & Velocity Loss:     ($1,368,000.00) (28.5% drag)
Net Effective R&D Capacity:               $3,432,000.00

Remediation Capital Allocation & ROI Forecast:
* Recommended Year 1 Remediation Capex:     $281,250.00
* Projected Annual Velocity Dividend:       $889,200.00/year unlocked capacity
* Projected 2-Year Remediation ROI:        +532.2%
```

---

## CLI Quickstart

### Running the End-to-End M&A + CFO Demo
```bash
PYTHONPATH=projects python3 -m tech_balance_sheet.cli demo
```

Output:
```text
🚀 Running Autonomous Tech Diligence & Balance Sheet Audit for: CloudFlow Logistics Corp
   Baseline EBITDA: $6,200,000.00 @ 14.0x
   Baseline Enterprise Value: $86,800,000.00

================================================================================
🏛️ PRIVATE EQUITY INVESTMENT COMMITTEE MEMO
================================================================================
Verdict: WALK_AWAY
Baseline Enterprise Value: $86,800,000.00
Adjusted Enterprise Value: $54,225,000.00
Defensive Haircut Captured: $32,575,000.00 (-37.5%)
Recommended Escrow Holdback: $1,990,500.00
Critical Red Flags Identified: 5

================================================================================
📊 BOARD OF DIRECTORS & CFO BALANCE SHEET
================================================================================
Total Technical Assets: $4,016,296.00
Total Technical Liabilities: $1,327,000.00
Net Technical Asset Value: $2,689,296.00
Software Health Credit Grade: A
Annual Wasted Payroll on Tech Debt: $2,208,000.00/yr (46.0%)
Projected 2-Year Remediation ROI: +380.7%

✅ Reports successfully generated:
   - ./output_reports/cfo_technical_balance_sheet.md
   - ./output_reports/ic_due_diligence_memo.md
   - ./output_reports/audit_summary.json
```

---

## Running Test Suite

```bash
PYTHONPATH=projects python3 -m unittest discover -s projects/tech_balance_sheet/tests -v
```

```text
test_cve_actuarial_engine ... ok
test_full_engine_accounting_invariants ... ok
test_git_forensics_bus_factor ... ok
test_license_forensics_copyleft ... ok
test_reporters_render_clean_markdown ... ok

Ran 5 tests in 0.001s (OK)
```

---

## License
Apache-2.0
