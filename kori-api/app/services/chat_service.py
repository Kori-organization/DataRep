import json

from app.repositories.student_repository import StudentRepository
from app.repositories.professor_repository import ProfessorRepository
from app.integrations.gemini import student_chain, professor_chain


class ChatService:

    @staticmethod
    async def ask_student_question(enrollment: int, question: str) -> dict:
        student = await StudentRepository.searchStudentByEnrollment(enrollment)

        if not student:
            return {"response": "Aluno não encontrado."}

        observations = await StudentRepository.get_student_observations(enrollment)
        events = await StudentRepository.get_all_events()

        context = {
            "student": student.model_dump(mode="json"),
            "observations": [obs.model_dump(mode="json") for obs in observations],
            "events": [event.model_dump(mode="json") for event in events]
        }

        answer = student_chain.invoke({
            "question": question,
            "context": json.dumps(context, ensure_ascii=False, indent=2, default=str)
        })

        return {"response": answer}

    @staticmethod
    async def ask_professor_question(professor_id: int, question: str) -> dict:
        students_grades = await ProfessorRepository.get_students_grades_by_professor(professor_id)
        ranking = await ProfessorRepository.get_students_ranking(professor_id)
        events = await ProfessorRepository.get_all_events()

        context = {
            "students_grades": [item.model_dump(mode="json") for item in students_grades],
            "ranking": [item.model_dump(mode="json") for item in ranking],
            "events": [event.model_dump(mode="json") for event in events]
        }

        answer = professor_chain.invoke({
            "question": question,
            "context": json.dumps(context, ensure_ascii=False, indent=2, default=str)
        })

        return {"response": answer}