bred = 10 
ice_cream = 25 
macarons = 50 
snicers = 15 
sale = 0.1 
a = input('введите что ви хотите купить : bred ,ice_cream , macarons , snicers ')
def calculate_price(line):
    if a == 'bred' :
        print(' внесите 9 гривен')
    if a == 'ice_cream' :
        print(' внесите 22.5 гривен') 
    if a == 'macarons' :
        print(' внесите 45 гривен')
    if a == 'snicers' :
        print(' внесите 13.5 гривен')
    else:
        print('етого товара нет в наличии')
calculate_price(line)
    
