import flet as ft
from pdf2docx import Converter
import os

def main(page: ft.Page):
    """
    Función principal de la aplicación Flet para convertir PDF a Word.
    """
    page.title = "Convertidor de PDF a Word"
    page.padding = ft.padding.all(250)
    page.adaptive = True
    page.bgcolor = ft.Colors.BLACK87

    # Campo de texto para que el usuario inserte la ruta del archivo
    file_path_input = ft.TextField(
        label="Ruta del archivo PDF",
        hint_text="Copia y pega la ruta del archivo PDF aquí...",
        expand=True,
        border_radius=ft.border_radius.all(10),
        border_color=ft.Colors.PURPLE_ACCENT_700,
        text_style=ft.TextStyle(color=ft.Colors.WHITE),
        focused_border_color=ft.Colors.PURPLE_ACCENT_700
    )

    def convert_pdf_to_word(e):
        """Maneja el evento de conversión del archivo PDF a Word."""
        pdf_file_path = file_path_input.value
        
        # Validación del path
        if not pdf_file_path or not os.path.exists(pdf_file_path):
            page.add(ft.Text("El archivo PDF no existe o la ruta no es válida.", color=ft.Colors.RED))
            page.update()
            return

        try:
            # Convertir PDF a DOCX
            docx_file_path = pdf_file_path.replace('.pdf', '.docx')
            cv = Converter(pdf_file_path)
            cv.convert(docx_file_path, start=0, end=None)
            cv.close()

            page.add(ft.Text(f"Conversión completa: {docx_file_path}", color=ft.Colors.GREEN))
        except Exception as ex:
            page.add(ft.Text(f"Error durante la conversión: {str(ex)}", color=ft.Colors.RED))
        
        page.update()

    # Elementos de la interfaz
    texto_titulo = ft.Text("Convertidor de PDF a Word", size=28, color=ft.Colors.WHITE, weight="bold")

    boton_convertir = ft.ElevatedButton(
        text="Convertir a Word",
        on_click=convert_pdf_to_word,
        bgcolor=ft.Colors.PURPLE_ACCENT_700,
        color=ft.Colors.WHITE
    )
    
    # Añadir elementos a la página
    page.add(
        ft.Column(
            [
                texto_titulo,
                ft.Row(
                    [
                        file_path_input
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                boton_convertir
            ],
            horizontal_alignment="center",
            alignment="center",
            spacing=20
        )
    )

# Ejecutar la aplicación
ft.app(target=main)
