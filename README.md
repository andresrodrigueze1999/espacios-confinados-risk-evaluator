# Confined Space Risk Evaluator (Res. 0491/2020 Colombia) 🇨🇴🦺

A Python library and CLI tool designed to automate risk classification, permit generation requirements, and safety compliance checks for confined spaces based on **Resolution 0491 of 2020 (Colombian Ministry of Labor)**.

## Features
- **Classification Engine:** Automatically categorizes confined spaces into **Type 1 / Type 2** and **Grade A, B, or C** depending on oxygen levels, toxic gases, and access constraints.
- **Compliance Validation:** Generates pre-entry checklists (Atmospheric testing, Ventilation, LOTO, Entry Permits, Supervisor assignment).
- **JSON & Markdown Export:** Outputs structured compliance payloads for safety management systems (SG-SST).
- **Zero Heavy Dependencies:** Written in pure Python 3.8+ with standard libraries.

## Legal Grounding
Implements algorithmic rules strictly aligned with:
- **Resolución 0491 de 2020** (Ministerio del Trabajo de Colombia).
- **ANSI/ASSE Z117.1** safety principles adapted for local legislation.

## Quick Start

```bash
# Clone the repository
git clone https://github.com/your-username/espacios-confinados-risk-evaluator.git
cd espacios-confinados-risk-evaluator

# Run test suite
python -m unittest discover tests

# Evaluate a confined space
python src/evaluator.py --o2 19.0 --h2s 12.0 --lfe 5.0
```

## Example Output

```json
{
  "classification_grade": "Grade A",
  "space_type": "Type 1",
  "requires_entry_permit": true,
  "continuous_ventilation_required": true,
  "hazard_level": "CRITICAL",
  "legal_warnings": [
    "Oxygen level below 19.5% (Resolution 0491 Art. 6)",
    "H2S level exceeds STEL/TWA threshold"
  ]
}
```

## Contributing
Pull requests, additional OEL (Occupational Exposure Limit) definitions, and local SG-SST integrations are welcome!

## License
[MIT](LICENSE)
