CREATE DATABASE ProjectDataScience;
USE ProjectDataScience;

CREATE TABLE Candidates (
    CandidateID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    TimeToHire INT,
    TimeToRecruit INT,
    MissingStartDate BOOLEAN,
    ActiveDemands INT,
    CandidateExperience DECIMAL(3,2),
    InterviewScores DECIMAL(3,2)
);

CREATE TABLE Summary (
    SummaryID INT AUTO_INCREMENT PRIMARY KEY,
    Metric VARCHAR(100),
    Value DECIMAL(18,2)
);

CREATE TABLE FileManagement (
    FileID INT AUTO_INCREMENT PRIMARY KEY,
    FileName VARCHAR(255),
    FilePath VARCHAR(255),
    FileExtension VARCHAR(10),
    DateMoved DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE PivotTableData (
    PivotID INT AUTO_INCREMENT PRIMARY KEY,
    Metric VARCHAR(100),
    Value DECIMAL(18,2),
    CreatedDate DATETIME DEFAULT CURRENT_TIMESTAMP
);