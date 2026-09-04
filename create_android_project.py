import os
import shutil

def create_project_structure():
    # Базовый путь
    base_path = r"C:\projects\test-app"
    
    # Структура папок и файлов с содержимым
    files = {
        # Корневой build.gradle
        r"build.gradle": '''buildscript {
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:8.2.0'
    }
}

allprojects {
    repositories {
        google()
        mavenCentral()
    }
}

task clean(type: Delete) {
    delete rootProject.buildDir
}''',

        # settings.gradle
        r"settings.gradle": '''pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}

rootProject.name = "TestApp"
include ':app''',

        # gradle.properties
        r"gradle.properties": '''org.gradle.jvmargs=-Xmx2048m
android.useAndroidX=true
android.enableJetifier=true''',

        # .gitignore
        r".gitignore": '''*.iml
.gradle/
/local.properties
/*.iml
.idea/
/build/
/app/build/
*.apk
*.dex
*.class
.DS_Store
*.log''',

        # app/build.gradle
        r"app/build.gradle": '''plugins {
    id 'com.android.application'
}

android {
    namespace 'com.example.testapp'
    compileSdk 34

    defaultConfig {
        applicationId "com.example.testapp"
        minSdk 21
        targetSdk 34
        versionCode 1
        versionName "1.0"
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'com.google.android.material:material:1.11.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.4'
}''',

        # AndroidManifest.xml
        r"app/src/main/AndroidManifest.xml": '''<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.testapp">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:theme="@style/Theme.AppCompat.Light">
        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>''',

        # MainActivity.java
        r"app/src/main/java/com/example/testapp/MainActivity.java": '''package com.example.testapp;

import android.os.Bundle;
import android.widget.TextView;
import android.view.View;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        TextView textView = findViewById(R.id.textView);
        textView.setText("Тестовое приложение работает!");
    }
    
    public void onButtonClick(View view) {
        Toast.makeText(this, "Кнопка нажата!", Toast.LENGTH_SHORT).show();
    }
}''',

        # activity_main.xml
        r"app/src/main/res/layout/activity_main.xml": '''<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center"
    android:padding="16dp">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello World!"
        android:textSize="24sp"
        android:textStyle="bold" />

    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Нажми меня"
        android:layout_marginTop="20dp"
        android:onClick="onButtonClick" />
</LinearLayout>''',

        # strings.xml
        r"app/src/main/res/values/strings.xml": '''<resources>
    <string name="app_name">Test App</string>
</resources>''',
    }

    # Создаем папки
    folders = [
        r"app/src/main/java/com/example/testapp",
        r"app/src/main/res/layout",
        r"app/src/main/res/values",
        r"app/build/outputs/apk/debug",
    ]

    # Создаем базовую папку
    os.makedirs(base_path, exist_ok=True)
    print(f"✓ Создана базовая папка: {base_path}")

    # Создаем все папки
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"✓ Создана папка: {folder}")

    # Создаем все файлы
    for file_path, content in files.items():
        full_path = os.path.join(base_path, file_path)
        # Создаем папку для файла, если её нет
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Создан файл: {file_path}")

    print("\n✅ Проект успешно создан!")
    print(f"📍 Путь: {base_path}")
    print("\n📝 Для сборки APK выполните:")
    print(f"   cd {base_path}")
    print("   gradlew assembleDebug")
    print("\n📦 APK будет создан в:")
    print(f"   {base_path}\\app\\build\\outputs\\apk\\debug\\app-debug.apk")

def create_gradle_wrapper():
    """Создает gradlew файлы для Windows"""
    base_path = r"C:\projects\test-app"
    
    # Создаем gradlew.bat
    gradlew_bat = r'''@rem
@rem Copyright 2015 the original author or authors.
@rem
@rem Licensed under the Apache License, Version 2.0 (the "License");
@rem you may not use this file except in compliance with the License.
@rem You may obtain a copy of the License at
@rem
@rem      https://www.apache.org/licenses/LICENSE-2.0
@rem
@rem Unless required by applicable law or agreed to in writing, software
@rem distributed under the License is distributed on an "AS IS" BASIS,
@rem WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
@rem See the License for the specific language governing permissions and
@rem limitations under the License.
@rem

@if "%DEBUG%"=="" @echo off
@rem ##########################################################################
@rem
@rem  Gradle startup script for Windows
@rem
@rem ##########################################################################

@rem Set local scope for the variables with windows NT shell
if "%OS%"=="Windows_NT" setlocal

set DIRNAME=%~dp0
if "%DIRNAME%"=="" set DIRNAME=.
@rem This is normally unused
set APP_BASE_NAME=%~n0
set APP_HOME=%DIRNAME%

@rem Resolve any "." and ".." in APP_HOME to make it shorter.
for %%i in ("%APP_HOME%") do set APP_HOME=%%~fi

@rem Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
set DEFAULT_JVM_OPTS="-Xmx64m" "-Xms64m"

@rem Find java.exe
if defined JAVA_HOME goto findJavaFromJavaHome

set JAVA_EXE=java.exe
%JAVA_EXE% -version >NUL 2>&1
if %ERRORLEVEL% equ 0 goto execute

echo.
echo ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:findJavaFromJavaHome
set JAVA_HOME=%JAVA_HOME:"=%
set JAVA_EXE=%JAVA_HOME%/bin/java.exe

if exist "%JAVA_EXE%" goto execute

echo.
echo ERROR: JAVA_HOME is set to an invalid directory: %JAVA_HOME%
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:execute
@rem Setup the command line

set CLASSPATH=%APP_HOME%\gradle\wrapper\gradle-wrapper.jar


@rem Execute Gradle
"%JAVA_EXE%" %DEFAULT_JVM_OPTS% %JAVA_OPTS% %GRADLE_OPTS% "-Dorg.gradle.appname=%APP_BASE_NAME%" -classpath "%CLASSPATH%" org.gradle.wrapper.GradleWrapperMain %*

:end
@rem End local scope for the variables with windows NT shell
if %ERRORLEVEL% equ 0 goto mainEnd

:fail
rem Set variable GRADLE_EXIT_CONSOLE if you need the _script_ return code instead of
rem the _cmd.exe /c_ return code!
set EXIT_CODE=%ERRORLEVEL%
if %EXIT_CODE% equ 0 set EXIT_CODE=1
if not ""=="%GRADLE_EXIT_CONSOLE%" exit %EXIT_CODE%
exit /b %EXIT_CODE%

:mainEnd
if "%OS%"=="Windows_NT" endlocal

:omega
'''

    # Создаем папку gradle/wrapper
    wrapper_dir = os.path.join(base_path, "gradle", "wrapper")
    os.makedirs(wrapper_dir, exist_ok=True)
    
    # Записываем gradlew.bat
    with open(os.path.join(base_path, "gradlew.bat"), 'w', encoding='utf-8') as f:
        f.write(gradlew_bat)
    print("✓ Создан gradlew.bat")

    # Создаем пустой файл gradle-wrapper.properties (Gradle скачает автоматически)
    wrapper_props = '''distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\\://services.gradle.org/distributions/gradle-8.4-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
'''
    with open(os.path.join(wrapper_dir, "gradle-wrapper.properties"), 'w', encoding='utf-8') as f:
        f.write(wrapper_props)
    print("✓ Создан gradle-wrapper.properties")

if __name__ == "__main__":
    try:
        print("🚀 Начинаем создание проекта Android...")
        print("=" * 50)
        
        create_project_structure()
        create_gradle_wrapper()
        
        print("\n" + "=" * 50)
        print("🎉 ВСЕ ГОТОВО! Проект создан успешно!")
        print("\n📌 Дальнейшие шаги:")
        print("1. Убедитесь, что установлены:")
        print("   - Java JDK 17+")
        print("   - Android SDK")
        print("2. Для сборки APK выполните:")
        print(f"   cd C:\\projects\\test-app")
        print("   gradlew assembleDebug")
        print("3. APK будет в папке:")
        print("   app\\build\\outputs\\apk\\debug\\")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        print("Проверьте права доступа к папке C:\\projects\\")