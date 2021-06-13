class Calculator:

    def __init__(self):
        self.__gasoline_value = 4.80
        self.__alcohol_value = 3.80
        self.__diesel_value = 3.90

    def spent_calculate(self, distance, consumption):
        if(distance <= 0 or consumption <= 0):
            raise Exception('The value received cannot be less or equal to zero')

        spent_gasoline = round(
            (distance/consumption) * self.__gasoline_value, 2)
        spent_alcohol = round(
            (distance/consumption) *self.__alcohol_value, 2)
        spent_diesel = round(
            (distance/consumption) * self.__diesel_value, 2)
        return """
        The total spent value will be:
        
        Gasoline: R$ {}
        Alcohol: R$ {}
        Diesel:  R$ {}
        """.format(
            spent_gasoline, spent_alcohol, spent_diesel
        )



