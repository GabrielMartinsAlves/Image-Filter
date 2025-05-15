import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk, ImageFilter, ImageOps, ImageEnhance
import os

class EditorImagem:
    def __init__(self, janela):
        self.janela = janela
        self.imagem_atual = None
        self.imagem_transformada = None
        self.imagem_original = None

        self.janela.title("Editor de Imagens")
        self.janela.geometry("1000x700")
        self.janela.minsize(800, 600)
        self.janela.config(bg="#f5f5f7")

        self.criar_interface()

    def criar_interface(self):
        self.configurar_estilo()

        self.frame_principal = tk.Frame(self.janela, bg="#f5f5f7", padx=15, pady=15)
        self.frame_principal.pack(fill=tk.BOTH, expand=True)

        titulo_frame = tk.Frame(self.frame_principal, bg="#f5f5f7")
        titulo_frame.pack(fill=tk.X, pady=(0, 15))

        titulo_label = tk.Label(titulo_frame, text="EDITOR DE IMAGENS", font=("Helvetica", 16, "bold"), bg="#f5f5f7", fg="#333333")
        titulo_label.pack()

        subtitulo_label = tk.Label(titulo_frame, text="Selecione uma imagem para começar", font=("Helvetica", 10), bg="#f5f5f7", fg="#666666")
        subtitulo_label.pack(pady=(0, 5))

        self.frame_imagens = tk.Frame(self.frame_principal, bg="#f5f5f7")
        self.frame_imagens.pack(fill=tk.BOTH, expand=True)

        self.frame_imagens.columnconfigure(0, weight=1)
        self.frame_imagens.columnconfigure(1, weight=1)
        self.frame_imagens.rowconfigure(0, weight=1)

        self.frame_original = tk.LabelFrame(self.frame_imagens, text="Imagem Original", font=("Helvetica", 11, "bold"), bg="#f5f5f7", fg="#333333", padx=8, pady=8)
        self.frame_original.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

        self.frame_resultado = tk.LabelFrame(self.frame_imagens, text="Resultado", font=("Helvetica", 11, "bold"), bg="#f5f5f7", fg="#333333", padx=8, pady=8)
        self.frame_resultado.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

        self.canvas_original = tk.Canvas(self.frame_original, bg="white", bd=0, highlightthickness=0)
        self.canvas_original.pack(fill=tk.BOTH, expand=True)

        self.canvas_resultado = tk.Canvas(self.frame_resultado, bg="white", bd=0, highlightthickness=0)
        self.canvas_resultado.pack(fill=tk.BOTH, expand=True)

        self.frame_botoes = tk.Frame(self.frame_principal, bg="#f5f5f7", pady=10)
        self.frame_botoes.pack(fill=tk.X)

        ttk.Separator(self.frame_principal, orient='horizontal').pack(fill=tk.X, pady=(5, 15))

        self.criar_botoes()

    def configurar_estilo(self):
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 10), padding=6)
        style.configure("Accent.TButton", background="#0078D7", foreground="white")
        style.configure("Tool.TButton", padding=7)

    def criar_botoes(self):
        for linha, botoes in enumerate([
            [("Abrir Imagem", self.abrir_imagem), ("Escala de Cinza", self.aplicar_escala_cinza),
             ("Inverter Cores", self.inverter_cores), ("Salvar Imagem", self.salvar_imagem)],
            [("+ Desfoque", self.aplicar_desfoque), ("+ Nitidez", self.aplicar_nitidez),
             ("+ Contraste", self.aumentar_contraste), ("Rotacionar 90°", self.rotacionar_imagem)],
            [("Aumentar (50%)", lambda: self.redimensionar_imagem(1.5)), ("Diminuir (50%)", lambda: self.redimensionar_imagem(0.5)),
             ("Restaurar Original", self.restaurar_original), ("Ajustar à Janela", self.ajustar_a_janela)]
        ]):
            frame = tk.Frame(self.frame_botoes, bg="#f5f5f7")
            frame.pack(fill=tk.X, pady=3)
            for col, (texto, comando) in enumerate(botoes):
                ttk.Button(frame, text=texto, style="Tool.TButton", command=comando, width=15).grid(row=0, column=col, padx=5, pady=3)
                frame.grid_columnconfigure(col, weight=1)

    def abrir_imagem(self):
        arquivo = filedialog.askopenfilename(title="Selecione a imagem", filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if arquivo:
            try:
                self.imagem_atual = Image.open(arquivo)
                self.imagem_original = self.imagem_atual.copy()
                self.imagem_transformada = self.imagem_atual.copy()
                self.atualizar_paineis()
                nome_arquivo = os.path.basename(arquivo)
                subtitulo_label = self.frame_principal.winfo_children()[0].winfo_children()[1]
                subtitulo_label.config(text=f"Arquivo: {nome_arquivo}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao abrir a imagem: {e}")

    def atualizar_paineis(self):
        if self.imagem_original:
            self.canvas_original.delete("all")
            self.canvas_resultado.delete("all")
            largura_canvas = self.canvas_original.winfo_width() or 350
            altura_canvas = self.canvas_original.winfo_height() or 350
            img_original = self.redimensionar_para_exibicao(self.imagem_original.copy(), largura_canvas, altura_canvas)
            self.foto_original = ImageTk.PhotoImage(img_original)
            self.canvas_original.create_image(largura_canvas // 2, altura_canvas // 2, image=self.foto_original, anchor=tk.CENTER)
            self.atualizar_resultado()

    def atualizar_resultado(self):
        if self.imagem_transformada:
            self.canvas_resultado.delete("all")
            largura_canvas = self.canvas_resultado.winfo_width() or 350
            altura_canvas = self.canvas_resultado.winfo_height() or 350
            img_resultado = self.redimensionar_para_exibicao(self.imagem_transformada.copy(), largura_canvas, altura_canvas)
            self.foto_resultado = ImageTk.PhotoImage(img_resultado)
            self.canvas_resultado.create_image(largura_canvas // 2, altura_canvas // 2, image=self.foto_resultado, anchor=tk.CENTER)

    def redimensionar_para_exibicao(self, imagem, largura_max, altura_max):
        largura_img, altura_img = imagem.size
        if largura_img > largura_max or altura_img > altura_max:
            ratio = min(largura_max / largura_img, altura_max / altura_img)
            nova_largura = int(largura_img * ratio)
            nova_altura = int(altura_img * ratio)
            return imagem.resize((nova_largura, nova_altura), Image.LANCZOS)
        return imagem

    def aplicar_escala_cinza(self):
        if self.imagem_transformada:
            self.imagem_transformada = self.imagem_transformada.convert("L").convert("RGB")
            self.atualizar_resultado()

    def inverter_cores(self):
        if self.imagem_transformada:
            self.imagem_transformada = ImageOps.invert(self.imagem_transformada.convert("RGB"))
            self.atualizar_resultado()

    def aplicar_desfoque(self):
        if self.imagem_transformada:
            self.imagem_transformada = self.imagem_transformada.filter(ImageFilter.BLUR)
            self.atualizar_resultado()

    def aplicar_nitidez(self):
        if self.imagem_transformada:
            self.imagem_transformada = self.imagem_transformada.filter(ImageFilter.SHARPEN)
            self.atualizar_resultado()

    def aumentar_contraste(self):
        if self.imagem_transformada:
            self.imagem_transformada = ImageEnhance.Contrast(self.imagem_transformada).enhance(1.5)
            self.atualizar_resultado()

    def rotacionar_imagem(self):
        if self.imagem_transformada:
            self.imagem_transformada = self.imagem_transformada.rotate(-90, expand=True)
            self.atualizar_resultado()

    def redimensionar_imagem(self, fator):
        if self.imagem_transformada:
            largura, altura = self.imagem_transformada.size
            nova_largura = int(largura * fator)
            nova_altura = int(altura * fator)
            self.imagem_transformada = self.imagem_transformada.resize((nova_largura, nova_altura), Image.LANCZOS)
            self.atualizar_resultado()

    def ajustar_a_janela(self):
        if self.imagem_transformada:
            largura_disponivel = self.canvas_resultado.winfo_width() - 20 or 350
            altura_disponivel = self.canvas_resultado.winfo_height() - 20 or 350
            largura_img, altura_img = self.imagem_transformada.size
            ratio = min(largura_disponivel / largura_img, altura_disponivel / altura_img)
            nova_largura = int(largura_img * ratio)
            nova_altura = int(altura_img * ratio)
            self.imagem_transformada = self.imagem_transformada.resize((nova_largura, nova_altura), Image.LANCZOS)
            self.atualizar_resultado()

    def restaurar_original(self):
        if self.imagem_original:
            self.imagem_transformada = self.imagem_original.copy()
            self.atualizar_resultado()

    def salvar_imagem(self):
        if self.imagem_transformada:
            arquivo = filedialog.asksaveasfilename(defaultextension=".png", initialfile="imagem_editada.png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp"), ("GIF", "*.gif")])
            if arquivo:
                try:
                    self.imagem_transformada.save(arquivo)
                    messagebox.showinfo("Sucesso", "Imagem salva com sucesso!")
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao salvar a imagem: {e}")

if __name__ == "__main__":
    janela = tk.Tk()
    app = EditorImagem(janela)
    janela.bind("<Configure>", lambda event: app.atualizar_paineis() if hasattr(app, 'imagem_original') and app.imagem_original else None)
    janela.mainloop()
