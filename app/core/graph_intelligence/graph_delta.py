
class GraphDeltaEngine:

    VERSION="6.2"

    def compare(self,previous,current):

        previous=previous or {}
        current=current or {}

        delta={}

        keys=set(previous)|set(current)

        for key in keys:

            if previous.get(key)!=current.get(key):

                delta[key]={
                    "previous":previous.get(key),
                    "current":current.get(key)
                }

        return{

            "version":"6.2",

            "changed":bool(delta),

            "delta":delta

        }
