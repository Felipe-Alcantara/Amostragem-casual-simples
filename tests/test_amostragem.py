"""Testes da lógica pura de amostragem (src/amostragem.py).

Usa apenas a biblioteca padrão (unittest). Para tornar o sorteio
determinístico, injeta um RNG falso onde necessário.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from amostragem import (  # noqa: E402
    amostra_casual_simples,
    amostra_sistematica,
    amostra_estratificada,
)


class RngFake:
    """RNG determinístico para teste.

    - ``sample`` devolve os ``k`` primeiros elementos da sequência.
    - ``randint`` devolve sempre o limite inferior ``a``.
    """

    def sample(self, populacao, k):
        return list(populacao)[:k]

    def randint(self, a, b):
        return a


class TestCasualSimples(unittest.TestCase):
    def test_tamanho_e_intervalo(self):
        r = amostra_casual_simples(1000, 10, rng=RngFake())
        self.assertEqual(r["tamanho_amostra"], 100)
        self.assertEqual(len(r["elementos"]), 100)
        self.assertTrue(all(1 <= e <= 1000 for e in r["elementos"]))

    def test_elementos_sem_repeticao_e_ordenados(self):
        r = amostra_casual_simples(50, 100)
        self.assertEqual(len(set(r["elementos"])), len(r["elementos"]))
        self.assertEqual(r["elementos"], sorted(r["elementos"]))

    def test_populacao_invalida(self):
        with self.assertRaises(ValueError):
            amostra_casual_simples(0, 10)
        with self.assertRaises(ValueError):
            amostra_casual_simples(-5, 10)

    def test_porcentagem_invalida(self):
        with self.assertRaises(ValueError):
            amostra_casual_simples(100, 0)
        with self.assertRaises(ValueError):
            amostra_casual_simples(100, 150)

    def test_amostra_zero(self):
        with self.assertRaises(ValueError):
            amostra_casual_simples(100, 0.5)  # int(0.5) == 0


class TestSistematica(unittest.TestCase):
    def test_intervalo_e_geracao(self):
        r = amostra_sistematica(500, 50, rng=RngFake())
        self.assertEqual(r["intervalo_int"], 10)
        self.assertEqual(r["semente"], 1)  # RngFake.randint devolve o limite inferior
        self.assertEqual(r["elementos"][0], 1)
        self.assertEqual(len(r["elementos"]), 50)

    def test_respeita_amostra_desejada(self):
        r = amostra_sistematica(100, 7)
        self.assertLessEqual(len(r["elementos"]), 7)

    def test_validacoes(self):
        with self.assertRaises(ValueError):
            amostra_sistematica(0, 5)
        with self.assertRaises(ValueError):
            amostra_sistematica(100, 0)
        with self.assertRaises(ValueError):
            amostra_sistematica(50, 100)  # amostra > população


class TestEstratificada(unittest.TestCase):
    def test_proporcoes_e_totais(self):
        r = amostra_estratificada(600, 400, 15)
        self.assertEqual(r["total"], 1000)
        self.assertAlmostEqual(r["proporcao_1"], 0.6)
        self.assertAlmostEqual(r["proporcao_2"], 0.4)
        self.assertEqual(r["amostra_1"], 90)
        self.assertEqual(r["amostra_2"], 60)
        self.assertEqual(r["total_amostra"], 150)

    def test_validacoes(self):
        with self.assertRaises(ValueError):
            amostra_estratificada(0, 400, 15)
        with self.assertRaises(ValueError):
            amostra_estratificada(600, -1, 15)
        with self.assertRaises(ValueError):
            amostra_estratificada(600, 400, 0)
        with self.assertRaises(ValueError):
            amostra_estratificada(600, 400, 101)


if __name__ == "__main__":
    unittest.main()
