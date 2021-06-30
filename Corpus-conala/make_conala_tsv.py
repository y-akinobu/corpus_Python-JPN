import json
import csv

with open('conala-json/conala-train.json') as f:
  with open('result.tsv', 'a') as f2:
    writer = csv.writer(f2, delimiter='\t')

    for data in json.load(f):

      code = str(data['snippet'])
      nl = str(data['rewritten_intent'])

      if not '\n' in code:
        if not nl == 'None':
          writer.writerow([code, nl])
