# Definindo os vetores v, w, u
v = (2, 6, 3)
w = (1, 0, 0)
u = (7, 7, 2)

# Operacoes nos vetores e criando a tupla com os resultados
result = tuple(3 * (2 * v_i - w_i) for v_i, w_i in zip(v, w))

# calculando o produto escalar e 2*u
dot_product = sum(result_i * (2 * u_i) for result_i, u_i in zip(result, u))

# Resultado
print("The result of 3*(2*v - w) ∙ 2*u is:", dot_product)
