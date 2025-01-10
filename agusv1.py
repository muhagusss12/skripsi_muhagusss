import subprocess
import argparse

def start_firewall():
    try:
        subprocess.run(['iptables', '-A INPUT -m conntrack --ctstate ESTABLISHED, RELATED -j ACCEPT'], check=True)
        subprocess.run(['iptables', '-A INPUT -p tcp --dport 22 -j REJECT'], check=True)
        subprocess.run(['iptables', '-A INPUT -p icmp -m icmp --icmp-type 8 -j DROP'], check=True)
        subprocess.run(['iptables', '-A INPUT -p icmp -m icmp --icmp-type 13 -j DROP'], check=True)
        subprocess.run(['iptables', '-A INPUT -p icmp -m icmp --icmp-type 14 -j DROP'], check=True)
        subprocess.run(['iptables', '-A INPUT -p tcp --tcp-flags ALL NONE -j DROP'], check=True)
        subprocess.run(['iptables', '-I INPUT -p tcp --dport 80 -m state --state NEW -m recent --set'], check=True)
        subprocess.run(['iptables', '-I INPUT -p tcp --dport 80 -m state --state NEW -m recent --update --seconds 20 --hitcount 10 -j DROP'], check=True)
        subprocess.run(['iptables', '-N BLOCK'], check=True)
        subprocess.run(['iptables', '-j LOG -I BLOCK --log-prefix=”IPTABLES_BLOCK” --log-level 7'], check=True)
        subprocess.run(['iptables', '-A BLOCK -j DROP'], check=True)
        subprocess.run(['iptables', '-i enp0s3 -A INPUT -p tcp -m tcp -m multiport ! --dports 80,22 -m recent -- name PORTSCAN --set'], check=True)
        subprocess.run(['iptables', '-i enp0s3 -A INPUT -m recent --name PORTSCAN --rcheck --seconds 30 -j BLOCK'], check=True)
        subprocess.run(['iptables', '-A INPUT -i enp0s3 -p tcp -m multiport ! --dport 22,80,443 -j REJECT --reject-with tcp-reset'], check=True)
        subprocess.run(['iptables', '-A INPUT -i enp0s3 -p tcp ! --syn -m state --state NEW -j DROP'], check=True)
        #subprocess.run(['iptables', '-N BLOCK'], check=True)

        print('Firewall telah diaktifkan')
        
    except subprocess.CalledProcessError as e:
        return f"Terjadi kesalahan: {e.output}"

def config_firewall():
    try:
        subprocess.run(['nano', '/etc/knockd.conf'], check=True)
        print("Konfigurasi selesai.")
    except subprocess.CalledProcessError as e:
        return f"Terjadi kesalahan: {e.output}"

def stop_firewall():
    try:
        subprocess.run(['iptables', '-F'], stderr=subprocess.STDOUT, text=True)
        print('Firewall telah dinonaktifkan.')
    except subprocess.CalledProcessError as e:
        return f"Terjadi kesalahan: {e.output}"

def main():
    parser = argparse.ArgumentParser(description='Firewall Skripsi Tugas Akhir by Muhammad Agus Saputra.')
    parser.add_argument('-s', '--start', action='store_true', help='Mengaktifkan Firewall.')
    parser.add_argument('-c', '--config', action='store_true', help='Konfigurasi Port Knocking.')
    parser.add_argument('-o', '--stop', action='store_true', help='Menonaktifkan Firewall.')
    
    args = parser.parse_args()
    print('Program ini ialah firewall menggunakan metode Firewall Filtering dan Port Knocking')
    print('Program ini ialah Tugas Skripsi Muhammad Agus Saputra')
    print('Gunakan -h atau memperoleh bantuan penggunaan aplikasi.')
    
    if args.start:
        start_firewall()
    elif args.config:
        config_firewall()
    elif args.stop:
        stop_firewall()
    else:
        print('Parameter tidak tersedia. Gunakan -h atau --help untuk bantuan.')

if __name__ == '__main__':
    main()
