#digite seu faturamento do mês
faturamentoMes = input('digite o seu faturamento do mês')
Metadomes = input('digite a sua meta do mês')

int_faturamentoMes = int(faturamentoMes)
int_Metadomes = int(Metadomes)

if int_faturamentoMes >= int_Metadomes: 
        print('sua meta foi batida')

elif int_faturamentoMes < int_Metadomes:
    print('sua meta não foi batida')

else:
        print('digite corretamente por favor')
