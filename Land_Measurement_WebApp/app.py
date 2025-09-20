from page import HomePage,InputPointsPage,InputThreadsPage,ResultsPage
from utils import *


class MainApp():
    def __init__(self):
        self.pages = {
            "home": HomePage(),
            "input_points": InputPointsPage(),
            "input_threads": InputThreadsPage(),
            "results": ResultsPage(),
            }
        
        if "current_page" not in session_state():
            set_state("current_page","home")
            set_state("results", [])

            
    
    def navigate_to(self,name_page):
        set_state("current_page",name_page)
        rerun()

    def render_current_page(self):
        current_page = self.pages[get_state("current_page")]
        current_page.render(self.navigate_to)

    def run(self):
        """Jalankan aplikasi dengan routing halaman."""
        # Render halaman saat ini
        self.render_current_page()

if __name__ == "__main__":
    app = MainApp()
    app.run()


