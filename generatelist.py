a = 2015
for i in range(1, 16):
    a = a - 1
    print('''<tr>
        <th scope="row">''',a,'''</th>
        <td><a href="int1/Int1SQAPP/Int1SQAPP''', a ,'''.pdf">''',a,''' Past Paper</a></td>
        <td><a href="int1/Int1JABchemMsch/Int1JABchemMsch''',a,'''.pdf">JABchem Solutions</a></td>
        <td><a href="int1/Int1SQAMsch/Int1SQAMsch''',a,'''.pdf">SQA Solutions</a></td>
</tr>''', sep='')
