
"""
DynamiCore Enterprise
DLIS-035
Kernel Gateway
"""

from datetime import datetime, timezone


class KernelGateway:

    VERSION = "DLIS-035"


    def __init__(self, kernel=None):

        self.kernel = kernel
        self.requests = 0
        self.responses = 0


    def process(self, request):

        self.requests += 1


        if self.kernel is None:

            return {
                "status": "KERNEL_NOT_CONNECTED",
                "version": self.VERSION
            }


        output = self.kernel.execute(request)

        self.responses += 1


        return {

            "gateway": {

                "version": self.VERSION,

                "timestamp":
                    datetime.now(
                        timezone.utc
                    ).isoformat(),

                "requests":
                    self.requests,

                "responses":
                    self.responses
            },

            "kernel_output":
                output
        }


    def status(self):

        return {

            "version":
                self.VERSION,

            "module":
                "KernelGateway",

            "requests":
                self.requests,

            "responses":
                self.responses,

            "status":
                "ONLINE"
        }
