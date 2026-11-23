# One Letter for Your Day — versi AMAN.
#
# Menulis tepat satu huruf, "G", ke entry.txt.
# G singkatan dari "groggy": kepala berkabut karena kurang tidur —
# gambaran hari yang nyata, spesifik, lucu, dan benar.
# Juri hanya melihat satu huruf ini; G membangkitkan satu kata yang
# langsung terbayang, bukan suasana hati yang samar.

import os


LETTER = "G"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Periksa sendiri: gate menolak apa pun selain tepat 1 karakter.
    with open(path, "rb") as f:
        data = f.read()
    if data != LETTER.encode("ascii"):
        raise SystemExit("entry.txt harus tepat satu huruf A-Z")


main()
