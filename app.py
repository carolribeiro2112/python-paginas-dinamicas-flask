from flask import Flask, render_template
from classes.curso import Curso

app = Flask(__name__)

@app.route('/')
def index():
  titulo = 'Página inicial' 
  conteudo = 'Agora sabemos criar páginas dinamicas'
  return render_template('index.html', titulo=titulo, conteudo=conteudo)

@app.route('/cursos')
def cursos():
  lista_de_cursos = ['Desenvolvimento web', 'Programação orientada a objetos']
  return render_template('cursos.html', lista=lista_de_cursos)

@app.route('/curso/<nome>')
def curso_por_nome(nome):
  if nome == 'devweb':
    info = Curso('Desenvolvimento Web', 'Disciplina que lida com as tecnologias da Web')
    habilidades = ['HTML','CSS', 'JavaScript']
    return render_template("info_curso.html", objeto=info, dificuldade=2, habilidades=habilidades)
  elif nome == 'poo':
    info = Curso('Programação Orientada a Objetos', 'Disciplina que ensina o paradigma orientado a objetos e técnicas avançadas de programação')
    habilidades = ['Dicionários', 'Tratamento de exceções', 'Classes', 'Herança']
    return render_template("info_curso.html", objeto=info, dificuldade=1 ,habilidades=habilidades)
  else:
    return "Curso inexistente"

if __name__ == '__main__':
  app.run(debug=True)