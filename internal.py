import flet as ft
import requestApi

api=requestApi.requestApi('')
print(api)

def mainPage(page: ft.Page):
    textTest=ft.TextField()
    btRequest=ft.ElevatedButton(text='Click', on_click=api)
    page.add(textTest, btRequest)
    page.update()
    return 
ft.app(mainPage)