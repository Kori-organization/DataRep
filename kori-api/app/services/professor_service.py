from app.repositories.professor_repository import ProfessorRepository


class ProfessorService:

    @staticmethod
    async def get_students_grades(professor_id: int):
        return await ProfessorRepository.get_students_grades_by_professor(professor_id)


    @staticmethod
    async def get_ranking(professor_id: int):
        return await ProfessorRepository.get_students_ranking(professor_id)