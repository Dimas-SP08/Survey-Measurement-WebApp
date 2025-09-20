def get_main_html():
    return"""
        <style>
            :root {
                --burgundy: #800020;
                --burgundy-light: #a83232;
                --burgundy-dark: #600018;
                --gray-light: #f5f5f5;
                --gray-medium: #e0e0e0;
                --gray-dark: #424242;
            }
            
            /* Main header */
            .main-header {
                background: linear-gradient(135deg, var(--burgundy) 0%, var(--burgundy-dark) 100%);
                padding: 2rem 2.5rem;
                border-radius: 0 0 15px 15px;
                margin-bottom: 2.5rem;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
                color: white;
                text-align: center;
            }

            /* Content cards */
            .card {
                background-color: burgundy;
                padding: 2rem;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
                border-left: 4px solid var(--burgundy);
                margin-top: 1.5rem; /* Spacing between cards */
            }
            
            /* Custom button styles */
            .stButton > button, .stDownloadButton > button, div[data-testid="stLinkButton"] > a {
                border-radius: 8px !important;
                font-weight: 600 !important;
                font-size: 1.05rem !important;
                padding: 0.7rem 1.5rem !important;
                transition: all 0.3s ease !important;
                width: 100%;
                background: linear-gradient(135deg, var(--burgundy) 0%, var(--burgundy-dark) 100%) !important;
                color: white !important;
                border: none !important;
                box-shadow: 0 4px 12px rgba(128, 0, 32, 0.25) !important;
                text-decoration: none !important; /* Remove underline from link */
                display: inline-block; /* Ensure it behaves like a block */
                text-align: center; /* Center the text */
                box-sizing: border-box; /* Include padding in width calculation */
            }
            
            .stButton > button:hover, .stDownloadButton > button:hover, div[data-testid="stLinkButton"] > a:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 6px 16px rgba(128, 0, 32, 0.3) !important;
                color: white !important; /* Ensure text color remains white on hover */
            }

            /* Styling for Streamlit tabs */
            .stTabs [data-baseweb="tab-list"] {
        		gap: 24px;
        	}
        	.stTabs [data-baseweb="tab"] {
        		height: 50px;
        		white-space: pre-wrap;
        		background-color: transparent;
        		border-radius: 4px 4px 0px 0px;
        		gap: 1px;
        		padding-top: 10px;
        		padding-bottom: 10px;
            }
            .stTabs [aria-selected="true"] {
                background-color: var(--burgundy);
                color: white;
            }

           
        </style>
        """

def get_header_html(title, subtitle):
    return f"""
            <div class="main-header">
                <h1 style="color: white; margin-bottom: 0.5rem; font-size: 2.5rem;">{title}</h1>
                <p style="font-size: 1.2rem; opacity: 0.95; margin-top: 0;">
                    {subtitle}
                </p>
            </div>
        """

def get_subheader_html(subheader="",icon="",text=""):
    return f"""
                
                <div class="card">
                    <h4><span style="font-size: 1em;">{icon}</span><br>{subheader}</h4>
                    <p>{text}</p>
                </div>
                
                """

def icon():
    instagram_icon = """<svg width="24" height="24" viewBox="0 0 24 24">
  <defs>
    <radialGradient id="ig-gradient" cx="0.3" cy="1.2" r="1.2">
      <stop offset="0" stop-color="#FCDA74"/>
      <stop offset="0.25" stop-color="#EE8862"/>
      <stop offset="0.5" stop-color="#D93480"/>
      <stop offset="0.75" stop-color="#AC2DBA"/>
      <stop offset="1" stop-color="#6A45C3"/>
    </radialGradient>
  </defs>
  <path fill="url(#ig-gradient)" d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.85s-.011 3.584-.069 4.85c-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07s-3.584-.012-4.85-.07c-3.252-.148-4.771-1.691-4.919-4.919-.058-1.265-.069-1.645-.069-4.85s.011-3.584.069-4.85c.149-3.225 1.664-4.771 4.919-4.919C8.416 2.175 8.796 2.163 12 2.163zm0 1.441c-3.21 0-3.567.012-4.803.07-2.764.127-4.004 1.369-4.133 4.133-.058 1.235-.069 1.583-.069 4.803s.011 3.567.069 4.803c.129 2.764 1.369 4.004 4.133 4.133 1.236.058 1.593.069 4.803.069s3.567-.011 4.803-.069c2.764-.129 4.004-1.369 4.133-4.133.058-1.235.069-1.583.069-4.803s-.011-3.567-.069-4.803c-.129-2.764-1.369-4.004-4.133-4.133C15.567 3.614 15.21 3.604 12 3.604zM12 8.118c-2.143 0-3.882 1.739-3.882 3.882s1.739 3.882 3.882 3.882 3.882-1.739 3.882-3.882-1.739-3.882-3.882-3.882zm0 6.321c-1.349 0-2.438-1.089-2.438-2.439s1.089-2.439 2.438-2.439 2.438 1.089 2.438 2.439-1.089 2.439-2.438 2.439zm6.321-7.227c-.702 0-1.271.569-1.271 1.271s.569 1.271 1.271 1.271 1.271-.569 1.271-1.271-.569-1.271-1.271-1.271z"/>
</svg>"""
 
    email_icon = """
<svg height="24px" width="24px" viewBox="0 0 24 24" fill="currentColor">
    <path d="M22 6c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6zm-2 0l-8 5-8-5h16zm0 12H4V8l8 5 8-5v10z"/>
</svg>
"""

    github_icon = """
<svg height="24px" width="24px" viewBox="0 0 24 24" fill="currentColor">
    <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>
</svg>
"""
    whatsapp_icon = """
<svg height="24px" width="24px" viewBox="0 0 24 24" fill="currentColor">
    <path d="M16.75,13.96C17.08,14.43 17.2,14.65 17.2,15.11C17.2,15.81 16.5,16.5 15.96,16.5C15.5,16.5 13.96,16.04 12.41,14.65C10.6,13.03 9.4,11.04 9.4,11.04C9.11,10.5 8.5,9.4 8.5,8.75C8.5,8.1 9,7.65 9.23,7.43C9.45,7.2 9.68,7.2 9.9,7.2H10.4C10.58,7.2 10.73,7.28 10.85,7.48C11.08,7.8 11.5,8.83 11.58,8.98C11.68,9.13 11.63,9.3 11.48,9.45L11.03,9.93C10.95,10 10.88,10.1 11.03,10.33C11.38,10.9 12.23,12.23 12.83,12.83C13.05,13.05 13.15,12.98 13.23,12.9L13.73,12.43C13.88,12.28 14.05,12.23 14.23,12.33C14.38,12.43 15.4,12.85 15.73,13C15.93,13.13 16.03,13.28 16.03,13.43V13.96H16.75M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22C13.66,22 15.25,21.54 16.6,20.73L21,22L20.27,17.7C21.35,16.1 22,14.1 22,12A10,10 0 0,0 12,2Z" />
</svg>
"""

    return instagram_icon, email_icon, github_icon, whatsapp_icon