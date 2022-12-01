from fpdf import FPDF
pdf=FPDF()
list_of_images=["1.jpg","2.jpg"]

for i in list_of_images:
    pdf.add_page()
    pdf.image(i)
 #   pdf.image(i,x,y,w,h)
pdf.output("images.pdf","F")