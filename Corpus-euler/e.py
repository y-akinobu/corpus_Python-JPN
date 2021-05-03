import csv

l = ['02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
for index in l:
  filename = 'ja-euler-lbl-tsv/euler' + index + '.tsv'
  with open(filename) as f:
    with open('euler-before.tsv', 'a') as f2:
      reader = csv.reader(f, delimiter='\t')
      writer = csv.writer(f2, delimiter='\t', quotechar='\\')

      for row in reader:
        code, doc = row[0], row[1]
        print('@@code', code)
        print('@@doc', doc)

        writer.writerow([code, doc])