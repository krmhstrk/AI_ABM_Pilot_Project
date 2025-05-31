# English: Import necessary libraries
# Deutsch: Notwendige Bibliotheken importieren
import streamlit as st
import pandas as pd # For potential future use with more complex data handling

# --- Page Configuration (Wide layout, Page Title, Icon) ---
st.set_page_config(page_title="ABM Simulator", page_icon="🎯", layout="wide")

# --- Language Selection (Sidebar) ---
language_options = {
    "English": "en",
    "Deutsch (German)": "de"
}
selected_language_key = st.sidebar.radio("Select Language | Sprache wählen:", list(language_options.keys()))
LANG = language_options[selected_language_key]

# --- UI Text Translations ---
texts = {
    "en": {
        "app_title": "🎯 AI-Powered ABM Personalization Simulator",
        "sidebar_header": "Selector Panel",
        "industry_select_label": "1. Select Target Industry:",
        "account_select_label": "2. Select Target Account (from Industry):",
        "persona_select_label": "3. Select Target Persona (within Account):",
        "output_header": "✨ Simulated Personalized Outputs ✨",
        "account_profile_title": "Account Profile Card (Simulated)",
        "persona_insights_title": "Key Insights & Focus for Persona:",
        "email_subject_suggestion": "AI-Suggested Email Subject:",
        "email_opening_suggestion": "AI-Suggested Email Opening Line:",
        "linkedin_message_suggestion": "AI-Suggested LinkedIn Message Snippet:",
        "content_themes_suggestion": "AI-Suggested Content Themes for this Account:",
        "footer_note": "Note: All outputs are dynamically simulated based on your selections using predefined mock data. This demonstrates conceptual personalization capabilities. No live AI models are used in this demo.",
        "welcome_message": "Please make selections in the sidebar to view simulated personalized ABM outputs.",
        "no_accounts_in_industry": "No accounts found for the selected industry in the mock database.",
        "no_personas_in_account": "No personas defined for the selected account in the mock database."
    },
    "de": {
        "app_title": "🎯 KI-gestützter ABM Personalisierungs-Simulator",
        "sidebar_header": "Auswahlpanel",
        "industry_select_label": "1. Zielbranche auswählen:",
        "account_select_label": "2. Zielkonto auswählen (aus Branche):",
        "persona_select_label": "3. Ziel-Persona auswählen (innerhalb des Kontos):",
        "output_header": "✨ Simulierte personalisierte Ausgaben ✨",
        "account_profile_title": "Kontoprofilkarte (Simuliert)",
        "persona_insights_title": "Wichtige Einblicke & Fokus für Persona:",
        "email_subject_suggestion": "KI-vorgeschlagener E-Mail-Betreff:",
        "email_opening_suggestion": "KI-vorgeschlagene E-Mail-Eröffnungszeile:",
        "linkedin_message_suggestion": "KI-vorgeschlagenes LinkedIn-Nachrichtenfragment:",
        "content_themes_suggestion": "KI-vorgeschlagene Inhaltsthemen für dieses Konto:",
        "footer_note": "Hinweis: Alle Ausgaben werden basierend auf Ihren Auswahlmöglichkeiten dynamisch mit vordefinierten Mock-Daten simuliert. Dies demonstriert konzeptionelle Personalisierungsfähigkeiten. In dieser Demo werden keine Live-KI-Modelle verwendet.",
        "welcome_message": "Bitte treffen Sie eine Auswahl in der Seitenleiste, um simulierte personalisierte ABM-Ausgaben anzuzeigen.",
        "no_accounts_in_industry": "Keine Konten für die ausgewählte Branche in der Mock-Datenbank gefunden.",
        "no_personas_in_account": "Keine Personas für das ausgewählte Konto in der Mock-Datenbank definiert."
    }
}

# --- Mock Data (Consistent with Colab Notebook) ---
MOCK_TARGET_ACCOUNTS_DB_ABM = {
    "GlobalTech Innovators AG": {
        "industry": "Technology (Enterprise SaaS)",
        "employees": 2500,
        "revenue_eur_M": 200,
        "hq_location": "Berlin, Germany",
        "strategic_initiatives_public": ["Expansion into North American market", "Launching new AI-powered product suite"],
        "potential_pain_points": ["Scaling sales & marketing for new markets", "Ensuring customer success for complex AI products"],
        "key_stakeholders": [
            {"name": "Dr. Lena Vogel (CEO)", "focus": "Market expansion, Strategic partnerships", "linkedin_snippet_idea": "Congratulations on GlobalTech's recent funding round for North American expansion!"},
            {"name": "Max Richter (VP Sales, EMEA)", "focus": "Enterprise sales targets, Sales team efficiency", "linkedin_snippet_idea": "Impressed by GlobalTech's growth in the EMEA SaaS market. How are you tackling sales efficiency for the new AI suite?"},
            {"name": "Sophie Keller (VP Marketing)", "focus": "Brand positioning for new markets, Lead generation for enterprise", "linkedin_snippet_idea": "Your recent article on 'The Future of Enterprise AI' resonated. How is GlobalTech positioning its new suite for this?"}
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
            {"name": "Markus Braun (Head of Digital Strategy)", "focus": "Digital platform adoption, Customer experience", "linkedin_snippet_idea": "The new digital wealth platform launch is exciting! How are you ensuring a seamless CX?"},
            {"name": "Julia Weiss (Chief Compliance Officer)", "focus": "Regulatory adherence, Risk management", "linkedin_snippet_idea": "With the increasing focus on RegTech, how is FinSecure leveraging AI for compliance?"}
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
            {"name": "Prof. Dr. Klaus Hoffmann (CTO)", "focus": "R&D innovation, Technology partnerships", "linkedin_snippet_idea": "The advancements in autonomous systems at AutoDrive are impressive. What's next for your R&D?"},
            {"name": "Stefan Lang (Head of Supply Chain)", "focus": "Logistics optimization, Supplier management", "linkedin_snippet_idea": "Read about AutoDrive's AI initiatives in supply chain. How are you tackling visibility challenges?"}
        ]
    }
}

# --- Application Title ---
st.title(texts[LANG]["app_title"])

# --- Sidebar for Selections ---
st.sidebar.header(texts[LANG]["sidebar_header"])

# 1. Select Industry
industries = sorted(list(set(data["industry"] for data in MOCK_TARGET_ACCOUNTS_DB_ABM.values())))
selected_industry = st.sidebar.selectbox(texts[LANG]["industry_select_label"], [""] + industries, index=0, format_func=lambda x: "Select an industry..." if x == "" else x)

# 2. Select Account based on Industry
accounts_in_industry = {}
if selected_industry:
    accounts_in_industry = {name: data for name, data in MOCK_TARGET_ACCOUNTS_DB_ABM.items() if data["industry"] == selected_industry}

account_names_in_industry = list(accounts_in_industry.keys())
selected_account_name = st.sidebar.selectbox(
    texts[LANG]["account_select_label"],
    [""] + account_names_in_industry,
    index=0,
    format_func=lambda x: "Select an account..." if x == "" else x,
    disabled=not selected_industry
)

# 3. Select Persona within Account
personas_in_account = []
persona_objects_in_account = []
if selected_account_name and selected_account_name in accounts_in_industry:
    persona_objects_in_account = accounts_in_industry[selected_account_name].get("key_stakeholders", [])
    personas_in_account = [stakeholder["name"] for stakeholder in persona_objects_in_account]

selected_persona_display_name = st.sidebar.selectbox(
    texts[LANG]["persona_select_label"],
    [""] + personas_in_account,
    index=0,
    format_func=lambda x: "Select a persona..." if x == "" else x.split('(')[0].strip(), # Show only name part
    disabled=not selected_account_name
)

selected_persona_object = None
if selected_persona_display_name:
    selected_persona_object = next((p for p in persona_objects_in_account if p["name"] == selected_persona_display_name), None)


# --- Main Area for Displaying Personalized Outputs ---
st.markdown("---") # Separator
st.header(texts[LANG]["output_header"])

if selected_account_name and selected_persona_object:
    account_data = accounts_in_industry[selected_account_name]
    persona_data = selected_persona_object

    # Layout with columns for better presentation
    col1, col2 = st.columns([1, 2]) # Adjust column ratios as needed

    with col1: # Account Profile Card
        st.subheader(texts[LANG]["account_profile_title"])
        st.markdown(f"""
        <div style="border: 1px solid #ddd; border-radius: 5px; padding: 15px; background-color: #f9f9f9;">
        <h4>{selected_account_name}</h4>
        <ul style="list-style-type: none; padding-left: 0;">
            <li><strong>Industry:</strong> {account_data.get("industry")}</li>
            <li><strong>Location:</strong> {account_data.get("hq_location")}</li>
            <li><strong>Employees:</strong> {account_data.get("employees", "N/A")}</li>
            <li><strong>Est. Revenue (EUR M):</strong> {account_data.get("revenue_eur_M", "N/A")}</li>
            <li><strong>Key Strategic Initiatives:</strong> {', '.join(account_data.get("strategic_initiatives_public", ["N/A"]))}</li>
            <li><strong>Potential Pain Points:</strong> {', '.join(account_data.get("potential_pain_points", ["N/A"]))}</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2: # Personalized Suggestions for Persona
        st.subheader(f"{texts[LANG]['persona_insights_title']} {persona_data['name']}")
        st.markdown(f"**Focus Area:** `{persona_data.get('focus')}`")
        st.markdown("---")

        # Simulated AI Suggestions
        st.markdown(f"**{texts[LANG]['suggested_email_subject']}**")
        # Simple heuristic for subject line
        email_subject = f"Strategic Insights for {persona_data.get('focus')} at {selected_account_name}"
        if "AI" in ' '.join(account_data.get("strategic_initiatives_public", [])):
             email_subject = f"Leveraging AI for {persona_data.get('focus')} at {selected_account_name}"
        st.info(email_subject)

        st.markdown(f"**{texts[LANG]['suggested_email_opening']}**")
        email_opening = f"Dear {persona_data['name'].split(' ')[0]},\n\nGiven {selected_account_name}'s focus on '{account_data.get('strategic_initiatives_public', ['key initiatives'])[0]}', I thought you'd be interested in how AI can specifically enhance '{persona_data.get('focus').lower()}' by..."
        st.info(email_opening)

        st.markdown(f"**{texts[LANG]['suggested_linkedin_message']}**")
        linkedin_message = persona_data.get("linkedin_snippet_idea", f"Hi {persona_data['name'].split(' ')[0]}, interested to discuss how AI can support {selected_account_name}'s goals related to {persona_data.get('focus').lower()}?")
        st.info(linkedin_message)

    st.markdown("---")
    st.subheader(texts[LANG]['suggested_content_themes'])
    # Simple logic for content themes based on industry and pain points
    content_themes = [
        f"Blog Post: How AI is transforming {account_data.get('industry')} for challenges like '{account_data.get('potential_pain_points', ['operations'])[0]}'.",
        f"Webinar: The Future of {account_data.get('strategic_initiatives_public', ['Workplace Solutions'])[0]} in {account_data.get('industry')} - An AI Perspective.",
        f"Case Study: Achieving [Quantifiable Benefit] in {persona_data.get('focus')} using Prop-Tech AI at a company like {selected_account_name}."
    ]
    for i, theme in enumerate(content_themes):
        st.markdown(f"<div style='border-left: 3px solid #007bff; padding-left: 10px; margin-bottom: 10px;'>{i+1}. {theme}</div>", unsafe_allow_html=True)

elif not selected_industry or not selected_account_name or not selected_persona_display_name :
     st.info(texts[LANG]["welcome_message"])
elif not accounts_in_industry:
    st.warning(texts[LANG]["no_accounts_in_industry"])
elif not personas_in_account:
    st.warning(texts[LANG]["no_personas_in_account"])


# --- Footer Note ---
st.markdown("---")
st.caption(texts[LANG]["simulation_note_footer"])