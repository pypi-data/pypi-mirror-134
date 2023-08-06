def class_sum(n, a, b):
    return (a+b)%n

def class_prod(n, a ,b):
    return (a*b)%n

def build_table(n, selected_operation):
    if type(n) != int:
        raise ValueError("Please pass an integer as first argument. ")
    if selected_operation in ["sum", "prod"]:
        operation = class_sum if selected_operation == 'sum' else class_prod
        table = list()

        for i in range(n):
            row = list()
            for j in range(n):
                row.append(operation(n, i, j))
            table.append(row)

        return table
    else:
        raise ValueError("Please pass a valid operation ('sum' or 'prod') as second argument.")