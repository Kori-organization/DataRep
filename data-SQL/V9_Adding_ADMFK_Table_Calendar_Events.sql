-- Calendar Events
CREATE TABLE calendar_events (
    id SERIAL PRIMARY KEY,
	event_date DATE NOT NULL,
	event_start TIME NOT NULL,
    event_end TIME NOT NULL,
    event_name VARCHAR(50) NOT NULL,
    event_desc TEXT,
    admin_id INT,
    FOREIGN KEY (admin_id) REFERENCES administrators(id)
);
