#IfWinActive, ahk_class OpusApp
+WheelUp:: ; scroll right
ComObjActive("Word.application").ActiveWindow.SmallScroll(0,0,1,0)
return

+WheelDown:: ; scroll left
ComObjActive("Word.application").ActiveWindow.SmallScroll(0,0,0,1)
return

#IfWinActive, ahk_class PPTFrameClass
+WheelUp:: ; scroll right
ComObjActive("Powerpoint.application").ActiveWindow.SmallScroll(0,0,0,1)
return

+WheelDown:: ; scroll left
ComObjActive("Powerpoint.application").ActiveWindow.SmallScroll(0,0,1,0)
return

#IfWinActive, ahk_class XLMAIN
+WheelUp:: ; scroll right
ComObjActive("Excel.application").ActiveWindow.SmallScroll(0,0,0,1)
return

+WheelDown:: ; scroll left
ComObjActive("Excel.application").ActiveWindow.SmallScroll(0,0,1,0)
return

#IfWinActive