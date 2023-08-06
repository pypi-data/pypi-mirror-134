
from termuxgui.view import View

class Spinner(View):
    """This represents a Spinner."""
    
    def __init__(self, activity, parent=None):
        args = {"aid": activity.aid}
        if parent != None:
            args["parent"] = parent.id
        View.__init__(self, activity, activity.c.send_read_msg({"method": "createSpinner", "params": args}))
    
    
    def setlist(self, list):
        """Sets the list of items displayed in the spinner. list has to be a list containing strings."""
        self.a.c.send_msg({"method": "setList", "params": {"aid": self.a.aid, "id": self.id, "list": list}})
    
    
    
    
