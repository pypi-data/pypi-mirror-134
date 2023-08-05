# Implementação de uma biblioteca para o algoritmo Gale-Shapley

> Fork do projeto ["_matching_"](https://github.com/daffidwilde/matching) de _Henry Wilde_ com modificações na API e inclusões de opções.

## COMO USAR

Definir as listas com elementos que serão pareados e as preferências de cada elemento de cada lista relativas aos elementos da outra lista:

```python
    from galeshapley import Player

    comerciantes = [
        Player(name='Cunha SA'),
        Player(name='Vieira SA'),
        Player(name='Lineu SA'),
        Player(name='Loubach SA'),
    ]

    influenciadores = [
        Player(name='Gildárcio'),
        Player(name='Shigemura'),
        Player(name='Henrique'),
        Player(name='Jean'),
    ]

    cunha, vieira, lineu, loubach = comerciantes
    gildarcio, shigemura, henrique, jean = influenciadores

    cunha.set_prefs([gildarcio, shigemura, henrique, jean])
    vieira.set_prefs([jean, shigemura, gildarcio, henrique])
    lineu.set_prefs([shigemura, henrique, gildarcio, jean])
    loubach.set_prefs([shigemura, henrique, gildarcio, jean])
    
    gildarcio.set_prefs([cunha, vieira, lineu, loubach])
    shigemura.set_prefs([loubach, lineu, cunha, vieira])
    henrique.set_prefs([cunha, loubach, vieira, lineu])
    jean.set_prefs([vieira, cunha, loubach, lineu])
```

Obter os melhores pares de acordo com o algoritmo:

```python
    from galeshapley.games import StablePairing

    game = StablePairing(comerciantes, influenciadores)
    resultado = game.solve()
```

> Obs.: _O algoritmo de Gale-Shapley retorna uma das soluções ótimas possíveis_


## REFERÊNCIAS

1. Gale, David, and Lloyd S. Shapley. "College admissions and the stability of marriage." The American Mathematical Monthly 69.1 (1962): 9-15.
2. Wilde, Henry, Vincent Knight, and Jonathan Gillard. "Matching: A Python library for solving matching games." Journal of Open Source Software 5.48 (2020): 2169.