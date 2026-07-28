from decimal import Decimal


def calcular_preco_total_pote(pote):
    preco_embalagem = pote.embalagem.preco if pote.embalagem else Decimal("0.00")
    preco_coberturas = sum(
        (cobertura.preco for cobertura in pote.cobertura.all()),
        Decimal("0.00"),
    )
    preco_sabores = Decimal("0.00")

    for selecao_sabor in pote.pote.all():
        preco_sabor = selecao_sabor.sabor.tipo.preco
        quantidade_bolas = selecao_sabor.quantidade_bolas
        preco_sabores += preco_sabor * quantidade_bolas

    total_pote = preco_embalagem + preco_coberturas + preco_sabores
    quantidade = pote.quantidade or 0
    return total_pote * quantidade


def calcular_preco_total_sacola(sacola):
    sacola_total = sum(
        (calcular_preco_total_pote(pote) for pote in sacola.potes.all()),
        Decimal("0.00"),
    )
    sacola.preco = sacola_total
    sacola.save(update_fields=["preco"])
    return sacola_total