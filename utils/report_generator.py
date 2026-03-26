def generate_summary(final_results, total_waste):

    total_resources = len(final_results)

    high = 0
    medium = 0
    low = 0

    issues_set = set()

    # Count risks + collect issues
    for r in final_results:

        if r['severity'] == "High":
            high += 1
        elif r['severity'] == "Medium":
            medium += 1
        else:
            low += 1

        issues = r['issues'].split(", ")
        for i in issues:
            if i != "No major issues":
                issues_set.add(i)

    # Convert to list
    issues_list = list(issues_set)

    # Cost conversion
    usd_waste = total_waste
    inr_waste = usd_waste * 83

    # Smart Recommendations
    recommendations = []

    if "Publicly accessible resource" in issues_set:
        recommendations.append("Disable public access to sensitive resources")

    if "Encryption disabled" in issues_set:
        recommendations.append("Enable encryption for all storage and databases")

    if "Excess IAM privileges (Admin access)" in issues_set:
        recommendations.append("Apply least privilege IAM policies")

    if usd_waste > 0:
        recommendations.append("Optimize or terminate underutilized resources to reduce cloud costs")

    # FINAL FORMATTED SUMMARY (VERY IMPORTANT)
    summary_text = f"""
================ EXECUTIVE SUMMARY ================

Total Resources Analyzed: {total_resources}

Risk Distribution:
- High Risk: {high}
- Medium Risk: {medium}
- Low Risk: {low}

Estimated Monthly Cost Waste:
- USD: ${usd_waste}
- INR: ₹{round(inr_waste, 2)}

Key Issues Identified:
"""

    for issue in issues_list:
        summary_text += f"\n• {issue}"

    summary_text += "\n\nTop Recommendations:\n"

    for rec in recommendations:
        summary_text += f"\n• {rec}"

    summary_text += "\n\n================================================="

    return summary_text