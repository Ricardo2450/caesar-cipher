from caesar_cipher.cipher import encrypt, decrypt, crack
import pytest

def test_encrypt_shift_1():
    actual = encrypt("apple", 1)
    expected = "bqqmf"
    assert actual == expected

#@pytest.mark.skip("TODO")
def test_encrypt_shift_10():
    actual = encrypt("apple", 10)
    expected = "kzzvo"
    assert actual == expected

#@pytest.mark.skip("TODO")
def test_encrypt_shift_20():
    actual = encrypt("apple", 20)
    expected = "ujjfy"
    assert actual == expected

#@pytest.mark.skip("TODO")
def test_uppercase():
    actual = encrypt("BANANA", 10)
    expected = "LKXKXK"
    assert actual == expected

#@pytest.mark.skip("TODO")
def test_with_whitespace():
    actual = encrypt("apples and bananas", 1)
    expected = "bqqmft boe cbobobt"
    assert actual == expected

#@pytest.mark.skip("TODO")
def test_with_non_alpha():
    actual = encrypt("Gimme a 1!", 1)
    expected = "Hjnnf b 1!"
    assert actual == expected

#@pytest.mark.skip("TODO")
def test_round_trip():
    original = "Gimme a 1!"
    shift = 5
    encrypted = encrypt(original, shift)
    actual = decrypt(encrypted, shift)
    expected = original
    assert actual == expected

#@pytest.mark.skip("TODO")
def test_crack_phrase():
    phrase = "It was the best of times, it was the worst of times."
    encrypted = encrypt(phrase, 10)
    actual = crack(encrypted)
    expected = phrase
    assert actual == expected

#@pytest.mark.skip("TODO")
def test_crack_nonsense():
    phrase = "Ix fhw txe fofg of ndhrl, it nad tho hndrk of allkd."
    encrypted = encrypt(phrase, 10)
    actual = crack(encrypted)
    expected = ""
    assert actual == expected


"""
def encrypt(string, shift):

    cipher = ""

    for char in string:

        new_char = char

        if new_char.isalpha():

            offset = 97 if char.islower() else 65

            new_char = chr((ord(char) + shift - offset) % 26 + offset)

        cipher += new_char

    return cipher
"""

