from engine.data_loader import load_and_process_data
from engine.security_analysis import detect_security_issues
from engine.cost_analysis import detect_cost_issues
from utils.risk_scoring import calculate_final_risk
from genai.insight_generator import generate_ai_insight
from utils.report_generator import generate_summary

from rag.rag_engine import build_vector_store
from rag.copilot import ask_copilot


# ================================
# STEP 1: Load Data
# ================================
df = load_and_process_data("data/cloud_resources.csv")


# ================================
# STEP 2: Run Analysis
# ================================
security_results = detect_security_issues(df)
cost_results, total_waste = detect_cost_issues(df)


# ================================
# STEP 3: Risk Scoring
# ================================
final_results = calculate_final_risk(security_results, cost_results)


# ================================
# STEP 4: AI Insights (Gemini)
# ================================
print("\n========= AI INSIGHTS =========")

for r in final_results:
    if r['severity'] == "High":
        print(f"\n--- Resource {r['resource_id']} ---")
        print(generate_ai_insight(r))


# ================================
# STEP 5: Build RAG Vector Store
# ================================
build_vector_store(final_results)


# ================================
# STEP 6: RAG Copilot Queries
# ================================
print("\n========= RAG COPILOT =========")

queries = [
    "Which resources are highest risk and why?",
    "How can I reduce cloud cost?",
    "What are the most critical security issues?"
]

for q in queries:
    print(f"\nUser: {q}")
    print("Copilot:", ask_copilot(q))


# ================================
# STEP 7: Executive Summary
# ================================
summary = generate_summary(final_results, total_waste)

print("\n========= EXECUTIVE SUMMARY =========")
print(summary)


# ================================
# STEP 8: Final Cost Display
# ================================
print("\n========= FINAL COST IMPACT =========")

print("Total Cost Waste (USD):", total_waste)
print("Total Cost Waste (INR):", round(total_waste * 83, 2))