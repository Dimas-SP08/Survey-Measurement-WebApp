"""import necessary libraries"""
from page import HomePage,InputPointsPage,InputThreadsPage,ResultsPage
from utils import *

class MainApp():
    """intialize application with routing pages"""
    def __init__(self):
        self.pages = {
            "home": HomePage(),
            "input_points": InputPointsPage(),
            "input_threads": InputThreadsPage(),
            "results": ResultsPage(),
            }
        
        """Initialize session state for current page"""
        if "current_page" not in session_state():
            set_state("current_page","home")
            set_state("results", [])

    """Navigate to a different page and rerun the app."""
    def navigate_to(self,name_page):
        set_state("current_page",name_page)
        rerun()

    """Render the current page based on the session state."""
    def render_current_page(self):
        current_page = self.pages[get_state("current_page")]
        current_page.render(self.navigate_to)

    """Run the application."""
    def run(self):
        self.render_current_page()

"""main entry point"""
if __name__ == "__main__":
    app = MainApp()
    app.run()


