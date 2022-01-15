quant=int(input("сколько билетов планируете купить:"))
count=0
for i in range(1, quant+1):
   text='возраст ' + str(i) + ' клиента:'
   age = int(input (text))
   if age >25:
        count += 1390
        print ("стоимость билета 1390 рублей")
   else:
       if age>=18:
           count += 990
           print("стоимость билета 990 рублей")
       else:
           print("бесплатный билет")


print ("сумарная стоимость билетов: %s рублей" %(count))
if quant>3 and count>0:
    sale=int (count/10)
    count=count-sale
    print ("у вас 10% скидка она состовляет {} рублей итого с вас {} рублей".format(sale, count))