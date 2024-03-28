def arithmetic_arranger(problems, show_answers=False):
    ### First condition: number of problems must not exceed 5
    if len(problems) > 5:
        problems = 'Error: Too many problems.'
    else:
        # Prepare the rows:
        # show_answer is False: first operands, operators with second operands, and dash lines
        # show_answer is True: fourth row showing answers
        row = [''] * 3
        if show_answers:
            row.append('')

        # Iterate through problem list
        for index, problem in enumerate(problems):
            # Initiate temporary holder for operands
            operands = None

            ### Second condition: only addition and subtraction are valid
            # Obtain the operator of the problem being processed
            operator = problem.find('+')
            if -1 == operator:
                operator = problem.find('-')
                if -1 == operator:
                    return "Error: Operator must be '+' or '-'."
                else:
                    operator = '- '
                    operands = problem.split(' - ')
            else:
                operator = '+ '
                operands = problem.split(' + ')

            ### Third condition: Only numeric operand inputs are allowed
            if not (operands[0].isnumeric() and operands[1].isnumeric()):
                return "Error: Numbers must only contain digits."

            ### Fourth condition: Numbers cannot be more than four digits
            if (len(operands[0]) > 4 or len(operands[1]) > 4):
                return "Error: Numbers cannot be more than four digits."

            # Temporary holder for the part of each row from the problem being processed
            rowTemp = [None] * 3

            # First-row string of each problem always starts with 2 space characters
            rowTemp[0] = ' ' * 2

            # Populate rowTemp with suitable strings from the problem being processed
            # The strings are to contain proper spacing
            if len(operands[0]) == len(operands[1]):
                rowTemp[0] += operands[0]
                rowTemp[1] = operator + operands[1]
            elif len(operands[0]) > len(operands[1]):
                sizeDif = len(operands[0]) - len(operands[1])
                rowTemp[0] += operands[0]
                rowTemp[1] = operator + ' ' * sizeDif + operands[1]
            else:
                sizeDif = len(operands[1]) - len(operands[0])
                rowTemp[0] += ' ' * sizeDif + operands[0]
                rowTemp[1] = operator + operands[1]

            # Dash line for each problem
            rowTemp[2] = '-' * len(rowTemp[1])

            # The 4th string from the problem being processed for the 4th row (if any)
            if show_answers:
                # Calculate the result of the input problem
                result = int(operands[0]) + int(operands[1])
                if '- ' == operator:
                    result = int(operands[0]) - int(operands[1])

                # Convert the result to string and add to the temporary holder
                result = str(result)
                result = ' ' * (len(rowTemp[2]) - len(result)) + result
                rowTemp.append(result)

            # Update each string element of row list
            for i in range(len(rowTemp)):
                row[i] += rowTemp[i]
                if index < len(problems) - 1:
                    row[i] += ' ' * 4

        # Merge the list to form a single string for output
        problems = '\n'.join(row)        
    return problems

if __name__ == '__main__':
    print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
    print(f'\n{arithmetic_arranger(["32 + 1412", "5 - 2", "45 - 493", "123 + 49"], True)}')