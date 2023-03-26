import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26305247")

API_HASH = os.environ.get("API_HASH", "20ca7e6687c281e11782856c7efd0ff7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6033306990:AAHlGOo2JtADZaCYT6I0d-yAbRLGYzm5VkU") 

FORCE_SUB = os.environ.get("FORCE_SUB", "dnsmsmsosmdnd") 

DB_NAME = os.environ.get("DB_NAME","renamerv1")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Dipanshu_021:ad8920@cluster0.f7migc1.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5152847809').split()]

PORT = os.environ.get("PORT", "8080")
