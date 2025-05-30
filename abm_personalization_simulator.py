# English: Import necessary libraries
# Deutsch: Notwendige Bibliotheken importieren
import streamlit as st
import pandas as pd # We might use this later if we decide to show some data in tables

# --- Page Configuration (English & German) ---
st.set_page_config(page_title="ABM Personalization Simulator", page_icon="🎯", layout="wide")

# --- Language Selection (English & German) ---
language_options = {
    "English": "en",
    "Deutsch (German)": "de"
}
selected_language_key = st.sidebar.radio("Select Language | Sprache wählen:", list(language_options.keys()))
LANG = language_options[selected_language_key]

# --- Text Translations for UI elements ---
texts = {
    "en": {
        "title": "🎯 ABM Personalization Simulator",
        "header_account_selection": "1. Target Account & Persona Selection",
        "select_industry": "Select Target Industry:",
        "select_account": "Select Target Account (based on Industry):",
        "select_persona": "Select Target Persona (within Account):",
        "header_personalized_outputs": "2. Simulated Personalized Outputs",
        "account_profile_card_title": "Target Account Profile Card (Simulated)",
        "persona_insights_title": "Key Insights for Persona",
        "suggested_email_subject": "AI-Suggested Email Subject:",
        "suggested_email_opening": "AI-Suggested Email Opening Line:",
        "suggested_linkedin_message": "AI-Suggested LinkedIn Message Snippet:",
        "suggested_content_themes": "AI-Suggested Content Themes for this Account:",
        "simulation_note_footer": "Note: All outputs are simulated based on predefined mock data to demonstrate conceptual personalization. Real AI would analyze vast amounts of real-time data.",
        "no_persona_selected": "Please select an account and persona to see suggestions.",
        "no_account_selected": "Please select an industry and account first."
    },
    "de": {
        "title": "🎯 ABM Personalisierungs-Simulator",
        "header_account_selection": "1. Zielkonto- & Persona-Auswahl",
        "select_industry": "Zielbranche auswählen:",
        "select_account": "Zielkonto auswählen (basierend auf Branche):",
        "select_persona": "Ziel-Persona auswählen (innerhalb des Kontos):",
        "header_personalized_outputs": "2. Simulierte personalisierte Ausgaben",
        "account_profile_card_title": "Zielkonto-Profilkarte (Simuliert)",
        "persona_insights_title": "Wichtige Einblicke für Persona",
        "suggested_email_subject": "KI-vorgeschlagener E-Mail-Betreff:",
        "suggested_email_opening": "KI-vorgeschlagene E-Mail-Eröffnungszeile:",
        "suggested_linkedin_message": "KI-vorgeschlagenes LinkedIn-Nachrichtenfragment:",
        "suggested_content_themes": "KI-vorgeschlagene Inhaltsthemen für dieses Konto:",
        "simulation_note_footer": "Hinweis: Alle Ausgaben basieren auf vordefinierten Mock-Daten, um die konzeptionelle Personalisierung zu demonstrieren. Echte KI würde riesige Mengen an Echtzeitdaten analysieren.",
        "no_persona_selected": "Bitte wählen Sie ein Konto und eine Persona aus, um Vorschläge anzuzeigen.",
        "no_account_selected": "Bitte wählen Sie zuerst eine Branche und ein Konto aus."
    }
}

# --- Mock Data (Copied from Colab notebook - ensure this is consistent) ---
MOCK_ICP_CRITERIA_ABM = {
    "industry_verticals": ["Technology (Enterprise SaaS)", "Financial Services (FinTech Focus)", "Advanced Manufacturing"],
    # ... (Add other ICP criteria if needed for more complex logic later, but not essential for this simple demo)
}

MOCK_TARGET_ACCOUNTS_DB_ABM = {
    "GlobalTech Innovators AG": {
        "industry": "Technology (Enterprise SaaS)",
        "employees": 2500,
        "revenue_eur_M": 200,
        "hq_location": "Berlin, Germany",
        "strategic_initiatives_public": ["Expansion into North American market", "Launching new AI-powered product suite"],
        "potential_pain_points": ["Scaling sales & marketing for new markets", "Ensuring customer success for complex AI products"],
        "key_stakeholders": [
            {"name": "Dr. Lena Vogel (CEO)", "focus": "Market expansion, Strategic partnerships"},
            {"name": "Max Richter (VP Sales, EMEA)", "focus": "Enterprise sales targets, Sales team efficiency"},
            {"name": "Sophie Keller (VP Marketing)", "focus": "Brand positioning for new markets, Lead generation for enterprise"}
        ]
    },
    "FinSecure Capital GmbH": {
        "industry": "Financial Services (FinTech Focus)",
        "employees": 1200,
        "revenue_eur_M": 350,
        "hq_location": "Frankfurt, Germany",
        "strategic_initiatives_public": ["Launching a new digital wealth management platform", "Focus on regulatory compliance (RegTech)"],
        "potential_pain_points": ["Acquiring high-net-worth individuals for the new platform", "Ensuring robust security and compliance"],
        "key_stakeholders": [
            {"name": "Markus Braun (Head of Digital Strategy)", "focus": "Digital platform adoption, Customer experience"},
            {"name": "Julia Weiss (Chief Compliance Officer)", "focus": "Regulatory adherence, Risk management"}
        ]
    },
     "AutoDrive Solutions": {
        "industry": "Advanced Manufacturing (Automotive Tech)",
        "employees": 8000,
        "revenue_eur_M": 1200,
        "hq_location": "Munich, Germany",
        "strategic_initiatives_public": ["Developing next-generation autonomous driving systems", "Optimizing supply chain with AI"],
        "potential_pain_points": ["Long R&D cycles for new automotive tech", "Need for specialized engineering talent"],
        "key_stakeholders": [
            {"name": "Prof. Dr. Klaus Hoffmann (CTO)", "focus": "R&D innovation, Technology partnerships"},
            {"name": "Stefan Lang (Head of Supply Chain)", "focus": "Logistics optimization, Supplier management"}
        ]
    }
}

# --- Main Application ---
st.title(texts[LANG]["title"])

st.sidebar.header(texts[LANG]["header_account_selection"])

# 1. Select Industry
industries = sorted(list(set(data["industry"] for data in MOCK_TARGET_ACCOUNTS_DB_ABM.values())))
selected_industry = st.sidebar.selectbox(texts[LANG]["select_industry"], industries, index=0)

# 2. Select Account based on Industry
accounts_in_industry = {name: data for name, data in MOCK_TARGET_ACCOUNTS_DB_ABM.items() if data["industry"] == selected_industry}
selected_account_name = st.sidebar.selectbox(texts[LANG]["select_account"], list(accounts_in_industry.keys()), index=0 if accounts_in_industry else None)

# 3. Select Persona within Account
personas_in_account = []
if selected_account_name:
    personas_in_account = [stakeholder["name"] for stakeholder in accounts_in_industry[selected_account_name].get("key_stakeholders", [])]

selected_persona_name = st.sidebar.selectbox(texts[LANG]["select_persona"], personas_in_account, index=0 if personas_in_account else None,
                                             format_func=lambda x: x.split('(')[0].strip() if '(' in x else x) # Show only name in selectbox


# --- Display Personalized Outputs ---
st.header(texts[LANG]["header_personalized_outputs"])

if selected_account_name and selected_persona_name:
    account_data = accounts_in_industry[selected_account_name]
    # Find full persona data
    persona_data = next((p for p in account_data.get("key_stakeholders", []) if p["name"] == selected_persona_name), None)

    # Column layout
    col1, col2 = st.columns(2)

    with col1:
        # Display Account Profile Card
        st.subheader(texts[LANG]["account_profile_card_title"])
        st.markdown(f"""
        **Company:** {selected_account_name}
        - **Industry:** {account_data.get("industry")}
        - **Location:** {account_data.get("hq_location")}
        - **Employees:** {account_data.get("employees")}
        - **Est. Revenue (EUR M):** {account_data.get("revenue_eur_M")}
        - **Key Strategic Initiatives:** {', '.join(account_data.get("strategic_initiatives_public", ["N/A"]))}
        """)

    with col2:
        # Display Persona Insights & Suggested Communications
        if persona_data:
            st.subheader(texts[LANG]["persona_insights_title"] + f": {selected_persona_name}")
            st.markdown(f"**Focus Area:** {persona_data.get('focus')}")

            # Simulated AI Suggestions
            st.markdown(f"---")
            st.markdown(f"**{texts[LANG]['suggested_email_subject']}**")
            st.info(f"Re: AI-Driven Strategies for {persona_data.get('focus')} at {selected_account_name}?")

            st.markdown(f"**{texts[LANG]['suggested_email_opening']}**")
            st.info(f"Dear {selected_persona_name.split(' ')[0]},\nNoting {selected_account_name}'s recent focus on '{account_data.get('strategic_initiatives_public', ['their current goals'])[0]}', leveraging AI for enhanced '{persona_data.get('focus').lower()}' could unlock significant efficiencies...")

            st.markdown(f"**{texts[LANG]['suggested_linkedin_message']}**")
            st.info(f"Hi {selected_persona_name.split(' ')[0]}, saw {selected_account_name}'s work on {account_data.get('strategic_initiatives_public', ['key projects'])[0]}. Our AI tools are helping leaders like you with '{persona_data.get('focus').lower()}'. Worth a quick chat?")

    st.markdown("---")
    st.subheader(texts[LANG]['suggested_content_themes'])
    # Simple logic for content themes based on industry and pain points
    content_themes = [
        f"Optimizing '{', '.join(account_data.get('potential_pain_points', ['operations']))[:50]}...' with AI for {account_data.get('industry')} sector.",
        f"The Future of '{account_data.get('strategic_initiatives_public', ['Workplace Solutions'])[0]}' in {account_data.get('industry')}.",
        f"Data-Driven Decision Making for '{persona_data.get('focus') if persona_data else 'Key Stakeholders'}' using Prop-Tech AI."
    ]
    for theme in content_themes:
        st.success(theme)

elif not selected_account_name:
    st.warning(texts[LANG]["no_account_selected"])
else: # Account selected but no persona (shouldn't happen if lists are populated correctly)
    st.warning(texts[LANG]["no_persona_selected"])


# --- Footer Note ---
st.markdown("---")
st.caption(texts[LANG]["simulation_note_footer"])
