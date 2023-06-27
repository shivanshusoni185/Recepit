import os

import boto3
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

from .models import Receipt


def get_receipt(request):
    if request.method == 'GET':
        receipt_no = request.GET.get('receipt_number')
        display_option = request.GET.get('display_option')

        if receipt_no:
            try:
                receipt = Receipt.objects.get(receipt_no=receipt_no)

                if display_option == 'pdf_horizontal' or display_option == 'pdf_vertical':
                    # Generate the PDF file
                    doc_filename = f"receipt_{receipt.receipt_no}.pdf"
                    doc_filepath = os.path.join(settings.MEDIA_ROOT, doc_filename)

                    doc = SimpleDocTemplate(doc_filepath, pagesize=letter)

                    elements = []

                    # Define custom styles for the PDF content
                    styles = getSampleStyleSheet()
                    header_style = styles['Heading1']
                    field_style = styles['Normal']

                    # Add content to the PDF
                    elements.append(Paragraph('Receipt Details', header_style))
                    elements.append(Spacer(1, 20))

                    if display_option == 'pdf_vertical':
                        # Create a table to contain the receipt details
                        table_data = [
                            ['Name:', receipt.name],
                            [ 'Date:', receipt.date,'Standard:', receipt.standard, 'Section:', receipt.section],
                            ['Enrollment No:', receipt.enrollment_no, 'Amount:', receipt.amount],
                            ['Received:', receipt.received, 'Status:', receipt.status],
                            ['Signature:', receipt.signature]


                        ]

                        table_style = TableStyle([
                            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('FONTSIZE', (0, 0), (-1, 0), 12),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                            ('FONTSIZE', (0, 1), (-1, -1), 10),
                            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
                            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                        ])
                        table = Table(table_data, style=table_style)

                        elements.append(table)
                    else:
                        # Create a table to contain the receipt details
                        table_data = [
                            ['Receipt Number:', receipt.receipt_no],
                            ['Name:', receipt.name],
                            ['Date:', receipt.date],
                            ['Standard:', receipt.standard],
                            ['Section:', receipt.section],
                            ['Enrollment No:', receipt.enrollment_no],
                            ['Amount:', receipt.amount],
                            ['Received:', receipt.received],
                            ['Status:', receipt.status],
                            ['Signature:', receipt.signature]
                        ]
                        table_style = TableStyle([
                            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('FONTSIZE', (0, 0), (-1, 0), 12),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                            ('FONTSIZE', (0, 1), (-1, -1), 10),
                            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
                            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                        ])
                        table = Table(table_data, style=table_style)

                        # Center the table horizontally
                        table._argW[0] = 200  # Set the first column width to 200 points

                        elements.append(table)

                    if display_option == 'pdf_horizontal':
                        doc.pagesize = landscape(letter)

                    doc.build(elements)

                    # Upload the PDF file to S3
                    s3 = boto3.client('s3',
                                      aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                      aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                                      verify=True)  # Enable SSL certificate verification

                    bucket_name = 'aitech11'  # Replace with your S3 bucket name
                    s3_filepath = f"receipts/{doc_filename}"

                    with open(doc_filepath, 'rb') as file_obj:
                        s3.upload_fileobj(file_obj, bucket_name, s3_filepath)

                    # Generate the S3 URL for the uploaded file
                    s3_url = f"https://{bucket_name}.s3.amazonaws.com/{s3_filepath}"
                    response = f"""
                                   <html>
                                   <head>
                                       <title>Admission Count</title>
                                       <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
                                       <style>
                                           .container {{
                                               display: flex;
                                               justify-content: center;
                                               align-items: center;
                                               height: 100vh;
                                           }}

                                           .container-content {{
                                               text-align: center;
                                           }}
                                       </style>
                                   </head>
                                   <body>
                                       <div class="container">
                                           <div class="container-content">
                                               <h1>Welcome to Digital Academy</h1>
                                               <div class="text-center">
                                                  <h3> PDF uploaded successfully.</h3> <a href="{s3_url}" class="btn btn-primary">Download PDF</a>
                                               </div>
                                               <div>
                                                   <div>
                                            
                                                   </div>
                                               </div>
                                           </div>
                                       </div>
                                   </body>
                                   </html>
                               """

                    return HttpResponse(response)

                    #return HttpResponse(f"PDF uploaded successfully. <a href='{s3_url}'>Download PDF</a>")
                    #return(response)

                elif display_option == 'receipt_details':
                    # Render the receipt details on receipt_details.html
                    return render(request, 'problem11/receipt_details.html', {'receipt': receipt})

            except Receipt.DoesNotExist:
                return HttpResponse('Receipt not found')

    return render(request, 'problem11/get_receipt.html')
