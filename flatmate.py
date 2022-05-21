from bill import Bill


class Flatmate:
    """
    Creates an object who needs to share the bill
    """

    def __init__(self, name: str, days_in_house: int):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill: Bill, *args) -> float:
        """
        Returns the weighted amount a person has to pay.
        :param bill: A Bill object
        :param args: A list of Flatmate objects.
        :return: float
        """
        total_amount_of_days = self.days_in_house
        for flatmate in args:
            total_amount_of_days += flatmate.days_in_house
        weight = self.days_in_house / total_amount_of_days
        return bill.amount * weight
