import flet as ft

def main(page: ft.Page):
    page.title = "Exemplo"

    nome_field = ft.TextField(label="Nome")
    email_field = ft.TextField(label="Email")
    faixa_field = ft.TextField(label="Faixa")
    data_nascimento_field = ft.TextField(label="Data de Nascimento (YYYY-MM-DD)")
    create_result = ft.Text()

    create_button = ft.ElevatedButton(text="Criar Aluno")

    criar_aluno_tab = ft.Column(
        [
            nome_field,
            email_field,
            faixa_field,
            data_nascimento_field,
            create_result,
            create_button,
        ],
        scroll=True
    )

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Criar Aluno", content=criar_aluno_tab)
            ]
    )

    page.add(tabs)

if __name__ == "__main__":
    ft.app(target=main)