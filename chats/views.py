from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
from django.conf import settings
# Initialize the OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key= settings.OPEN_AI_KEY 
)

def chatbot_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        # Prepare the message for the API
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_input
                    }
                ]
            }
        ]

        # Call the OpenRouter API
        try:
            completion = client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": "http://127.0.0.1:8000/",  
                    "X-Title": "P & B Chatbot", 
                },
                model="google/gemma-3-1b-it:free",
                messages=messages
            )
            chatbot_reply = completion.choices[0].message.content
        except Exception as e:
            chatbot_reply = f'Error: {str(e)}'

        return JsonResponse({'reply': chatbot_reply})

    return render(request, "chatbot.html")


def home(request):
    return render(request,"index.html")
