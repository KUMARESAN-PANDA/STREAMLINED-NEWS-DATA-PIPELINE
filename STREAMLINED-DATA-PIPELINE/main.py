import streamlit as st
from streamlit_option_menu import option_menu
import business,  entertain,  home, latest, life, music, political, science,sports, technology

# Define custom CSS styles for the sidebar menu
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f0f0;
    }
    .sidebar .sidebar-content .stSelectbox {
        color: #333333;
        font-family: Arial;
        font-size: 20px;
        border-radius: 5px;
        background-color: #f0f0f0;
    }
    .sidebar .sidebar-content .stSelectbox .stSelectbox-options {
        background-color: #f0f0f0;
    }
    .sidebar .sidebar-content .stSelectbox .stSelectbox-options ul li {
        color: #333333;
        cursor: pointer;  /* Add pointer cursor to indicate clickable */
    }
    .sidebar .sidebar-content .stSelectbox .stSelectbox-options ul li:hover {
        background-color: #007bff;  /* Change background color on hover */
        color: #ffffff;  /* Change text color on hover */
    }
    .selected-option {
        background-color: #28a745 !important;  /* Change background color of selected option */
        color: #ffffff !important;  /* Change text color of selected option */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to add some color to the sidebar
def add_color_to_sidebar():
    st.sidebar.markdown("---")
    st.sidebar.markdown("<h1 style='color:#ff6347;text-align:center;'>News Categories</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("---")

class Multipage:
    def __init__(self):
        self.app = []

    def add_app(self, title, function):
        self.app.append({
            "title": title,
            "function": function
        })

    def run(self):
        add_color_to_sidebar()  # Add color to the sidebar

        with st.sidebar:
            selected_option = st.empty()  # Placeholder for the selected option

            app = option_menu(
                menu_title="",
                options=['Home', 'Business',  'Entertain',  'Latest', 'Life',
                         'Music', 'Political', 'Science',  'Sports', 'Technology'],
                icons=['house', 'briefcase', 'play',  'flag', 'heart', 'music-note-beamed', 'people', 'box', 'file-earmark', 'cpu'],
                menu_icon='chat-text-fill',
                default_index=0
            )

        for item in self.app:
            if app == item['title']:
                selected_option.markdown(f"## {item['title']}", unsafe_allow_html=True)  # Update selected option
                item['function'].app()

# Create an instance of the Multipage class
multipage = Multipage()

# Add apps to the Multipage instance
multipage.add_app('Home', home)
multipage.add_app('Business', business)

multipage.add_app('Entertain', entertain)

multipage.add_app('Latest', latest)
multipage.add_app('Life', life)
multipage.add_app('Music', music)
multipage.add_app('Political', political)
multipage.add_app('Science', science)

multipage.add_app('Sports', sports)
multipage.add_app('Technology', technology)

# Run the Streamlit app
multipage.run()
