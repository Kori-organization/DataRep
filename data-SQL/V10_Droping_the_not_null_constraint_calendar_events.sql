-- calendar_events
ALTER TABLE calendar_events
ALTER COLUMN event_start DROP NOT NULL;

ALTER TABLE calendar_events
ALTER COLUMN event_end DROP NOT NULL;

