import requests
import json
import time
import sys
import os
from platform import system
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Custom Unique Logo
logo = r'''
  

  
 __ _           _                  _       
/ _\ |__   __ _| |__  ______ _  __| | __ _ 
\ \| '_ \ / _` | '_ \|_  / _` |/ _` |/ _` |
_\ \ | | | (_| | | | |/ / (_| | (_| | (_| |
\__/_| |_|\__,_|_| |_/___\__,_|\__,_|\__,_|
                                           
                                           
((We are born to do something special ;💸♥️))
                                                         
[ Tool Selector ]
[ This tool is made by Shahzada ]
'''

# Function to check if the user is approved based on their ID
def shahzadascurty():
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)
    try:
        approval_url = "https://pastebin.com/raw/xCAMxqAK"  
        response = requests.get(approval_url)

        if response.status_code == 200:
            approved_tokens = response.text.splitlines()
            if id in approved_tokens:
                print("\n\nOWNER: SHAHZADA Xd\n")
                print('You are approved by SHAHZADA Enjoy the tool')
            else:

                print("\n\nOWNER: SHAHZADA Xd\n")
                print('You are not approved. Please take approval first My ID link: https://www.facebook.com/L3G3ND.SH4HZ4D4.INSID3')
                print("Your Token : " + id)
                sys.exit()
        else:
            print("Internet needed for approval")
            sys.exit()

    except requests.exceptions.RequestException as e:
        print("\033[91mWarning: Internet connection is needed for approval")
        sys.exit()

# Token Checker function
def check_single_token(token):
    GRAPH_API_URL = "https://graph.facebook.com/me?access_token="
    url = GRAPH_API_URL + token
    response = requests.get(url)
    
    if response.status_code == 200:
        user_details = response.json()
        
        print(Fore.GREEN + "Token: " + token)
        print("ID: ", user_details.get('id'))
        print("Name: ", user_details.get('name'))
        print("Email: ", user_details.get('email', 'Not Available'))
        print("_____________________________")
    else:
        print(Fore.RED + "Invalid Token: " + token)
        return False
    return True

# Function to check multiple tokens
def check_multiple_tokens(file_path):
    valid_tokens = []
    invalid_tokens = []

    with open(file_path, 'r') as file:
        tokens = file.readlines()

    print("\nChecking tokens...\n")
    for token in tokens:
        token = token.strip()
        print(f"Checking Token: {token}")
        is_valid = check_single_token(token)
        
        if is_valid:
            valid_tokens.append(token)
        else:
            invalid_tokens.append(token)

    # Displaying Summary
    print("\nSummary:")
    print(f"Total Tokens Checked: {len(tokens)}")
    print(f"Valid Tokens: {len(valid_tokens)}")
    print(f"Invalid Tokens: {len(invalid_tokens)}")

    # Updating the file with only valid tokens
    with open(file_path, 'w') as file:
        for token in valid_tokens:
            file.write(token + '\n')

    print("\nInvalid tokens have been removed from the file.")

# Function to get Messenger Groups details
def get_groups_details(token):
    GRAPH_API_URL = "https://graph.facebook.com/v12.0/"
    url = f"{GRAPH_API_URL}me/groups?access_token={token}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        groups_data = response.json()

        if 'data' in groups_data:
            groups = groups_data['data']
            return groups
        else:
            print(Fore.RED + "No groups found or insufficient permissions.")
            return []
    else:
        print(Fore.RED + "Invalid Token or API Error.")
        return []

# Function to display group details in different colors
def display_groups_details(groups):
    colors = [Fore.GREEN, Fore.CYAN, Fore.YELLOW, Fore.MAGENTA, Fore.BLUE]
    color_index = 0
    
    for group in groups:
        group_id = group.get('id')
        group_name = group.get('name')
        
        # Display each group with different color
        print(colors[color_index % len(colors)] + f"Group ID: {group_id}")
        print(colors[color_index % len(colors)] + f"Group Name: {group_name}")
        print(colors[color_index % len(colors)] + "_______________")
        
        color_index += 1

# Function for sending messages (Convo Tool)
def send_convo_messages():
    # Getting inputs from the user
    token_file = input(f"Enter the Token File path: ")
    tokens = open(token_file, "r").read().splitlines()
    num_tokens = len(tokens)

    requests.packages.urllib3.disable_warnings()

    def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
    cls()

    def liness():
        print('\33[0;37;40m---------------------------------------------------')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14.0.0; Infinix X6850 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    liness()

    access_tokens = [token.strip() for token in tokens]

    convo_id = input(f"Enter the Convo/Inbox ID: ")

    text_file_path = input(f"Enter the Messages File path: ")

    messages = open(text_file_path, "r").readlines()

    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)

    haters_name = input(f"Enter Hater Name: ")

    speed = int(input(f"Enter Delay (in seconds): "))

    liness()

    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = access_tokens[token_index]

                message = messages[message_index].strip()

                url = "https://graph.facebook.com/v15.0/{}/".format('t_' + convo_id)
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("[+] Messages {} of Convo {} sent by Token {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                    print("  - Time: {}".format(current_time))
                    liness()
                else:
                    print("[x] Failed to send Messages {} of Convo {} with Token {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                    print("  - Time: {}".format(current_time))
                    liness()
                time.sleep(speed)

            print("[+] All messages sent. Restarting the process...")
        except Exception as e:
            print("[!] An error occurred: {}".format(e))

# Function for sending post comments (Post Tool)
def send_post_messages():
    # Getting inputs from the user
    token_file = input(f"Enter the Token File path: ")
    tokens = open(token_file, "r").read().splitlines()
    num_tokens = len(tokens)

    requests.packages.urllib3.disable_warnings()

    def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
    cls()

    def liness():
        print('\33[0;37;40m---------------------------------------------------')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14.0.0; Infinix X6850 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    liness()

    access_tokens = [token.strip() for token in tokens]

    post_id = input(f"Enter the Post ID: ")

    text_file_path = input(f"Enter the Messages File path: ")

    messages = open(text_file_path, "r").readlines()

    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)

    haters_name = input(f"Enter Hater Name: ")

    speed = int(input(f"Enter Delay (in seconds): "))

    liness()

    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = access_tokens[token_index]

                message = messages[message_index].strip()

                # Facebook Post URL updated for comments
                url = f"https://graph.facebook.com/v15.0/{post_id}/comments"
                parameters = {
                    'access_token': access_token,
                    'message': f"{haters_name} {message}"  # Combining hater name with message
                }

                # Send the POST request to Facebook API to comment on the post
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("[+] Message {} of Post {} sent by Token {}: {}".format(
                        message_index + 1, post_id, token_index + 1, f"{haters_name} {message}"))
                    print("  - Time: {}".format(current_time))
                    liness()
                else:
                    print("[x] Failed to send Message {} of Post {} with Token {}: {}".format(
                        message_index + 1, post_id, token_index + 1, f"{haters_name} {message}"))
                    print("  - Time: {}".format(current_time))
                    liness()
                time.sleep(speed)

            print("[+] All messages sent. Restarting the process...")
        except requests.exceptions.RequestException as e:
            print(f"[!] Network issue detected. Retrying...")
            time.sleep(5)  # Retry after 5 seconds if a network error occurs
        except Exception as e:
            print(f"[!] An error occurred: {e}")
            time.sleep(5)  # Retry after 5 seconds if any other error occurs

# Main function to select which tool to use
def main():
    print(Fore.CYAN + logo)  # Display the custom logo
    # Prompt for User ID for approval check
    shahzadascurty()

    while True:
        print(Fore.YELLOW + "[1] Convo Tool")
        print("[2] Post Tool")
        print("[3] Token Checker")
        print("[4] Group ID Checker")
        print("[5] Exit" + Style.RESET_ALL)

        choice = input("Enter your choice: ")

        if choice == '1':
            send_convo_messages()  # Convo Tool
        elif choice == '2':
            send_post_messages()  # Post Tool
        elif choice == '3':
            print("\nSelect an option for Token Checker:")
            print("1. Single Token Checker")
            print("2. Multi Token Checker")
            token_choice = input("Enter your choice (1/2): ").strip()

            if token_choice == '1':
                token = input("Enter the token: ")
                check_single_token(token)  # Single Token Checker
            elif token_choice == '2':
                file_path = input("Enter the file path containing the tokens: ")
                check_multiple_tokens(file_path)  # Multi Token Checker
        elif choice == '4':
            token = input("Enter your access token: ")
            groups = get_groups_details(token)  # Group ID Checker
            display_groups_details(groups)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
