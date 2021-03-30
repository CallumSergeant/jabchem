a = 2
for i in range(1977, 2000):
    a = a + 1
    print('''<tr>
    <th scope="row">''', i, '''</th>
    <td>''', i, ''' Past Paper</td>
    <td><a href="H Chem Archive PP/oldoldHchem PP ''', i, '''.pdf">Past Paper</a>
    </td>
</tr>''', sep='')
