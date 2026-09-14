

tipo_de_imovel=input("digite o tipo de imóvel ex:(casa,apartamento,comercial. )")

cosumo_mensal_de_agua=float(input("digite o consumo mensal de água em metros cúbicos (m³)(número decimal.)"))
if tipo_de_imovel=="comercial":
    print("tarifa comercial aplicada-consulte o plano corporativo")
elif tipo_de_imovel=="apartamento" and cosumo_mensal_de_agua < 10:
    print(" Consumo econômico-excelente controle de água!")
elif tipo_de_imovel=="apartamento" or ("casa" and cosumo_mensal_de_agua <=25):
    print("Consumo moderado-dentro do padrão residencial")  
else:
     print("Consumo excessivo-adote medidas de economia e verifique vazamentos.")

 