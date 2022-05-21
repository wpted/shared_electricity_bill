from fpdf import FPDF
from bill import Bill


class PDFReport:
    """
    Creates a Pdf file that contains the results of the shared bill.
    """

    def __init__(self, filename: str):
        self.filename = filename

    def generate(self, bill: Bill, flatmate_list: list) -> None:
        """
        Generate a pdf file with the passed in bill and flatmate list
        :param bill: Bill
        :param flatmate_list: List
        :return: None
        """
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=100, h=40, ln=1, align="c", txt="Shared Electricity Bill")


        # Insert Period
        pdf.cell(w=100, h=40, txt="period:")
        pdf.cell(w=150, h=40, txt=bill.period, ln=1)

        # Insert Flatmate
        for flatmate in flatmate_list:
            pdf.cell(w=100, h=40, txt=flatmate.name)
            pdf.cell(w=150, h=40, ln=1, txt=str(flatmate.pays(bill, flatmate_list)))

        pdf.output(self.filename)
