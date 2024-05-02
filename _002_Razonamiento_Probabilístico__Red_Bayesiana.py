# Importar las clases necesarias de la biblioteca pgmpy
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

# Definir la estructura de la red bayesiana
modelo = BayesianModel([('A', 'C'), ('B', 'C'), ('C', 'D')])

# Definir las distribuciones de probabilidad condicional (CPDs) para cada variable
# CPD para la variable A
cpd_A = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
# CPD para la variable B
cpd_B = TabularCPD(variable='B', variable_card=2, values=[[0.7], [0.3]])
# CPD para la variable C, que depende de las variables A y B
cpd_C = TabularCPD(variable='C', variable_card=2, 
                   values=[[0.8, 0.9, 0.4, 0.7],  # Valores de C para A=0, B=0 y A=0, B=1
                           [0.2, 0.1, 0.6, 0.3]],  # Valores de C para A=1, B=0 y A=1, B=1
                   evidence=['A', 'B'], evidence_card=[2, 2])
# CPD para la variable D, que depende de la variable C
cpd_D = TabularCPD(variable='D', variable_card=2, 
                   values=[[0.9, 0.6],  # Valores de D para C=0 y C=1
                           [0.1, 0.4]],  # Valores de D para C=0 y C=1
                   evidence=['C'], evidence_card=[2])

# Anadir las CPDs al modelo
modelo.add_cpds(cpd_A, cpd_B, cpd_C, cpd_D)

# Verificar si las CPDs son validas para el modelo
validacion = modelo.check_model()
print("El modelo es valido", validacion)

