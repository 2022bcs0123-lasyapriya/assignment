# Churn Prediction DevOps System by Bagadi Lasya Priya (2022BCS0123)

## Overview
This project implements a rule-based churn prediction system using DevOps practices.

## Features
- Rule-based prediction engine
- REST API (/predict-risk)
- Dockerized service
- CI/CD pipeline using GitHub Actions
- Logging and testing

## Rules Used
1. >5 tickets → HIGH RISK
2. Monthly increase + 3 tickets → MEDIUM RISK
3. Month-to-Month + complaint → HIGH RISK
4. Else → LOW RISK

## How to Run

```bash
uvicorn app:app --reload
