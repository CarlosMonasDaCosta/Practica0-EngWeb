from flask import Flask, request, render_template
app = Flask(__name__,template_folder='template')

@app.route('/')

def description():
   return render_template("description.html")


@app.route('/operacion', methods=['GET','POST'])

def html_operate():
   if request.method == "POST":
      numero1 = request.form['Num1']
      numero2 = request.form['Num2']
      nombreO = request.form["operacionString"]
      resultado = operacion(nombreO,numero1,numero2)
      if(resultado==-1):
         return render_template("400.html")
      return render_template("operate.html",Resultado = resultado)
   else:
      return render_template("operate.html")
   
def operacion(operacion,n1,n2):
   if(operacion == "suma"):
      r = sumar(n1,n2)
      return(r)
   if(operacion == "resta"):
      r = restar(n1,n2)
      return(r)
   if(operacion == "multiplicacion"):
      r = multiplicar(n1,n2)
      return(r)
   if(operacion == "division"):
      r = dividir(n1,n2)
      return(r)
   


def sumar(a,b):
   c = float(a)+float(b)
   return(c)

def restar(a,b):
   c = float(a)-float(b)
   return(c)

def multiplicar(a,b):
   c = float(a)*float(b)
   return(c)

def dividir(a,b):
   if int(b)!=0:
      c=int(a)/int(b)
      return(c)
   else:
      return -1
      
   
if __name__== '__main__':
   app.run(host='0.0.0.0', port=80)



