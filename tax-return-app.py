#!/usr/bin/env python3

def money(x):
    return f"${x:,.2f}"

def ask_number(title, explanation, default=None):
    print(f"\n{title}")
    print(f"→ {explanation}")
    while True:
        raw = input(f"Enter amount{f' (default {default})' if default is not None else ''}: ").strip()
        if raw == "" and default is not None:
            return float(default)
        try:
            return float(raw.replace(",", ""))
        except ValueError:
            print("Please enter a valid number (e.g. 80000 or 80,000)")

def donation_credit(d):
    d = max(0, d)
    return min(d, 200) * 0.20 + max(d - 200, 0) * 0.40

def calculate(income, tax_deducted, rrsp, donation, tax_rate):
    taxable_income = max(0, income - rrsp)
    estimated_tax = taxable_income * tax_rate
    donation_cr = donation_credit(donation)
    final_tax = max(0, estimated_tax - donation_cr)

    refund = max(0, tax_deducted - final_tax)
    owing = max(0, final_tax - tax_deducted)

    return {
        "taxable_income": taxable_income,
        "estimated_tax": estimated_tax,
        "donation_credit": donation_cr,
        "final_tax": final_tax,
        "refund": refund,
        "owing": owing
    }

def main():
    print("\n==============================")
    print(" TaxImpact – Guided Tax Simulator (MVP)")
    print("==============================")
    print("This tool helps you SEE the tax impact of your decisions.")
    print("It is an estimation tool, not official tax filing.\n")

    # BOX 14
    income = ask_number(
        "T4 – Box 14: Employment Income",
        "This is your TOTAL employment income for the year.\n"
        "You can find this on your T4 slip, Box 14."
    )

    # BOX 22
    tax_deducted = ask_number(
        "T4 – Box 22: Income Tax Deducted",
        "This is the TOTAL income tax your employer already deducted\n"
        "from your paycheques during the year."
    )

    # RRSP
    rrsp = ask_number(
        "RRSP Contribution",
        "RRSP reduces your TAXABLE income.\n"
        "If you contributed during the year, enter the total amount.",
        default=0
    )

    # DONATION
    donation = ask_number(
        "Charitable Donations",
        "Donations do NOT reduce income.\n"
        "They give you a TAX CREDIT that reduces tax payable.",
        default=0
    )

    # TAX RATE
    tax_rate = ask_number(
        "Estimated Total Tax Rate (Federal + Ontario)",
        "This is an approximation used for simulation.\n"
        "For Ontario employees, 0.30 is a reasonable average.",
        default=0.30
    )

    # CALCULATIONS
    baseline = calculate(income, tax_deducted, 0, 0, tax_rate)
    after = calculate(income, tax_deducted, rrsp, donation, tax_rate)

    improvement = baseline["final_tax"] - after["final_tax"]

    # SUMMARY
    print("\n==============================")
    print(" SUMMARY")
    print("==============================")

    print("\n--- Current situation (no RRSP, no donation) ---")
    print(f"Estimated tax payable: {money(baseline['final_tax'])}")
    print(f"Refund:               {money(baseline['refund'])}")
    print(f"Amount owing:         {money(baseline['owing'])}")

    print("\n--- After your decisions (RRSP + donation) ---")
    print(f"Estimated tax payable: {money(after['final_tax'])}")
    print(f"Refund:               {money(after['refund'])}")
    print(f"Amount owing:         {money(after['owing'])}")

    print("\n--- Impact of your decisions ---")
    if improvement > 0:
        print(f"✅ Your tax position improved by {money(improvement)}")
    elif improvement < 0:
        print(f"⚠️ Your tax position worsened by {money(-improvement)}")
    else:
        print("No change in tax position.")

    print("\nThank you for using TaxImpact.")
    print("Remember: this is an estimate, not CRA filing.\n")

if __name__ == "__main__":
    main()
