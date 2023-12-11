import os
import maya.cmds as mc
import maya.mel as mm
import json
import maya.OpenMaya as openmaya
import time

from maya import OpenMayaUI as omui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtUiTools import *
from PySide2.QtWidgets import *

from shiboken2 import wrapInstance
import os.path

myFolder = r"C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool"

# open a pointer to the Maya Main Window
mayaMainWindowPtr = omui.MQtUtil.mainWindow()

# Create a wrapper around QtWidget instance to seperate it from Maya thread
mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QWidget)


class mySetCreationClass(QWidget):
    ''' Class that opens our UI and holds all of the tools functionality '''

    def __init__(self, *args, **kwargs):
        ''' Constructor for your GUI class '''

        super(mySetCreationClass, self).__init__(*args, **kwargs)  # Initialize the class as a typical QWidget class
        self.setParent(mayaMainWindow)  # Make this new Gui a child of the Maya manin window
        self.setWindowFlags(Qt.Window)
        self.initUI()

    def initUI(self):
        ''' Create the GUI and pass off the interface bindings '''

        # A loader is a special device in QtUiTools
        loader = QUiLoader()

        # Get the unbiased path to your UI file
        currentDir = os.path.abspath(myFolder)

        # A QfILE IS A SPECIAL qTio DEVICE for handling file streams
        uiFile = QFile(currentDir + "\controllerCreation.ui")

        # Open the stream as read only
        uiFile.open(QFile.ReadOnly)

        # Convert the UI file from xml to python and send the stream to the Class' UI
        self.ui = loader.load(uiFile, parentWidget=self)

        # Perform the rest of the interface configuration
        self.bindMyButtons()
        

    # Function that creates our circle controller
    def circleCtrl(self):
        mc.circle(nr=[0, 1, 0])

        # Function that creates our square controller

    def squareCtrl(self):
        square = cmds.curve(degree=1, point=[(-1, 0, 1), (1, 0, 1), (1, 0, -1), (-1, 0, -1), (-1, 0, 1)])

    # Function that creates our triangle controller
    def triangleCtrl(self):
        triangle = cmds.curve(degree=1, point=[(0, 0, 1), (-1, 0, -1), (1, 0, -1), (0, 0, 1)])

    # Function that creates our diamond controller
    def diamondCtrl(self):
        diamond = cmds.curve(degree=1, point=[(0, 0, 1), (1, 0, 0), (0, 0, -1), (-1, 0, 0), (0, 0, 1)])

    # Function that creates our X controller
    def xCtrl(self):
        x = cmds.curve(degree=1, point=[(0, 0, -1), (1, 0, -2), (2, 0, -1), (1, 0, 0), (2, 0, 1), (1, 0, 2), (0, 0, 1),
                                        (-1, 0, 2), (-2, 0, 1), (-1, 0, 0), (-2, 0, -1), (-1, 0, -2), (0, 0, -1)])

    # Function that creates our plus controller
    def plusCtrl(self):
        plus = cmds.curve(degree=1,
                          point=[(0, 0, -1), (1, 0, -2), (2, 0, -1), (1, 0, 0), (2, 0, 1), (1, 0, 2), (0, 0, 1),
                                 (-1, 0, 2), (-2, 0, 1), (-1, 0, 0), (-2, 0, -1), (-1, 0, -2), (0, 0, -1)])
        cmds.rotate(0, -45, 0)
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=2)

        # Function that creates our heart controller

    def heartCtrl(self):
        heart = cmds.curve(degree=1, point=[(0, 0, .2), (-0.3, 0, 0.3), (0, 0, .2)])

    # Function that creates our arrowR controller
    def arrowRCtrl(self):
        arrowR = cmds.curve(degree=1,
                            point=[(0, 0, -1), (2, 0, -1), (2, 0, -2), (4, 0, 0), (2, 0, 2), (2, 0, 1), (0, 0, 1),
                                   (0, 0, -1)])

    # Function that creates our arrowUp controller
    def arrowUpCtrl(self):
        arrowUp = cmds.curve(degree=1,
                             point=[(0, 0, -1), (2, 0, -1), (2, 0, -2), (4, 0, 0), (2, 0, 2), (2, 0, 1), (0, 0, 1),
                                    (0, 0, -1)])
        cmds.rotate(0, 90, 0)
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=2)

        # Function that creates our arrowDown controller

    def arrowDownCtrl(self):
        arrowUp = cmds.curve(degree=1,
                             point=[(0, 0, -1), (2, 0, -1), (2, 0, -2), (4, 0, 0), (2, 0, 2), (2, 0, 1), (0, 0, 1),
                                    (0, 0, -1)])
        cmds.rotate(0, -90, 0)
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=2)

    # Function that creates our arrowL controller
    def arrowLCtrl(self):
        arrowL = cmds.curve(degree=1,
                            point=[(0, 0, -1), (-2, 0, -1), (-2, 0, -2), (-4, 0, 0), (-2, 0, 2), (-2, 0, 1), (0, 0, 1),
                                   (0, 0, -1)])

    # Function that creates our arrowL controller
    def arrow2Ctrl(self):
        arrow2 = cmds.curve(degree=1,
                            point=[(0, 0, -1), (2, 0, -1), (2, 0, -2), (4, 0, 0), (2, 0, 2), (2, 0, 1), (0, 0, 1),
                                   (-2, 0, 1), (-2, 0, 2), (-4, 0, 0), (-2, 0, -2), (-2, 0, -1), (0, 0, -1)])

    # Function that creates a text curve and turns it into a controller
    def textCtrl(self, text):
        curve = cmds.textCurves(text=text, font="Arial", t=0.01)

    def textUserInput(self, *args):
        # Get the text from the text field
        object_name = self.ui.TCLineEdit.text()
        if object_name:
            self.textCtrl(object_name)

    # Function that creates the Zero and Offset group on a selected controller
    def groupControllers(self, group_name):
        sel = mc.ls(sl=True)
        for item in sel:
            xTrans = mc.getAttr(item + '.tx')
            yTrans = mc.getAttr(item + '.ty')
            zTrans = mc.getAttr(item + '.tz')
            xRot = mc.getAttr(item + '.rx')
            yRot = mc.getAttr(item + '.ry')
            zRot = mc.getAttr(item + '.rz')

        mc.select(cl=True)
        zero = mc.group(em=True, n=item + '_ZeroGrp')
        offset = mc.group(em=True, n=item + '_OffsetGrp')
        mc.parent(offset, zero)
        mc.setAttr(zero + '.tx', xTrans)
        mc.setAttr(zero + '.ty', yTrans)
        mc.setAttr(zero + '.tz', zTrans)
        mc.setAttr(zero + '.rx', xRot)
        mc.setAttr(zero + '.ry', yRot)
        mc.setAttr(zero + '.rz', zRot)
        mc.parent(item, offset)

    def applyControllers(self):
        sel = mc.ls(sl=True)
        xTrans = mc.getAttr(sel[0] + '.tx')
        yTrans = mc.getAttr(sel[0] + '.ty')
        zTrans = mc.getAttr(sel[0] + '.tz')
        xRot = mc.getAttr(sel[0] + '.rx')
        yRot = mc.getAttr(sel[0] + '.ry')
        zRot = mc.getAttr(sel[0] + '.rz')

        for item in sel:
            mc.setAttr(item + '.tx', xTrans)
            mc.setAttr(item + '.ty', yTrans)
            mc.setAttr(item + '.tz', zTrans)
            mc.setAttr(item + '.rx', xRot)
            mc.setAttr(item + '.ry', yRot)
            mc.setAttr(item + '.rz', zRot)

    def combineCurves(self, controller_name):
        selected_curve_transforms = cmds.ls(selection=True, type="transform")

        if not selected_curve_transforms:
            cmds.warning("No NURBS curve transforms selected.")
            return None

        # Create a group to serve as the controller
        controller_group = cmds.group(empty=True)

        # Parent the selected curve transforms under the controller group
        for curve_transform in selected_curve_transforms:
            # Get the shape node of the curve transform
            curve_shape = cmds.listRelatives(curve_transform, shapes=True, type="nurbsCurve")
            if curve_shape:
                cmds.parent(curve_shape, controller_group, relative=True, shape=True)

    # Function that connects to our saveCurvesSet button that saves the selected curves in the scene to a unique json file
    def saveCurveSet(self):
        def get_selected_curves_data():
            selected_curves = cmds.ls(selection=True, dag=True, type='nurbsCurve')
            output = []

            # Iterate through the selected curves and get their control vertices.
            for curve in selected_curves:
                cv_positions = cmds.getAttr(curve + ".cv[*]")
                points = [[pos[0], pos[1], pos[2]] for pos in cv_positions]

                # Create an object to store the curve info.
                node = {"name": curve, "points": points}
                output.append(node)

            return output

        def save_curves_to_json(filename, data):
            with open(filename, mode="w") as fOut:
                json.dump(data, fOut)

        # Get the timestamp to create a unique filename.
        timestamp = time.strftime("%Y%m%d%H%M%S")
        filename = "C:/Program Files/Autodesk/Maya2022/scripts/CurveSetCreationTool/Temp/curveSet_{}.json".format(
            timestamp)

        # Get the selected curves data.
        selected_curves_data = get_selected_curves_data()

        # Save the selected curves as a new JSON file with a unique filename.
        save_curves_to_json(filename, selected_curves_data)

        popup = cmds.confirmDialog(title='Curve Set Saved', message='Curve Set Saved!', button=['OK'],
                                   defaultButton='OK')

    def importCurveSet(self):
        myDir = "C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool/Temp"
        # cmds.fileDialog2()
        # Opening JSON file
        f = open('data.json')

        # returns JSON object as
        # a dictionary
        data = json.load(f)

        # Iterating through the json
        # list
        for i in data['emp_details']:
            print(i)

        # Closing file
        f.close()

    def bindMyButtons(self):
        ''' Function that binds the buttons in my UI to the functions in this class '''

        # Connect all of the shape creation buttons
        self.ui.circleButton.clicked.connect(self.circleCtrl)

        self.ui.squareButton.clicked.connect(self.squareCtrl)

        self.ui.triangleButton.clicked.connect(self.triangleCtrl)

        self.ui.diamondButton.clicked.connect(self.diamondCtrl)

        self.ui.xButton.clicked.connect(self.xCtrl)

        self.ui.plusButton.clicked.connect(self.plusCtrl)

        self.ui.heartButton.clicked.connect(self.heartCtrl)

        self.ui.arrowRButton.clicked.connect(self.arrowRCtrl)

        self.ui.arrowLButton.clicked.connect(self.arrowLCtrl)

        self.ui.arrowUpButton.clicked.connect(self.arrowUpCtrl)

        self.ui.arrowDownButton.clicked.connect(self.arrowDownCtrl)

        self.ui.arrow2Button.clicked.connect(self.arrow2Ctrl)

        self.ui.CreateCurvButton.clicked.connect(self.textUserInput)

        # Connect the saveCurveSet function to our SCSButton
        self.ui.SCSButton.clicked.connect(self.saveCurveSet)

        # Connect the importCurveSet function to our LCSButton
        self.ui.LCSButton.clicked.connect(self.importCurveSet)

        # Connects the groupControllers function to our COGButton
        self.ui.COGButton.clicked.connect(self.groupControllers)

        # Connects the groupControllers function to our ASButton
        self.ui.ASButton.clicked.connect(self.applyControllers)

        # Connects the groupControllers function to our ComCurvButton
        self.ui.ComCurvButton.clicked.connect(self.combineCurves)
        
        # Connect the icons to the UI on the Buttons
        circlePixmap = QPixmap("C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool/Icons/Circle.png")
        button_icon = QIcon(circlePixmap)
        self.ui.circleButton.setIcon(button_icon)
        
        squarePixmap = QPixmap("C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool/Icons/Square.png")
        button_icon = QIcon(squarePixmap)
        self.ui.squareButton.setIcon(button_icon)
        
        trianglePixmap = QPixmap("C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool/Icons/Triangle.png")
        button_icon = QIcon(trianglePixmap)
        self.ui.triangleButton.setIcon(button_icon)
        
        diamondPixmap = QPixmap("C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool/Icons/rhombus.png")
        button_icon = QIcon(diamondPixmap)
        self.ui.diamondButton.setIcon(button_icon)
        
        xPixmap = QPixmap("C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool/Icons/X.png")
        button_icon = QIcon(xPixmap)
        self.ui.xButton.setIcon(button_icon)
        
        plusPixmap = QPixmap("C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool/Icons/Plus.png")
        button_icon = QIcon(plusPixmap)
        self.ui.plusButton.setIcon(button_icon)
        
        starPixmap = QPixmap("C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool/Icons/Star.png")
        button_icon = QIcon(starPixmap)
        self.ui.starButton.setIcon(button_icon)
        
        heartPixmap = QPixmap("C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool/Icons/Heart.png")
        button_icon = QIcon(heartPixmap)
        self.ui.heartButton.setIcon(button_icon)
        
        spherePixmap = QPixmap("C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool/Icons/Sphere.png")
        button_icon = QIcon(spherePixmap)
        self.ui.sphereButton.setIcon(button_icon)
        
        cubePixmap = QPixmap("C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool/Icons/Cube.png")
        button_icon = QIcon(cubePixmap)
        self.ui.cubeButton.setIcon(button_icon)
        
        pyramidPixmap = QPixmap("C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool/Icons/Pyramid.png")
        button_icon = QIcon(pyramidPixmap)
        self.ui.pyramidButton.setIcon(button_icon)
        
        arrowRpixmap = QPixmap("C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool/Icons/ArrowR.png")
        button_icon = QIcon(arrowRpixmap)
        self.ui.arrowRButton.setIcon(button_icon)
        
        arrowLpixmap = QPixmap("C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool/Icons/ArrowL.png")
        button_icon = QIcon(arrowLpixmap)
        self.ui.arrowLButton.setIcon(button_icon)
        
        arrowUpPixmap = QPixmap("C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool/Icons/ArrowUp.png")
        button_icon = QIcon(arrowUpPixmap)
        self.ui.arrowUpButton.setIcon(button_icon)
        
        arrowDownPixmap = QPixmap("C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool/Icons/ArrowDown.png")
        button_icon = QIcon(arrowDownPixmap)
        self.ui.arrowDownButton.setIcon(button_icon)
        
        arrow2Pixmap = QPixmap("C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool/Icons/Arrow2.png")
        button_icon = QIcon(arrow2Pixmap)
        self.ui.arrow2Button.setIcon(button_icon)
        
        arrow3Pixmap = QPixmap("C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool/Icons/Arrow3.png")
        button_icon = QIcon(arrow3Pixmap)
        self.ui.arrow3Button.setIcon(button_icon)
        
        arrow4Pixmap = QPixmap("C:/Program Files/Autodesk/Maya2024/scripts/CurveSetCreationTool/Icons/4Arrow.png")
        button_icon = QIcon(arrow4Pixmap)
        self.ui.arrow4Button.setIcon(button_icon)
        
def main():
    ''' Creates an instance of your gui class and call it '''
    ui = mySetCreationClass()
    ui.show()
    return ui


if __name__ == '__main__':
    main()
