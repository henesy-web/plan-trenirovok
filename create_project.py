import os

files = {
    "build.gradle": """
plugins {
    id("com.android.application") version "8.2.0" apply false
    id("org.jetbrains.kotlin.android") version "1.9.20" apply false
}
""",
    "settings.gradle": """
pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}
rootProject.name = "PlanTrenirovok"
include(":app")
""",
    "app/build.gradle": """
plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}
android {
    namespace = "com.example.plantrenirovok"
    compileSdk = 34
    defaultConfig {
        applicationId = "com.example.plantrenirovok"
        minSdk = 24
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions {
        jvmTarget = "17"
    }
}
dependencies {
    implementation("androidx.core:core-ktx:1.12.0")
    implementation("androidx.appcompat:appcompat:1.6.1")
}
""",
    "app/src/main/AndroidManifest.xml": """
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.plantrenirovok">
    <application
        android:allowBackup="true"
        android:label="@string/app_name"
        android:theme="@style/Theme.PlanTrenirovok">
        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
""",
    "app/src/main/java/com/example/plantrenirovok/MainActivity.kt": """
package com.example.plantrenirovok
import android.os.Bundle
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val button: Button = findViewById(R.id.btn_start)
        button.setOnClickListener {
            Toast.makeText(this, "Тренировка началась!", Toast.LENGTH_SHORT).show()
        }
    }
}
""",
    "app/src/main/res/layout/activity_main.xml": """
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center"
    android:background="#000000"
    android:padding="16dp">
    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="ПЛАН ТРЕНИРОВОК"
        android:textColor="#FFFFFF"
        android:textSize="28sp"
        android:textStyle="bold"
        android:layout_marginBottom="40dp" />
    <Button
        android:id="@+id/btn_start"
        android:layout_width="match_parent"
        android:layout_height="60dp"
        android:text="НАЧАТЬ ТРЕНИРОВКУ"
        android:textColor="#FFFFFF"
        android:textSize="18sp"
        android:background="#4CAF50" />
</LinearLayout>
""",
    "app/src/main/res/values/strings.xml": """
<resources>
    <string name="app_name">План тренировок</string>
</resources>
""",
    "app/src/main/res/values/themes.xml": """
<resources>
    <style name="Theme.PlanTrenirovok" parent="Theme.MaterialComponents.DayNight.NoActionBar">
        <item name="android:windowBackground">#000000</item>
    </style>
</resources>
""",
    "gradle/wrapper/gradle-wrapper.properties": """
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\\://services.gradle.org/distributions/gradle-8.2-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
""",
    ".github/workflows/build.yml": """
name: Build APK
on:
  push:
    branches: [ main ]
  workflow_dispatch:
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Set up JDK 17
      uses: actions/setup-java@v4
      with:
        java-version: '17'
        distribution: 'temurin'
    - name: Build APK
      run: ./gradlew assembleDebug --no-daemon --stacktrace
    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: app-debug
        path: app/build/outputs/apk/debug/*.apk
"""
}

# Создаём папки и файлы
for filepath, content in files.items():
    # Получаем директорию файла
    dirname = os.path.dirname(filepath)
    # Если директория не пустая - создаём её
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    # Записываем файл
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"✅ {filepath}")

print("\n🎉 Проект создан в C:\\projects\\plan-trenirovok-ai")
print("📤 Теперь загрузите папку на GitHub через 'Add file → Upload files'")