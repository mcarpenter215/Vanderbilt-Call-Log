import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Vanderbilt Transfusion Medicine On-Call Generator",
    page_icon="⚓",
    layout="wide"
)

# 2. Custom CSS Injection (Official Vanderbilt University Palette)
st.markdown("""
<style>
    /* Vanderbilt Palette:
       Vanderbilt Black: #1C1C1C
       Flat Gold: #CFAE70
       Highlight Gold: #ECB748
       Oak Gold: #946E24
       Vanderbilt Cream: #F5F3EF
    */
    
    .stApp {
        background-color: #121212;
        color: #F5F3EF;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #1C1C1C;
        border-right: 1px solid #946E24;
    }
    
    /* Executive Card Output */
    .vanderbilt-card {
        background-color: #1C1C1C;
        border-left: 6px solid #CFAE70;
        border-top: 1px solid #2D2D2D;
        border-right: 1px solid #2D2D2D;
        border-bottom: 1px solid #2D2D2D;
        border-radius: 6px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.6);
    }
    
    .badge-vanderbilt {
        background-color: #CFAE70;
        color: #1C1C1C;
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 0.8em;
        font-weight: 800;
        letter-spacing: 0.8px;
    }
    
    .badge-stat {
        background-color: #991B1B;
        color: #FFFFFF;
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 0.8em;
        font-weight: 800;
        letter-spacing: 0.8px;
    }

    .gold-header {
        color: #CFAE70 !important;
        font-weight: 700;
    }

    .decision-box {
        background-color: #262626;
        padding: 12px;
        border-radius: 4px;
        border-left: 3px solid #ECB748;
        margin-bottom: 14px;
        color: #FFFFFF;
    }
</style>
""", unsafe_allow_html=True)

# 3. Application Header
st.markdown("<h1 class='gold-header'>⚓ Vanderbilt Transfusion Medicine On-Call Generator</h1>", unsafe_allow_html=True)
st.caption("Department of Pathology, Microbiology and Immunology • Vanderbilt University Medical Center")

st.divider()

# 4. Main Workspace Layout
col_input, col_output = st.columns([1, 1])

with col_input:
    st.subheader("📥 Input Call Details")
    
    case_type = st.selectbox(
        "Priority / Call Type", 
        ["STAT Consult", "Informational Page", "Transfusion Reaction Investigation", "System / Operational Issue"]
    )
    
    mrn = st.text_input("Patient ID / MRN", value="048783659")
    demographics = st.text_input("Demographics & Primary Context", value="33F, 25w Pregnant • Major ABO Mismatch (Group A given B-pos RBCs)")
    
    raw_notes = st.text_area(
        "Raw On-Call Notes & Lab Findings", 
        height=140, 
        value="Transfused 2u B-pos pRBCs OSH. Jaundiced, dark urine, vomiting. Post-reaction DAT negative. ICU team requested guidance on Eculizumab + TPE."
    )
    
    rec = st.text_input(
        "Executive Decision & Primary Action", 
        value="Denied Eculizumab and TPE. Advised aggressive IV hydration and renal monitoring. Approved A-negative RBCs."
    )
    
    mechanics = st.text_area(
        "Mechanistic Breakdown & Physical Analogy", 
        height=130,
        value="Host anti-B IgM fixed classical complement cascade -> C5b-9 MAC assembly -> hyperacute intravascular lysis. Giving Eculizumab 24h later when DAT is negative is like turning on sprinklers after the house has already burned down."
    )
    
    board_pearls = st.text_area(
        "Board & Teaching Pearls (AP / CP / Fellowship)", 
        height=110,
        value="Post-AHTR DAT Paradox: In complete intravascular hemolysis, the post-reaction DAT is strictly NEGATIVE because 100% of donor cells have been destroyed."
    )

with col_output:
    st.subheader("📄 Formatted Vanderbilt Executive Report")
    
    badge_style = "badge-stat" if "STAT" in case_type else "badge-vanderbilt"
    
    # HTML Output Card
    formatted_html = f"""
    <div class="vanderbilt-card">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #946E24; padding-bottom: 10px; margin-bottom: 14px;">
            <span style="font-size: 1.15em; font-weight: bold; color: #CFAE70;">MRN: {mrn} — {demographics}</span>
            <span class="{badge_style}">{case_type.upper()}</span>
        </div>
        
        <p style="margin-bottom: 4px; color: #CFAE70; font-weight: 600;">Executive Strategy & Recommendation:</p>
        <div class="decision-box">
            <u><strong>{rec}</strong></u>
        </div>
        
        <p style="margin-bottom: 4px; color: #CFAE70; font-weight: 600;">Clinical Context & Findings:</p>
        <p style="color: #D4D4D4; font-size: 0.9em; margin-bottom: 14px;">{raw_notes}</p>
        
        <hr style="border-color: #333333; margin: 14px 0;">
        
        <p style="margin-bottom: 4px; color: #CFAE70; font-weight: 600;">🔬 Mechanistic & Molecular Breakdown:</p>
        <p style="color: #F5F3EF; font-size: 0.95em; line-height: 1.5; margin-bottom: 14px;">{mechanics}</p>
        
        <p style="margin-bottom: 4px; color: #ECB748; font-weight: 600;">🎓 Board Exam & Teaching Pearls:</p>
        <p style="color: #F5F3EF; font-size: 0.95em; line-height: 1.5;">💡 {board_pearls}</p>
    </div>
    """
    
    st.markdown(formatted_html, unsafe_allow_html=True)
    
    st.subheader("📋 Export Markdown for Email / Documentation")
    raw_md = f"""### Case: {mrn} ({demographics})
**Type:** {case_type}  
**Recommendation:** <u>**{rec}**</u>  

**Clinical Summary:** {raw_notes}  

**Mechanistic Breakdown:**  
* {mechanics}  

**Board Exam & Teaching Pearls:**  
* 💡 {board_pearls}
"""
    st.code(raw_md, language="markdown")
