from rag.rag_engine import retrieve_context
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "gemini-1.5-flash"


# ================================
# SMART PREDEFINED QUERIES
# ================================
def handle_predefined_queries(query, results):

    query = query.lower()

    if "highest risk" in query:
        high = [r for r in results if r['severity'] == "High"]

        return f"""
🚨 High Risk Resources Identified:

{[r['resource_id'] for r in high]}

These resources have:
- Public exposure
- Missing encryption
- Excess IAM privileges

👉 Immediate action recommended.
"""

    if "cost" in query or "waste" in query:
        total = sum(r['estimated_savings'] for r in results)

        return f"""
💰 Cloud Cost Optimization Insight:

Total Potential Savings:
- USD: ${total}
- INR: ₹{round(total * 83, 2)}

👉 Optimize or terminate underutilized resources.
"""

    if "security issues" in query:
        issues = set()

        for r in results:
            for i in r['issues'].split(", "):
                if i != "No major issues":
                    issues.add(i)

        return f"""
🔐 Critical Security Issues Detected:

{list(issues)}

👉 These increase vulnerability and attack surface.
"""

    return None


# ================================
# FALLBACK RESPONSE
# ================================
def fallback_response():

    return """
[AI Copilot - Context Mode]

🔍 Key Observations:
- Public exposure exists in multiple resources
- Encryption is missing in critical components
- IAM permissions are overly broad

⚠️ Risk Insight:
These increase attack surface and breach risk.

💡 Recommended Actions:
- Restrict public access
- Enable encryption
- Apply least privilege IAM
- Optimize unused resources

📊 Generated using contextual reasoning (RAG).
"""


# ================================
# MAIN COPILOT FUNCTION
# ================================
def ask_copilot(query, final_results):

    # 1. Try predefined logic
    pre = handle_predefined_queries(query, final_results)
    if pre:
        return pre

    # 2. RAG context
    context = retrieve_context(query)

    prompt = f"""
You are a Cloud Security AI Copilot.

Use the following cloud data:

{context}

User Question:
{query}

Answer clearly with:
- Explanation
- Risk reasoning
- Suggested actions
"""

    # 3. Try Gemini
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[prompt]
        )

        return response.text if hasattr(response, "text") else str(response)

    except Exception as e:
        print("RAG ERROR:", e)

        # 4. Fallback
        return fallback_response()