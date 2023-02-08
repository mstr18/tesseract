import win32gui
import win32ui
import win32con
import pyautogui
import time
import cv2
import pytesseract

def get_window_by_title(title):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) == title:
            hwnds.append(hwnd)
        return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds[0] if hwnds else None

def capture_window_screenshot(hwnd):
    # Obter as dimensões da janela
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width, height = right - left, bottom - top

    # Obter o contexto da janela
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)

    # Salvar a captura de tela como imagem
    saveBitMap.SaveBitmapFile(saveDC, "window_screenshot.bmp")

# Encontrar a janela pelo título
title = "Calculadora"
hwnd = get_window_by_title(title)

if hwnd:
    # Capturar a captura de tela da janela
    capture_window_screenshot(hwnd)
    print("Captura de tela salva como 'window_screenshot.bmp'")
else:
    print("A janela com o título '{}' não foi encontrada.".format(title))

# Load image
img = cv2.imread("tela2.png")

# Apply OCR
text = pytesseract.image_to_string(img)

# Extract numbers


with open("file.txt", "w") as file:
    # Write the string to the file
    file.write(text)