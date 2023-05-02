import funcoes

window, assets, state = funcoes.inicializa()
while funcoes.recebe_eventos(state):
        funcoes.desenha(window, assets, state)

    