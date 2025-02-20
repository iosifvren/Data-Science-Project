Sub CreatePivotTables()
    Dim wb As Workbook
    Dim wsData As Worksheet
    Dim wsPivot As Worksheet
    Dim pt As PivotTable
    Dim ptCache As PivotCache
    Dim dataRange As Range

    Set wb = ThisWorkbook
    On Error Resume Next
    Set wsData = wb.Sheets("Baseline") 
    On Error GoTo 0

    If wsData Is Nothing Then
        MsgBox "Sheet 'Baseline' not found!", vbExclamation
        Exit Sub
    End If

    On Error Resume Next
    Set wsPivot = wb.Sheets("Pivot Summary")
    If wsPivot Is Nothing Then
        Set wsPivot = wb.Sheets.Add(After:=wsData)
        wsPivot.Name = "Pivot Summary"
    Else
        wsPivot.Cells.Clear 
    End If
    On Error GoTo 0

    Set dataRange = wsData.Range("A1").CurrentRegion

    Set ptCache = wb.PivotTableCaches.Create(SourceType:=xlDatabase, SourceData:=dataRange)

    Set pt = ptCache.CreatePivotTable(TableDestination:=wsPivot.Range("A1"), TableName:="PivotSummary")

    With pt
        .PivotFields("Metric").Orientation = xlRowField
        .PivotFields("Metric").Position = 1
        .PivotFields("Value").Orientation = xlDataField
        .PivotFields("Value").Function = xlSum 
    End With

    MsgBox "Pivot Tables created successfully!"
End Sub