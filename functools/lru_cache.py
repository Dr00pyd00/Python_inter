
from functools import lru_cache 
import time 


@lru_cache
def calcul_rect(x: int, y: int):
    time.sleep(2)
    return x * y 


print(f"premier lancement: {calcul_rect(3,8)}")
print(f"deuxieme lancement: {calcul_rect(3,8)}")
print(f"troiseme lancement: {calcul_rect(3,8)}")
print(f"premier lancement: {calcul_rect(5,5)}")
print(f"deuxieme lancement: {calcul_rect(5,5)}")
print(f"autre lancement: {calcul_rect(1,1)}")


print(calcul_rect.cache_info())

# ca donne:
# CacheInfo(hits=3, misses=3, maxsize=128, currsize=3)

# hits : 3 appels ou le res etait deja en cache 
# misses : 3 appels ou le res n'etait pas en cache 
# maxsize : taille du cache ( par defaut 129)
# currsize : nombre de res actuellement stocker 
