from datetime import datetime, timezone
import uuid


class EnterpriseSDKCore:

    VERSION = "1.0"


    def __init__(
        self,
        gateway=None
    ):

        self.gateway = gateway
        self.requests = []


    def create_request(
        self,
        operation,
        payload
    ):

        request = {
            "sdk_request_id": str(uuid.uuid4()),
            "operation": operation,
            "payload": payload,
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
            "version": self.VERSION
        }

        self.requests.append(request)

        return request


    def send(
        self,
        request
    ):

        if self.gateway:

            response = self.gateway.process(
                request
            )

        else:

            response = {
                "status": "SIMULATED",
                "request_id": request["sdk_request_id"]
            }


        return response


    def history(self):

        return self.requests


    def diagnostics(self):

        return {
            "version": self.VERSION,
            "requests": len(self.requests),
            "status": "READY"
        }