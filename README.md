# ClassCompare

`ClassCompare`為一衝堂處理與排課程式。

## 目錄

- [簡介](#簡介)
- [安裝](#安裝)
- [使用方法](#使用方法)
- [貢獻](#貢獻)
- [許可證](#許可證)
 

## 依賴項

`ClassCompare`需要以下依賴項才能正常運行：

- Python 3.x
- Git
- openpyxl
- datetime
- holidays
- requests
- pdfplumber
- selenium
- bs4
- Chrome Driver(需在google chrome lab的網頁下載與電腦上Chrome相同的版本，https://googlechromelabs.github.io/chrome-for-testing/#stable)

請確保您已經安裝了這些依賴項，以便順利使用`ClassCompare`程式。

## 簡介

`ClassCompare`是一個衝堂處理與排課的Python程式，可以讓您比較課程。
1. `NewMain.py`為主要模組，目前可以進行中乙排課、牙醫排課以及牙醫實驗排課。
2. `classcompare.py`單獨運行時可以輸出中乙與醫學系同時上課的日期(若欲運行此功能需將第102行程式碼從註解形式改回程式形式)。
3. 單獨運行`DenMain.py`模組時可進行牙醫排課。
4. 單獨運行`classmenu.py`模組可進行中乙排課。
5. 運行`add_new_class_to_courselist.py`模組可自動查詢某堂課的上課時間，並將該堂課的詳細資訊寫入`courselist.json`中，方便排課。

## 安裝

要使用`ClassCompare`，您需要在系統上安裝Python。您可以從官方網站[python.org](https://www.python.org/)下載Python。

安裝完Python後，您可以使用以下命令將此repository下載到本機：

```
git clone https://github.com/Walther-Chen/ClassCompare.git
```

## 使用方法
要在您的機器上運行`classmenu.py`，請按照以下步驟進行操作：

1. 開啟終端機（Terminal）應用程式。
2. 執行以下命令以運行`classmenu.py`：
    ```
    python classmenu.py
    ```
3. 程式將開始運行，並根據您的需求進行衝堂處理與排課。

請確保您已經安裝了Python並且已經成功下載了`ClassCompare`的程式碼庫。

## 貢獻

- [WaltherChen](https://github.com/WalterChen)
- [kblab2024](https://github.com/kblab2024)

## 許可證
- [MIT licence](https://opensource.org/licenses/MIT)
