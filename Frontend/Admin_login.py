
"""
Nom du fichier       : Admin_login.py
Auteur               : Even
Date de création     : 15.01.2026
Date de modification : 23.01.2026
"""

import customtkinter as ctk

ctk.set_appearance_mode("light")


class LoginApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # === FENETRE PRINCIPALE ===

        self.title("ATELIER+ - Connexion")
        self.geometry("834x570")
        # "834x570"
        self.minsize(834, 570)

        self.configure(fg_color="#F2F5FA")

        # === CONFIGURATION GRID ===

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # ==================================================
        # PARTIE GAUCHE
        # ==================================================

        self.left = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="#192235"
        )

        self.left.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        # LOGO

        self.logo = ctk.CTkLabel(
            self.left,
            text="ATELIER+",
            font=ctk.CTkFont(
                family="Arial",
                size=19,
                weight="bold"
            ),
            text_color="#FFFFFF"
        )

        self.logo.place(
            x=41,
            y=49
        )

        self.logo_subtitle = ctk.CTkLabel(
            self.left,
            text="GESTION DES RÉPARATIONS",
            font=ctk.CTkFont(size=7),
            text_color="#B8C0CE"
        )

        self.logo_subtitle.place(
            x=42,
            y=79
        )

        # TEXTE PRINCIPAL

        self.welcome_title = ctk.CTkLabel(
            self.left,
            text="Bienvenue dans votre\nespace de gestion.",
            font=ctk.CTkFont(
                family="Arial",
                size=18,
                weight="bold"
            ),
            text_color="#FFFFFF",
            justify="left"
        )

        self.welcome_title.place(
            x=41,
            y=192
        )

        # DESCRIPTION

        self.welcome_description = ctk.CTkLabel(
            self.left,
            text=(
                "Connectez-vous avec votre compte administrateur\n"
                "pour gérer les clients, appareils et interventions."
            ),
            font=ctk.CTkFont(size=8),
            text_color="#C5CBD5",
            justify="left"
        )

        self.welcome_description.place(
            x=42,
            y=269
        )

        # PIED DE PAGE

        self.footer = ctk.CTkLabel(
            self.left,
            text="ATELIER+  •  APPLICATION INTERNE",
            font=ctk.CTkFont(size=7),
            text_color="#AAB3C2"
        )

        self.footer.place(
            x=42,
            y=526
        )

        # ==================================================
        # PARTIE DROITE
        # ==================================================

        self.right = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="#F2F5FA"
        )

        self.right.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        # CARTE DE CONNEXION

        self.login_card = ctk.CTkFrame(
            self.right,
            width=354,
            height=385,
            corner_radius=10,
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#DCE3ED"
        )

        self.login_card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        self.login_card.pack_propagate(False)

        # ==================================================
        # TITRE
        # ==================================================

        self.title_label = ctk.CTkLabel(
            self.login_card,
            text="Connexion administrateur",
            font=ctk.CTkFont(
                family="Arial",
                size=16,
                weight="bold"
            ),
            text_color="#202939"
        )

        self.title_label.place(
            x=27,
            y=26
        )

        self.subtitle = ctk.CTkLabel(
            self.login_card,
            text="Veuillez saisir vos identifiants pour continuer.",
            font=ctk.CTkFont(size=8),
            text_color="#8792A5"
        )

        self.subtitle.place(
            x=27,
            y=56
        )

        # ==================================================
        # IDENTIFIANT
        # ==================================================

        self.username_label = ctk.CTkLabel(
            self.login_card,
            text="IDENTIFIANT",
            font=ctk.CTkFont(size=7),
            text_color="#202939"
        )

        self.username_label.place(
            x=27,
            y=100
        )

        self.username_entry = ctk.CTkEntry(
            self.login_card,
            width=298,
            height=31,
            corner_radius=5,
            border_width=1,
            border_color="#DCE3ED",
            fg_color="#FFFFFF",
            text_color="#202939",
            placeholder_text="Nom d'utilisateur ou adresse e-mail",
            placeholder_text_color="#8792A5",
            font=ctk.CTkFont(size=8)
        )

        self.username_entry.place(
            x=27,
            y=116
        )

        # ==================================================
        # MOT DE PASSE
        # ==================================================

        self.password_label = ctk.CTkLabel(
            self.login_card,
            text="MOT DE PASSE",
            font=ctk.CTkFont(size=7),
            text_color="#202939"
        )

        self.password_label.place(
            x=27,
            y=166
        )

        self.password_entry = ctk.CTkEntry(
            self.login_card,
            width=298,
            height=31,
            corner_radius=5,
            border_width=1,
            border_color="#DCE3ED",
            fg_color="#FFFFFF",
            text_color="#202939",
            placeholder_text="Mot de passe",
            placeholder_text_color="#8792A5",
            show="•",
            font=ctk.CTkFont(size=8)
        )

        self.password_entry.place(
            x=27,
            y=182
        )

        # ==================================================
        # MOT DE PASSE OUBLIE
        # ==================================================

        self.forgot_password = ctk.CTkButton(
            self.login_card,
            text="Mot de passe oublié ?",
            width=110,
            height=18,
            corner_radius=0,
            fg_color="transparent",
            hover_color="#F2F5FA",
            text_color="#3155B7",
            font=ctk.CTkFont(size=7)
        )

        self.forgot_password.place(
            x=215,
            y=216
        )

        # ==================================================
        # BOUTON CONNEXION
        # ==================================================

        self.login_button = ctk.CTkButton(
            self.login_card,
            text="Se connecter",
            width=298,
            height=32,
            corner_radius=6,
            fg_color="#3155B7",
            hover_color="#25449B",
            text_color="#FFFFFF",
            font=ctk.CTkFont(size=8)
        )

        self.login_button.place(
            x=27,
            y=255
        )

        # ==================================================
        # SEPARATEUR
        # ==================================================

        self.separator = ctk.CTkFrame(
            self.login_card,
            width=298,
            height=2,
            corner_radius=0,
            fg_color="#DCE3ED"
        )

        self.separator.place(
            x=27,
            y=310
        )

        # ==================================================
        # INFORMATIONS
        # ==================================================

        self.info1 = ctk.CTkLabel(
            self.login_card,
            text="Accès réservé aux comptes administrateur autorisés.",
            font=ctk.CTkFont(size=7),
            text_color="#8792A5"
        )

        self.info1.place(
            x=27,
            y=327
        )

        self.info2 = ctk.CTkLabel(
            self.login_card,
            text="Vos identifiants restent confidentiels.",
            font=ctk.CTkFont(size=7),
            text_color="#8792A5"
        )

        self.info2.place(
            x=27,
            y=349
        )

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
