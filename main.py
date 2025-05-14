import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageFilter, ImageOps, ImageEnhance

def abrir_imagem():
    arquivo = filedialog.askopenfilename(title="Selecione a imagem", filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if arquivo:
        global imagem_atual, imagem_transformada
        imagem_atual = Image.open(arquivo)
        imagem_transformada = imagem_atual.copy()
        imagem_atual.thumbnail((300, 300))
        img_tk = ImageTk.PhotoImage(imagem_atual)
        painel_imagem_original.config(image=img_tk)
        painel_imagem_original.image = img_tk
        painel_imagem_resultado.config(image=img_tk)
        painel_imagem_resultado.image = img_tk

def aplicar_escala_cinza():
    global imagem_transformada
    if imagem_atual:
        imagem_transformada = imagem_atual.convert("L")
        img_tk = ImageTk.PhotoImage(imagem_transformada)
        painel_imagem_resultado.config(image=img_tk)
        painel_imagem_resultado.image = img_tk

def inverter_cores():
    global imagem_transformada
    if imagem_atual:
        imagem_transformada = ImageOps.invert(imagem_atual.convert("RGB"))
        img_tk = ImageTk.PhotoImage(imagem_transformada)
        painel_imagem_resultado.config(image=img_tk)
        painel_imagem_resultado.image = img_tk

def aplicar_desfoque():
    global imagem_transformada
    if imagem_atual:
        imagem_transformada = imagem_atual.filter(ImageFilter.BLUR)
        img_tk = ImageTk.PhotoImage(imagem_transformada)
        painel_imagem_resultado.config(image=img_tk)
        painel_imagem_resultado.image = img_tk

def aplicar_nitidez():
    global imagem_transformada
    if imagem_atual:
        imagem_transformada = imagem_atual.filter(ImageFilter.SHARPEN)
        img_tk = ImageTk.PhotoImage(imagem_transformada)
        painel_imagem_resultado.config(image=img_tk)
        painel_imagem_resultado.image = img_tk

def aumentar_contraste():
    global imagem_transformada
    if imagem_atual:
        imagem_transformada = ImageEnhance.Contrast(imagem_atual).enhance(2)
        img_tk = ImageTk.PhotoImage(imagem_transformada)
        painel_imagem_resultado.config(image=img_tk)
        painel_imagem_resultado.image = img_tk

def salvar_imagem():
    if imagem_transformada:
        arquivo = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])
        if arquivo:
            imagem_transformada.save(arquivo)
            messagebox.showinfo("Sucesso", "Imagem salva com sucesso!")

def iniciar_interface():
    global imagem_atual, imagem_transformada, painel_imagem_original, painel_imagem_resultado

    janela = tk.Tk()
    janela.title("Visualizador de Imagens")
    janela.geometry("800x600")

    janela.config(bg="#f5f5f5")

    frame_imagens = tk.Frame(janela, bg="#f5f5f5")
    frame_imagens.pack(padx=20, pady=20)

    painel_imagem_original = tk.Label(frame_imagens, bg="#f5f5f5")
    painel_imagem_original.grid(row=0, column=0, padx=10, pady=10)

    painel_imagem_resultado = tk.Label(frame_imagens, bg="#f5f5f5")
    painel_imagem_resultado.grid(row=0, column=1, padx=10, pady=10)

    frame_botoes = tk.Frame(janela, bg="#f5f5f5")
    frame_botoes.pack(pady=10)

    cores_botao = ["#4CAF50", "#9E9E9E", "#FF5722", "#9C27B0", "#FA8107", "#673AB7"]

    btn_abrir = tk.Button(frame_botoes, text="Abrir Imagem", command=abrir_imagem, width=20, height=2, bg=cores_botao[0], fg="white", font=("Arial", 12))
    btn_abrir.grid(row=0, column=0, padx=10, pady=5)

    btn_gray = tk.Button(frame_botoes, text="Escala de Cinza", command=aplicar_escala_cinza, width=20, height=2, bg=cores_botao[1], fg="white", font=("Arial", 12))
    btn_gray.grid(row=0, column=1, padx=10, pady=5)

    btn_inverter = tk.Button(frame_botoes, text="Inverter Cores", command=inverter_cores, width=20, height=2, bg=cores_botao[2], fg="white", font=("Arial", 12))
    btn_inverter.grid(row=1, column=0, padx=10, pady=5)

    btn_blur = tk.Button(frame_botoes, text="Desfoque", command=aplicar_desfoque, width=20, height=2, bg=cores_botao[3], fg="white", font=("Arial", 12))
    btn_blur.grid(row=1, column=1, padx=10, pady=5)

    btn_sharpen = tk.Button(frame_botoes, text="Nitidez", command=aplicar_nitidez, width=20, height=2, bg=cores_botao[4], fg="white", font=("Arial", 12))
    btn_sharpen.grid(row=2, column=0, padx=10, pady=5)

    btn_contraste = tk.Button(frame_botoes, text="Aumentar Contraste", command=aumentar_contraste, width=20, height=2, bg=cores_botao[5], fg="white", font=("Arial", 12))
    btn_contraste.grid(row=2, column=1, padx=10, pady=5)

    btn_salvar = tk.Button(frame_botoes, text="Salvar Imagem", command=salvar_imagem, width=20, height=2, bg=cores_botao[0], fg="white", font=("Arial", 12))
    btn_salvar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    imagem_atual = None
    imagem_transformada = None

    janela.mainloop()

if __name__ == "__main__":
    iniciar_interface()
