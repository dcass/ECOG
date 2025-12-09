import streamlit as st
from datetime import datetime

# --- ECOG data ---
ECOG_OPTIONS = {
    0: "Fully active, able to carry on all pre-disease performance without restriction.",
    1: "Restricted in physically strenuous activity but ambulatory and able to carry out work of a light or sedentary nature (e.g., light housework, office work).",
    2: "Ambulatory and capable of all self-care but unable to carry out any work activities; up and about more than 50% of waking hours.",
    3: "Capable of only limited self-care; confined to bed or chair more than 50% of waking hours.",
    4: "Completely disabled; cannot carry on any self-care; totally confined to bed or chair.",
    5: "Dead."
}

def main():
    st.set_page_config(
        page_title="ECOG Performance Status",
        page_icon="🩺",
        layout="centered"
    )

    st.title("🩺 ECOG Performance Status")
    st.caption("Eastern Cooperative Oncology Group (ECOG) Performance Status Scale")

    with st.expander("ℹ️ About this tool", expanded=False):
        st.write(
            """
            This app helps you **record and document** a patient's ECOG Performance Status.  
            It does *not* provide medical advice or replace clinical judgment.
            """
        )

    # Optional patient details
    st.subheader("Patient Information (optional)")
    col1, col2 = st.columns(2)
    with col1:
        patient_id = st.text_input("Patient name / ID", value="")
    with col2:
        assessment_date = st.date_input("Assessment date", value=datetime.today())

    st.markdown("---")

    st.subheader("Select ECOG Performance Status")

    # Build radio options with nice labels
    radio_labels = [
        f"{score} – {desc}"
        for score, desc in ECOG_OPTIONS.items()
    ]

    # Default to 0
    selection = st.radio(
        "Choose the statement that best describes the patient:",
        options=radio_labels,
        index=0
    )

    # Extract the selected score (first character until space)
    selected_score = int(selection.split(" ", 1)[0])

    # Display result
    st.markdown("### Result")
    st.metric(
        label="ECOG Performance Status",
        value=str(selected_score),
    )

    st.write(f"**Definition:** {ECOG_OPTIONS[selected_score]}")

    # Simple summary block
    st.markdown("### Summary")
    summary_lines = []

    if patient_id:
        summary_lines.append(f"**Patient:** {patient_id}")
    summary_lines.append(f"**Date:** {assessment_date.strftime('%Y-%m-%d')}")
    summary_lines.append(f"**ECOG PS:** {selected_score}")
    summary_lines.append(f"**Description:** {ECOG_OPTIONS[selected_score]}")

    st.markdown("\n\n".join(summary_lines))

    # Copyable text (for pasting into notes/EMR)
    st.markdown("### Copy for Clinical Notes")
    note_text = f"ECOG Performance Status: {selected_score} – {ECOG_OPTIONS[selected_score]}"

    if patient_id:
        note_text = (
            f"Patient: {patient_id}\n"
            f"Date: {assessment_date.strftime('%Y-%m-%d')}\n"
            + note_text
        )

    st.code(note_text, language="text")


if __name__ == "__main__":
    main()
