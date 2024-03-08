"""Taller evaluable presencial"""

import nltk
import pandas as pd


def load_data(input_file):

    # file=open("input.txt", mode="r")
    # df=pd.DataFrame(file)
    # file.close()
    # return(print(df))
    df=pd.read_csv(input_file)
    return df
    """Lea el archivo usando pandas y devuelva un DataFrame"""
#print(load_data("input.txt"))

def create_fingerprint(df):

    """Cree una nueva columna en el DataFrame que contenga el fingerprint de la columna 'text'"""


    df = df.copy()
    df["key"]=df["text"]
    df["key"]=df["key"].str.strip() # me borra espacios en blanco inicio-final
    df["key"]=df["key"].str.lower() # Reemplazar todo por minuscula
    df["key"]=df["key"].str.replace("_","") # Reemplazar todo por minuscula
    df["key"]=df["key"].str.lower() # Reemplazar todo por minuscula
    df["key"] = df["key"].str.translate(
        str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")) # revisar notas al respecto
    df["key"]=df["key"].str.split()
    stemmer = nltk.PorterStemmer()
    df["key"] = df["key"].apply(lambda x: [stemmer.stem(word) for word in x])
    df["key"] = df["key"].apply(lambda x: sorted(set(x)))  # set un conjunto que no se repiten elementos
    # sorted ordena 
    df["key"]=df["key"].str.join(" ") # me uno los dos strings de la lista.

    # Toma las palabras individuales y devuelve la raiz.
    return df



    # 1. Copie la columna 'text' a la columna 'fingerprint'
    # 2. Remueva los espacios en blanco al principio y al final de la cadena
    # 3. Convierta el texto a minúsculas
    # 4. Transforme palabras que pueden (o no) contener guiones por su version sin guion.
    # 5. Remueva puntuación y caracteres de control
    # 6. Convierta el texto a una lista de tokens
    # 7. Transforme cada palabra con un stemmer de Porter
    # 8. Ordene la lista de tokens y remueve duplicados
    # 9. Convierta la lista de tokens a una cadena de texto separada por espacios

def generate_cleaned_column(df):
    """Crea la columna 'cleaned' en el DataFrame"""
    df = df.copy()
    df = df.sort_values(by=["key", "text"], ascending   =[True, True])
    keys = df.drop_duplicates(subset="key", keep="first")
    key_dict=dict(zip(keys["key"], keys["text"]))
    df["cleaned"] = df["key"].map(key_dict)

    # zip es un iterador :
    return df





  #  df = df.copy()

    # 1. Ordene el dataframe por 'fingerprint' y 'text'
    # 2. Seleccione la primera fila de cada grupo de 'fingerprint'
    # 3.  Cree un diccionario con 'fingerprint' como clave y 'text' como valor
    # 4. Cree la columna 'cleaned' usando el diccionario


def save_data(df, output_file):
    """Guarda el DataFrame en un archivo"""
    # Solo contiene una columna llamada 'texto' al igual
    # que en el archivo original pero con los datos limpios
    df = df.copy()
    df = df[["cleaned"]]
    df = df.rename(columns={"cleaned": "text"})
    df.to_csv(output_file, index=False)
    



df=load_data("input.txt")
df=create_fingerprint(df)
df=generate_cleaned_column(df)
print(df)



def main(input_file, output_file):
    """Ejecuta la limpieza de datos"""

    df = load_data(input_file)
    df = create_fingerprint(df)
    df = generate_cleaned_column(df)
    df.to_csv("test.csv", index=False)
    save_data(df, output_file)


if __name__ == "__main__":
     main(
         input_file="input.txt",
         output_file="output.txt",
     )
