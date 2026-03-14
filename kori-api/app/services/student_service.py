from app.repositories.student_repository import StudentRepository


class AlunoService:

    @staticmethod
    async def get_student_report(enrollment: int):
        student = await StudentRepository.searchStudentByEnrollment(enrollment)

        if not student:
            return {"error": "Aluno não encontrado"}

        return student


    @staticmethod
    async def get_student_observations(enrollment: int):
        return await StudentRepository.get_student_observations(enrollment)


    @staticmethod
    async def get_calendar_events():
        return await StudentRepository.get_all_events()