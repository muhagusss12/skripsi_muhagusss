import subprocess
import argparse

def start_firewall():
    try:
        output = subprocess.check_output(['sudo', 'iptables', '-L'], stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Terjadi kesalahan: {e.output}"

def config_firewall():
    try:
        subprocess.run(['sudo', 'nano', '/etc/knockd.conf'], check=True)
        return "Konfigurasi selesai."
    except subprocess.CalledProcessError as e:
        return f"Terjadi kesalahan: {e.output}"

def stop_firewall():
    try:
        output = subprocess.check_output(['sudo', 'iptables', '-F'], stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Terjadi kesalahan: {e.output}"

def main():
    parser = argparse.ArgumentParser(description='Firewall Skripsi Tugas Akhir by Muhammad Agus Saputra.')
    parser.add_argument('-s', '--start', action='store_true', help='Mengaktifkan Firewall.')
    parser.add_argument('-c', '--config', action='store_true', help='Konfigurasi Port Knocking.')
    parser.add_argument('-o', '--stop', action='store_true', help='Menonaktifkan Firewall.')
    
    args = parser.parse_args()
    
    if args.start:
        print("Firewall telah aktif.")
        print(start_firewall())
    elif args.config:
        print("Mengedit konfigurasi firewall.")
        print(config_firewall())
    elif args.stop:
        print('Firewall telah nonaktif.')
        print(stop_firewall())
    else:
        print('Parameter tidak tersedia. Gunakan -h atau --help untuk bantuan.')

if __name__ == '__main__':
    main()
