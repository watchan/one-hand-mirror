import sys
import os
import datetime
import subprocess

from keyhac import *


def configure(keymap):


    # 英数キーを仮想キー235に割り当てる 
    keymap.replaceKey( 102, 235 )

    # 仮想キー235にUser0キーを割り当てる
    keymap.defineModifier( 235, "User0")

    

    # グローバルKeymapオブジェクトを取得する
    keymap_global = keymap.defineWindowKeymap()

    # 左手入力用
    keymap_global[ "User0-Ctrl-T"    ] = "102"
    keymap_global[ "User0-Ctrl-G"    ] = "104"

    keymap_global[ "User0-Tab"    ] = "Return"
    keymap_global[ "User0-LCtrl-Q"    ] = "Escape"
    keymap_global[ "User0-LCtrl-R"    ] = "Back"

    keymap_global[ "User0-Q"    ] = "P"
    keymap_global[ "Shift-User0-Q"    ] = "Shift-P"

    keymap_global[ "User0-W"    ] = "O"
    keymap_global[ "Shift-User0-W"    ] = "Shift-O"

    keymap_global[ "User0-E"    ] = "I"
    keymap_global[ "Shift-User0-E"    ] = "Shift-I"

    keymap_global[ "User0-R"    ] = "U"
    keymap_global[ "Shift-User0-R"    ] = "Shift-U"

    keymap_global[ "User0-T"    ] = "Y"
    keymap_global[ "Shift-User0-T"    ] = "Shift-Y"

    keymap_global[ "User0-A"    ] = "Semicolon"
    keymap_global[ "Shift-User0-A"    ] = "Shift-Semicolon"

    keymap_global[ "User0-S"    ] = "L"
    keymap_global[ "Shift-User0-S"    ] = "Shift-L"

    keymap_global[ "User0-D"    ] = "K"
    keymap_global[ "Shift-User0-D"    ] = "Shift-K"

    keymap_global[ "User0-F"    ] = "J"
    keymap_global[ "Shift-User0-F"    ] = "Shift-J"

    keymap_global[ "User0-G"    ] = "H"
    keymap_global[ "Shift-User0-G"    ] = "Shift-H"

    keymap_global[ "User0-Z"    ] = "Slash"
    keymap_global[ "Shift-User0-Z"    ] = "Shift-Slash"

    keymap_global[ "User0-X"    ] = "Period"
    keymap_global[ "Shift-User0-X"    ] = "Shift-Period"

    keymap_global[ "User0-C"    ] = "Comma"
    keymap_global[ "Shift-User0-C"    ] = "Shift-Comma"

    keymap_global[ "User0-V"    ] = "M"
    keymap_global[ "Shift-User0-V"    ] = "Shift-M"

    keymap_global[ "User0-B"    ] = "N"
    keymap_global[ "Shift-User0-B"    ] = "Shift-N"
    
    keymap_global[ "User0-Tab"    ] = "Return"
    keymap_global[ "User0-LCtrl-Q"    ] = "Escape"
    keymap_global[ "User0-LCtrl-R"    ] = "Back"
    
    keymap_global[ "User0-1"    ] = "0"
    keymap_global[ "Shift-User0-1"    ] = "Shift-0"
 
    keymap_global[ "User0-2"    ] = "9"
    keymap_global[ "Shift-User0-2"    ] = "Shift-9"
    
    keymap_global[ "User0-3"    ] = "8"
    keymap_global[ "Shift-User0-3"    ] = "Shift-8"
    
    keymap_global[ "User0-4"    ] = "7"
    keymap_global[ "Shift-User0-4"    ] = "Shift-7"
    
    keymap_global[ "User0-LCtrl-2"    ] = "Minus"
    keymap_global[ "Shift-User0-LCtrl-2"    ] = "Shift-Minus"
    
    keymap_global[ "User0-LCtrl-3"    ] = "Plus"
    keymap_global[ "Shift-User0-LCtrl-3"    ] = "Shift-Plus"

    keymap_global[ "User0-LCtrl-4"    ] = "Yen"
    keymap_global[ "Shift-User0-LCtrl-4"    ] = "Shift-Yen"

    keymap_global[ "User0-LCtrl-W"    ] = "OpenBracket"
    keymap_global[ "Shift-User0-LCtrl-W"    ] = "Shift-OpenBracket"

    keymap_global[ "User0-LCtrl-E"    ] = "CloseBracket"
    keymap_global[ "Shift-User0-LCtrl-E"    ] = "Shift-CloseBracket"

    keymap_global[ "User0-LCtrl-S"    ] = "Quote"
    keymap_global[ "Shift-User0-LCtrl-S"    ] = "Shift-Quote"

    keymap_global[ "User0-LCtrl-D"    ] = "BackSlash"
    keymap_global[ "Shift-User0-LCtrl-D"    ] = "Shift-BackSlash"

    keymap_global[ "User0-LCtrl-X"    ] = "UnderScore"
    keymap_global[ "Shift-User0-LCtrl-X"    ] = "Shift-UnderScore"



