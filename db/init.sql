use studentdb;
CREATE TABLE students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  registration_number VARCHAR(10) NOT NULL,
  vaccinated TINYINT NOT NULL
);

INSERT INTO students (registration_number,st_name, vaccinated) VALUES ('1234', 1);
INSERT INTO students (registration_number,st_name, vaccinated) VALUES ('5678', 1);
