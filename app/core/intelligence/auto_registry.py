
import importlib


class AutoRegistry:

    VERSION = "7.1"


    def __init__(self, kernel):

        self.kernel = kernel



    def register_module(self, name, module_path):

        try:

            importlib.import_module(module_path)

            self.kernel.register(name)

            return {
                "module": name,
                "path": module_path,
                "status": "REGISTERED"
            }

        except Exception as e:

            return {
                "module": name,
                "path": module_path,
                "status": "FAILED",
                "error": str(e)
            }



    def register_core_stack(self):

        modules = {

            "graph_intelligence":
                "app.core.graph_intelligence",

            "prediction":
                "app.core.predictive",

            "decision":
                "app.core.decision",

            "enterprise":
                "app.core.enterprise"

        }


        results = []


        for name, path in modules.items():

            results.append(
                self.register_module(
                    name,
                    path
                )
            )


        return results
