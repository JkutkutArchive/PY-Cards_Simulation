from .card import Card

class SpanishCard(Card):
    SUIT = {
        "OROS": 0,
        "COPAS": 1,
        "ESPADAS": 2,
        "BASTOS": 3
    }
    SUITNAME = ["Oros", "Copas", "Espadas", "Bastos"]
    RANK = {
        "MIN": 1,
        "MAX": 12
    }
    RANKNAME = {
        1: "As",
        10: "Sota",
        11: "Caballo",
        12: "Rey"
    }