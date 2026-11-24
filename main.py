# One Letter for Your Day — kandidat v2.
#
# Menulis tepat satu huruf, "O", ke entry.txt.
# O singkatan dari "overcaffeinated": tangan gemetar, mata terbelalak,
# espresso kelima — hari yang dijalani dengan jantung berdegup kencang.
# Kata yang spesifik, langsung terbayang, lucu, dan benar: bukan suasana
# hati yang samar, melainkan adegan yang bisa diceritakan ke teman.
# Penantang untuk GAHAR live "D (doomscrolling)": dinilai dengan 5
# kriteria juri yang sama sebelum diputuskan layak submit atau tidak.

import os
import sys


WORD = "overcaffeinated"
LETTER = WORD[0].upper()


def main():
    if len(LETTER) != 1 or not LETTER.isalpha() or not LETTER.isupper():
        sys.exit("huruf entri harus satu huruf A-Z")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "wb") as f:
        f.write(LETTER.encode("ascii"))
    # Periksa sendiri: gate menolak apa pun selain tepat 1 karakter.
    with open(target, "rb") as f:
        if f.read() != LETTER.encode("ascii"):
            sys.exit("entry.txt harus tepat satu huruf A-Z")


main()
