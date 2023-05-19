import pandas
import random
import streamlit as st
import pandas as pd



df_plat = pd.read_csv(r'proyecto_menu/plats.csv')
container_menu = st.container()



#-------------------------Fonctions-----------------------------------------------------------------
if 'validated_menu' not in st.session_state:
    st.session_state['validated_menu'] = False
if 'index_a_supprimer' not in st.session_state:
    st.session_state['index_a_supprimer'] = ""
if "menu" not in st.session_state:
    st.session_state["menu"] = 'test'
if 'confirmation_button_count' not in st.session_state:
    st.session_state['confirmation_button_count'] = 0
if 'montrer_confirmation_bouton' not in st.session_state:
    st.session_state['montrer_confirmation_bouton'] = False
if 'fin_du_menu' not in st.session_state:
    st.session_state['fin_du_menu'] = 0
if 'cumul_prix' not in st.session_state:
    st.session_state['cumul_prix'] = 0
if 'menu_y_bode' not in st.session_state:
    st.session_state['menu_y_bode'] = 0
if 'liste_finale_bode' not in st.session_state:
    st.session_state['liste_finale_bode'] = pd.DataFrame([])
if 'generation1' not in st.session_state:
    st.session_state.disabled = False



#--------------------centre-----------------------
container_menu.header("Menu de la semana")

edited_df_plat = st.experimental_data_editor(df_plat)

productos = {}
selected_products = {}

for index, row in edited_df_plat.iterrows():
    if row['AGREGAR']:
        # Récupération des informations du produit 1
        ingredient_name1 = row['Ingrediente 1']
        qty_product1 = row['Qtdad 1']
        price_product1 = row['Precio 1']
        total_product1 = qty_product1 * price_product1
        # Récupération des informations du produit 2
        ingredient_name2 = row['Ingrediente 2']
        qty_product2 = row['Qtdad 2']
        price_product2 = row['Precio 2']
        total_product2 = qty_product2 * price_product2
        # Récupération des informations du produit 3
        ingredient_name3 = row['Ingrediente 3']
        qty_product3 = row['Qtdad 3']
        price_product3 = row['Precio 3']
        total_product3 = qty_product3 * price_product3
        # Récupération des informations du produit 4
        ingredient_name4 = row['Ingrediente 4']
        qty_product4 = row['Qtdad 4']
        price_product4 = row['Precio 4']
        total_product4 = qty_product4 * price_product4
        # Récupération des informations du produit 5
        ingredient_name5 = row['Ingrediente 5']
        qty_product5 = row['Qtdad 5']
        price_product5 = row['Precio 5']
        total_product5 = qty_product5 * price_product5
        # Récupération des informations du produit 6
        ingredient_name6 = row['Ingrediente 6']
        qty_product6 = row['Qtdad 6']
        price_product6 = row['Precio 6']
        total_product6 = qty_product6 * price_product6
        # Récupération des informations du produit 7
        ingredient_name7 = row['Ingrediente 7']
        qty_product7 = row['Qtdad 7']
        price_product7 = row['Precio 7']
        total_product7 = qty_product7 * price_product7
        # Récupération des informations du produit 8
        ingredient_name8 = row['Ingrediente 8']
        qty_product8 = row['Qtdad 8']
        price_product8 = row['Precio 8']
        total_product8 = qty_product8 * price_product8
        # Récupération des informations du produit 9
        ingredient_name9 = row['Ingrediente 9']
        qty_product9 = row['Qtdad 9']
        price_product9 = row['Precio 9']
        total_product9 = qty_product9 * price_product9
        # Ajout du produit au dictionnaire productos
        if ingredient_name1 is not None:
            if ingredient_name1 not in productos:
                productos[ingredient_name1] = {
                    'QTDAD': qty_product1,
                    'PRECIO': price_product1,
                    'TOTAL': total_product1
                }
            else:
                productos[ingredient_name1]['QTDAD'] += qty_product1
                productos[ingredient_name1]['TOTAL'] += total_product1
        if ingredient_name2 is not None:
            if ingredient_name2 not in productos:
                productos[ingredient_name2] = {
                    'QTDAD': qty_product2,
                    'PRECIO': price_product2,
                    'TOTAL': total_product2
                }
            else:
                productos[ingredient_name2]['QTDAD'] += qty_product2
                productos[ingredient_name2]['TOTAL'] += total_product2
        if ingredient_name3 is not None:
            if ingredient_name3 not in productos:
                productos[ingredient_name3] = {
                    'QTDAD': qty_product3,
                    'PRECIO': price_product3,
                    'TOTAL': total_product3
                }
            else:
                productos[ingredient_name3]['QTDAD'] += qty_product3
                productos[ingredient_name3]['TOTAL'] += total_product3
        if ingredient_name4 is not None:
            if ingredient_name4 not in productos:
                productos[ingredient_name4] = {
                    'QTDAD': qty_product4,
                    'PRECIO': price_product4,
                    'TOTAL': total_product4
                }
            else:
                productos[ingredient_name4]['QTDAD'] += qty_product4
                productos[ingredient_name4]['TOTAL'] += total_product4

        if ingredient_name5 is not None:
            if ingredient_name5 not in productos:
                productos[ingredient_name5] = {
                    'QTDAD': qty_product5,
                    'PRECIO': price_product5,
                    'TOTAL': total_product5
                }
            else:
                productos[ingredient_name5]['QTDAD'] += qty_product5
                productos[ingredient_name5]['TOTAL'] += total_product5
        if ingredient_name6 is not None:
            if ingredient_name6 not in productos:
                productos[ingredient_name6] = {
                    'QTDAD': qty_product6,
                    'PRECIO': price_product6,
                    'TOTAL': total_product6
                }
            else:
                productos[ingredient_name6]['QTDAD'] += qty_product6
                productos[ingredient_name6]['TOTAL'] += total_product6
        if ingredient_name7 is not None:
            if ingredient_name7 not in productos:
                productos[ingredient_name7] = {
                    'QTDAD': qty_product7,
                    'PRECIO': price_product7,
                    'TOTAL': total_product7
                }
            else:
                productos[ingredient_name7]['QTDAD'] += qty_product7
                productos[ingredient_name7]['TOTAL'] += total_product7
        if ingredient_name8 is not None:
            if ingredient_name8 not in productos:
                productos[ingredient_name8] = {
                    'QTDAD': qty_product8,
                    'PRECIO': price_product8,
                    'TOTAL': total_product8
                }
            else:
                productos[ingredient_name8]['QTDAD'] += qty_product8
                productos[ingredient_name8]['TOTAL'] += total_product8
        if ingredient_name9 is not None:
            if ingredient_name9 not in productos:
                productos[ingredient_name9] = {
                    'QTDAD': qty_product9,
                    'PRECIO': price_product9,
                    'TOTAL': total_product9
                }
            else:
                productos[ingredient_name9]['QTDAD'] += qty_product9
                productos[ingredient_name9]['TOTAL'] += total_product9

for key, value in productos.items():
    selected_products[key] = value['QTDAD']

df_selected_productos = pd.DataFrame(productos)

if not df_selected_productos.empty:
    total_menu = df_selected_productos.iloc[2, :].sum()
    some_dispo = 1500 - st.session_state['menu_y_bode']
    st.write(f'El total por el menu de la semana es de {total_menu}')

    if (some_dispo - total_menu) < 0:
        st.warning(f'Suma disponible para la semana :  {some_dispo - total_menu}')
    else:
        st.write(f'Suma disponible para la semana :  {some_dispo - total_menu}')

    qtite = list(df_selected_productos.loc['QTDAD'])
    produits = list(df_selected_productos.keys())
    df_final = pd.DataFrame(produits,columns=['Ingredientes'])
    df_final['Cantidad'] = qtite
    df_final_dropna = df_final.dropna()
    string_selected = df_final_dropna.to_string(index=False)


total_bode_merca = st.session_state['menu_y_bode']
liste_bode = st.session_state['liste_finale_bode']

listes = [liste_bode, df_final_dropna]
final_df = pd.concat(listes)
st.write(final_df)
string_selected2 = final_df.to_string()

#Export de la liste
with open("final_list.txt", "w") as fichier:
    fichier.write(string_selected2)
    st.download_button(
        label="Descargar la lista",
        file_name='Menu.txt',
        data=string_selected2,
    )
