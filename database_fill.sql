-- Department Table
INSERT INTO department (dept_name, description) VALUES
('HR', 'Human Resources Department'),
('IT', 'Information Technology Department'),
('Finance', 'Finance Department'),
('Marketing', 'Marketing Department'),
('Operations', 'Operations Department'),
('Sales', 'Sales Department'),
('Research', 'Research and Development Department'),
('Customer Support', 'Customer Support Department'),
('Legal', 'Legal Department'),
('Reception', 'Reception Department');

-- Employee Table
INSERT INTO employee (dept_id, last_name, first_name, birth_date, wage) VALUES
(1, 'Smith', 'John', '1990-05-15', 60000.00),
(2, 'Johnson', 'Anna', '1985-11-28', 75000.00),
(3, 'Williams', 'Robert', '1992-08-10', 80000.00),
(4, 'Davis', 'Jessica', '1988-04-22', 65000.00),
(5, 'Jones', 'Michael', '1995-07-07', 70000.00),
(6, 'Miller', 'Emily', '1991-01-12', 72000.00),
(7, 'Wilson', 'Daniel', '1987-09-05', 85000.00),
(10, 'Moore', 'Olivia', '1993-03-18', 67000.00),
(10, 'Taylor', 'Matthew', '1989-06-25', 78000.00),
(10, 'Anderson', 'Sophia', '1994-12-08', 71000.00);

-- Work Slot Table
INSERT INTO work_slot (start_time, end_time, day) VALUES
('08:00:00', '12:00:00', 'Monday'),
('13:00:00', '17:00:00', 'Monday'),
('09:00:00', '14:00:00', 'Tuesday'),
('10:00:00', '16:00:00', 'Wednesday'),
('08:30:00', '12:30:00', 'Thursday'),
('11:00:00', '15:00:00', 'Friday'),
('12:00:00', '18:00:00', 'Saturday'),
('10:30:00', '14:30:00', 'Sunday'),
('14:00:00', '17:00:00', 'Monday'),
('08:00:00', '13:00:00', 'Wednesday');

-- Employee Work Slot Table
INSERT INTO employee_work_slot (slot_id, employee_id) VALUES
(1, 1),
(1, 5), 
(1, 6),
(2, 1),  
(2, 3),
(2, 10),
(3, 2), 
(3, 3),
(3, 4),
(4, 6),
(4, 7),
(5, 1), 
(5, 3),
(5, 4), 
(5, 5), 
(5, 6),
(6, 8),
(6, 10),
(7, 1),
(7, 5),
(7, 6),
(8, 8),
(9, 7);

-- Employee Check In Table
INSERT INTO employee_check_in (employee_id, date, check_in, check_out) VALUES
(1, '2023-01-02', '07:57:00', '12:04:00'),
(1, '2023-01-05', '07:59:00', '12:10:00'),
(1, '2023-01-06', '11:02:00', '12:57:00'),
(2, '2023-01-02', '7:49:00', '12:19:00'),
(2, '2023-01-03', '8:59:00', '14:09:00'),
(2, '2023-01-04', '08:15:00', '13:30:00'),
(3, '2023-01-02', '13:00:00', '17:00:00'),
(3, '2023-01-03', '09:00:00', '14:01:00'),
(3, '2023-01-04', '10:01:00', '16:02:00'),
(4, '2023-01-02', '10:45:00', '16:30:00'),
(5, '2023-01-02', '08:00:00', '12:00:00'),
(5, '2023-01-03', '08:47:00', '14:04:00'),
(5, '2023-01-04', '10:05:00', '16:03:00'),
(5, '2023-01-05', '08:35:00', '12:27:00'),
(5, '2023-01-06', '11:00:00', '15:07:00'),
(6, '2023-01-04', '08:15:00', '13:42:00'),
(8, '2023-01-01', '10:26:00', '13:45:00'),
(9, '2023-01-07', '12:00:00', '17:39:00');

-- Exhibit Table
INSERT INTO exhibit (manager_id, theme, description) VALUES
(1, 'Modern Art', 'A collection of contemporary artworks'),
(2, 'Ancient History', 'Artifacts and exhibits from ancient civilizations'),
(3, 'Nature in Focus', 'Photographs and paintings celebrating nature'),
(4, 'Space Exploration', 'A journey through the cosmos'),
(5, 'Abstract Expressionism', 'Exploring abstract art forms'),
(6, 'Cultural Diversity', 'Showcasing diverse cultural influences'),
(7, 'Innovation and Technology', 'Advancements in science and technology'),
(8, 'Wildlife Safari', 'A virtual safari experience'),	
(9, 'Renaissance Revival', 'A tribute to Renaissance art and culture'),
(10, 'Fantasy World', 'Imaginative and fantastical artworks');

-- Artist Table
INSERT INTO artist (last_name, first_name, birth_date, death_date, nationality, biography) VALUES
('Johnson', 'David', '1975-06-20', '2020-04-15', 'American', 'Renowned painter known for his landscapes'),
('Smith', 'Emily', '1980-03-12', NULL, 'British', 'Sculptor specializing in abstract forms'),
('Williams', 'Daniel', '1992-09-28', NULL, 'Canadian', 'Photographer capturing moments of everyday life'),
('Miller', 'Sophia', '1985-12-05', NULL, 'French', 'Painter with a focus on abstract expressionism'),
('Jones', 'Matthew', '1970-08-18', '2015-11-10', 'German', 'Sculptor known for his bronze sculptures'),
('Davis', 'Olivia', '1988-04-22', NULL, 'Italian', 'Photographer with a passion for nature photography'),
('Moore', 'Michael', '1995-02-10', NULL, 'Japanese', 'Multimedia artist exploring various art forms'),
('Taylor', 'Anna', '1983-07-30', '2010-12-25', 'Mexican', 'Painter influenced by Mexican folk art'),
('Wilson', 'Robert', '1978-11-15', NULL, 'Russian', 'Sculptor creating dynamic and kinetic sculptures'),
('Anderson', 'Jessica', '1990-01-08', NULL, 'Spanish', 'Painter known for her vibrant and colorful compositions');

-- Piece Table
INSERT INTO piece (artist_id, exhibit_id, name, description, year) VALUES
(1, 1, 'Sunset Over the Horizon', 'A breathtaking landscape capturing the beauty of sunset', 2010),
(1, 1, 'Mountain Sunrise II', 'Oil painting capturing the serene sunrise over the mountains', 2022),
(1, 2, 'Whispers of Nature', 'A delicate watercolor depicting the beauty of nature', 2023),
(2, 2, 'Ancient Relics', 'A collection of artifacts from ancient civilizations', NULL),
(2, 3, 'The Essence of Silence', 'Sculpture embodying the calmness found in silence', 2021),
(2, 4, 'Dance of Shadows', 'Abstract piece exploring the interplay of light and shadows', 2023),
(3, 3, 'Mechanical Symphony', 'Sculpture series inspired by the harmony of mechanical components', 2018),
(3, 4, 'Infinite Realities', 'Digital art exploring the concept of infinite parallel realities', 2021),
(3, 3, "Nature's Harmony", 'Photograph series depicting the beauty of nature',  2018),
(3, 5, 'The Golden Age', 'A majestic sculpture symbolizing the golden age of civilization', 2020),
(3, 6, 'Harmony in Chaos', 'Mixed media artwork depicting a harmonious balance within chaos', 2022),
(4, 4, 'Cosmic Journey', 'Abstract painting representing a journey through space', 2015),
(4, 8, 'Beyond the Horizon', 'Photorealistic painting capturing the allure of distant horizons', 2021),
(4, 7, 'Celestial Harmony', 'Digital art portraying the harmony of celestial bodies', 2023),
(5, 9, 'Serenade of Seasons', 'Sculpture series representing the changing seasons in nature', 2019),
(5, 10, 'Lost in Time', 'Contemporary piece exploring the concept of time and memory', 2022),
(5, 5, 'Eternal Bronze', 'Bronze sculptures reflecting themes of eternity', 2005),
(6, 1, 'Metamorphosis', 'Abstract artwork symbolizing transformation and rebirth', 2020),
(6, 2, 'The Colors Within', 'Vibrant painting showcasing the depth of emotions through colors', 2023),
(6, 2, 'Renaissance Revisited', 'Artworks inspired by the Renaissance period', 2012),
(6, 8, 'Floral Symphony', 'Photographs and paintings celebrating floral diversity', 2021),
(7, 7, 'Technological Wonders', 'Artistic representations of technological innovations', 2019),
(8, 10, 'Wildlife Wonderland', 'Virtual safari experience featuring wildlife', NULL),
(10, 1, 'Fantasy Dreams', 'Imaginative artworks exploring fantasy worlds', 2017);

-- Visitor Table
INSERT INTO visitor (last_name, first_name, email, phone_num, birth_date) VALUES
('Brown', 'Emma', 'emma.brown@example.com', 1234567890, '1995-08-10'),
('Johnson', 'Liam', 'liam.johnson@example.com', 9876543210, '1988-02-25'),
('Smith', 'Olivia', 'olivia.smith@example.com', 5551234567, '1992-11-30'),
('Williams', 'Noah', 'noah.williams@example.com', 7779876543, '1985-05-15'),
('Jones', 'Ava', 'ava.jones@example.com', 4445556789, '1998-07-20'),
('Davis', 'Sophia', 'sophia.davis@example.com', 1112223333, '1990-04-18'),
('Moore', 'Michael', 'michael.moore@example.com', 6667778888, '1993-09-05'),
('Taylor', 'Emily', 'emily.taylor@example.com', 2223334444, '1987-12-22'),
('Wilson', 'Daniel', 'daniel.wilson@example.com', 8889990000, '1994-01-08'),
('Anderson', 'Matthew', 'matthew.anderson@example.com', 3334445555, '1980-06-12');

-- Visit Slot Table
INSERT INTO visit_slot (time) VALUES
('9:00:00'),
('10:00:00'),
('11:00:00'),
('12:00:00'),
('13:00:00'),
('14:00:00'),
('15:00:00'),
('16:00:00'),
('17:00:00'),
('18:00:00'),
('19:00:00');

-- Reservation Table
INSERT INTO reservation (visitor_id, slot_id, date, visitor_count) VALUES
(1, 1, '2023-02-01', 2),
(2, 3, '2023-02-02', 1),
(3, 5, '2023-02-03', 4),
(4, 7, '2023-02-04', 3),
(5, 9, '2023-02-05', 2),
(6, 2, '2023-02-06', 1),
(7, 4, '2023-02-07', 5),
(8, 6, '2023-02-08', 3),
(9, 8, '2023-02-09', 2),
(10, 10, '2023-02-10', 4);

-- Ticket Table
INSERT INTO ticket (type, price) VALUES
('Standard', 20.00),
('VIP', 50.00),
('Student', 15.00),
('Senior Citizen', 18.00),
('Family Pack', 75.00),
('Group Discount', 12.00),
('Special Exhibition', 30.00),
('Audio Guide', 5.00),
('Child (Under 12)', 10.00),
('Member Exclusive', 0.00);

-- Visit Table
INSERT INTO visit (ticket_id, visitor_id, receptionist_id, check_in, date) VALUES
(1, 1, 9, '10:30:00', '2023-02-01'),
(2, 2, 9, '11:15:00', '2023-02-02'),
(3, 3, 10, '12:30:00', '2023-02-03'),
(4, 4, 8, '14:45:00', '2023-02-04'),
(5, 5, 10, '16:00:00', '2023-02-05'),
(6, 6, 9, '13:00:00', '2023-02-06'),
(7, 7, 10, '15:30:00', '2023-02-07'),
(8, 8, 8, '17:00:00', '2023-02-08'),
(9, 9, 8, '18:15:00', '2023-02-09'),
(10, 10, 10, '19:30:00', '2023-02-10'),
(2, 1, 9, '10:30:00', '2023-02-02'),
(1, 3, 9, '10:30:00', '2023-02-05'),
(4, 2, 9, '16:30:00', '2023-02-03'),
(10, 9, 9, '9:30:00', '2023-02-05'),
(1, 1, 9, '14:45:00', '2023-02-02'),
(1, 1, 9, '10:00:00', '2023-02-15'),
(2, 2, 9, '11:45:00', '2023-02-20'),
(3, 3, 10, '13:15:00', '2023-02-25'),
(4, 4, 8, '14:30:00', '2023-03-01'),
(5, 5, 10, '15:45:00', '2023-02-05'),
(6, 6, 9, '16:30:00', '2023-02-10'),
(7, 7, 10, '17:45:00', '2023-02-05'),
(8, 8, 8, '18:30:00', '2023-02-02'),
(9, 9, 8, '19:15:00', '2023-02-25');
