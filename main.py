from fastapi import FastAPI, HTTPException

app = FastAPI()

# Variable para simular saldo
saldo = 1000

@app.get('/consultar_saldo')
def consultar_saldo():
    return {"saldo": saldo}

@app.post('/depositar/{monto}')
def depositar(monto: float):
    global saldo
    saldo += monto
    return {"mensaje": f"Depósito exitoso. Saldo actual: {saldo}"}

@app.post('/retirar/{monto}')
def retirar(monto: float):
    global saldo
    if saldo >= monto:
        saldo -= monto
        return {"mensaje": f"Retiro exitoso. Saldo actual: {saldo}"}
    else:
        raise HTTPException(status_code=400, detail="Saldo insuficiente")

