import requests
import time
from colorama import init, Fore, Style

init(autoreset=True)

# Banner author
def banner():
    print(f"""{Fore.CYAN}
╔════════════════════════════════════════╗
║                                        ║
║     Bot Cek Rekening BANK/E-WALLET     ║
║          Author: @yourdre4m7           ║
║     Github: github.com/ItsMeAlf404     ║
║                                        ║
╚════════════════════════════════════════╝
{Style.RESET_ALL}""")

# Daftar bank / e-wallet (singkat, tambahkan sesuai kebutuhan)
BANKS = {
    "dana": "DANA",
    "ovo": "OVO",
    "linkaja": "LinkAja",
    "ovo": "OVO",
    "shopeepay": "ShopeePay",  
    "harda": "Allo Bank/Bank Harda Internasional",
    "anz": "ANZ Indonesia",
    "aceh": "Bank Aceh Syariah",
    "aladin": "Bank Aladin Syariah",
    "amar": "Bank Amar Indonesia",
    "antardaerah": "Bank Antardaerah",
    "artha": "Bank Artha Graha Internasional",
    "bengkulu": "Bank Bengkulu",
    "daerah_istimewa": "Bank BPD DIY",
    "daerah_istimewa_syr": "Bank BPD DIY Syariah",
    "btpn_syr": "Bank BTPN Syariah",
    "bukopin_syr": "Bank Bukopin Syariah",
    "bumi_arta": "Bank Bumi Arta",
    "capital": "Bank Capital Indonesia",
    "bca": "Bank Central Asia",
    "ccb": "Bank China Construction Bank Indonesia",
    "cnb": "Bank CNB (Centratama Nasional Bank)",
    "danamon": "Bank Danamon & Danamon Syariah",
    "dinar": "Bank Dinar Indonesia",
    "dki": "Bank DKI",
    "dki_syr": "Bank DKI Syariah",
    "ganesha": "Bank Ganesha",
    "agris": "Bank IBK Indonesia",
    "ina_perdana": "Bank Ina Perdana",
    "index_selindo": "Bank Index Selindo",
    "artos_syr": "Bank Jago Syariah",
    "jambi": "Bank Jambi",
    "jambi_syr": "Bank Jambi Syariah",
    "jasa_jakarta": "Bank Jasa Jakarta",
    "jawa_tengah": "Bank Jateng",
    "jawa_tengah_syr": "Bank Jateng Syariah",
    "jawa_timur": "Bank Jatim",
    "jawa_timur_syr": "Bank Jatim Syariah",
    "kalimantan_barat": "Bank Kalbar",
    "kalimantan_barat_syr": "Bank Kalbar Syariah",
    "kalimantan_selatan": "Bank Kalsel",
    "kalimantan_selatan_syr": "Bank Kalsel Syariah",
    "kalimantan_tengah": "Bank Kalteng",
    "kalimantan_timur_syr": "Bank Kaltim Syariah",
    "kalimantan_timur": "Bank Kaltimtara",
    "lampung": "Bank Lampung",
    "maluku": "Bank Maluku",
    "mandiri": "Bank Mandiri",
    "mantap": "Bank MANTAP (Mandiri Taspen)",
    "maspion": "Bank Maspion Indonesia",
    "mayapada": "Bank Mayapada",
    "mayora": "Bank Mayora Indonesia",
    "mega": "Bank Mega",
    "mega_syr": "Bank Mega Syariah",
    "mestika_dharma": "Bank Mestika Dharma",
    "mizuho": "Bank Mizuho Indonesia",
    "mas": "Bank Multi Arta Sentosa (Bank MAS)",
    "mutiara": "Bank Mutiara",
    "sumatera_barat": "Bank Nagari",
    "sumatera_barat_syr": "Bank Nagari Syariah",
    "nusa_tenggara_barat": "Bank NTB Syariah",
    "nusa_tenggara_timur": "Bank NTT",
    "nusantara_parahyangan": "Bank Nusantara Parahyangan",
    "ocbc": "Bank OCBC NISP",
    "ocbc_syr": "Bank OCBC NISP Syariah",
    "america_na": "Bank of America NA",
    "boc": "Bank of China (Hong Kong) Limited",
    "india": "Bank of India Indonesia",
    "tokyo": "Bank of Tokyo Mitsubishi UFJ",
    "papua": "Bank Papua",
    "prima": "Bank Prima Master",
    "bri": "Bank Rakyat Indonesia",
    "riau_dan_kepri": "Bank Riau Kepri",
    "sahabat_sampoerna": "Bank Sahabat Sampoerna",
    "shinhan": "Bank Shinhan Indonesia",
    "sinarmas": "Bank Sinarmas",
    "sinarmas_syr": "Bank Sinarmas Syariah",
    "sulselbar": "Bank Sulselbar",
    "sulselbar_syr": "Bank Sulselbar Syariah",
    "sulawesi": "Bank Sulteng",
    "sulawesi_tenggara": "Bank Sultra",
    "sulut": "Bank SulutGo",
    "sumsel_dan_babel": "Bank Sumsel Babel",
    "sumsel_dan_babel_syr": "Bank Sumsel Babel Syariah",
    "sumut": "Bank Sumut",
    "sumut_syr": "Bank Sumut Syariah",
    "resona_perdania": "Bank Resona Perdania",
    "victoria_internasional": "Bank Victoria International",
    "victoria_syr": "Bank Victoria Syariah",
    "woori": "Bank Woori Saudara",
    "bca_syr": "BCA (Bank Central Asia) Syariah",
    "bjb": "BJB",
    "bjb_syr": "BJB Syariah",
    "royal": "Blu/BCA Digital",
    "bni": "BNI (Bank Negara Indonesia)",
    "bnp_paribas": "BNP Paribas Indonesia",
    "bali": "BPD Bali",
    "banten": "BPD Banten",
    "eka": "BPR EKA (Bank Eka)",
    "agroniaga": "BRI Agroniaga",
    "bsm": "BSI (Bank Syariah Indonesia)",
    "btn": "BTN",
    "btn_syr": "BTN Syariah",
    "tabungan_pensiunan_nasional": "BTPN",
    "cimb": "CIMB Niaga & CIMB Niaga Syariah",
    "citibank": "Citibank",
    "commonwealth": "Commonwealth Bank",
    "chinatrust": "CTBC (Chinatrust) Indonesia",
    "dbs": "DBS Indonesia",
    "hsbc": "HSBC Indonesia",
    "icbc": "ICBC Indonesia",
    "artos": "Jago/Artos",
    "hana": "LINE Bank/KEB Hana",
    "bii": "Maybank Indonesia",
    "bii_syr": "Maybank Syariah",
    "mnc_internasional": "Motion/MNC Bank",
    "muamalat": "Muamalat",
    "yudha_bakti": "Neo Commerce/Yudha Bhakti",
    "nationalnobu": "Nobu (Nationalnobu) Bank",
    "panin": "Panin Bank",
    "panin_syr": "Panin Dubai Syariah",
    "permata": "Permata",
    "permata_syr": "Permata Syariah",
    "qnb_kesawan": "QNB Indonesia",
    "rabobank": "Rabobank International Indonesia",
    "sbi_indonesia": "SBI Indonesia",
    "kesejahteraan_ekonomi": "Seabank/Bank BKE",
    "standard_chartered": "Standard Chartered Bank",
    "super_bank": "Superbank",
    "uob": "TMRW/UOB",
    "bukopin": "Wokee/Bukopin",
    "krom": "Krom Bank Indonesia",
  
}

RATE_LIMIT = 3
RATE_LIMIT_INTERVAL = 60
user_requests = []

def check_rate_limit():
    global user_requests
    now = time.time()
    # Bersihkan request lebih dari interval
    user_requests = [t for t in user_requests if now - t < RATE_LIMIT_INTERVAL]

    if len(user_requests) >= RATE_LIMIT:
        return False
    user_requests.append(now)
    return True

def cek_rekening(bank: str, nomor: str):
    bank = bank.lower()
    if bank not in BANKS:
        print(f"{Fore.RED}❌ Bank '{bank}' tidak dikenali. Gunakan bank yang tersedia.")
        return

    if not check_rate_limit():
        print(f"{Fore.YELLOW}⏳ Kamu sudah mencapai batas request (3x per menit). Silakan coba lagi nanti.")
        return

    print(f"{Fore.CYAN}🔍 Mengecek rekening {BANKS[bank]} dengan nomor {nomor}...{Style.RESET_ALL}")
    time.sleep(2)  # Delay 2 detik sebelum request API

    try:
        url = "https://cekrekening-api.belibayar.online/api/v1/account-inquiry"
        headers = {"Content-Type": "application/json"}
        payload = {"account_number": nomor, "account_bank": bank}

        response = requests.post(url, json=payload, headers=headers, timeout=10)
        result = response.json()

        success = result.get("success", False)
        message = result.get("message", "-")
        data = result.get("data", {})

        account_holder = data.get("account_holder")
        bank_name = BANKS.get(bank, bank.upper())

        if success and message == "ACCOUNT FOUND":
            if account_holder:
                print(f"{Fore.GREEN}✅ Rekening Ditemukan!")
                print(f"{Fore.GREEN}👤 Nama Pemilik: {account_holder}")
                print(f"{Fore.GREEN}🏦 Bank: {bank_name}")
                print(f"{Fore.GREEN}💳 Nomor Rekening: {nomor}")
            else:
                print(f"{Fore.GREEN}✅ Rekening Ditemukan!")
                print(f"{Fore.GREEN}🏦 Bank: {bank_name}")
                print(f"{Fore.GREEN}💳 Nomor Rekening: {nomor}")
                print(f"{Fore.YELLOW}⚠️ Nama pemilik tidak tersedia.")
                print(f"{Fore.YELLOW}ℹ️ Catatan: Beberapa e-wallet tidak menampilkan nama pemilik.")
        else:
            print(f"{Fore.RED}❌ Gagal mendapatkan data:")
            print(f"{Fore.RED}Pesan: {message}")

    except Exception as e:
        print(f"{Fore.RED}❌ Terjadi kesalahan saat menghubungi API:\n{e}")

def tampilkan_banklist():
    print(f"{Fore.MAGENTA}🏦 Daftar Bank / E-Wallet yang Didukung:")
    for kode, nama in BANKS.items():
        print(f"- {kode}: {nama}")
    print(Style.RESET_ALL)

def main():
    banner()
    while True:
        print(f"\n{Fore.BLUE}Menu:")
        print("1. Cek Rekening")
        print("2. Tampilkan Daftar Bank")
        print("3. Keluar")
        pilihan = input("Pilih (1/2/3): ").strip()

        if pilihan == "1":
            bank = input("Masukkan kode bank: ").strip()
            nomor = input("Masukkan nomor rekening: ").strip()
            cek_rekening(bank, nomor)
        elif pilihan == "2":
            tampilkan_banklist()
        elif pilihan == "3":
            print(f"{Fore.GREEN}Terima kasih sudah menggunakan program ini!")
            break
        else:
            print(f"{Fore.RED}Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
