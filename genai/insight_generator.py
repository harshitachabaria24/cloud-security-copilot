import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "gemini-1.5-flash"  # try this, fallback handles failure

def generate_ai_insight(resource):

    usd_value = resource['estimated_savings']
    inr_value = usd_value * 83

    prompt = f"""
You are a Cloud Security AI Copilot.

Analyze this cloud resource:

Resource ID: {resource['resource_id']}
Cloud Provider: {resource['cloud_provider']}
Resource Type: {resource['resource_type']}
Detected Issues: {resource['issues']}
Risk Score: {resource['final_risk_score']}

Estimated Cost Savings:
- USD: ${usd_value}
- INR: ₹{round(inr_value, 2)}

Provide:
1. Security Risk Explanation
2. Business Impact
3. Cost Impact (USD + INR)
4. Recommended Fixes

Keep it simple and professional.
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[prompt]
        )

        return response.text if hasattr(response, "text") else str(response)

    except Exception as e:
        print("ERROR:", e)
        return fallback_insight(resource)


def fallback_insight(resource):

    usd_value = resource['estimated_savings']
    inr_value = usd_value * 83

    return f"""
[AI Insight Engine - Offline Mode]

🔴 Security Risk:
This resource is affected by: {resource['issues']}.

These issues increase exposure to cyber threats such as unauthorized access and data breaches.

💼 Business Impact:
- Potential compliance violations
- Increased attack surface
- Risk of financial and reputational loss

💰 Cost Impact:
- Estimated Waste: ${usd_value} (~₹{round(inr_value, 2)})

⚡ Recommended Actions:
- Remove public access immediately
- Enable encryption for sensitive data
- Apply least privilege IAM roles
- Optimize or terminate underutilized resources

📊 Priority Level: {resource['severity']}
"""