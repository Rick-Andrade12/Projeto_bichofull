import api from "./api";

export async function buscarSaldo() {
  const response = await api.get("/carteira/saldo");
  return response.data;
}

export async function buscarHistorico() {
  const response = await api.get("/apostas/historico");
  return response.data;
}

export async function realizarAposta(dados) {
  const response = await api.post("/apostas/apostar", dados);
  return response.data;
}