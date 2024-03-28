class Category:
    def __init__(self, category):
        ### Initiate the class instance with no balance and empty ledger
        self.category = category
        self.balance = 0
        self.ledger = []

    def __repr__(self):
        ### Change how the object is printed as required
        temp = (30 - len(self.category)) // 2
        output = '*' * temp
        output += self.category
        temp = 30 - len(output)
        output += '*' * temp
        output += '\n'

        # Iterate through the ledger list
        for ledger in self.ledger:
            # Format the amount with 2 decimal places
            amount = format(ledger['amount'], '.2f')

            # Format the description to a maximum of 23 characters
            description = ledger['description']
            if (len(description) > 23):
                description = description[0:23]

            # Put description and amount to a row; amount is right-aligned
            output += description
            temp = 30 - len(description) - len(amount)
            output += ' ' * temp

            output += amount
            output += '\n'

        # Add the balance
        amount = format(self.balance, '.2f')
        output += "Total: " + amount
        
        return output

    def deposit(self, amount, description=''):
        # Add deposit entry to the ledger
        ledgerEntry = {
            "amount": amount,
            "description": description
        }
        self.ledger.append(ledgerEntry)

        # Update the balance
        self.balance += amount

    def withdraw(self, amount, description=''):
        # Check if the balance is sufficient for withdrawal
        if not self.check_funds(amount):
            return False

        # Add the withdrawal entry to the ledger
        ledgerEntry = {
            "amount": -amount,
            "description": description
        }
        self.ledger.append(ledgerEntry)

        # Update the balance
        self.balance -= amount

        # Indicate the status of the withdrawal
        return True

    def get_balance(self):
        # Obtain the balance
        return self.balance

    def transfer(self, amount, destination):
        # Check if the balance is sufficient for transfer
        if not self.check_funds(amount):
            return False

        # Withdraw from the balance for the transfer
        msg = f"Transfer to {destination.category}"
        self.withdraw(amount, msg)

        # Deposit the withdrawn amount to the destination
        msg = f"Transfer from {self.category}"
        destination.deposit(amount, msg)

        # Indicate the status of the transfer
        return True

    def check_funds(self, amount):
        # Check if the balance if sufficient for withdrawal or transfer
        return self.balance >= amount

def create_spend_chart(categories):
    # Create a list of rows, with the first entry being a fixed title
    rows = ['Percentage spent by category']

    # Temporary holders for spending categories and spent amount
    columns = {}
    dictKeys = []

    # Obtain the number of rows displaying the x-axis
    nameMaxSize = 0

    # Obtain the total amount of spending; populate the 2 temporary holders
    spending_all = 0
    for instance in categories:
        name = instance.category
        totalSpent = 0
        for entry in instance.ledger:
            if entry['amount'] < 0:
                totalSpent -= entry['amount']
        spending_all += totalSpent
        
        columns.update({name: totalSpent})
        dictKeys.append(name)

        if len(name) > nameMaxSize:
            nameMaxSize = len(name)

    # Convert the spent amount of each category to percentage, rounded down accordingly
    for key in dictKeys:
        columns[key] = ((columns[key] * 100) / spending_all) // 10 * 10

    # Loop through the charting region
    row = 100
    while row >= 0:
        # y-axis part displaying percentile
        temp = str(row)
        if len(temp) < 3:
            temp = ' ' * (3 - len(temp)) + temp
        temp += '| '

        # Charting part containing columns
        for key in dictKeys:
            if row <= columns[key]:
                temp += 'o'
            else:
                temp += ' '
            temp += ' ' * 2

        rows.append(temp)
        row -= 10

    # Horizontal line below the charting region
    temp = ' ' * 4
    temp += '-' * (len(rows[-1]) - 4)
    rows.append(temp)

    # x-axis
    for index in range(nameMaxSize):
        temp = ' ' * 4
        for key in dictKeys:
            if index >= len(key):
                temp += ' ' * 3
            else:
                temp += ' ' + key[index] + ' '

        temp += ' '
        rows.append(temp)

    # Put the rows into a string for function return
    temp = ''
    for index in range(len(rows)):
        temp += rows[index]
        if index == (len(rows) - 1):
            pass
        elif index < (len(rows) - 1):
            temp += '\n'
        else:
            temp += ' '

    # Return the complete chart
    return temp

if __name__ == '__main__':
    food = Category("Food")
    clothing = Category("Clothing")
    auto = Category("Auto")
    house = Category("House")

    food.deposit(1000, "deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")

    clothing.deposit(500, "deposit")
    clothing.withdraw(5, "new shirt")
    clothing.withdraw(15.89, "new shoes")

    auto.deposit(100, "deposit")
    auto.withdraw(2.45, "car wash")
    auto.withdraw(50, "maintenance")

    house.deposit(10, "deposit")
    house.transfer(10, food)
    house.transfer(10, auto)
    
    print(f'{food}')
    print(f'\n{clothing}')
    print(f'\n{auto}')
    print(f'\n{house}')

    print(f'\n\n{create_spend_chart([food, clothing, auto, house])}')