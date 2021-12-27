per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=float(input("планируемая сумма взноса:"))
proc=money/100
proc_list=list(per_cent.values())
deposit = [round(i * proc,2) for i in proc_list]
print ("максимальный доход:",max(deposit))
