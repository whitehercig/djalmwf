import asyncio 
import flet as ft

async def main(page: ft.Page) ->None:
    page.title = 'Hackaton clicker'
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "blue"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {"FulboArgenta": "fonts/FulboArgenta.ttf"}
    page.theme = ft.Theme(font_family="FurboArgenta")

    async def score_up(event: ft.ContainerTapEvent) -> None:
        score.data += 1
        score.value = str(score.data)

        image.scale = 0.95
        
        await page.update_async()
        
        await asyncio.sleep(0.1)
        image.scale = 1
        await page.update_async()

    score = ft.Text(value="0", size = 100, data = 0)
    score_counter = ft.Text(size=50, animate_opacity = ft.Animation(duration=600, curve = ft.AnimationCurve.BOUNCE_IN)) 

    image = ft.Image(
        src = "https://e7.pngegg.com/pngimages/487/888/png-clipart-snake-ball-python-reptile-cartoon-african-rock-python-snake-cartoon-animals-shoe.png",
        fit = ft.ImageFit.CONTAIN, 
        width=30,
        height = 30,
        animate_scale = ft.Animation(duration=600, curve = ft.AnimationCurve.EASE)
    )

    progress_bar = ft.ProgressBar(
        value = 0, #0-1
        width = page.width - 100,
        bar_height= 20,
        color = "#ff8b1f",
        bgcolor = "#bf6524",
    )

    await page.add_async(
        score,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            on_click = score_up,
            margin = ft.Margin(0,0,0,30)  
        ),
        ft.Container(
            content=progress_bar,
            border_radius = ft.BorderRadius(10,10,10,10)
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
