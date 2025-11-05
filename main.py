import PIL
import pytesseract
import keyboard
import pyautogui
import dotenv
dotenv.load_dotenv()
from openai import OpenAI
client = OpenAI()

pos_1_x = 0
pos_1_y = 0

pos_2_x = 0
pos_2_y = 0

a_pressed = 0
b_pressed = 0

while True:
    if keyboard.is_pressed("a") and a_pressed != 1:
        pos_1_x, pos_1_y = pyautogui.position()
        a_pressed = 1
        print("'a' pressed")

    if keyboard.is_pressed("b") and b_pressed != 1:
        pos_2_x, pos_2_y = pyautogui.position()
        b_pressed = 1
        print("'b' pressed")


    if a_pressed == 1 and b_pressed == 1:
        image = PIL.ImageGrab.grab(bbox=(pos_1_x, pos_1_y, pos_2_x, pos_2_y))

        question = pytesseract.image_to_string(image)
        print(question)



        response = client.responses.create(
            model="gpt-5-nano",
            input=f"Answer this question with either 1, 2, 3, 4, etc. corresponding to the number answer it is from the question: {question}"
        )

        
        answer = response.output_text
        print(answer)

        if int(answer) == 1:
            pyautogui.moveTo((0, 0))
        elif int(answer) == 2:
            pyautogui.moveTo((2500, 0))
        elif int(answer) == 3:
            pyautogui.moveTo((0, 1500))
        elif int(answer) == 4:
            pyautogui.moveTo((2500, 1500))

        a_pressed = 0
        b_pressed = 0