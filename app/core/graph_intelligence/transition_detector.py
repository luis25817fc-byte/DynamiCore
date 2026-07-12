
class TransitionDetector:

    VERSION = "6.5.0"

    def detect(self, diff):

        if abs(diff.get("growth",0)) > 5:
            return "STRUCTURAL_TRANSITION"

        return "STABLE"
