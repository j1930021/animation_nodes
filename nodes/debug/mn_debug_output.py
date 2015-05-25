import bpy
from bpy.types import Node
from ... mn_node_base import AnimationNode
from ... mn_execution import nodePropertyChanged, allowCompiling, forbidCompiling

class mn_DebugOutputNode(Node, AnimationNode):
    bl_idname = "mn_DebugOutputNode"
    bl_label = "Debug Output"
    
    printDebugString = bpy.props.BoolProperty(default = False)
    debugOutputString = bpy.props.StringProperty(default = "")
    
    def init(self, context):
        forbidCompiling()
        self.inputs.new("mn_GenericSocket", "Data")
        self.bl_width_max = 10000
        allowCompiling()
        
    def draw_buttons(self, context, layout):
        layout.label(self.debugOutputString)
        
    def draw_buttons_ext(self, context, layout):
        layout.prop(self, "printDebugString", text = "Print")
        
    def execute(self, input):
        self.debugOutputString = str(input["Data"])
        if self.printDebugString: print(self.debugOutputString)
        return {}
