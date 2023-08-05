#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


import re
import json
from pycoin.key import Key
from pycoin.tx.Tx import Tx
from pycoin.serialize import b2h, h2b, b2h_rev, h2b_rev
from pycoin.tx.script import tools
from pycoin.encoding import bitcoin_address_to_hash160_sec
from pycoin.encoding import wif_to_secret_exponent
from pycoin.tx.pay_to import build_hash160_lookup
from pycoin.tx.TxOut import TxOut
from pycoin.tx.TxIn import TxIn                                                  


class InvalidInput(Exception): pass


def tx(rawtx):
    return Tx.tx_from_hex(rawtx)


def signedtx(rawtx):
    # FIXME validate tx is signed
    return Tx.tx_from_hex(rawtx)


def unsignedtx(rawtx):
    # FIXME validate tx is unsigned
    return Tx.tx_from_hex(rawtx)


def binary(hexdata):
    return h2b(hexdata)


def integer(number):
    return int(number)


def flag(flag):
    return bool(flag)


def positiveinteger(number):
    number = int(number)
    if number < 0:
        raise InvalidInput("Integer may not be < 0!")
    return number


def txid(txhash):
    return h2b_rev(txhash)


def address(address):
    return address # TODO sanitize


def txin(txhash, index):
    txhash = txid(txhash)
    index = positiveinteger(index)
    return TxIn(txhash, index)


def txout(testnet, targetaddress, value):
    testnet = flag(testnet)
    targetaddress = address(targetaddress)
    value = positiveinteger(value)
    prefix = b'\x6f' if testnet else b"\0"
    hash160 = b2h(bitcoin_address_to_hash160_sec(targetaddress, prefix))
    script_text = "OP_DUP OP_HASH160 %s OP_EQUALVERIFY OP_CHECKSIG" % hash160
    script_bin = tools.compile(script_text)
    return TxOut(value, script_bin)


def txins(jsondata):
    data = json.loads(jsondata)
    return map(lambda x: txin(x['txid'], x['index']), data)


def txouts(testnet, jsondata):
    data = json.loads(jsondata)
    return map(lambda x: txout(testnet, x['address'], x['value']), data)


def nulldatatxout(hexdata):
    data = binary(hexdata)
    if len(data) > 40:
        raise Exception("Data exceeds maximum of 40 bytes!")
    script_text = "OP_RETURN %s" % b2h(data)
    script_bin = tools.compile(script_text)
    return TxOut(0, script_bin)


def secretexponents(testnet, jsondata):
    wifs = json.loads(jsondata)
    valid_prefixes = [b'\xef' if testnet else b'\x80']
    return map(lambda wif: wif_to_secret_exponent(wif, valid_prefixes), wifs)


