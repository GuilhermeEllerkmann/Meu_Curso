# Maria pegou um emprestimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o emprestimo foi
# 20/12/2020 e o vencimento de cada parcela
# e no dia 20 de cada mes.
# - Crie a data do emprestimo
# - crie a data do final do emprestimo
# - mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta

fmt3 = '%d/%m/%Y'
data_start = datetime.strptime('2020-12-20', '%Y-%m-%d')
data_end = datetime.strptime('2025-12-20', '%Y-%m-%d')


def show_all_parcelas(ano_atual, ano_final, loan_value, years_to_divide):
    print(f'{ano_atual.day}/{ano_atual.month}/{ano_atual.year} R${loan_value}')
    amount_of_parcelas = years_to_divide * 12
    parcela_price = loan_value / amount_of_parcelas

    while True:
        next_month = ano_atual + relativedelta(months=1)
        new_value_parcela = loan_value - parcela_price
        print(
            f'{next_month.day}/{next_month.month}/{next_month.year}/'
            f' Valor atual restante =  R${new_value_parcela:,.2f}'
            )
        ano_atual = next_month
        loan_value = new_value_parcela
        if next_month == ano_final:
            break
        else:
            continue


show_all_parcelas(data_start, data_end, 1000000, 5)
