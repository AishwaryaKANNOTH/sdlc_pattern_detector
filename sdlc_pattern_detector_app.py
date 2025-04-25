import streamlit as st
import pandas as pd

# --- SDLC Logic ---
ideal_phases = ['Requirements', 'Design', 'Dev', 'QA', 'UAT', 'Deploy']

def check_pattern_breaks(actual_phases):
    missing = [p for p in ideal_phases if p not in actual_phases]
    indexes = [ideal_phases.index(p) for p in actual_phases if p in ideal_phases]
    is_ordered = indexes == sorted(indexes)
    return missing, not is_ordered

def generate_insight(missing, out_of_order):
    if not missing and not out_of_order:
        return "✅ No issues detected."
    msg = []
    if missing:
        msg.append(f"⚠️ Missing: {', '.join(missing)}.")
    if out_of_order:
        msg.append("🔄 Out-of-order phases.")
    if 'QA' in missing or 'UAT' in missing:
        msg.append("🚨 Risk: untested deployment.")
    return " ".join(msg)

def mermaid_from_phases(phases):
    return " --> ".join(phases)

# --- Streamlit UI ---
st.set_page_config(page_title="SDLC Pattern Break Detector", layout="centered")
st.title("🧠 SDLC Pattern Break Detector")
st.markdown("Upload an SDLC timeline CSV file to detect skipped steps and anti-patterns.")

uploaded_file = st.file_uploader("📤 Upload your CSV file here", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File loaded successfully.")
    st.write("### Raw SDLC Data")
    st.dataframe(df)

    # Analyze each ticket
    results = []
    for ticket_id, group in df.groupby("Ticket ID"):
        phases = list(group["Phase"])
        missing, out_of_order = check_pattern_breaks(phases)
        insight = generate_insight(missing, out_of_order)
        mermaid_code = mermaid_from_phases(phases)
        results.append({
            "Ticket ID": ticket_id,
            "Insight": insight,
            "Mermaid": f"```mermaid\ngraph TD\n{mermaid_code}\n```"
        })

    st.write("### 🧠 Pattern Analysis")
    for res in results:
        st.subheader(f"🎫 Ticket {res['Ticket ID']}")
        st.markdown(res["Insight"])
        st.code(res["Mermaid"], language="markdown")
else:
    st.info("⬆️ Please upload a CSV to begin analysis.")
