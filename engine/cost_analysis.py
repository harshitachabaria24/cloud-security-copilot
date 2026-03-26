def detect_cost_issues(df):

    results = []
    total_waste = 0

    for index, row in df.iterrows():

        issues = []
        estimated_savings = 0

        # Rule 1: Low CPU utilization (idle resource)
        if row['cpu_utilization'] < 10:
            issues.append("Underutilized resource (CPU < 10%)")
            estimated_savings += row['monthly_cost'] * 0.5

        # Rule 2: Zero utilization (completely unused)
        if row['cpu_utilization'] == 0:
            issues.append("Unused resource (CPU = 0%)")
            estimated_savings += row['monthly_cost'] * 0.8

        # Rule 3: Storage without usage (simple assumption)
        if row['resource_type'] == 'storage' and row['cpu_utilization'] == 0:
            issues.append("Unused storage resource")
            estimated_savings += row['monthly_cost'] * 0.7

        total_waste += estimated_savings

        results.append({
            "resource_id": row['resource_id'],
            "cost_issues": ", ".join(issues) if issues else "No major cost issues",
            "estimated_savings": round(estimated_savings, 2),
            "monthly_cost": row['monthly_cost']
        })

    return results, round(total_waste, 2)