from typing import Optional, List
import asyncpg

from app.core.database import get_connection
from app.schemas.studentDTO import StudentReportDTO, StudentGradeDTO
from app.models.reportCard import ReportCardResponse
from app.models.grades import GradesResponse
from app.models.observation import Observation
from app.models.calendar_event import CalendarEvent


class StudentRepository:

    @staticmethod
    async def searchStudentByEnrollment(enrollment: int) -> Optional[StudentReportDTO]:
        sql = """
            SELECT
                s.enrollment,
                s.name AS student_name,
                s.serie,
                s.issue_date,
                rc.id AS report_id,
                rc.final_situation,
                su.name AS subject_name,
                g.subject_id,
                g.grade1,
                g.grade2,
                g.rec
            FROM students s
            LEFT JOIN report_card rc ON rc.student_id = s.enrollment
            LEFT JOIN grade_rep gr ON gr.rep_id = rc.id
            LEFT JOIN grades g ON g.id = gr.grade_id
            LEFT JOIN subjects su ON su.id = g.subject_id 
            WHERE s.enrollment = $1
            ORDER BY g.subject_id
        """

        conn: asyncpg.Connection = await get_connection()
        try:
            rows = await conn.fetch(sql, enrollment)

            if not rows:
                return None

            first_row = rows[0]
            report_card = None
            grades: List[StudentGradeDTO] = []

            # Initialize report card if it exists
            if first_row["report_id"] is not None:
                report_card = ReportCardResponse(
                    id=first_row["report_id"],
                    student_id=first_row["enrollment"],
                    final_situation=first_row["final_situation"]
                )

            # Map grades from all rows
            for row in rows:
                if row["subject_id"] is not None:
                    grades.append(
                        StudentGradeDTO(
                            subject_id=row["subject_id"],
                            subject_name=row["subject_name"],
                            grade1=row["grade1"],
                            grade2=row["grade2"],
                            rec=row["rec"]
                        )
                    )

            return StudentReportDTO(
                enrollment=first_row["enrollment"],
                name=first_row["student_name"],
                serie=first_row["serie"],
                issue_date=first_row["issue_date"],
                report_card=report_card,
                grades=grades
            )
        finally:
            await conn.close()

    @staticmethod
    async def get_student_observations(enrollment: int) -> List[Observation]:
        sql = """
            SELECT id, student_id, observation
            FROM observations
            WHERE student_id = $1
        """
        conn: asyncpg.Connection = await get_connection()
        try:
            rows = await conn.fetch(sql, enrollment)
            return [
                Observation(
                    id=row['id'],
                    student_id=row['student_id'],
                    observation=row['observation']
                )
                for row in rows
            ]
        finally:
            await conn.close()

    @staticmethod
    async def get_all_events() -> List[CalendarEvent]:
        sql = """
            SELECT id, event_date, event_start, event_end, event_name, event_desc, admin_id
            FROM calendar_events
            ORDER BY event_date ASC
        """
        conn: asyncpg.Connection = await get_connection()
        try:
            rows = await conn.fetch(sql)
            return [
                CalendarEvent(
                    id=row['id'],
                    event_date=row['event_date'],
                    event_start=row['event_start'],
                    event_end=row['event_end'],
                    event_name=row['event_name'],
                    event_desc=row['event_desc'],
                    admin_id=row['admin_id']
                )
                for row in rows
            ]
        finally:
            await conn.close()