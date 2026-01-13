from view.streamlit_view import StreamlitView


class HomeController:
    def __init__(self, view: StreamlitView):
        self._view = view

    def execute(self) -> None:
        self._view.show_home()
