import os
import argparse

def start_firewall():
    try:
        output = os.popen('sudo iptables -L').read()
        return output
    except Exception as e:
        return f"Terjadi kesalahan: {e}"

def config_firewall():
    try:
        output = os.popen('sudo nano /etc/knockd.conf').read()
        return output
    except Exception as e:
        return f"Terjadi kesalahan: {e}"

def stop_firewall():
    try:
        output = os.popen('sudo iptables -F').read()
        return output
    except Exception as e:
        return f"Terjadi kesalahan: {e}"

def main():
    # Membuat parser argumen
    parser = argparse.ArgumentParser(description='Firewall Skripsi Tugas Akhir by Muhammad Agus Saputra.')
    parser.add_argument('-s', '--start', action='store_true', help='Mengaktifkan Firewall.')
    parser.add_argument('-c', '--config', action='store_true', help='Konfigurasi Port Knocking.')
    parser.add_argument('-o', '--stop', action='store_true', help='Menonaktifkan Firewall.')
    
    # Mengambil argumen dari command line
    args = parser.parse_args()

    a = start_firewall()
    b = config_firewall()
    c = stop_firewall()
    
    if args.start:
        print("Firewall telah aktif.")
        print(a)
    elif args.config:
        print("Aturan iptables:")
        config_firewall()
        print(b)
    elif args.stop:
        print('Firewall telah nonaktif')
        stop_firewall()
        print(c)
    else:
        print('Parameter tidak tersedia. Gunakan -h atau --help untuk bantuan.')

if __name__ == '__main__':
    main()