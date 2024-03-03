# Definierar en klass som heter BudgetManager för att hantera budget och utgifter
class BudgetManager:
    # Initialiserare som sätter upp de grundläggande egenskaperna för klassen
    def __init__(self):
        self.budget = 0  # Startbudgeten sätts till 0
        self.expenses = {}  # Initierar en tom dictionary för att lagra utgifter

    # Metod för att sätta budgeten till ett specifikt belopp
    def set_budget(self, amount):
        self.budget = amount  # Uppdaterar klassens budgetegenskap med det angivna beloppet

    # Metod för att lägga till en utgift under en specifik kategori
    def add_expense(self, category, amount):
        # Kontrollerar om kategorin redan finns i utgifts-dictionaryn
        if category in self.expenses:
            self.expenses[category] += amount  # Lägger till beloppet till befintlig kategori
        else:
            self.expenses[category] = amount  # Skapar en ny kategori med beloppet om den inte finns

    # Metod för att beräkna och returnera den återstående budgeten
    def get_remaining_budget(self):
        # Subtraherar summan av alla utgifter från den totala budgeten och returnerar resultatet
        return self.budget - sum(self.expenses.values())

# Kodblock som körs om denna fil körs som ett huvudprogram
if __name__ == "__main__":
    manager = BudgetManager()  # Skapar en instans av BudgetManager
    manager.set_budget(1000)  # Sätter en månadsbudget till 1000
    manager.add_expense("Mat", 250)  # Lägger till en utgift på 250 under kategorin "Mat"
    remaining_budget = manager.get_remaining_budget()  # Beräknar den återstående budgeten
    # Skriver ut den återstående budgeten till konsolen
    print(f"Återstående budget: {remaining_budget}kr")
