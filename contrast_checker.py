import streamlit as st
from colorsys import rgb_to_hls

def apply_current_contrast():
    """Apply the current contrast filter from session state."""
    if "contrast_multiplier" not in st.session_state:
        st.session_state.contrast_multiplier = 1.0
    
    contrast = st.session_state.contrast_multiplier
    
    if contrast != 1.0:
        contrast_css = f"""
        <style>
            .main {{
                filter: contrast({contrast}) !important;
            }}
        </style>
        """
        st.markdown(contrast_css, unsafe_allow_html=True)


def apply_contrast_filter():
    """Apply contrast adjustment filter to the entire page."""
    if "contrast_multiplier" not in st.session_state:
        st.session_state.contrast_multiplier = 1.0
    
    multiplier = st.session_state.contrast_multiplier
    
    if multiplier != 1.0:
        contrast_css = f"""
        <style>
            .main {{
                filter: contrast({multiplier});
            }}
        </style>
        """
        st.markdown(contrast_css, unsafe_allow_html=True)

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    """Convert RGB tuple to hex color."""
    return '#{:02x}{:02x}{:02x}'.format(int(r), int(g), int(b))

def get_luminance(rgb):
    """Calculate relative luminance for WCAG contrast calculation."""
    r, g, b = [x / 255.0 for x in rgb]
    
    r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
    g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
    b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4
    
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def get_contrast_ratio(color1, color2):
    """Calculate WCAG contrast ratio between two colors."""
    rgb1 = hex_to_rgb(color1) if isinstance(color1, str) else color1
    rgb2 = hex_to_rgb(color2) if isinstance(color2, str) else color2
    
    lum1 = get_luminance(rgb1)
    lum2 = get_luminance(rgb2)
    
    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)
    
    return (lighter + 0.05) / (darker + 0.05)

def check_wcag_compliance(contrast_ratio, level="AA"):
    """Check if contrast ratio meets WCAG standards."""
    if level == "AAA":
        return contrast_ratio >= 7.0
    elif level == "AA":
        return contrast_ratio >= 4.5
    elif level == "AA_large":
        return contrast_ratio >= 3.0
    return False

def display_contrast_checker():
    """Display an interactive contrast checker for the page."""
    with st.expander("🎨 Contrast Checker", expanded=False):
        col1, col2 = st.columns(2)
        
        with col1:
            text_color = st.color_picker("Text Color", "#1f2937")
        
        with col2:
            bg_color = st.color_picker("Background Color", "#ffffff")
        
        # Contrast adjustment slider
        st.markdown("---")
        st.markdown("### Contrast Adjustment")
        contrast_boost = st.slider(
            "Adjust contrast strength",
            min_value=0.0,
            max_value=2.0,
            value=1.0,
            step=0.1,
            help="Increase to boost contrast, decrease to reduce it",
            key="contrast_slider"
        )
        
        # Store in session state to apply to page
        st.session_state.contrast_multiplier = contrast_boost
        
        # Apply contrast filter dynamically
        if contrast_boost != 1.0:
            contrast_css = f"""
            <style>
                .main {{
                    filter: contrast({contrast_boost}) !important;
                }}
            </style>
            """
            st.markdown(contrast_css, unsafe_allow_html=True)
        
        if contrast_boost != 1.0:
            st.info(f"📊 Page contrast adjusted: **{contrast_boost:.1f}x** (this affects all elements on the page)")
        
        # Calculate contrast ratio
        contrast = get_contrast_ratio(text_color, bg_color)
        adjusted_contrast = contrast * contrast_boost
        
        # Check WCAG levels
        wcag_aaa = check_wcag_compliance(adjusted_contrast, "AAA")
        wcag_aa = check_wcag_compliance(adjusted_contrast, "AA")
        wcag_aa_large = check_wcag_compliance(adjusted_contrast, "AA_large")
        
        st.markdown("---")
        st.markdown("### Results")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if wcag_aaa:
                st.success(f"✅ AAA (7.0:1)\n**{adjusted_contrast:.2f}:1**")
            else:
                st.error(f"❌ AAA (7.0:1)\n**{adjusted_contrast:.2f}:1**")
        
        with col2:
            if wcag_aa:
                st.success(f"✅ AA (4.5:1)\n**{adjusted_contrast:.2f}:1**")
            else:
                st.error(f"❌ AA (4.5:1)\n**{adjusted_contrast:.2f}:1**")
        
        with col3:
            if wcag_aa_large:
                st.success(f"✅ AA Large (3.0:1)\n**{adjusted_contrast:.2f}:1**")
            else:
                st.error(f"❌ AA Large (3.0:1)\n**{adjusted_contrast:.2f}:1**")
        
        st.markdown("---")
        
        # Visual preview
        st.markdown("### Preview")
        st.markdown(
            f'<div style="background-color: {bg_color}; color: {text_color}; padding: 20px; border-radius: 8px; text-align: center; font-size: 18px; font-weight: 500;">Sample Text Preview</div>',
            unsafe_allow_html=True
        )
        
        st.markdown("---")
        st.markdown("### Current App Colors")
        
        # Display current app color scheme
        colors = {
            "Primary (Indigo)": "#6366f1",
            "Secondary (Purple)": "#8b5cf6",
            "Success (Green)": "#10b981",
            "Warning (Orange)": "#f59e0b",
            "Danger (Red)": "#ef4444",
            "Dark Text": "#1f2937",
            "Light Background": "#f9fafb",
            "White": "#ffffff",
        }
        
        st.markdown("**Text on White Background:**")
        for name, color in colors.items():
            ratio = get_contrast_ratio(color, "#ffffff")
            status = "✅" if ratio >= 4.5 else "⚠️"
            st.write(f"{status} {name}: **{ratio:.2f}:1**")


def check_page_contrast():
    """Check contrast compliance for the entire page."""
    st.sidebar.markdown("---")
    
    with st.sidebar.expander("📊 Page Contrast Info", expanded=False):
        st.markdown("""
        ### WCAG Standards:
        - **AAA (7.0:1)**: Enhanced contrast, best for accessibility
        - **AA (4.5:1)**: Standard, recommended minimum
        - **AA Large (3.0:1)**: For large text (18pt+)
        
        ### Current App Contrast Ratios:
        """)
        
        colors = {
            "Primary on White": ("#6366f1", "#ffffff"),
            "Text on White": ("#1f2937", "#ffffff"),
            "White on Primary": ("#ffffff", "#6366f1"),
            "Success on White": ("#10b981", "#ffffff"),
            "Warning on White": ("#f59e0b", "#ffffff"),
            "Danger on White": ("#ef4444", "#ffffff"),
        }
        
        for label, (fg, bg) in colors.items():
            ratio = get_contrast_ratio(fg, bg)
            meets_aa = ratio >= 4.5
            meets_aaa = ratio >= 7.0
            
            icon = "✅" if meets_aaa else "✓" if meets_aa else "⚠️"
            st.markdown(f"{icon} **{label}**: {ratio:.2f}:1")
