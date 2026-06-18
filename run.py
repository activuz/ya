import subprocess
import sys
import platform

def run_frontend_project():
    # Windows tizimida npm buyruqlarini ishga tushirish uchun shell=True kerak bo'lishi mumkin
    use_shell = platform.system() == "Windows"
    
    try:
        print("1. Kutubxonalar o'rnatilmoqda (npm install)...")
        # npm install buyrug'ini bajarish
        subprocess.run(["npm", "install"], check=True, shell=use_shell)
        
        print("\n2. Loyiha ishga tushirilmoqda (npm run dev)...")
        # npm run dev buyrug'ini bajarish
        subprocess.run(["npm", "run", "dev"], check=True, shell=use_shell)
        
    except subprocess.CalledProcessError as e:
        print(f"\nXatolik yuz berdi: Buyruqni bajarishda xatolik ({e})", file=sys.stderr)
    except FileNotFoundError:
        print("\nXatolik: Kompyuteringizda 'npm' topilmadi. Iltimos, Node.js o'rnatilganligini tekshiring.", file=sys.stderr)
    except KeyboardInterrupt:
        print("\nLoyiha to'xtatildi.")

if __name__ == "__main__":
    run_frontend_project()