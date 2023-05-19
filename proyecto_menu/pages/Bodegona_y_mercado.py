import streamlit as st
import pandas as pd

df = pd.read_csv("proyecto_menu/pages/bodegona.csv")
edited_df = st.experimental_data_editor(df)

if 'menu_y_bode' not in st.session_state:
    st.session_state['menu_y_bode'] = 0

if 'liste_finale_bode' not in st.session_state:
    st.session_state['liste_finale_bode'] = False
#----------------------------------------------- Ajout des produits séléctionés dans une liste------------------------#
productos = {}
selected_products = {}

for index, row in edited_df.iterrows():
    if row['AGREGAR']:
        # Récupération des informations du produit
        product_name = row['PRODUCTO']
        qty_product = row['QTDAD']
        price_product = row['PRECIO']
        total_product = qty_product * price_product

        # Ajout du produit au dictionnaire productos
        if product_name not in productos:
            productos[product_name] = {
                'QTDAD': qty_product,
                'PRECIO': price_product,
                'TOTAL': total_product
            }
        else:
            productos[product_name]['QTDAD'] += qty_product
            productos[product_name]['TOTAL'] += total_product


for key, value in productos.items():
    selected_products[key] = value['QTDAD']

df_selected_productos = pd.DataFrame(productos)

if not df_selected_productos.empty:
    total_bode_merca = df_selected_productos.iloc[2, :].sum()
    st.write(f'El total por la bodegona y el mercado es de {total_bode_merca}')
    st.session_state['menu_y_bode'] = total_bode_merca
    qtite = list(df_selected_productos.loc['QTDAD'])
    produits = list(df_selected_productos.keys())
    df_final = pd.DataFrame(produits,columns=['Ingredientes'])
    df_final['Cantidad'] = qtite
    string_selected = df_final.to_string(index=False)

    st.write(df_final)
    st.session_state['liste_finale_bode'] = df_final
        #Export de la liste
    with open("Lista_bode.txt", "w") as fichier:
        fichier.write(string_selected)
        st.download_button(
            label="Descargar la lista",
            file_name='Lista_bode.txt',
            data=string_selected,
        )








