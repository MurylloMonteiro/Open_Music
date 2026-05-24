from flask_mail import Message
import random

recoveryUser = [];

def generateRandomNumber():
    return(random.randrange(111111, 999999, 1))


def sendMail(mailObj, request):

    Code = generateRandomNumber()

    msg = Message(
        subject="Password recovery",
        recipients=[request["email"]]
    )

    recoveryUser.append({
        "email": request["email"],
        "recoveryCode": Code
    })

    msg.body = msg.html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
    </head>
    <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">

        <div style="
            max-width: 600px;
            margin: auto;
            background: white;
            border-radius: 12px;
            padding: 40px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        ">

            <h1 style="color: #ff6b35; text-align: center;">
                Open Music
            </h1>

            <h2 style="color: #333;">
                Recuperação de Senha
            </h2>

            <p style="color: #555; font-size: 16px;">
                Olá,
            </p>

            <p style="color: #555; font-size: 16px;">
                Recebemos uma solicitação para redefinir a senha da sua conta.
                Caso tenha sido você, utilize o código abaixo para continuar:
            </p>

            <div style="
                text-align: center;
                margin: 30px 0;
            ">
                <span style="
                    display: inline-block;
                    background-color: #ff6b35;
                    color: white;
                    padding: 15px 30px;
                    border-radius: 8px;
                    font-size: 28px;
                    font-weight: bold;
                    letter-spacing: 4px;
                ">
                    {Code}
                </span>
            </div>

            <p style="color: #555; font-size: 16px;">
                Este código expira em <strong>15 minutos</strong>.
            </p>

            <p style="color: #555; font-size: 16px;">
                Se você não solicitou esta alteração, ignore este e-mail.
                Sua senha permanecerá inalterada.
            </p>

            <hr style="margin: 30px 0; border: none; border-top: 1px solid #ddd;">

            <p style="
                color: #888;
                text-align: center;
                font-size: 13px;
            ">
                © 2026 OpenMusic — Musica gratuita de qualidade!.
            </p>

        </div>

    </body>
    </html>
    """
    mailObj.send(msg)
    return {"status": "email enviado"}




def verifyCode(email, UserInputCode):

    if not email:
        return False
    
    for i in range(len(recoveryUser)):
        if email == recoveryUser[i]["email"] and recoveryUser[i]["recoveryCode"] == UserInputCode:
            recoveryUser.pop(i)
            return True
    
    return False


