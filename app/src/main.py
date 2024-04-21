import flet as ft
import sys as sis

# VARIABLES
LIMIT_VD1_MAX=200
LIMIT_VD1_MIN=100

LIMIT_VD2_MAX=200
LIMIT_VD2_MIN=100

COLOR1="#f3ae35"
COLORR="#00e8b2"
COLOR2="#222222"

async def main(page: ft.Page):
    async def button_exit(e):
        await page.window_destroy_async()
        await page.update_async()
    async def button_maximize(e):
        page.window_height = 1080
        page.window_width = 1920
        await page.update_async()
    async def button_minimize(e):
        page.window_minimized=True
        await page.update_async()
    
    page.window_height = 600   
    page.window_width = 600
    page.window_resizable = True
    # page.window_movable = True
    page.title = "PAYMENTS"
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.padding = 0
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.WIFI),
        leading_width=10,
        title=ft.Text("PAYMENTS"),
        center_title=False,
        bgcolor=COLOR1,
        actions=[
            ft.IconButton(ft.icons.MAXIMIZE_ROUNDED, icon_color=COLOR2, on_click=button_maximize),
            ft.IconButton(ft.icons.MINIMIZE_SHARP, icon_color=COLOR2, on_click=button_minimize),
            ft.IconButton(ft.icons.EXIT_TO_APP, icon_color=COLOR2, on_click=button_exit),
        ],
    )

    async def move_vertical_divider1(e: ft.DragUpdateEvent):
        if (e.delta_x > 0 and left01.width < LIMIT_VD1_MAX) or (e.delta_x < 0 and left01.width > LIMIT_VD1_MIN):
            left01.width += e.delta_x
        await left01.update_async()

    async def move_vertical_divider2(e: ft.DragUpdateEvent):
        if (e.delta_x > 0 and left02.width < LIMIT_VD2_MAX) or (e.delta_x < 0 and left02.width > LIMIT_VD2_MIN):
            left02.width += e.delta_x
        await left02.update_async()

    async def show_draggable_cursor(e: ft.HoverEvent):
        e.control.mouse_cursor = ft.MouseCursor.RESIZE_LEFT_RIGHT
        await e.control.update_async()

    left01 = ft.Container(
        bgcolor=COLOR1,
        alignment=ft.alignment.center,
        width=100,
    )
    left02 = ft.Container(
        bgcolor= COLOR1,
        alignment=ft.alignment.center,
        width=100,
    )
    right01 = ft.Container(
        bgcolor= COLOR1,
        alignment=ft.alignment.center,
        expand=1,
    )

    gestureDetector1 = ft.GestureDetector(
        content=ft.VerticalDivider(),
        drag_interval=10,
        on_pan_update=move_vertical_divider1,
        on_hover=show_draggable_cursor,
    )

    gestureDetector2 = ft.GestureDetector(
        content=ft.VerticalDivider(),
        drag_interval=10,
        on_pan_update=move_vertical_divider2,
        on_hover=show_draggable_cursor,
    )

    row = ft.Row(spacing=10, controls=[
        left01,
        gestureDetector1,
        left02,
        gestureDetector2,
        right01,
    ])

    container = ft.Container(row,
                              width=1920, 
                              height=1080 ,
                              bgcolor=COLOR1, 
                              alignment=ft.alignment.bottom_center)
    await page.add_async(container)
    pass
# ft.app(port=3000,target=main,assets_dir="assets", view=ft.AppView.WEB_BROWSER)
ft.app(target=main, assets_dir="assets") 