from pyomo.environ import ConcreteModel, Var, NonNegativeReals, Objective, Constraint, SolverFactory, maximize
from pyomo.environ import *

# Create a model
model = ConcreteModel()

# Decision variables
model.x1 = Var(within=NonNegativeReals)
model.x2 = Var(within=NonNegativeReals)
model.M = Var(within=NonNegativeReals)

# Objective function
model.profit = Objective(expr=50*model.x1 + 30*model.x2 - 2*model.M, sense=maximize)

# Constraints
model.time_constraint = Constraint(expr=1*model.M + 5*model.x1 + 2*model.x2 <= 120)
model.mp_constraint = Constraint(expr=8*model.x1 + 4*model.x2 <= model.M + 80)

# Solve the model
solver = SolverFactory('glpk')
result = solver.solve(model, tee=True)

# Print results
print(f"PCs produced (x1): {model.x1()}")
print(f"Ts produced (x2): {model.x2()}")
print(f"MPs produced (M): {model.M()}")
print(f"Maximum Profit: {model.profit()}")
