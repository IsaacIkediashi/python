import csv
from datetime import datetime
def main():
  try:
    class_time = datetime.now()
    products_dict = read_dictionary('CSE 111\grocery\products.csv', 0)
    with open('CSE 111\grocery\\request.csv', mode='r') as request_csv:
      reader = csv.reader(request_csv)
      next(request_csv)
      sub_total = 0
      i = 0
      print('Icy Daddy Store')
      for row_list in reader:
       if len(row_list) != 0:
        order = row_list[0]
        quantity = float(row_list[1])
        details = products_dict[order]
        name = details[0]
        price = float(details[1])
        print(f'{name}: {quantity} @ {price}')
        sub_total += price * quantity
        i += 1
      sales_tax = sub_total * 0.06
      total = sub_total + sales_tax
      print(f'Number of items: {i}')
      print(f'Subtotal: {round(sub_total, 2)}')
      print(f'Sales Tax: {round(sales_tax, 2)} ')
      print(f'Total: {round(total, 2)}')
      print(f'Thank you for shopping at Ice Daddy Goceries')
      print(f'{class_time:%c}')
  except KeyError as key_err:
   print(f'Error: {key_err}', \
         'unknown product ID in the request.csv file')

  except FileNotFoundError as not_found_err:
    print(f'Error: missing file {not_found_err}', \
          'No such file or directory: "products.csv"')


def read_dictionary(file_name, key_column_index):
  with open(file_name, mode='r') as csv_file:
   reader = csv.reader(csv_file)  
   next(reader)
   grocery_dict = {}
   
   for  row_list in reader:
     if len(row_list) != 0: 
      product = row_list[key_column_index]
      name = row_list[1]
      price = row_list[2]
      grocery_dict[product] = [name, price]
   return grocery_dict
if __name__ == '__main__':
    main()
