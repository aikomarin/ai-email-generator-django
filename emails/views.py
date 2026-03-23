from django.shortcuts import render
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def email_generator(request):
    resultado = None

    if request.method == "POST":
        prompt_usuario = request.POST.get("prompt")
        tipo = request.POST.get("tipo")

        prompt = f"""
        Escribe un correo {tipo} basado en la siguiente solicitud:

        {prompt_usuario}

        El correo debe ser claro, bien estructurado y listo para enviarse.
        """

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        resultado = res.choices[0].message.content

    return render(request, "emails/index.html", {"resultado": resultado})