import paramiko

def get_mac_addresses_per_port(ssh_client, port):
    command = f"show mac address-table interface gigabitEthernet 1/0/{port}"  # Ajuste conforme necessário
    stdin, stdout, stderr = ssh_client.exec_command(command)
    output = stdout.read().decode()
    mac_addresses = parse_mac_addresses(output)
    return mac_addresses

def parse_mac_addresses(output):
    mac_addresses = []
    lines = output.split('\n')
    for line in lines:
        if "dynamic" in line:  # Ajuste conforme o formato específico da saída do switch
            parts = line.split()
            if len(parts) > 1:
                mac_addresses.append(parts[1])
    return mac_addresses

def main():
    hostname = 'your_switch_ip'
    username = 'your_username'
    password = 'your_password'
    
    ssh_client = paramiko.SSHClient()
    
    # Carregar as chaves de host conhecidas
    ssh_client.load_system_host_keys()
    ssh_client.load_host_keys('/path/to/your/known_hosts')  # Especifique o caminho para o seu arquivo known_hosts AQUI
    
    # Usar política de rejeição de chaves desconhecidas
    ssh_client.set_missing_host_key_policy(paramiko.RejectPolicy())

    try:
        ssh_client.connect(hostname, username=username, password=password)
        all_mac_addresses = {}
        
        # Iterar por todas as portas (1 a 48)
        for port in range(1, 49):
            mac_addresses = get_mac_addresses_per_port(ssh_client, port)
            all_mac_addresses[port] = mac_addresses
        
    except paramiko.SSHException as e:
        print(f"Erro na conexão SSH: {e}")
    except Exception as e:
        print(f"Erro ao executar comando: {e}")
    finally:
        ssh_client.close()

    # Escrever as informações em um arquivo txt
    with open('mac_addresses.txt', 'w') as file:
        for port, mac_addresses in all_mac_addresses.items():
            file.write(f"Port {port}:\n")
            file.write(f"Total MACs: {len(mac_addresses)}\n")
            for mac in mac_addresses:
                file.write(f"{mac}\n")
            file.write("\n")

if __name__ == '__main__':
    main()
