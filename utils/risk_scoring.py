def calculate_final_risk(security_results, cost_results):

    final_results = []

    for sec, cost in zip(security_results, cost_results):

        score = 0
        issues = sec['issues']

        # =========================
        # SECURITY SCORING
        # =========================

        if "Publicly accessible resource" in issues:
            score += 40

        if "Encryption disabled" in issues:
            score += 30

        if "Excess IAM privileges" in issues:
            score += 30

        # =========================
        # COST SCORING
        # =========================

        savings = cost['estimated_savings']

        if savings > 100:
            score += 20
        elif savings > 50:
            score += 10

        # =========================
        # LIMIT SCORE
        # =========================

        score = min(score, 100)

        # =========================
        # SEVERITY
        # =========================

        if score >= 80:
            severity = "High"
        elif score >= 40:
            severity = "Medium"
        else:
            severity = "Low"

        final_results.append({
            "resource_id": sec['resource_id'],
            "cloud_provider": sec['cloud_provider'],
            "resource_type": sec['resource_type'],
            "issues": issues,
            "estimated_savings": savings,
            "final_risk_score": score,
            "severity": severity
        })

    return final_results