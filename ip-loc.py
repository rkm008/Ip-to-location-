import requests
import colorama
import time
import sys
from colorama import Fore, Style

# Function to display an animated logo
def animated_logo():
    logo = f"""
{Fore.YELLOW}███████╗████████╗██████╗ ███████╗██╗███╗   ██╗ ██████╗{Style.RESET_ALL}
{Fore.YELLOW}██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║████╗  ██║██╔════╝{Style.RESET_ALL}
{Fore.YELLOW}███████╗   ██║   ██████╔╝█████╗  ██║██╔██╗ ██║██║  ███╗{Style.RESET_ALL}
{Fore.YELLOW}╚════██║   ██║   ██╔══██╗██╔══╝  ██║██║╚██╗██║██║   ██║{Style.RESET_ALL}
{Fore.YELLOW}███████║   ██║   ██║  ██║███████╗██║██║ ╚████║╚██████╔╝{Style.RESET_ALL}
{Fore.YELLOW}╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝{Style.RESET_ALL}
    """
    for line in logo.splitlines():
        print(line)
        time.sleep(0.1)

# Function for a loading effect
def loading_animation():
    animation = ["[■□□□□□□□]", "[■■□□□□□□]", "[■■■□□□□□]", "[■■■■□□□□]", 
                 "[■■■■■□□□]", "[■■■■■■□□]", "[■■■■■■■□]", "[■■■■■■■■]"]
    
    for i in range(8):
        sys.stdout.write(f"\r{Fore.CYAN}Fetching Data {animation[i % len(animation)]}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(0.2)

# Function to get IP location details
def get_ip_location(ip_address):
    loading_animation()  # Display loading animation while fetching data
    response = requests.get(f'http://ip-api.com/json/{ip_address}')
    data = response.json()
    return data

# Main function
def main():
    colorama.init()
    animated_logo()  # Show the animated logo
    print(f"{Fore.GREEN}Get victim's IP location{Style.RESET_ALL}")
    ip_address = input(f"{Fore.CYAN}Enter an IP address: {Style.RESET_ALL}")
    location_data = get_ip_location(ip_address)
    print("\n" + f"{Fore.YELLOW}Location Data:{Style.RESET_ALL}")

    # Safely access each key with .get() to avoid KeyErrors
    print(f"{Fore.MAGENTA}IP Address:{Style.RESET_ALL} {location_data.get('query', 'N/A')}")
    print(f"{Fore.MAGENTA}Country:{Style.RESET_ALL} {location_data.get('country', 'N/A')}")
    print(f"{Fore.MAGENTA}City:{Style.RESET_ALL} {location_data.get('city', 'N/A')}")
    print(f"{Fore.MAGENTA}Region:{Style.RESET_ALL} {location_data.get('regionName', 'N/A')}")
    print(f"{Fore.MAGENTA}ISP:{Style.RESET_ALL} {location_data.get('isp', 'N/A')}")
    print(f"{Fore.MAGENTA}Latitude:{Style.RESET_ALL} {location_data.get('lat', 'N/A')}")
    print(f"{Fore.MAGENTA}Longitude:{Style.RESET_ALL} {location_data.get('lon', 'N/A')}")
    print(f"{Fore.MAGENTA}Timezone:{Style.RESET_ALL} {location_data.get('timezone', 'N/A')}")
    print(f"{Fore.MAGENTA}Organization:{Style.RESET_ALL} {location_data.get('org', 'N/A')}")

if __name__ == "__main__":
    main()
