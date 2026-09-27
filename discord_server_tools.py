import requests
import json

#  تحذير: استخدام سيلف توكن يخالف شروط ديسكورد وقد يؤدي لحظر حسابك
TOKEN = ""

def get_guild_owner(guild_id):
    """الحصول على معلومات مالك السيرفر"""
    
    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/json"
    }
    
    # جلب معلومات السيرفر
    response = requests.get(
        f"https://discord.com/api/v10/guilds/{guild_id}",
        headers=headers
    )
    
    if response.status_code == 200:
        data = response.json()
        owner_id = data.get('owner_id')
        guild_name = data.get('name')
        
        print(f" اسم السيرفر: {guild_name}")
        print(f" معرف المالك: {owner_id}")
        
        # -----------------------------------------------------
        # طريقة جديدة ومحسنة لجلب معلومات المالك
        # -----------------------------------------------------
        
        # الطريقة 1: جلب معلومات المالك كعضو في السيرفر
        print("\n محاولة جلب معلومات المالك كعضو في السيرفر...")
        member_response = requests.get(
            f"https://discord.com/api/v10/guilds/{guild_id}/members/{owner_id}",
            headers=headers
        )
        
        if member_response.status_code == 200:
            member_data = member_response.json()
            user = member_data.get('user', {})
            print(f" تم جلب معلومات المالك بنجاح!")
            print(f" الاسم: {user.get('username')}#{user.get('discriminator', '0')}")
            print(f" الآيدي: {user.get('id')}")
            print(f" تاريخ الانضمام: {member_data.get('joined_at')}")
            
            # جلب الصورة الرمزية
            avatar_hash = user.get('avatar')
            if avatar_hash:
                avatar_url = f"https://cdn.discordapp.com/avatars/{user.get('id')}/{avatar_hash}.png"
                print(f" الصورة الرمزية: {avatar_url}")
            
            return member_data
            
        else:
            print(f" فشل جلب المالك كعضو (الكود: {member_response.status_code})")
            
            # الطريقة 2: محاولة جلب المستخدم مباشرة
            print("\n محاولة جلب معلومات المستخدم مباشرة...")
            user_response = requests.get(
                f"https://discord.com/api/v10/users/{owner_id}",
                headers=headers
            )
            
            if user_response.status_code == 200:
                user_data = user_response.json()
                print(f" تم جلب معلومات المستخدم بنجاح!")
                print(f" الاسم: {user_data.get('username')}#{user_data.get('discriminator', '0')}")
                print(f" الآيدي: {user_data.get('id')}")
            else:
                print(f" فشل جلب المستخدم (الكود: {user_response.status_code})")
                print(" سبب الفشل: قد يكون التوكن لا يملك صلاحية قراءة معلومات المستخدمين")
                
                # الطريقة 3: عرض معلومات متاحة من API العام
                print("\n محاولة جلب معلومات عامة عن السيرفر...")
                public_response = requests.get(
                    f"https://discord.com/api/v10/guilds/{guild_id}/widget.json"
                )
                
                if public_response.status_code == 200:
                    widget_data = public_response.json()
                    print(f" معلومات السيرفر العامة:")
                    print(f" الاسم: {widget_data.get('name')}")
                    print(f" عدد الأعضاء: {widget_data.get('members', [])}")
                else:
                    print(f" السيرفر ليس عاماً أو لا يدعم الويدجت")
                    
    else:
        print(f" خطأ في جلب السيرفر: {response.status_code}")
        print(f" التفاصيل: {response.text}")

def get_all_servers():
    """جلب قائمة بجميع السيرفرات التي أنت فيها"""
    
    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/json"
    }
    
    response = requests.get(
        "https://discord.com/api/v10/users/@me/guilds",
        headers=headers
    )
    
    if response.status_code == 200:
        guilds = response.json()
        print(f"\n أنت في {len(guilds)} سيرفر:")
        print("-" * 50)
        for guild in guilds:
            print(f" {guild.get('name')} - آيدي: {guild.get('id')}")
            if guild.get('owner'):
                print(f"    أنت مالك هذا السيرفر")
        print("-" * 50)
        return guilds
    else:
        print(f" خطأ في جلب السيرفرات: {response.status_code}")
        return []

if __name__ == "__main__":
    # عرض جميع السيرفرات أولاً
    print(" جاري جلب قائمة السيرفرات...")
    get_all_servers()
    
    print("\n" + "="*50)
    
    # استخدم معرف السيرفر الذي حصلت عليه
    GUILD_ID = "1439271484127318221"  # 𝐀𝐑𝐄𝐍𝐀 𝐗
    
    print(f"\n جاري جلب معلومات السيرفر {GUILD_ID}...")
    print("="*50)
    get_guild_owner(GUILD_ID)