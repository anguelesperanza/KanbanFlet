import flet as ft

def main(page: ft.Page):

    # Nested functions is a thing apparently??????
    def add_to_todo(e):
        if kanban_add.value:
            todo_col.controls.append(
                ft.Draggable(
                    group="kan",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.ORANGE,
                        border_radius=5,
                        content=ft.Text(kanban_add.value,size=20),
                        alignment=ft.alignment.center,
                    )
                )
            )
            page.update()



    kanban_add = ft.TextField(hint_text="New Kanban Task!")
    kanban_add_button = ft.ElevatedButton("Add", on_click=add_to_todo)

    todo_col = ft.Column(
        spacing=10,
        width = 70,
        height = page.window_height - 50,
        scroll=ft.ScrollMode.ALWAYS,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    doing_col = ft.Column(
        spacing=10,
        width = 70,
        height = page.window_height - 50,
        scroll=ft.ScrollMode.ALWAYS,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,        
    )

    done_col = ft.Column(
        spacing=10,
        width = 70,
        height = page.window_height - 50,
        scroll=ft.ScrollMode.ALWAYS,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,        
    )

    page.add(
        ft.Row([
            kanban_add, kanban_add_button
        ]),
        ft.Row([
            ft.Container(todo_col, border=ft.border.all(1)),
            ft.Container(doing_col, border=ft.border.all(1)),
            ft.Container(done_col, border=ft.border.all(1)),

        ])
    )

        # ft.Container(todo_col, border=ft.border.all(1))


ft.app(target=main)