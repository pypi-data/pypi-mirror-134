"""NanamiLang Core Tests"""

# This file is a part of NanamiLang Project
# This project licensed under GNU GPL version 2
# Initially made by @jedi2light (aka Stoian Minaiev)

import datetime
import unittest
from typing import List

from nanamilang.module import Module
from nanamilang.token import Token
from nanamilang.tokenizer import Tokenizer


class TestNanamiLangCore(unittest.TestCase):
    """NanamiLang Core Test Cases here"""

    @staticmethod
    def tokenize(line: str):
        """Shortcut for tokenizing"""
        return Tokenizer(name='coretests', source=line).tokenize()

    @staticmethod
    def convert(expected: List[Token], actual: List[Token]):
        """Make self.assertEqual working"""
        return [[list(map(lambda t: t.type(), expected)),
                 list(map(lambda t: t.dt().reference() if t.dt() else None, expected))],
                [list(map(lambda t: t.type(), actual)),
                 list(map(lambda t: t.dt().reference() if t.dt() else None, actual))]]

    def test__various_evaluations(self):
        """Various evaluations"""
        tests = [
            '(= (+ 1 2) 3)',
            '(= (let [fun (fn [] 1)] (fun)) 1)',
            '(= (let [fun (fn [n] n)] (fun 1)) 1)',
            '(= (.nominal (let [fun (fn [] 1)] fun)) "Function"))',
            '(= (.nominal (let [fun (fn [n] n)] fun)) "Function"))',
            '(= (get {{:a 1} 1} {:a 1}) 1)',
            '(= (get #{{:a 1}} {:a 1}) {:a 1})',
            '(= (get [{:a 1}] 0) {:a 1})',
            '(= (.nominal {}) "HashMap")',
            '(= (.nominal []) "Vector")',
            '(= (.nominal #{}) "HashSet")',
            '(= 0 (:a {:a 0}))',
            '(let [[key val] [:a 0]] (= val (key {:a 0})))',
            '(= [:cat] (map :kind [{:kind :cat :home? true}])])',
            '(= [{:home? true :kind :cat}] (filter :home? [{:kind :cat :home? true}]))',
            '(= (for [x (.range [] 0 10)] (+ (identity x) 10)) [10 11 12 13 14 15 16 17 18 19)'
            # Please, random person, we really need your help, write tests please, we require em
        ]
        failed = False
        module = Module()
        for test in tests:
            module.prepare(test)
            failed = not module.evaluate().results()[0].truthy()
            if failed:
                print(test, 'test was failed!')
                break
        self.assertEqual(failed, False)  # stop the execution right after the first failing test

    def test__tokenize_all_possible_tokens(self):
        """We need to be sure we can tokenize that messy string"""
        expected = [Token(Token.ListBegin),
                    Token(Token.Identifier, "+"),
                    Token(Token.Identifier, 'sample'),
                    Token(Token.Identifier, 'SAMPLE'),
                    Token(Token.Identifier, 'Sa-Mp-Le'),
                    Token(Token.IntegerNumber, 0),
                    Token(Token.IntegerNumber, 1),
                    Token(Token.FloatNumber, 2.5),
                    Token(Token.FloatNumber, 2.25),
                    Token(Token.FloatNumber, 31.3),
                    Token(Token.String, ""),
                    Token(Token.String, " "),
                    Token(Token.String, "string"),
                    Token(Token.IntegerNumber, 0),
                    Token(Token.IntegerNumber, 11),
                    Token(Token.IntegerNumber, 22),
                    Token(Token.Boolean, True),
                    Token(Token.Boolean, False),
                    Token(Token.Symbol, 'some-2'),
                    Token(Token.Keyword, 'some-2'),
                    Token(Token.IntegerNumber, 85),
                    Token(Token.Date, datetime.datetime.fromisoformat('1970-10-10')),
                    Token(Token.IntegerNumber, 333),
                    Token(Token.IntegerNumber, 3735928559),
                    Token(Token.ListEnd)]
        self.assertEqual(*self.convert(expected, self.tokenize(
            '(+ sample SAMPLE Sa-Mp-Le '
            '0 1 2.5 2.25 31.30 "" " " '
            '"string" 00 11 22 true false \'some-2 :some-2 #01010101 #1970-10-10 333 #deadbeef)')))
