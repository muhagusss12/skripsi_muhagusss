import os
import argparse

def start_firewall():
    try:
        output = os.popen('iptables -L').read()
        print(output)
    except Exception as e:
        return f"Terjadi kesalahan: {e}"

def config_firewall():
    try:
        output = os.popen('sudo nano /etc/knockd.conf').read()
        print(output)
    except Exception as e:
        return f"Terjadi kesalahan: {e}"

def stop_firewall():
    try:
        output = os.popen('sudo iptables -F').read()
        print(output)
    except Exception as e:
        return f"Terjadi kesalahan: {e}"

def main():
    # Membuat parser argumen
    parser = argparse.ArgumentParser(description='Firewall Skripsi Tugas Akhir by Muhammad Agus Saputra.')
    parser.add_argument('-S', '--start', action='store_true', help='Mengaktifkan Firewall.')
    parser.add_argument('-s', '--stop', action='store_true', help='Menonaktifkan Firewall.')
    
    # Mengambil argumen dari command line
    args = parser.parse_args()

    print(start_firewall())
    
    if args.start:
        print("Firewall telah aktif.")
        print(start_firewall())
    elif args.stop:
        print('Firewall telah nonaktif')
        print(stop_firewall())
    else:
        return f'Parameter tidak tersedia. Gunakan -h atau --help untuk bantuan.'

if __name__ == '__main__':
    main()