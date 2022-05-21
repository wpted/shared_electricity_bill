from flatmate import Flatmate
from bill import Bill
from pdf_report import PDFReport

amount = float(input("Enter the electricity bill amount: "))
period = input("Enter the time period(ex.March 2021): ").capitalize()

bill_to_share = Bill(amount=amount, period=period)
stop_input = False
flatmate_list = []
while not stop_input:
    name = input("Enter a name: ").capitalize()
    days = int(input("Enter the days stayed within the house: "))
    flatmate = Flatmate(name=name, days_in_house=days)
    flatmate_list.append(flatmate)


    continue_input = input("Do you want to insert other flatmates?(y/n):").lower()
    if continue_input == "n":
        stop_input = True



def main():
    p = PDFReport(f"{period} shared bill.pdf")
    p.generate(bill_to_share, flatmate_list=flatmate_list)



if __name__ == '__main__':
    main()
