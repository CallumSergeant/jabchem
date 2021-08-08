a = 2013
for i in range(1, 18):
    a = a - 1
    print('''<tr>
    <th scope="row">''',a,'''</th>
    <td><a href="SGGeneralSQAPP/SGGeneralMathsSQApp''',a,'''.pdf">''',a,''' Past Paper</a></td>
    <td><a href="SGGeneralSQAMSch/SGGeneralMathsSQAmsch''',a,'''.pdf">SQA Solutions</a></td>
</tr>''', sep='')
