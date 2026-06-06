
mots = ["bonjour", "chat", "python", "clé", "serveur"]

mots_dict = {mot:len(mot) for mot in mots if len(mot) > 4}

print(mots_dict)


alerts = ["ERROR", "info", "ERROR", "warning", "INFO", "warning"]

alerts_set_cleaned = {mot.upper() for mot in alerts}

print(alerts_set_cleaned)


liste = [1500, 2048, 800, 4096, 300]

# mocha : ok
# frappe : gris claire nul
# machiato plus foncé que mocha  
total = sum(    ( x for x in liste if x > 1000    )    )

print(total)

