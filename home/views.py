from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import io
from django.conf import settings
import os




# Create your views here.
def index(request):
  context={
    'variable1':"Harry",
    'variable2':"Rohan"
  }
  return render(request,'index.html',context)
  # return HttpResponse("this is homepage")

def about(request):
  return render(request,'about.html')

def services(request):
  return render(request,'certificate.html')

def contact(request):
  if request.method == "POST":
    name=request.POST.get('name')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    desc=request.POST.get('desc')
    contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
    contact.save()
    messages.success(request, "Your message has been sent!")
    
  return render(request,'contact.html')

# from django.shortcuts import render
# from django.http import HttpResponse
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# import io

# def generate_certificate(request):
#     if request.method == "POST":
#         name = request.POST.get("name", "").strip()
#         if not name:
#             return HttpResponse("Please enter your name.")

#         # Create a PDF in memory
#         buffer = io.BytesIO()
#         pdf = canvas.Canvas(buffer, pagesize=letter)
#         width, height = letter

#         # Title
#         pdf.setFont("Helvetica-Bold", 24)
#         pdf.drawCentredString(width / 2, height - 100, "Certificate of Appreciation")

#         # Recipient's Name
#         pdf.setFont("Times-Bold", 22)
#         pdf.drawCentredString(width / 2, height - 200, name)

#         # Message
#         pdf.setFont("Times-Roman", 14)
#         pdf.drawCentredString(width / 2, height - 250, "Thank you for your generous hair donation.")

#         # Signature
#         pdf.line(width / 2 - 60, height - 350, width / 2 + 60, height - 350)
#         pdf.drawCentredString(width / 2, height - 370, "Here Hope Organization")

#         # Save and return PDF
#         pdf.showPage()
#         pdf.save()
#         buffer.seek(0)

#         response = HttpResponse(buffer, content_type="application/pdf")
#         response["Content-Disposition"] = f'attachment; filename="{name}_Certificate.pdf"'
#         return response

#     return render(request, "certificate.html")

# Certificate Generator View
# def generate_certificate(request):
#     if request.method == "POST":
#         name = request.POST.get("name", "").strip()
#         if not name:
#             return HttpResponse("Please enter your name.")

#         # Create PDF in memory
#         buffer = io.BytesIO()
#         pdf = canvas.Canvas(buffer, pagesize=letter)
#         width, height = letter

#         # Background Color
#         pdf.setFillColor(HexColor("#f7f7f7"))
#         pdf.rect(0, 0, width, height, fill=True, stroke=False)

#         # Border
#         pdf.setStrokeColor(HexColor("#FF9800"))  # Orange border
#         pdf.setLineWidth(10)
#         pdf.rect(30, 30, width - 60, height - 60)

#         # Title
#         pdf.setFont("Helvetica-Bold", 30)
#         pdf.setFillColor(HexColor("#FF5722"))  # Deep Orange
#         pdf.drawCentredString(width / 2, height - 100, "Certificate of Appreciation")

#         # Logo (Optional - Place Your Logo in static/ folder)
#         logo_path = "static/logo.png"
#         try:
#             pdf.drawImage(logo_path, width / 2 - 50, height - 180, 100, 100, mask="auto")
#         except:
#             pdf.setFont("Helvetica", 12)
#             pdf.setFillColor(HexColor("#000000"))
#             pdf.drawCentredString(width / 2, height - 170, "[Hair Hope Logo]")

#         # Recipient's Name
#         pdf.setFont("Helvetica-Bold", 24)
#         pdf.setFillColor(HexColor("#333333"))
#         pdf.drawCentredString(width / 2, height - 250, f"{name}")

#         # Thank You Message
#         pdf.setFont("Times-Roman", 16)
#         pdf.setFillColor(HexColor("#000000"))
#         text_lines = [
#             "We, at Hair Hope, sincerely appreciate your",
#             "kindness and generosity in donating your hair.",
#             "Your contribution will help bring a smile to someone's face.",
#             "This act of kindness reflects your noble heart.",
#             "Thank you for making the world a better place!"
#         ]

#         y_position = height - 300
#         for line in text_lines:
#             pdf.drawCentredString(width / 2, y_position, line)
#             y_position -= 30

#         # Signature
#         pdf.setFont("Helvetica-Oblique", 16)
#         pdf.drawCentredString(width / 2, height - 420, "__________")
#         pdf.drawCentredString(width / 2, height - 440, "Hair Hope Organization")

#         # Save and return PDF
#         pdf.showPage()
#         pdf.save()
#         buffer.seek(0)

#         response = HttpResponse(buffer, content_type="application/pdf")
#         response["Content-Disposition"] = f'attachment; filename="{name}_Certificate.pdf"'
#         return response

#     return render(request, "certificate.html")

def generate_certificate(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        if not name:
            return HttpResponse("Please enter your name.")

        # Create PDF in memory
        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter

        # Background Color
        pdf.setFillColor(HexColor("#f7f7f7"))
        pdf.rect(0, 0, width, height, fill=True, stroke=False)

        # Border
        pdf.setStrokeColor(HexColor("#FF9800"))  # Orange border
        pdf.setLineWidth(10)
        pdf.rect(30, 30, width - 60, height - 60)

        # Title
        pdf.setFont("Helvetica-Bold", 30)
        pdf.setFillColor(HexColor("#FF5722"))  # Deep Orange
        pdf.drawCentredString(width / 2, height - 100, "Certificate of Appreciation")

        # Get Absolute Logo Path
        logo_path = os.path.join(settings.BASE_DIR, "static", "images", "logo.png")

        # Debug: Print logo path to check if it exists
        print("Logo Path:", logo_path)

        # Draw Logo
        # if os.path.exists(logo_path):
        #     pdf.drawImage(logo_path, width / 2 - 50, height - 180, 100, 100, mask="auto")
        # else:
        #     pdf.setFont("Helvetica", 12)
        #     pdf.setFillColor(HexColor("#000000"))
        #     pdf.drawCentredString(width / 2, height - 170, "[Hair Hope Logo Not Found]")
        logo_width = 150  # Increase width
        logo_height = 100  # Increase height
        logo_x = (width - logo_width) / 2  # Centered horizontally
        logo_y = height - 230  # Move it down (lower value moves it down)

        if os.path.exists(logo_path):
              pdf.drawImage(logo_path, logo_x, logo_y, logo_width, logo_height, mask="auto")
        else:
              pdf.setFont("Helvetica", 12)
              pdf.setFillColor(HexColor("#000000"))
              pdf.drawCentredString(width / 2, height - 200, "[Hair Hope Logo Not Found]")

        # Recipient Name
        pdf.setFont("Helvetica-Bold", 24)
        pdf.setFillColor(HexColor("#333333"))
        pdf.drawCentredString(width / 2, height - 250, f"{name}")

        # Thank You Message
        pdf.setFont("Times-Roman", 16)
        pdf.setFillColor(HexColor("#000000"))
        text_lines = [
            "We, at Hair Hope, sincerely appreciate your",
            "kindness and generosity in donating your hair.",
            "Your contribution will help bring a smile to someone's face.",
            "This act of kindness reflects your noble heart.",
            "Thank you for making the world a better place!"
        ]

        y_position = height - 300
        for line in text_lines:
            pdf.drawCentredString(width / 2, y_position, line)
            y_position -= 30

        # Signature
        pdf.setFont("Helvetica-Oblique", 16)
        pdf.drawCentredString(width / 2, height - 420, "__________")
        pdf.drawCentredString(width / 2, height - 440, "Hair Hope Organization")

        # Save and return PDF
        pdf.showPage()
        pdf.save()
        buffer.seek(0)

        response = HttpResponse(buffer, content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="{name}_Certificate.pdf"'
        return response

    return render(request, "certificate.html")
