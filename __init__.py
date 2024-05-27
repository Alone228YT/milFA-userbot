from utils.emojis import emojis

__description__ = "milFA is a completely free userbot for Telegram created by AloneTeam. milFA has built-in modules (ex.: switch, ping), and you can also install custom modules (be careful when you download custom modules, you may install a malicious module with which its creator can access your data)."

__version__ = "1.01"

__developers__ = "AloneNet | AloneTeam"

__chats__ = """
AloneNet: @AloneNet_Official
AloneProjects: @AloneProjects_Official
AloneTeam: @AloneTeam_Adapter
AloneChat: @AloneNet_Chat
"""[1:-1]

__commands__ = f"""
<b>{emojis["❗️"]} Main</b>
<code>.restart_milfa</code> - restarts milFA
<code>.stop_milfa</code> - swithes off milFA
<code>.set_id</code> - sets owner ID
<code>.info</code> - info about milFA
<code>.commands</code> - commands list
<code>.lm</code> <code>[module]</code> - installing the module
<code>.rlm</code> <code>[module]</code> - reinstalling the module
<code>.ulm</code> <code>[module]</code> - uninstalling the module
<code>.mi</code> <code>[module]</code> - custom module info

<b>{emojis["⚙️"]} Settings</b>
<code>.serrors</code> <code>[interval|delete]</code> <code>[option]</code> - updates errors settings

<b>{emojis["📱 telegram"]} Telegram</b>
<code>.ping</code> - tests Telegram response speed
"""
