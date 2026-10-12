base_tariff = 264
tariff_step = 20
debt_history = {
    "A01": [0, 800, 1600, 2500],
    "A02": [1000, 1600, 2200, 0],
    "A03": [500, 1100, 700, 900],
    "A04": [0, 0, 0, 0],
}

total_debt = 0

for apt in sorted(debt_history.keys()):
    history = debt_history[apt]
    current_tariff = base_tariff
    
    if len(history) > 1:
        for i in range(1, len(history)):
            prev_debt = history[i-1]
            curr_debt = history[i]
            
            # Борг повністю погашено
            if curr_debt == 0 and prev_debt > 0:
                current_tariff = base_tariff
            
            # Відбулася часткова оплата
            elif curr_debt < prev_debt and curr_debt > 0:
                current_tariff -= tariff_step
                if current_tariff < base_tariff:
                    current_tariff = base_tariff
            
            # Борг не було зменшено (збільшився або лишився незмінним)
            elif curr_debt >= prev_debt and curr_debt > 0:
                current_tariff += tariff_step
            
            # Борг був і залишається 0
            elif curr_debt == 0 and prev_debt == 0:
                pass

    current_debt = history[-1]
    total_debt += current_debt
    
    if current_debt == 0:
        status = "PAID"
    else:
        status = "OVERDUE"
        
    print(f"{apt} {current_debt} {current_tariff} {status}")

print(f"TOTAL DEBT: {total_debt}")
