from flask import Flask
import random
app = Flask(__name__)
@app.route("/")
def index():
    return f"""<h1>Hola, en esta página puedes aprender un par de cosas interesantes o apostar por si sale cara o sello.</h1></h1>
    <a href="/random_fact">¡Ver un dato al azar!</a>
    <a href="/datos_lectura">¡Ver un dato sobre la lectura!</a>
    <a href="/moneda">¿Cara o sello?</a>"""

@app.route("/random_fact")
def random_fact():
    facts_list = [
        "Los delfines tienen nombres específicos entre ellos.",
        "El corazón de un camarón está en su cabeza.",
        "La miel nunca se echa a perder.",
        "Los plátanos son bayas, pero las fresas no.",
        "Una nube promedio pesa alrededor de 1.1 millones de libras."
    ]
    return f'<p>{random.choice(facts_list)}</p>'


@app.route("/datos_lectura")
def datos_lectura():
    facts_list1 = [
        "La lectura reduce el estrés.",
        "La lectura puede ayudar con la depresión y la ansiedad.",
        "Leer te hace una persona más feliz.",
        "La lectura te convierte en una mejor persona .",
        "Al leer más, te vuelves más inteligente."
    ]
    return f'<p>{random.choice(facts_list1)}</p>'

@app.route("/moneda")
def moneda():
    facts_list2 = [
        "¡Salió cara!.",
        "¡Salió sello!.",
        
    ]
    return f'<p>{random.choice(facts_list2)}</p>'


app.run(debug=True)