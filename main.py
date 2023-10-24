import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# Retrieve file list
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    # generate the dataframes
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # generate the pdf
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename= Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    print(invoice_nr)
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}")
    pdf.output(f"PDFs/{filename}.pdf")
