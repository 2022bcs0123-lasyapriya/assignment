from rules import predict_risk

def test_high_risk():
    data = {
        "tickets_last_30": 6,
        "monthly_increase": False,
        "contract": "Yearly",
        "complaint_ticket": False
    }
    assert predict_risk(data) == "HIGH RISK"