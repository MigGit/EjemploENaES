from transformers import MarianMTModel, MarianTokenizer

# Cargar el modelo y el tokenizador
model_name = 'Helsinki-NLP/opus-mt-es-en'
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Texto a traducir
texto_es = "Hola, ¿cómo estás?"

# Codificar el texto en español
texto_es_codificado = tokenizer(texto_es, return_tensors="pt")

# Realizar la traducción
texto_traducido = model.generate(**texto_es_codificado, max_length=128)

# Decodificar el texto traducido en inglés
texto_traducido_decodificado = tokenizer.decode(texto_traducido[0], skip_special_tokens=True)

# Imprimir el texto traducido
print(' ', texto_traducido_decodificado,' ', sep='\n')