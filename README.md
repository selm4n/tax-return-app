# Tax Return Impact Simulator (MVP)

This is a simple **command-line tax simulation tool** for Canadian residents,
starting with **T4 employees in Ontario**.

The goal is not tax filing, but **tax awareness and planning**:
to help users see the **impact of their financial decisions**
*before* tax season.

---

## What This Tool Does

- Explains **T4 boxes** (Box 14, Box 22, etc.) in plain language
- Simulates tax outcomes step by step
- Shows the impact of:
  - RRSP contributions
  - Charitable donations
- Clearly separates:
  - **Refund**
  - **Amount owing**

This is an **estimation tool**, not official CRA tax software.

---

## Current Scope (MVP)

- T4 employment income
- Ontario residents
- RRSP impact on taxable income
- Donation tax credits (simplified)
- Single estimated tax rate (configurable)

Future versions may include:
- Progressive tax brackets
- Self-employed income
- Small business / corporation scenarios

---

## Requirements

- Python 3.8 or newer
- No external libraries required

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/selm4n/tax-return-app.git
cd tax-return-app
