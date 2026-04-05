def cifrado_cesar(texto, desplazamiento):
    resultado = ''
    for char in texto:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - start + desplazamiento) %26 + start)
        else:
            resultado += char
    return resultado

