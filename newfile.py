# TAHAP 3: PROTEKSI PANGGULAN ASING SHUXIN

def menu_awal():
    print("====================================")
    print("       AI SHUXIN SYSTEM ONLINE      ")
    print("====================================")
    print("Selamat malam, Tuan Irfan.")
    print("Shuxin siap menerima perintah.")
    print("====================================")

def periksa_panggilan(nomor_masuk):
    # Memori daftar nomor kontak yang aman (Nomor Anda & Istri)
    kontak_aman = ["08123456789", "08987654321"]
    
    if nomor_masuk in kontak_aman:
        print("\n[✓] SHUXIN: Nomor dikenali sebagai Kontak Aman.")
        print("[+] Status: Panggilan telepon diizinkan masuk.")
    else:
        print(f"\n[!] SHUXIN PERINGATAN: Nomor Asing ({nomor_masuk}) Mendeteksi!")
        print("[!] Tindakan: MEMUTUS PANGGILAN OTOMATIS...")
        print("[!] Tindakan: Mengirim laporan keamanan otomatis ke WhatsApp Istri...")

if __name__ == "__main__":
    menu_awal()
    
    # Tes simulasi deteksi panggilan masuk pada sistem Shuxin
    no_telp = input("\nSimulasi Ada Telepon Masuk Dari Nomor: ")
    periksa_panggilan(no_telp)
