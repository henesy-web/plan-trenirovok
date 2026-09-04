import subprocess
import os
import sys

def build_apk():
    os.chdir(r"C:\projects\test-app")
    
    print("🔨 Начинаем сборку APK...")
    try:
        # Запускаем сборку
        result = subprocess.run(
            ["gradlew.bat", "assembleDebug"],
            capture_output=True,
            text=True,
            shell=True
        )
        
        if result.returncode == 0:
            print("✅ APK успешно собран!")
            print("📦 Путь к APK:")
            print("   C:\\projects\\test-app\\app\\build\\outputs\\apk\\debug\\app-debug.apk")
        else:
            print("❌ Ошибка сборки:")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    build_apk()