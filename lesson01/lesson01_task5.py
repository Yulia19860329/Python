revenue = int(input("Enter revenue:"))
costs = int(input("Enter costs:"))
if revenue > costs:
     print("Revenue is more than costs")
     net_revenue = revenue - costs
     profitability = net_revenue / revenue
     print("Great profit")
     staff = int(input("Enter number of employees:"))
     profitability_per_employee = float(profitability / staff)
else:
     print("The company operates at a loss")