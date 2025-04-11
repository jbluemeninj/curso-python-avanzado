

def magic_function(lista_input):
    lista_output = [a[::-1] for a in lista_input]
    """    for a  in lista_input:
            if a == str(a):
                lista_output.append(a[::-1])
            else:
                continue
        return lista_output
    """
    return lista_output

A = ["Hello", "VEGETA", "1234", '<A>']
B = magic_function(A)
print(B)