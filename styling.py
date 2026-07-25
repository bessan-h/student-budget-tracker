import streamlit as st

def apply_custom_styling():
    """Apply modern, professional styling to the entire app."""
    st.set_page_config(
        page_title="Student Budget Tracker",
        page_icon="💰",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
    # Initialize contrast multiplier if not set
    if "contrast_multiplier" not in st.session_state:
        st.session_state.contrast_multiplier = 1.0
    
    custom_css = f"""
    <style>
        /* Color Scheme */
        :root {{
            --primary: #6366f1;
            --secondary: #8b5cf6;
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
            --dark: #1f2937;
            --light: #f9fafb;
        }}
        
        /* Global Styles */
        * {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}
        
        body {{
            background-color: #f3f4f6;
            color: #1f2937;
        }}
        
        /* Main Content */
        .main {{
            padding: 2rem;
            background-color: #f3f4f6;
        }}
        
        /* Typography */
        h1 {{
            color: #1f2937;
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            letter-spacing: -0.5px;
        }}
        
        h2 {{
            color: #1f2937;
            font-size: 1.875rem;
            font-weight: 600;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
            border-bottom: 3px solid #6366f1;
            padding-bottom: 0.5rem;
        }}
        
        h3 {{
            color: #374151;
            font-size: 1.25rem;
            font-weight: 600;
            margin-top: 1rem;
            margin-bottom: 0.75rem;
        }}
        
        p {{
            line-height: 1.6;
            color: #4b5563;
        }}
        
        /* Metrics Container */
        .metric-container {{
            display: flex;
            gap: 1.5rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }}
        
        .metric-card {{
            flex: 1;
            min-width: 250px;
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            border-left: 4px solid #6366f1;
            transition: all 0.3s ease;
        }}
        
        .metric-card:hover {{
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.15);
            transform: translateY(-2px);
        }}
        
        .metric-card.success {{
            border-left-color: #10b981;
        }}
        
        .metric-card.warning {{
            border-left-color: #f59e0b;
        }}
        
        .metric-card.danger {{
            border-left-color: #ef4444;
        }}
        
        .metric-label {{
            font-size: 0.875rem;
            color: #ffffff;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 0.5rem;
        }}
        
        .metric-value {{
            font-size: 2rem;
            font-weight: 700;
            color: #1f2937;
        }}
        
        /* Cards */
        .stContainer {{
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            margin-bottom: 1.5rem;
        }}
        
        /* Buttons */
        .stButton > button {{
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.75rem 1.5rem;
            font-weight: 600;
            font-size: 0.95rem;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(99, 102, 241, 0.3);
        }}
        
        .stButton > button:hover {{
            box-shadow: 0 4px 16px rgba(99, 102, 241, 0.4);
            transform: translateY(-2px);
        }}
        
        /* Inputs */
        .stTextInput > div > div > input,
        .stNumberInput > div > div > input,
        .stSelectbox > div > div > div {{
            border: 2px solid #e5e7eb !important;
            border-radius: 8px !important;
            padding: 0.75rem !important;
            font-size: 0.95rem !important;
            white-space: normal !important;
            overflow: visible !important;
            display: flex !important;
            align-items: center !important;
            min-height: 44px !important;
        }}
        
        .stSelectbox {{
            min-width: 100% !important;
            width: 100% !important;
        }}
        
        .stSelectbox div {{
            white-space: normal !important;
            overflow: visible !important;
        }}
        
        .stSelectbox [role="listbox"] {{
            vertical-align: middle !important;
        }}
        
        /* Progress Bar */
        .stProgress > div > div > div > div {{
            background: linear-gradient(90deg, #6366f1, #8b5cf6) !important;
            border-radius: 10px !important;
        }}
        
        /* Dataframe */
        .stDataFrame {{
            border-radius: 8px !important;
            overflow: hidden !important;
        }}
        
        .stDataFrame tbody tr:hover {{
            background-color: #f3f4f6 !important;
        }}
        
        /* Messages */
        .stSuccess {{
            background-color: #d1fae5;
            border-left: 4px solid #10b981;
            border-radius: 8px;
            padding: 1rem;
        }}
        
        .stError {{
            background-color: #fee2e2;
            border-left: 4px solid #ef4444;
            border-radius: 8px;
            padding: 1rem;
        }}
        
        .stWarning {{
            background-color: #fef3c7;
            border-left: 4px solid #f59e0b;
            border-radius: 8px;
            padding: 1rem;
        }}
        
        .stInfo {{
            background-color: #dbeafe;
            border-left: 4px solid #3b82f6;
            border-radius: 8px;
            padding: 1rem;
        }}
        
        /* Dividers */
        .stMarkdown hr {{
            border-color: #e5e7eb;
            margin: 2rem 0;
        }}
        
        /* Sidebar - Dark mode text styling */
        .stSidebar {{
            color: #ffffff;
        }}
        
        .stSidebar [data-testid="stMarkdownContainer"] {{
            color: #ffffff;
        }}
        
        .stSidebar p, .stSidebar label, .stSidebar span {{
            color: #f0f0f0 !important;
        }}
        
        .stSidebar button {{
            color: #ffffff;
        }}
        
        /* Columns */
        .stColumns {{
            gap: 1.5rem;
        }}
        
        /* Contrast Checker Styling */
        .stExpander {{
            color: #ffffff !important;
        }}
        
        .stExpander label {{
            color: #ffffff !important;
        }}
        
        .stExpander p {{
            color: #ffffff !important;
        }}
        
        .stExpander [data-testid="stMarkdownContainer"] {{
            color: #ffffff !important;
        }}
        
        .stExpander h3 {{
            color: #ffffff !important;
        }}
        
        .stExpander h4 {{
            color: #ffffff !important;
        }}
        
        .stExpander strong {{
            color: #ffffff !important;
        }}
    </style>
    """
    
    st.markdown(custom_css, unsafe_allow_html=True)


def render_metric_card(label, value, icon="", style="primary"):
    """Render a styled metric card."""
    color_map = {
        "primary": "#6366f1",
        "success": "#10b981",
        "warning": "#f59e0b",
        "danger": "#ef4444",
    }
    
    color = color_map.get(style, "#6366f1")
    
    html_content = f"""
    <div style="
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        border-left: 4px solid {color};
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    ">
        <div style="
            font-size: 0.875rem;
            color: #ffffff;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 0.5rem;
        ">
            {icon} {label}
        </div>
        <div style="
            font-size: 2rem;
            font-weight: 700;
            color: #1f2937;
        ">
            {value}
        </div>
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)


def section_divider(title=""):
    """Render a styled section divider."""
    if title:
        st.markdown(f"### {title}")
    else:
        st.markdown("---")


def render_column_metrics(metrics_data):
    """
    Render metrics in columns.
    metrics_data: list of dicts with keys: label, value, icon, style
    """
    cols = st.columns(len(metrics_data))
    for col, metric in zip(cols, metrics_data):
        with col:
            render_metric_card(
                metric.get("label", ""),
                metric.get("value", ""),
                metric.get("icon", ""),
                metric.get("style", "primary"),
            )
