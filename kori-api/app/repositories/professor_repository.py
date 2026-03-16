from typing import List
import asyncpg

from app.core.database import get_connection
from app.schemas.professorDTO import ProfessorStudentGradesDTO, StudentRankingDTO
from app.models.calendar_event import CalendarEvent
from typing import List
import asyncpg

from app.core.database import get_connection
from app.schemas.professorDTO import ProfessorStudentGradesDTO, StudentRankingDTO
from app.models.calendar_event import CalendarEvent

from app.core.database import get_connection
from app.schemas.professorDTO import ProfessorStudentGradesDTO, StudentRankingDTO
from app.models.calendar_event import CalendarEvent


class ProfessorRepository:

    @staticmethod
    async def get_students_grades_by_professor(professor_id: int) -> List[ProfessorStudentGradesDTO]:
        sql = """
        SELECT
            s.enrollment,
            s.name,
            s.serie,
            g.grade1,
            g.grade2,
            g.rec
        FROM professors p
        JOIN grades g ON g.subject_id = p.subject_id
        JOIN grade_rep gr ON gr.grade_id = g.id
        JOIN report_card rc ON rc.id = gr.rep_id
        JOIN students s ON s.enrollment = rc.student_id
        WHERE p.id = $1
        ORDER BY s.name;
        """

        conn: asyncpg.Connection = await get_connection()
        try:
            rows = await conn.fetch(sql, professor_id)
            return [
                ProfessorStudentGradesDTO(
                    enrollment=row['enrollment'],
                    name=row['name'],
                    serie=row['serie'],
                    grade1=float(row['grade1']) if row['grade1'] is not None else None,
                    grade2=float(row['grade2']) if row['grade2'] is not None else None,
                    rec=float(row['rec']) if row['rec'] is not None else None
                )
                for row in rows
            ]
        finally:
            await conn.close()
class ProfessorRepository:

    @staticmethod
    async def get_students_grades_by_professor(professor_id: int) -> List[ProfessorStudentGradesDTO]:
        sql = """
            SELECT
                s.enrollment,
                s.name,
                s.serie,
                g.grade1,
                g.grade2,
                g.rec
            FROM professors p
            JOIN grades g ON g.subject_id = p.subject_id
            JOIN grade_rep gr ON gr.grade_id = g.id
            JOIN report_card rc ON rc.id = gr.rep_id
            JOIN students s ON s.enrollment = rc.student_id
            WHERE p.id = $1
            ORDER BY s.name;
        """

        conn: asyncpg.Connection = await get_connection()
        try:
            rows = await conn.fetch(sql, professor_id)
            return [
                ProfessorStudentGradesDTO(
                    enrollment=row['enrollment'],
                    name=row['name'],
                    serie=row['serie'],
                    grade1=float(row['grade1']) if row['grade1'] is not None else None,
                    grade2=float(row['grade2']) if row['grade2'] is not None else None,
                    rec=float(row['rec']) if row['rec'] is not None else None
                )
                for row in rows
            ]
        finally:
            await conn.close()

    @staticmethod
    async def get_students_ranking(professor_id: int) -> List[StudentRankingDTO]:
        sql = """
            SELECT
                s.serie,
                ROUND(
                    AVG(
                        CASE
                            WHEN g.rec IS NOT NULL
                                THEN (COALESCE(g.grade1, 0) + COALESCE(g.grade2, 0) + COALESCE(g.rec, 0)) / 3.0
                            ELSE (COALESCE(g.grade1, 0) + COALESCE(g.grade2, 0)) / 2.0
                        END
                    )
                , 2) AS average
            FROM professors p
            JOIN grades g ON g.subject_id = p.subject_id
            JOIN grade_rep gr ON gr.grade_id = g.id
            JOIN report_card rc ON rc.id = gr.rep_id
            JOIN students s ON s.enrollment = rc.student_id
            WHERE p.id = $1
            GROUP BY s.serie
            ORDER BY average DESC;
        """

        conn: asyncpg.Connection = await get_connection()
        try:
            rows = await conn.fetch(sql, professor_id)
            return [
                StudentRankingDTO(
                    serie=row["serie"],
                    average=float(row["average"]) if row["average"] is not None else None
                )
                for row in rows
            ]
        finally:
            await conn.close()

    @staticmethod
    async def get_all_events() -> List[CalendarEvent]:
        sql = """
            SELECT
                id,
                event_date,
                event_start,
                event_end,
                event_name,
                event_desc,
                admin_id
            FROM calendar_events
            ORDER BY event_date ASC, event_start ASC
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

    @staticmethod
    async def get_all_events() -> List[CalendarEvent]:
        sql = """
        SELECT
            id,
            event_date,
            event_start,
            event_end,
            event_name,
            event_desc,
            admin_id
        FROM calendar_events
        ORDER BY event_date ASC, event_start ASC
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
