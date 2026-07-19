
class EvolutionLayer:

    VERSION="6.2.2"

    def analyze(self,previous,current):

        previous=previous or {}
        current=current or {}

        changes={}

        keys=set(previous)|set(current)

        for k in keys:

            if previous.get(k)!=current.get(k):

                changes[k]={
                    "previous":previous.get(k),
                    "current":current.get(k)
                }

        return{

            "version":self.VERSION,

            "evolved":bool(changes),

            "changes":changes,

            "evolution_score":len(changes)

        }
