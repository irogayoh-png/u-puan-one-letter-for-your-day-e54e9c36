# One Letter for Your Day — versi GAHAR.
#
# Menulis tepat satu huruf, "D", ke entry.txt.
# D singkatan dari "doomscrolling": menggulir kabar buruk sampai larut —
# gambaran hari yang sangat spesifik, langsung terbayang, lucu, dan benar.
# Dari semua kata yang menggambarkan hari, doomscrolling yang paling
# tajam: satu huruf D sudah membawa seluruh adegan (ponsel menyala,
# jam 3 pagi, umpan yang tak ada habisnya). Bukan suasana hati yang samar.

from pathlib import Path
import os


# Kata di balik huruf ini. Huruf entri = huruf pertama kata tersebut.
WORD_BEHIND_THE_LETTER = "doomscrolling"


def entry_letter(word):
    first = word[0].upper()
    if not ("A" <= first <= "Z"):
        raise SystemExit("kata harus diawali huruf A-Z")
    return first


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    letter = entry_letter(WORD_BEHIND_THE_LETTER)
    target = out_dir / "entry.txt"
    target.write_bytes(letter.encode("ascii"))
    # Periksa sendiri: gate menolak apa pun selain tepat 1 karakter.
    if target.read_bytes() != letter.encode("ascii"):
        raise SystemExit("entry.txt harus tepat satu huruf A-Z")


main()
