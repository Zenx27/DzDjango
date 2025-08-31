
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core import signing

def index(request):
    if request.method == "POST":
        data = request.POST.get("message")
        if data:
            messages.success(request, f"Вы отправили сообщение: {data}")

         
            signed = signing.dumps({"text": data})
            request.session['signed_data'] = signed
            return redirect("signed")
    return render(request, "main/index.html")


def signed_data(request):
    signed = request.session.get("signed_data")
    unsigned = None
    if signed:
        try:
            unsigned = signing.loads(signed)
        except signing.BadSignature:
            unsigned = {"error": "Подпись недействительна!"}
    return render(request, "main/signed.html", {"signed": signed, "unsigned": unsigned})
