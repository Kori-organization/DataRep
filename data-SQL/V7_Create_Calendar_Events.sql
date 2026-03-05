-- Calendar Events
CREATE TABLE calendar_events (
    id SERIAL PRIMARY KEY,
    event_date DATE NOT NULL,
    note TEXT,
    admin_id INT
);

