import flet as ft
import requests

def main(page: ft.Page):
    page.title="Погода"
    page.theme_mode='dark'  #light
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    
    user_data=ft.TextField(label="Введите город",width=400)
    weather_data=ft.Text('')
    feels_like_data=ft.Text('')
    pressure_data=ft.Text('')
    temp_max_data=ft.Text('')
    temp_min_data=ft.Text('')
    humidity_data=ft.Text('')
    wind_speed_data=ft.Text('')
    sunset_data=ft.Text('')




    def get_info(e):
        if len(user_data.value)<2:
            return
        API='a1dafd748ba7dcc10adf20bf27d5a085'
        URL=f'https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric'
        res=requests.get(URL).json()
        temp=res['main']['temp']
        feels_like=res['main']['feels_like']
        pressure=res['main']['pressure']
        temp_max=res['main']['temp_max']
        temp_min=res['main']['temp_min']
        humidity=res['main']['humidity']
        wind_speed=res['wind']['speed']
        sunset=res['sys']['sunset']



        weather_data.value='Погода:'+ str(temp)
        feels_like_data.value='Описание:'+  str(feels_like)
        pressure_data.value="Давление:"+  str(pressure)
        temp_max_data.value="Температура максимум:"+  str(temp_max)+"C"
        temp_min_data.value="Температура минимум:"+  str(temp_min)+"C"
        humidity_data.value="Влажность:"+  str(humidity)
        wind_speed_data.value="Скорость ветра:"+  str(wind_speed)+ "м\с"
        sunset_data.value="Закат :"+  str(sunset)
        page.update()


    def change_theme(e):
        page.theme_mode='light' if page.theme_mode=='dark' else 'dark'
        page.update()

    page.add(
        ft.Row(
            [
            ft.IconButton(ft.icons.SUNNY,on_click=change_theme),
            ft.Text('Погодная программа')
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data],  alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_data],  alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([feels_like_data],  alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([pressure_data],  alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([temp_max_data],  alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([temp_min_data],  alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([humidity_data],  alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([wind_speed_data],  alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([sunset_data],  alignment=ft.MainAxisAlignment.CENTER),
        
        ft.Row([ft.ElevatedButton(text='Получить',on_click=get_info)],alignment=ft.MainAxisAlignment.CENTER)
    )



ft.app(target=main)   