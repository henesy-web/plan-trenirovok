import subprocess
import os

def check_java():
    try:
        result = subprocess.run(["java", "-version"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Java установлена")
            return True
    except:
        pass
    print("❌ Java НЕ найдена")
    return False

def check_adb():
    try:
        result = subprocess.run(["adb", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Android SDK установлен")
            return True
    except:
        pass
    print("❌ Android SDK НЕ найден")
    return False

if __name__ == "__main__":
    print("Проверка окружения для сборки Android:")
    print("-" * 40)
    
    java_ok = check_java()
    sdk_ok = check_adb()
    
    print("-" * 40)
    if java_ok and sdk_ok:
        print("✅ ВСЕ ГОТОВО! Можно запускать build_apk.py")
    else:
        print("❌ Не все компоненты установлены")
        if not java_ok:
            print("   Java установлена, но не добавлена в PATH")
            print("   Выполните в командной строке:")
            print('   setx JAVA_HOME "C:\\Program Files\\Eclipse Adoptium\\jdk-17.0.20.101-hotspot"')
            print('   setx PATH "%PATH%;%JAVA_HOME%\\bin"')
        if not sdk_ok:
            print("   Установите Android Studio: https://developer.android.com/studio")