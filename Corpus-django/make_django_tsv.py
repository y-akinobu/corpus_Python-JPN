import csv

with open('all.anno') as f:
  with open('all.code') as f2:
    with open('result.tsv', 'a') as f3:
      anno = csv.reader(f, delimiter='\t')
      code = csv.reader(f2, delimiter='\t')
      writer = csv.writer(f3, delimiter='\t', quotechar='\\')

      for row_anno, row_code in zip(anno, code):
        row_anno = row_anno[0]
        row_code = row_code[0]
        writer.writerow([row_code, row_anno])
