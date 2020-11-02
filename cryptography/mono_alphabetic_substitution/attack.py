def get_char_frequencies(encrypted_text):
    frequency_char_object = {}
    for char in encrypted_text:
        if ord(char) != 32:
            if char in frequency_char_object:
                frequency_char_object[char] += 1
            else:
                frequency_char_object[char] = 1

    return sorted(frequency_char_object.items(), key=lambda item: item[1], reverse=True)


encrypted_text = """ZMYL RFA OQXXGR-FMJA

QJGUA YQP XADGLLGLD RM DAR TAOW RGOAZ MC PGRRGLD XW FAO PGPRAO ML RFA XQLI, QLZ MC FQTGLD LMRFGLD RM ZM: MLUA MO RYGUA PFA FQZ EAAEAZ GLRM RFA XMMI FAO PGPRAO YQP OAQZGLD, XSR GR FQZ LM EGURSOAP MO UMLTAOPQRGMLP GL GR, "QLZ YFQR GP RFA SPA MC Q XMMI," RFMSDFR QJGUA, "YGRFMSR EGURSOAP MO UMLTAOPQRGMLP?"

PM PFA YQP UMLPGZAOGLD GL FAO MYL KGLZ (QP YAJJ QP PFA UMSJZ, CMO RFA FMR ZQW KQZA FAO CAAJ TAOW PJAAEW QLZ PRSEGZ) YFARFAO RFA EJAQPSOA MC KQIGLD Q ZQGPW-UFQGL YMSJZ XA YMORF RFA ROMSXJA MC DARRGLD SE QLZ EGUIGLD RFA ZQGPGAP, YFAL PSZZALJW Q YFGRA OQXXGR YGRF EGLI AWAP OQL UJMPA XW FAO."""

# 1. get char frequency
frequencies = get_char_frequencies(encrypted_text)
#print(frequencies)

# 1. Analyse frequency (only letters)
# 'A'  =>  58
# 'R'  =>  42
# 'G'  =>  41
# 'M'  =>  38
# 'L'  =>  36
# 'F'  =>  33
# 'Q'  =>  32
# 'P'  =>  32
# 'O'  =>  27
# 'Z'  =>  22
# 'Y'  =>  15
# 'X'  =>  13
# 'J'  =>  13
# 'U'  =>  13
# 'D'  =>  13
# 'S'  =>  13
# 'E'  =>  10
# 'W'  =>  9
# 'C'  =>  7
# 'I'  =>  6
# 'T'  =>  5
# 'K'  =>  3
# based on 'https://en.wikipedia.org/wiki/Letter_frequency' the mosts are
# 'e' and 'a'

# 2. findings
# 'A' and 'R' are occure the most
# Q is either 'i' or 'a'
# replace 'A' => 'e'

encrypted_text = encrypted_text.replace("A", "\033[33me\033[0m")
# print(encrypted_text)

# 3. 'RFe' looks interesting 
# replace 'R' with 't' and 'F' with 'h'. maybe we have 'the' found?

encrypted_text = encrypted_text.replace("R", "\033[33mt\033[0m")
encrypted_text = encrypted_text.replace("F", "\033[33mh\033[0m")
# print(encrypted_text)


# 4. Okay. Interessting
"""
ZMYL the OQXXGt-hMJe

QJGUe YQP XeDGLLGLD tM Det TeOW tGOeZ MC PGttGLD XW heO PGPteO ML the XQLI, QLZ MC hQTGLD LMthGLD tM ZM: MLUe MO tYGUe Phe hQZ EeeEeZ GLtM the XMMI heO PGPteO YQP OeQZGLD, XSt Gt hQZ LM EGUtSOeP MO UMLTeOPQtGMLP GL Gt, "QLZ YhQt GP the SPe MC Q XMMI," thMSDht QJGUe, "YGthMSt EGUtSOeP MO UMLTeOPQtGMLP?"

PM Phe YQP UMLPGZeOGLD GL heO MYL KGLZ (QP YeJJ QP Phe UMSJZ, CMO the hMt ZQW KQZe heO CeeJ TeOW PJeeEW QLZ PtSEGZ) YhetheO the EJeQPSOe MC KQIGLD Q ZQGPW-UhQGL YMSJZ Xe YMOth the tOMSXJe MC DettGLD SE QLZ EGUIGLD the ZQGPGeP, YheL PSZZeLJW Q YhGte OQXXGt YGth EGLI eWeP OQL UJMPe XW heO.
"""
# after running step 3 we have some interesting occurences.
# 'YhetheO' => whether ? 
# 'heO' => her ?
# 'Phe' => she ?

# let's start with 'heO' and 'YhetheO' => whether

encrypted_text = encrypted_text.replace("O", "\033[33mr\033[0m")
encrypted_text = encrypted_text.replace("Y", "\033[33mw\033[0m")
# print(encrypted_text)


"""
ZMwL the rQXXGt-hMJe

QJGUe wQP XeDGLLGLD tM Det TerW tGreZ MC PGttGLD XW her PGPter ML the XQLI, QLZ MC hQTGLD LMthGLD tM ZM: MLUe Mr twGUe Phe hQZ EeeEeZ GLtM the XMMI her PGPter wQP reQZGLD, XSt Gt hQZ LM EGUtSreP Mr UMLTerPQtGMLP GL Gt, "QLZ whQt GP the SPe MC Q XMMI," thMSDht QJGUe, "wGthMSt EGUtSreP Mr UMLTerPQtGMLP?"

PM Phe wQP UMLPGZerGLD GL her MwL KGLZ (QP weJJ QP Phe UMSJZ, CMr the hMt ZQW KQZe her CeeJ TerW PJeeEW QLZ PtSEGZ) whether the EJeQPSre MC KQIGLD Q ZQGPW-UhQGL wMSJZ Xe wMrth the trMSXJe MC DettGLD SE QLZ EGUIGLD the ZQGPGeP, wheL PSZZeLJW Q whGte rQXXGt wGth EGLI eWeP rQL UJMPe XW her.
"""

# 5. Going deeper
# after running step 4 we have some interesting occurences.
# 'wMrth' => worth ? 
# 'wheL' => when ?
encrypted_text = encrypted_text.replace("M", "\033[33mo\033[0m")
encrypted_text = encrypted_text.replace("L", "\033[33mn\033[0m")
# print(encrypted_text)

"""
Zown the rQXXGt-hoJe

QJGUe wQP XeDGnnGnD to Det TerW tGreZ oC PGttGnD XW her PGPter on the XQnI, QnZ oC hQTGnD nothGnD to Zo: onUe or twGUe Phe hQZ EeeEeZ Gnto the XooI her PGPter wQP reQZGnD, XSt Gt hQZ no EGUtSreP or UonTerPQtGonP Gn Gt, "QnZ whQt GP the SPe oC Q XooI," thoSDht QJGUe, "wGthoSt EGUtSreP or UonTerPQtGonP?"

Po Phe wQP UonPGZerGnD Gn her own KGnZ (QP weJJ QP Phe UoSJZ, Cor the hot ZQW KQZe her CeeJ TerW PJeeEW QnZ PtSEGZ) whether the EJeQPSre oC KQIGnD Q ZQGPW-UhQGn woSJZ Xe worth the troSXJe oC DettGnD SE QnZ EGUIGnD the ZQGPGeP, when PSZZenJW Q whGte rQXXGt wGth EGnI eWeP rQn UJoPe XW her.
"""

# 6. Nice. First guessing parts
# 'Zown the rQXXGt-hoJe' => 'down the rabbit-whole' ? let's replace
encrypted_text = encrypted_text.replace("Q", "\033[33ma\033[0m")
encrypted_text = encrypted_text.replace("X", "\033[33mb\033[0m")
encrypted_text = encrypted_text.replace("Z", "\033[33md\033[0m")
encrypted_text = encrypted_text.replace("G", "\033[33mi\033[0m")
encrypted_text = encrypted_text.replace("J", "\033[33ml\033[0m")
# print(encrypted_text)


"""
down the rabbit-hole

aliUe waP beDinninD to Det TerW tired oC PittinD bW her PiPter on the banI, and oC haTinD nothinD to do: onUe or twiUe Phe had EeeEed into the booI her PiPter waP readinD, bSt it had no EiUtSreP or UonTerPationP in it, "and what iP the SPe oC a booI," thoSDht aliUe, "withoSt EiUtSreP or UonTerPationP?"

Po Phe waP UonPiderinD in her own Kind (aP well aP Phe UoSld, Cor the hot daW Kade her Ceel TerW PleeEW and PtSEid) whether the EleaPSre oC KaIinD a daiPW-Uhain woSld be worth the troSble oC DettinD SE and EiUIinD the daiPieP, when PSddenlW a white rabbit with EinI eWeP ran UloPe bW her.
"""
# 7. Bingo
# 'aliUe' => 'alice' ?
# 'waP' => 'was' ?
# 'beDinninD' => beginning ?
encrypted_text = encrypted_text.replace("U", "\033[33mc\033[0m")
encrypted_text = encrypted_text.replace("P", "\033[33ms\033[0m")
encrypted_text = encrypted_text.replace("D", "\033[33mg\033[0m")
# print(encrypted_text)

"""
down the rabbit-hole

alice was beginning to get TerW tired oC sitting bW her sister on the banI, and oC haTing nothing to do: once or twice she had EeeEed into the booI her sister was reading, bSt it had no EictSres or conTersations in it, "and what is the Sse oC a booI," thoSght alice, "withoSt EictSres or conTersations?"

so she was considering in her own Kind (as well as she coSld, Cor the hot daW Kade her Ceel TerW sleeEW and stSEid) whether the EleasSre oC KaIing a daisW-chain woSld be worth the troSble oC getting SE and EicIing the daisies, when sSddenlW a white rabbit with EinI eWes ran close bW her.
"""

# 8. Bingo-Bingo
# 'bW' => 'by' ?
# 'oC' => 'of' ?
# 'banI' => 'bank' ?
# 'haTing' => 'having' ?
encrypted_text = encrypted_text.replace("W", "\033[33my\033[0m")
encrypted_text = encrypted_text.replace("C", "\033[33mf\033[0m")
encrypted_text = encrypted_text.replace("I", "\033[33mk\033[0m")
encrypted_text = encrypted_text.replace("T", "\033[33mv\033[0m")
# print(encrypted_text)

"""
down the rabbit-hole

alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had EeeEed into the book her sister was reading, bSt it had no EictSres or conversations in it, "and what is the Sse of a book," thoSght alice, "withoSt EictSres or conversations?"

so she was considering in her own Kind (as well as she coSld, for the hot day Kade her feel very sleeEy and stSEid) whether the EleasSre of Kaking a daisy-chain woSld be worth the troSble of getting SE and Eicking the daisies, when sSddenly a white rabbit with Eink eyes ran close by her.
"""

# 9. Final
# we have the folling letter left: 'E','S','K'
# 'sSddenly' => suddenly ; S => u then e => s, then k => m
encrypted_text = encrypted_text.replace("S", "\033[33mu\033[0m")
encrypted_text = encrypted_text.replace("E", "\033[33ms\033[0m")
encrypted_text = encrypted_text.replace("K", "\033[33mm\033[0m")
print(encrypted_text)