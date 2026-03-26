def detect_security_issues(df):

    results = []

    for _, row in df.iterrows():

        issues = []

        # Normalize values
        public_access = str(row['public_access']).strip().lower()
        encryption = str(row['encryption_enabled']).strip().lower()
        iam = str(row['iam_privilege']).strip().lower()

        # =========================
        # RULES
        # =========================

        if public_access == "yes":
            issues.append("Publicly accessible resource")

        if encryption == "no":
            issues.append("Encryption disabled")

        if iam == "admin":
            issues.append("Excess IAM privileges (Admin access)")

        # Default
        if not issues:
            issues.append("No major issues")

        results.append({
            "resource_id": row['resource_id'],
            "cloud_provider": row['cloud_provider'],
            "resource_type": row['resource_type'],
            "issues": ", ".join(issues)
        })

    return results