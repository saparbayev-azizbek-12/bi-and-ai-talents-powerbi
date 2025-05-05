USE demo_project;
GO

CREATE TABLE retrieveinfo (
	retrieve_id INT IDENTITY(1,1) PRIMARY KEY,
	source_file NVARCHAR(255) NOT NULL,
	retrieved_at DATETIME DEFAULT GETDATE(),
	total_rows INT NOT NULL,
	processed_rows INT NOT NULL,
	errors INT NOT NULL,
	notes NVARCHAR(MAX)
);