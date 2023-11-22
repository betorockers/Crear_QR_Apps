# ACA TENDREMOS LA CLASE QUE LE DARA ESTRUCTURA A NUESTRO DISEÑO MAESTRO

import tkinter as tk #! => para la ventana
from tkinter import ttk #! => para los estilos, mas witget, etc
import util.util_ventana as util_ven #! => para centrar y ponerle el tamaño a la ventana
import util.util_img as util_img #! => para redimensionar nuestras imagenes y utilizarlas
import config as conf #! => para la configuracion de los colores de la ventana

class FormMasterDesign(tk.Tk):
    
    #* instanciacion de los objetos
    def __init__(self):
        super().__init__()
        self.qr_guardado = None
        self.qr_img_base = util_img.leer_imagen("img\QR_base.png", (330, 330))
        self.qr_mensaje = util_img.leer_imagen("img\Scan_me.png", (300, 200))
        self.config_window()
        self.paneles()
        self.widget_panel_superior()
        self.widget_panel_inferior()
        
    #* configuracion de la ventana principal
    def config_window(self):
        self.title("Diseña tu propio código QR")
        self.iconbitmap("img\logo_ico.ico")
        w, h = 800, 450
        util_ven.centrar_ventana(self, w, h)
    
    def paneles(self):
        #* barra superior 
        self.barra_superior = tk.Frame(self,)
        self.barra_superior.pack(side=tk.TOP, fill='both', expand=True)
        
        #* barra superior izquierda
        self.barra_superior_izq = tk.Frame(
            self.barra_superior, bg=conf.color_barra_superior_izq
        )
        self.barra_superior_izq.pack(side=tk.LEFT, fill='both', expand=True)
        
        #* barra superior derecha
        self.barra_superior_der = tk.Frame(
            self.barra_superior, bg=conf.color_barra_superior_der
        )
        self.barra_superior_der.pack(side=tk.RIGHT, fill='both', expand=True)
        
        #* barra inferior
        self.barra_inferior = tk.Frame(
            self, bg=conf.color_barra_inferior, height=50
        )
        self.barra_inferior.pack(side=tk.BOTTOM, fill='x', expand=False)
        
        
    #* widget para el panel superior
    def widget_panel_superior(self):
        self.labelTitulo = tk.Label(
            self.barra_superior_izq, text="Crea tu codigo QR aquí", bg=conf.color_barra_superior_izq
        )
        self.labelTitulo.config(fg="#000000", font=("Roboto", 16, "bold"), pady=10, width=25)
        self.labelTitulo.pack(side=tk.TOP, expand=False, pady=20)
        
        #* estilos para la entrada de datos 
        estilo = ttk.Style()
        estilo.configure("EstiloEntry.TEntry", padding=(10, 5, 10, 5), relief="flat")
        
        self.entrada_texto = ttk.Entry(
            self.barra_superior_izq, width=50, style="EstiloEntry.TEntry"
        )
        self.entrada_texto.pack(side=tk.TOP, expand=False, pady=20)
        
        #! acciones para las entradas y caja de texto
        
        self.placeholder_text = "Escribe tu texto aquí"
        self.entrada_texto.insert(0, self.placeholder_text)
        self.entrada_texto.bind("<FocusIn>", self.on_entry_focus_in)
        self.entrada_texto.bind("<FocusOut>", self.on_entry_focus_out)
        
        #* mensaje al usuario panel izquierdo
        self.etiqueta_mensaje = ttk.Label(self.barra_superior_izq, image=self.qr_mensaje)
        self.etiqueta_mensaje.pack(side=tk.TOP, expand=True, pady=20, padx=20)
        
        #* etiqueta panel derecho
        self.etiqueta_qr = ttk.Label(self.barra_superior_der, image=self.qr_img_base)
        self.etiqueta_qr.pack(side=tk.TOP, expand=True, pady=20, padx=20)
        
    #* widget para el panel inferior(boton)
    def widget_panel_inferior(self):
        #? boton para generar codigo QR
        self.boton_generar = tk.Button(
            self.barra_inferior, text="Generar QR", width=15, height=2, bg=conf.color_boton, fg=conf.color_texto_boton, 
            relief=tk.RAISED, padx=5, pady=5, overrelief='flat', command=self.on_button_click_mostrar_qr
        )
        self.boton_generar.pack(side=tk.RIGHT, expand=False, padx=10, pady=10)
        
        #? boton para descargar codigo QR
        self.boton_descargar = tk.Button(
            self.barra_inferior, text="Descargar QR", width=15, height=2, bg=conf.color_boton,fg=conf.color_texto_boton,
            relief=tk.RAISED, padx=5, pady=5, overrelief='flat', command=self.on_button_click_guardar_qr
        )
        self.boton_descargar.pack(side=tk.RIGHT, expand=False, padx=10, pady=10)
        
        
        
    #! clases de funcionalidad
    def on_button_click_mostrar_qr(self):
        pass
    
    def on_button_click_guardar_qr(self):
        pass
    
    def on_entry_focus_in(self, event):
        pass
    
    def on_entry_focus_out(self, event):
        pass
        
        
        
