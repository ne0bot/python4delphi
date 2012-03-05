###
#  This file was generated by VCL Generator
#  Copyright 1998 - Morgan Martinet
#  29/06/1999 12:59:48
#  it declares the symbols of the Delphi unit Forms.pas
###

from System import *
from Classes import *
from Graphics import *
from Menus import *
from Controls import *
import _Forms

# TScrollBarKind = ( sbHorizontal, sbVertical );
sbHorizontal = 0
sbVertical = 1

# TFormBorderStyle = ( bsNone, bsSingle, bsSizeable, bsDialog, bsToolWindow, bsSizeToolWin );
bsNone = 0
bsSingle = 1
bsSizeable = 2
bsDialog = 3
bsToolWindow = 4
bsSizeToolWin = 5

# TWindowState = ( wsNormal, wsMinimized, wsMaximized );
wsNormal = 0
wsMinimized = 1
wsMaximized = 2

# TFormStyle = ( fsNormal, fsMDIChild, fsMDIForm, fsStayOnTop );
fsNormal = 0
fsMDIChild = 1
fsMDIForm = 2
fsStayOnTop = 3

# TBorderIcon = ( biSystemMenu, biMinimize, biMaximize, biHelp );
biSystemMenu = 0
biMinimize = 1
biMaximize = 2
biHelp = 3

# TPosition = ( poDesigned, poDefault, poDefaultPosOnly, poDefaultSizeOnly, poScreenCenter );
poDesigned = 0
poDefault = 1
poDefaultPosOnly = 2
poDefaultSizeOnly = 3
poScreenCenter = 4

# TPrintScale = ( poNone, poProportional, poPrintToFit );
poNone = 0
poProportional = 1
poPrintToFit = 2

# TShowAction = ( saIgnore, saRestore, saMinimize, saMaximize );
saIgnore = 0
saRestore = 1
saMinimize = 2
saMaximize = 3

# TTileMode = ( tbHorizontal, tbVertical );
tbHorizontal = 0
tbVertical = 1

# TCloseAction = ( caNone, caHide, caFree, caMinimize );
caNone = 0
caHide = 1
caFree = 2
caMinimize = 3

# TFormState = set of ( fsCreating, fsVisible, fsShowing, fsModal, fsCreatedMDIChild );
fsCreating = 0
fsVisible = 1
fsShowing = 2
fsModal = 3
fsCreatedMDIChild = 4

# TTimerMode = ( tmShow, tmHide );
tmShow = 0
tmHide = 1

####################################################
class TControlScrollBar( TPersistent ):
    def Create( Self ):
        return _Forms.CreateControlScrollBar( Self )

    def __getattr__( Self, Key ):
        return _Forms.ControlScrollBar_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Forms.ControlScrollBar_SetAttr( Self, Key, Value )

####################################################
class TScrollingWinControl( TWinControl ):
    def Create( Self, AOwner ):
        return _Forms.CreateScrollingWinControl( Self, AOwner )

    def CreateParented( Self, ParentWindow ):
        return _Forms.CreateParentedScrollingWinControl( Self, ParentWindow )

    def __getattr__( Self, Key ):
        return _Forms.ScrollingWinControl_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Forms.ScrollingWinControl_SetAttr( Self, Key, Value )

####################################################
class TScrollBox( TScrollingWinControl ):
    def Create( Self, AOwner ):
        return _Forms.CreateScrollBox( Self, AOwner )

    def CreateParented( Self, ParentWindow ):
        return _Forms.CreateParentedScrollBox( Self, ParentWindow )

    def __getattr__( Self, Key ):
        return _Forms.ScrollBox_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Forms.ScrollBox_SetAttr( Self, Key, Value )

####################################################
class TDesigner( TObject ):
    def Create( Self ):
        return _Forms.CreateDesigner( Self )

    def __getattr__( Self, Key ):
        return _Forms.Designer_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Forms.Designer_SetAttr( Self, Key, Value )

####################################################
class TCustomForm( TScrollingWinControl ):
    def Create( Self, AOwner ):
        return _Forms.CreateCustomForm( Self, AOwner )

    def CreateNew( Self, AOwner ):
        return _Forms.CreateNewCustomForm( Self, AOwner )

    def CreateParented( Self, ParentWindow ):
        return _Forms.CreateParentedCustomForm( Self, ParentWindow )

    def __getattr__( Self, Key ):
        return _Forms.CustomForm_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Forms.CustomForm_SetAttr( Self, Key, Value )

####################################################
class TForm( TCustomForm ):
    def Create( Self, AOwner ):
        return _Forms.CreateForm( Self, AOwner )

    def CreateNew( Self, AOwner ):
        return _Forms.CreateNewForm( Self, AOwner )

    def CreateParented( Self, ParentWindow ):
        return _Forms.CreateParentedForm( Self, ParentWindow )

    def __getattr__( Self, Key ):
        return _Forms.Form_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Forms.Form_SetAttr( Self, Key, Value )

####################################################
class TDataModule( TComponent ):
    def Create( Self, AOwner ):
        return _Forms.CreateDataModule( Self, AOwner )

    def CreateNew( Self, AOwner ):
        return _Forms.CreateNewDataModule( Self, AOwner )

    def __getattr__( Self, Key ):
        return _Forms.DataModule_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Forms.DataModule_SetAttr( Self, Key, Value )

####################################################
class TScreen( TComponent ):
    def Create( Self, AOwner ):
        return _Forms.CreateScreen( Self, AOwner )

    def __getattr__( Self, Key ):
        return _Forms.Screen_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Forms.Screen_SetAttr( Self, Key, Value )

Screen = TScreen().Create( None )

####################################################
class TApplication( TComponent ):
    def Create( Self, AOwner ):
        return _Forms.CreateApplication( Self, AOwner )

    def __getattr__( Self, Key ):
        return _Forms.Application_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _Forms.Application_SetAttr( Self, Key, Value )

Application = TApplication().Create( None )
