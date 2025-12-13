from controller.pipeline_controller import PipelineController
from view.web_ui import WebUI

def main():
    controler = PipelineController(view=WebUI())
    controler.run()

if __name__ == "__main__":
    main()
