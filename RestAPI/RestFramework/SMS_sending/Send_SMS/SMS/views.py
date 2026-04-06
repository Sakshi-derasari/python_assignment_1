from django.shortcuts import render
import requests

def sendsms(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        APIKEY = "nOwAHF1YBtVIggXxRAGn54nIpGNWLKcTCJPVSVUjA0A8pKSbS4Py8SqrNcyY"

        url = "https://www.fast2sms.com/dev/bulkV2"

        querystring = {
            "authorization": APIKEY,
            "route": "q",
            "message": message,
            "numbers": phone
        }
        
        headers = {
            "cache-control": "no-cache"
        }

        try:
            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()
            print(data)

            if data.get("return") == True:
                return render(request, "index.html", {
                    "success": "Message sent successfully ✅"
                })
            else:
                return render(request, "index.html", {
                    "error": "Failed to send message ❌"
                })

        except Exception as e:
            return render(request, "index.html", {
                "error": str(e)
            })

    return render(request, "index.html")