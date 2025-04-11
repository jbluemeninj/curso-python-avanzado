"""
Palindromos

radar
atar a la rata
"""


def palindromo():
    str_input = input("Ingrese una frase: ")
    str_original = str_input.replace(" ", "")
    str_reverso =  str_original[::-1].replace(" ", "")

    if str_original == str_reverso:
        print("Es palindromo")
    else :
        print("No es palindromo")

if __name__ == "__main__":
    palindromo()