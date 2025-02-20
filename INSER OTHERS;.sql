USE ProjectDataScience;

INSERT INTO Summary (Metric, Value)
VALUES 
('Count of Candidates', 2),
('Average Time to Hire', 27.5),
('Average Candidate Experience', 4.25);

INSERT INTO FileManagement (FileName, FilePath, FileExtension)
VALUES 
('Summary.xlsx', 'C:/Users/a880862/OneDrive - ATOS/Desktop/new proj/xlsx/Summary.xlsx', '.xlsx'),
('Report.xlsx', 'C:/Users/a880862/OneDrive - ATOS/Desktop/new proj/xlsx/Report.xlsx', '.xlsx');

INSERT INTO PivotTableData (Metric, Value)
VALUES 
('Average Time to Hire', 27.5),
('Average Interview Scores', 8.0);