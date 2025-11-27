from controller.pipeline_controller import PipelineController
from view.web_ui import WebUI

controler = PipelineController(view=WebUI())
controler.run()
