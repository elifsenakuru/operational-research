from pyomo.environ import NonNegativeReals, NonNegativeIntegers
from pyomo.environ import ConcreteModel, Var, Objective, Constraint, maximize, SolverFactory

# Create a model
model = ConcreteModel()

# Decision variables
model.x1 = Var(within=NonNegativeReals)
model.x2 = Var(within=NonNegativeIntegers)
model.x3 = Var(within=NonNegativeIntegers)

# Objective function
model.profit = Objective(expr=8*model.x1 + 6*model.x2 + 2*model.x3, sense=maximize)

# Constraints
model.constraint1 = Constraint(expr=6*model.x1 + 4*model.x2 + 2*model.x3 <= 14)
model.constraint2 = Constraint(expr=4*model.x1 + 2*model.x2 + 4*model.x3 <= 22)

# Solve the model
solver = SolverFactory('cbc')
result = solver.solve(model, tee=True)

# Print results
print(f"x1: {model.x1()}")
print(f"x2: {model.x2()}")
print(f"x3: {model.x3()}")
print(f"Maximum Profit: {model.profit()}")
