from fastapi_mail import FastMail, MessageSchema

async def send_verification(email: str, token: str):
    message = MessageSchema(
        subject="Verify email",
        recipients=[email],
        body=f"http://localhost:8000/verify/{token}",
        subtype="html"
    )

    fm = FastMail(...)  # конфіг з .env
    await fm.send_message(message)
