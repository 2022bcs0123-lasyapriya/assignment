# Bagadi Lasya Priya - 2022BCS0123

def predict_risk(data):
    tickets_last_30 = data.get("tickets_last_30", 0)
    monthly_increase = data.get("monthly_increase", False)
    contract = data.get("contract", "")
    complaint = data.get("complaint_ticket", False)

    # RULE 1
    if tickets_last_30 > 5:
        return "HIGH RISK"

    # RULE 2
    if monthly_increase and tickets_last_30 >= 3:
        return "MEDIUM RISK"

    # RULE 3
    if contract == "Month-to-Month" and complaint:
        return "HIGH RISK"

    return "LOW RISK"