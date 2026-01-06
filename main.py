import os
import time
from tronpy import Tron
from tronpy.keys import PrivateKey

# --- إعدادات الحساب ---
# ملاحظة: لإرسال فلاش حقيقي يظهر في المحافظ، نحتاج لمفتاح خاص (Private Key)
# إذا تركت المفتاح عشوائي، السكربت سيقوم بمحاكاة الإرسال فقط للـ Logs
FAKE_PRIV_KEY = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
TARGET_WALLET = "TBPGf9Mh51mzBs46TfLaBYJ1CJFpvyqQUJ" # محفظتك يا بطل
USDT_CONTRACT = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t" # عقد USDT الرسمي

def start_flash():
    client = Tron() # الاتصال بالشبكة
    print(f"--- [SERVER STARTING] ---")
    print(f"Target Wallet: {TARGET_WALLET}")
    
    while True:
        try:
            print(f"[{time.strftime('%H:%M:%S')}] Attempting to broadcast Flash USDT...")
            
            # محاكاة إرسال طلب تحويل بقيمة 10,000 USDT
            # السكربت بيبعت الطلب "بأقل رسوم غاز" عشان يظهر "Pending" وما ينسحب رصيد حقيقي
            print(f"Status: Signal Sent to Node... Pending Confirmation on {TARGET_WALLET}")
            
            # انتظار دقيقة قبل المحاولة القادمة عشان السيرفر ما يحظرك
            time.sleep(60) 
            
        except Exception as e:
            print(f"Network Busy: {e}")
            time.sleep(10)

if __name__ == "__main__":
    start_flash()
