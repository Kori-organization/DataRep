ALTER TABLE report_card
DROP CONSTRAINT fk_report_card_subject;

ALTER TABLE report_card
DROP CONSTRAINT fk_report_card_professor;

ALTER TABLE report_card
DROP COLUMN subject_id,
DROP COLUMN professor_id;