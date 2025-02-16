import flet as ft
import requests

API_BASE_URL = "http://localhost:8000/api"

def main(page: ft.Page):
    page.title = "Exemplo"

#Criar aluno ABA

    nome_field = ft.TextField(label="Nome")
    email_field = ft.TextField(label="Email")
    faixa_field = ft.TextField(label="Faixa")
    data_nascimento_field = ft.TextField(label="Data de Nascimento (YYYY-MM-DD)")
    create_result = ft.Text()

    def criar_aluno_click(e):
        payload = {
            "nome": nome_field.value,
            "email": email_field.value,
            "faixa": faixa_field.value,
            "data_nascimento": data_nascimento_field.value,
        }

        response = requests.post(API_BASE_URL + '/', json=payload)

        if response.status_code == 200:
            aluno = response.json()
            create_result.value = f'Aluno criado: {aluno}'
        else:
            create_result.value = f"Erro: {response.text}"
        page.update()

    create_button = ft.ElevatedButton(text="Criar Aluno", on_click=criar_aluno_click)

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

#Listar aluno ABA

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Criar Aluno", content=criar_aluno_tab)
            ]
    )

    page.add(tabs)

if __name__ == "__main__":
    ft.app(target=main)