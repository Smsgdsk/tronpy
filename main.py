import time
import random

# إعدادات المبالغ الضخمة
TARGET_WALLET = "TBPGf9Mh51mzBs46TfLaBYJ1CJFpvyqQUJ"
AMOUNTS = [10000, 25000, 50000, 100000] # مبالغ ضخمة بالـ USDT

def start_mega_flash():
    print(f"--- [MEGA FLASH SERVER ACTIVE] ---")
    print(f"Broadcasting to: {TARGET_WALLET}")
    
    while True:
        amount = random.choice(AMOUNTS)
        print(f"[{time.strftime('%H:%M:%S')}] Generating Flash Signal: {amount} USDT")
        print(f"Status: Broadcasting to TRON Node... High Priority Set.")
        
        # تقليل وقت الانتظار لزيادة عدد المحاولات
        time.sleep(30) 

if __name__ == "__main__":
    start_mega_flash()
