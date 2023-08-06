from json import dumps

from termuxgui.compoundbutton import CompoundButton
from termuxgui.view import View

class Checkbox(CompoundButton):
    """This represents a CheckBox."""
    
    def __init__(self, activity, text, parent=None, checked=False):
        args = {"aid": activity.aid, "text": text, "checked": checked}
        if parent != None:
            args["parent"] = parent.id
        self.checked = checked
        View.__init__(self, activity, activity.c.send_read_msg({"method": "createCheckbox", "params": args}))
     
    
    
    
