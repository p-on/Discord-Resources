try:
    import httpx, os
    from dotenv import load_dotenv
    from colr import Colr as C
except:
    print("httpx or python-dotenv or colr not installed, please install then run again")
    exit()

load_dotenv()

try:
    token = os.getenv('token')
except:
    token = input("Please enter your Discord Bot token here: ")

id = input("Enter Discord ID to search here: ")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bot {token}"
}

response = httpx.get(f"https://discord.com/api/v9/users/{id}", headers=headers)
if response.status_code == 200:
    data = response.json()
    tag = f"{data['username']}#{data['discriminator']}"
    print(f"ID — {id}\nTag — {tag}")
    if data["avatar"]:
        avatar = f"https://cdn.discordapp.com/avatars/{id}/{data['avatar']}.{'gif' if data['avatar'][:2] == 'a_' else 'png'}?size=80"
        print(f"Avatar — {avatar}")
    if data["banner"]:
        banner = f"https://cdn.discordapp.com/banners/{id}/{data['banner']}.{'gif' if data['banner'][:2] == 'a_' else 'png'}?size=80"
        print(f"Banner — {banner}")
    if data["banner_color"]:
        print(f"Banner Color — {C().hex(data['banner_color'], '████████', rgb_mode=True)}")

else:
    print("Invalid token or operation did not find a user with that Discord ID")
