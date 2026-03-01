ALTER TABLE grade_rep
DROP CONSTRAINT fk_grade_rep_rep;

ALTER TABLE grade_rep
ADD CONSTRAINT fk_grade_rep_rep
FOREIGN KEY (rep_id)
REFERENCES report_card(id)
ON DELETE CASCADE
ON UPDATE CASCADE;