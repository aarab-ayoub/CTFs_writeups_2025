Shady Spreadsheet
Analyze this suspicious Excel file and discover the hidden flag . The file mimics a phishing document, so proceed with caution.


<!-- Sub SuspiciousMacro()
    Dim secretData As Variant
    secretData = Array(89, 90, 91, 74, 106, 55, 91, 57, 94, 55, 91, 120, 93, 55, 54, 109, 94, 108, 69, 123, 93, 55, 95, 120, 94, 92, 105, 62)
    Dim shift As Integer
    shift = 5
    Dim hiddenString As String
    hiddenString = ""
    Dim i As Integer
    
    ' Assemble the encoded string
    For i = LBound(secretData) To UBound(secretData)
        hiddenString = hiddenString & Chr(secretData(i) - shift)
    Next i
    
    ' Decoy code to confuse
    Dim fakeData As Variant
    fakeData = Array(84, 72, 73, 83, 95, 73, 83, 95, 70, 65, 75, 69)
    Dim fakeString As String
    fakeString = ""
    For i = LBound(fakeData) To UBound(fakeData)
        fakeString = fakeString & Chr(fakeData(i))
    Next i
    
    If 1 = 2 Then
        MsgBox "Flag: " & fakeString ' Decoy: "THIS_IS_FAKE"
    End If
    
    ' More confusion
    Dim dummy As String
    dummy = "MED{not_the_flag}"
    ' Suspicious action (does nothing useful)
    Range("A1").Value = "Login required"
End Sub -->
