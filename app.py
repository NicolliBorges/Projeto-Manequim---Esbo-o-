# app.py
import os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import SelectField

app = Flask(__name__)

# ... (restante do código)

class MedidaForm(FlaskForm):
    class Meta:
        csrf = False
    altura = StringField('Altura')
    peso = StringField('Peso')
    cintura = StringField('Cintura')
    seios = StringField('Seios')
    quadril = StringField('Quadril')
    largura_ombro = StringField('Largura do Ombro')
    submit = SubmitField('Calcular IMC')

class RostoForm(FlaskForm):
    class Meta:
        csrf = False
        opcoes_cabelo = [('cabelo1', 'Cabelo 1'), ('cabelo2', 'Cabelo 2'), ('cabelo3', 'Cabelo 3')]
        cabelo = SelectField('cabelo', choices=opcoes_cabelo)
        cor_cabelo = SelectField('Cor do Cabelo', choices=[('castanho', 'Castanho'), ('loiro', 'Loiro'), ('preto', 'Preto')])
        sobrancelha = StringField('Sobrancelha')
        cor_sobrancelha = SelectField('Cor da Sobrancelha', choices=[('castanho', 'Castanho'), ('loiro', 'Loiro'), ('preto', 'Preto')])
        olhos = StringField('Olhos')
        cor_olhos = SelectField('Cor dos Olhos', choices=[('azul', 'Azul'), ('verde', 'Verde'), ('castanho', 'Castanho')])
        cilios = StringField('Cílios')
        nariz = StringField('Nariz')
        boca = StringField('Boca')
        orelhas = StringField('Orelhas')
        acessorios = StringField('Acessórios')
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
app = Flask(__name__, template_folder=template_dir)

@app.route('/calcular_imc', methods=['GET', 'POST'])
def calcular_imc():
    form = MedidaForm()
    imc = None  # Defina a variável imc para evitar o erro UnboundLocalError

    if form.validate_on_submit():
        # Lógica de cálculo do IMC
        altura = float(form.altura.data)
        peso = float(form.peso.data)
        imc = peso / (altura ** 2)

    return render_template('calcular_imc.html', form=form, imc=imc)

        # ...

@app.route('/criar_rosto', methods=['GET', 'POST'])
def criar_rosto():
    form = RostoForm()

    # Adicione esta linha para inicializar dados_rosto
    dados_rosto = {}

    if form.validate_on_submit():
        # Obter dados do formulário
        dados_rosto = {
            'cabelo': form.cabelo.data,
            'cor_cabelo': form.cor_cabelo.data,
            'sobrancelha': form.sobrancelha.data,
            'cor_sobrancelha': form.cor_sobrancelha.data,
            'olhos': form.olhos.data,
            'cor_olhos': form.cor_olhos.data,
            'cilios': form.cilios.data,
            'nariz': form.nariz.data,
            'boca': form.boca.data,
            'orelhas': form.orelhas.data,
            'acessorios': form.acessorios.data,
        }

    # Movido o print para fora do bloco if
    print("Dados do rosto:", dados_rosto)

    return render_template('criar_rosto.html', form=form)
# Restante do código...

if __name__ == '__main__':
    app.run(debug=True)
