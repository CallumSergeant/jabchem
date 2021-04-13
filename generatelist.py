a = 2015
for i in range(1, 25):
    a = a - 1
    print('''<tr>
    <th scope="row">''', a, '''</th>
    <td>''', a, ''' Past Paper</td>
    <td><a href="H Chem Archive PP/oldoldHchem PP ''', a, '''.pdf">Past Paper</a>
    </td>
</tr>''', sep='')
