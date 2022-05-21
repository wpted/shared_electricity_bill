from bill import Bill


class Flatmate:
    """
    Creates an object who needs to share the bill
    """

    def __init__(self, name: str, days_in_house: int):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill: Bill, flatmate_list: list) -> float:
        """
        Returns the weighted amount a person has to pay.
        :param bill: A Bill object
        :param flatmate_list: A list of Flatmate objects.
        :return: float
        """
        all_flatmate_days_in_house = [flatmate.days_in_house for flatmate in flatmate_list]
        weight = self.days_in_house / sum(all_flatmate_days_in_house)
        return round(bill.amount * weight, 2)
