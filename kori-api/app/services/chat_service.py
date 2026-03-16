import json

from app.repositories.student_repository import StudentRepository
from app.integrations.gemini import student_chain


class ChatService:

    @staticmethod
    async def ask_student_question(enrollment: int, question: str):

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

        return {
            "response": answer
        }