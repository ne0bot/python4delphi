////
//  This file was generated by VCL Generator
//  Copyright 1998 - Morgan Martinet
//  29/06/1999 12:59:58
//  it subclasses all classes of the unit Menus
////

unit Delphi_Menus;

interface

uses
  Windows,
  SysUtils,
  Classes,
  Messages,
  Menus,
  PythonEngine,
  PyVarArg,
  PyRecords,
  PyDelphiAssoc;

type
  TPyMenuItem = class( TMenuItem )
  protected
    FAssoc : Integer;
  public
    destructor Destroy; override;
    procedure EventOnClick( Sender : TObject );
  published
    property __assoc__ : Integer read FAssoc write FAssoc;
  end;

  TPyMenu = class( TMenu )
  protected
    FAssoc : Integer;
  public
    destructor Destroy; override;
  published
    property __assoc__ : Integer read FAssoc write FAssoc;
  end;

  TPyMainMenu = class( TMainMenu )
  protected
    FAssoc : Integer;
  public
    destructor Destroy; override;
  published
    property __assoc__ : Integer read FAssoc write FAssoc;
  end;

  TPyPopupMenu = class( TPopupMenu )
  protected
    FAssoc : Integer;
  public
    destructor Destroy; override;
    procedure EventOnPopup( Sender : TObject );
  published
    property __assoc__ : Integer read FAssoc write FAssoc;
  end;


implementation

Uses Py_Misc;

/////////// class TPyMenuItem /////////////////////

destructor TPyMenuItem.Destroy;
begin
  ClearInterface( TDelphiAssoc(FAssoc) );
  FAssoc := 0;
  inherited;
end;

procedure TPyMenuItem.EventOnClick( Sender : TObject );
var
  args, rslt : PPyObject;
  L : TList;
begin
  L := TList.Create;
  try
    L.Add( GetPythonObject( Sender, 'Menus', 'TMenuItem' ) ); 
    rslt := ExecuteEvent( 'OnClick', TDelphiAssoc(__assoc__), L, args );
    GetPythonEngine.Py_XDecRef( rslt );
    GetPythonEngine.Py_XDecRef( args );
  finally
    L.Free;
  end;
end;

/////////// class TPyMenu /////////////////////

destructor TPyMenu.Destroy;
begin
  ClearInterface( TDelphiAssoc(FAssoc) );
  FAssoc := 0;
  inherited;
end;

/////////// class TPyMainMenu /////////////////////

destructor TPyMainMenu.Destroy;
begin
  ClearInterface( TDelphiAssoc(FAssoc) );
  FAssoc := 0;
  inherited;
end;

/////////// class TPyPopupMenu /////////////////////

destructor TPyPopupMenu.Destroy;
begin
  ClearInterface( TDelphiAssoc(FAssoc) );
  FAssoc := 0;
  inherited;
end;

procedure TPyPopupMenu.EventOnPopup( Sender : TObject );
var
  args, rslt : PPyObject;
  L : TList;
begin
  L := TList.Create;
  try
    L.Add( GetPythonObject( Sender, 'Menus', 'TPopupMenu' ) ); 
    rslt := ExecuteEvent( 'OnPopup', TDelphiAssoc(__assoc__), L, args );
    GetPythonEngine.Py_XDecRef( rslt );
    GetPythonEngine.Py_XDecRef( args );
  finally
    L.Free;
  end;
end;


end.