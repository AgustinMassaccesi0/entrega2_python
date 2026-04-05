def email_valido (email):
    if  email.count('@') != 1:
        return False
    
    if email.startswith(('@', '.')):
        return False
    
    if email.endswith(('@', '.')):
        return False
    
    inicio, final = email.split('@')

    if len(inicio) < 1:
        return False
    
    if '.' not in final:
        return False
    
    dominio = final.rsplit('.', 1)[-1]
    if len(dominio) < 2:
        return False
    
    return True 
    