import maya.cmds as cm

class Turntable(object):

    def __init__(self, camera):     # default constructor
        self.window = "Turnable_Window"
        self.title = "Turntable Manager"
        self.size = (800, 600)

        if cm.window(self.window, exists = True):   # prevention of double instantiation
            cm.deleteUI(self.window, window = True)

        self.window = cm.window(self.window, title = self.title, 
                                widthHeight = self.size)

        cm.columnLayout(adj = True)
        cm.text(self.title)
        cm.separator(height=20)

        # Referencing what camera is being controlled
        self.camera = camera

        # Declaring fields
        self.camera.focal_length = cm.floatSlider( label='Focal Length', min=0, max=100, value=30, step=1 )
        self.camera.camera_height = cm.floatSlider( label='Camera Height', min=0, max=100, value=5, step=1)
        self.camera.camera_angle_interval = cm.floatField( label="Camera Angle Steps", min=1, max=180, value=1)
        
        
        cm.showWindow

        
    
# Creating sphere reference at origin
sphere_ref = cm.sphere( ax=[0,0,0], r=100 )

# Render Camera at 30 unit from center, height of 5, centered around POI 0,0,0
demo_camera = cm.camera( p=[30, 0, 5], wci=[0,0,0] )

cm.orbit( demo_camera )

exampleWindow = Turntable(demo_camera)