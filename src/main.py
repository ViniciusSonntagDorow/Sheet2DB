from controller.main_controller import MainController
from controller.home_controller import HomeController
from controller.insert_controller import InsertController
from controller.dashboard_controller import DashboardController
from controller.delete_controller import DeleteController
from view.streamlit_view import StreamlitView
from model.pandera_validator import PanderaValidator
from model.postgres_loader import PostgresLoader
from model.postgres_reader import PostgresReader
from model.postgres_deleter import PostgresDeleter
from utils.config import config


def create_controllers(view: StreamlitView) -> MainController:
    connection_string = config.get_connection_string()
    table_name = config.POSTGRES_TABLE

    validator = PanderaValidator()
    loader = PostgresLoader(connection_string=connection_string, table_name=table_name)
    reader = PostgresReader(connection_string=connection_string)
    deleter = PostgresDeleter(connection_string=connection_string)

    return MainController(
        view=view,
        home_controller=HomeController(view=view),
        insert_controller=InsertController(
            view=view,
            validator=validator,
            loader=loader,
            table_name=table_name,
        ),
        dashboard_controller=DashboardController(
            view=view,
            reader=reader,
        ),
        delete_controller=DeleteController(
            view=view,
            reader=reader,
            deleter=deleter,
            table_name=table_name,
        ),
    )


def main():
    view = StreamlitView()

    main_controller = create_controllers(view)

    main_controller.execute()


if __name__ == "__main__":
    main()
